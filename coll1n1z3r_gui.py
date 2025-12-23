from flask import Flask, render_template_string, jsonify, request
import subprocess
import threading

app = Flask(__name__)

APPS = [
    # Creative
    {"name": "GIMP", "category": "Creative", "icon": "🎨", "type": "apt", "pkg": "gimp", "desc": "Professional photo editor"},
    {"name": "Inkscape", "category": "Creative", "icon": "🎨", "type": "apt", "pkg": "inkscape", "desc": "Vector graphics"},
    {"name": "Krita", "category": "Creative", "icon": "🎨", "type": "flatpak", "pkg": "org.kde.krita", "desc": "Digital painting"},
    {"name": "Blender", "category": "Creative", "icon": "🎨", "type": "flatpak", "pkg": "org.blender.Blender", "desc": "3D creation"},
    {"name": "Pinta", "category": "Creative", "icon": "🎨", "type": "apt", "pkg": "pinta", "desc": "Simple paint"},
    {"name": "Tux Paint", "category": "Creative", "icon": "🎨", "type": "apt", "pkg": "tuxpaint", "desc": "Kid-friendly drawing"},
    {"name": "LibreOffice", "category": "Creative", "icon": "📄", "type": "apt", "pkg": "libreoffice", "desc": "Office suite"},
    
    # Games
    {"name": "FreeCiv", "category": "Games", "icon": "⚔️", "type": "apt", "pkg": "freeciv", "desc": "Build civilizations"},
    {"name": "0 A.D.", "category": "Games", "icon": "⚔️", "type": "apt", "pkg": "0ad", "desc": "Ancient warfare RTS"},
    {"name": "Hedgewars", "category": "Games", "icon": "⚔️", "type": "apt", "pkg": "hedgewars", "desc": "Turn-based strategy"},
    {"name": "Wesnoth", "category": "Games", "icon": "⚔️", "type": "flatpak", "pkg": "org.wesnoth.Wesnoth", "desc": "Fantasy tactics RPG"},
    
    # Coding
    {"name": "Scratch", "category": "Coding", "icon": "💻", "type": "apt", "pkg": "scratch", "desc": "Visual programming"},
    
    # Desktop
    {"name": "GNOME Tweaks", "category": "Desktop", "icon": "🔧", "type": "apt", "pkg": "gnome-tweaks", "desc": "Desktop customization"},
    {"name": "Extension Manager", "category": "Desktop", "icon": "🧩", "type": "flatpak", "pkg": "com.mattjakeman.ExtensionManager", "desc": "Manage extensions"},
    
    # Effects
    {"name": "⭐ Extension Manager", "category": "Effects", "icon": "🧩", "type": "flatpak", "pkg": "com.mattjakeman.ExtensionManager", "desc": "⭐ REQUIRED! Install this first!"},
    {"name": "Burn My Windows", "category": "Effects", "icon": "🔥", "type": "extension", "pkg": "burn-my-windows@schneegans.github.com", "desc": "Window fire effects"},
    {"name": "Blur My Shell", "category": "Effects", "icon": "✨", "type": "extension", "pkg": "blur-my-shell@aunetx", "desc": "Beautiful blur"},
    {"name": "Desktop Cube", "category": "Effects", "icon": "🎲", "type": "extension", "pkg": "desktop-cube@schneegans.github.com", "desc": "3D desktop cube"},
    {"name": "Gnomelets", "category": "Effects", "icon": "🐶", "type": "extension", "pkg": "gnomelets@gnomelets.github.com", "desc": "Desktop pets"},
    {"name": "Impatience", "category": "Effects", "icon": "⚡", "type": "extension", "pkg": "impatience@noctilucent.github.com", "desc": "Fast animations"},
]

@app.route('/')
def index():
    html = '''
<!DOCTYPE html>
<html>
<head>
    <title>C0LL1N-1Z3R</title>
    <style>
        body { font-family: Arial; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; }
        .header { text-align: center; margin-bottom: 30px; }
        .tabs { display: flex; justify-content: center; gap: 10px; margin-bottom: 30px; flex-wrap: wrap; }
        .tab { background: rgba(255,255,255,0.2); color: white; border: none; padding: 12px 24px; border-radius: 25px; cursor: pointer; font-size: 16px; font-weight: bold; transition: all 0.3s; }
        .tab:hover { background: rgba(255,255,255,0.3); transform: translateY(-2px); }
        .tab.active { background: white; color: #667eea; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 20px; max-width: 1200px; margin: 0 auto; }
        .card { background: white; color: #333; border-radius: 15px; padding: 20px; text-align: center; }
        .card-icon { font-size: 48px; margin-bottom: 10px; }
        .card-name { font-size: 20px; font-weight: bold; margin-bottom: 10px; }
        .card-desc { font-size: 14px; color: #666; margin-bottom: 10px; }
        .install-btn { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border: none; padding: 10px 20px; border-radius: 25px; cursor: pointer; font-size: 16px; font-weight: bold; }
        .install-btn:disabled { opacity: 0.5; cursor: not-allowed; }
        .installing { background: #ffa500 !important; }
        .installed { background: #4caf50 !important; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🔥 C0LL1N-1Z3R 🔥</h1>
        <p>Kid Power Edition - Epic Creative + Gaming + Pet Command Center</p>
    </div>
    <div class="tabs">
        <button class="tab active" onclick="filterApps('All')">📦 All</button>
        <button class="tab" onclick="filterApps('Creative')">🎨 Creative</button>
        <button class="tab" onclick="filterApps('Games')">⚔️ Games</button>
        <button class="tab" onclick="filterApps('Coding')">💻 Coding</button>
        <button class="tab" onclick="filterApps('Desktop')">🔧 Desktop</button>
        <button class="tab" onclick="filterApps('Effects')">✨ Effects</button>
    </div>
    <div class="grid" id="grid"></div>
    <script>
        let allApps = [];
        let currentFilter = 'All';

        fetch('/api/apps')
            .then(r => r.json())
            .then(apps => {
                allApps = apps;
                renderApps();
            });

        function filterApps(category) {
            currentFilter = category;
            document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));
            event.target.classList.add('active');
            renderApps();
        }

        function renderApps() {
            const grid = document.getElementById('grid');
            const filtered = currentFilter === 'All' ? allApps : allApps.filter(app => app.category === currentFilter);
            
            grid.innerHTML = filtered.map((app, idx) => `
                <div class="card" id="app-${idx}">
                    <div class="card-icon">${app.icon}</div>
                    <div class="card-name">${app.name}</div>
                    <div class="card-desc">${app.desc}</div>
                    <div style="margin: 10px 0; color: #999; font-size: 12px;">📦 ${app.type.toUpperCase()}</div>
                    <button class="install-btn" onclick="installApp('${app.pkg}', '${app.type}', this, ${idx})">Install</button>
                </div>
            `).join('');
        }

        function installApp(pkg, type, btn, idx) {
            btn.textContent = 'Installing...';
            btn.classList.add('installing');
            btn.disabled = true;

            fetch('/api/install', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({pkg: pkg, type: type})
            })
            .then(r => r.json())
            .then(data => {
                if (data.error) {
                    alert('Error: ' + data.error);
                    btn.textContent = 'Install';
                    btn.classList.remove('installing');
                    btn.disabled = false;
                } else {
                    btn.textContent = 'INSTALLED';
                    btn.classList.remove('installing');
                    btn.classList.add('installed');
                    btn.disabled = false;
                    
                    // Add Launch button if not an extension
                    if (type !== 'extension') {
                        const card = document.getElementById('app-' + idx);
                        const launchBtn = document.createElement('button');
                        launchBtn.className = 'install-btn';
                        launchBtn.style.marginLeft = '10px';
                        launchBtn.textContent = 'Launch';
                        launchBtn.onclick = () => launchApp(pkg, type, launchBtn);
                        btn.parentNode.appendChild(launchBtn);
                    }
                }
            })
            .catch(error => {
                alert('Installation failed: ' + error);
                btn.textContent = 'Install';
                btn.classList.remove('installing');
                btn.disabled = false;
            });
        }

        function launchApp(pkg, type, btn) {
            btn.textContent = 'Launching...';
            btn.disabled = true;

            fetch('/api/launch', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({pkg: pkg, type: type})
            })
            .then(r => r.json())
            .then(data => {
                if (data.error) {
                    alert('Error: ' + data.error);
                } else {
                    setTimeout(() => {
                        btn.textContent = 'Launch';
                        btn.disabled = false;
                    }, 1000);
                }
            })
            .catch(error => {
                alert('Launch failed: ' + error);
                btn.textContent = 'Launch';
                btn.disabled = false;
            });
        }
    </script>
</body>
</html>
'''
    return html

@app.route('/api/apps')
def get_apps():
    return jsonify(APPS)

@app.route('/api/launch', methods=['POST'])
def launch_app():
    data = request.json
    pkg = data.get('pkg')
    launch_type = data.get('type')
    
    if not pkg or not launch_type:
        return jsonify({'error': 'Missing package or type'}), 400
    
    try:
        if launch_type == 'apt':
            # For APT packages, try to launch using the package name as command
            # Most GUI apps have the same command name as package
            subprocess.Popen([pkg], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return jsonify({'status': 'launched'})
            
        elif launch_type == 'flatpak':
            # Launch flatpak app
            subprocess.Popen(['flatpak', 'run', pkg],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return jsonify({'status': 'launched'})
            
        elif launch_type == 'extension':
            # Extensions don't launch, they're already active
            return jsonify({'error': 'Extensions are active in GNOME Shell. Restart shell (Alt+F2, r) to load.'}), 400
            
        return jsonify({'error': 'Unknown launch type'}), 400
        
    except Exception as e:
        return jsonify({'error': f'Launch failed: {str(e)}'}), 500

@app.route('/api/install', methods=['POST'])
def install_app():
    data = request.json
    pkg = data.get('pkg')
    install_type = data.get('type')

    if not pkg or not install_type:
        return jsonify({'error': 'Missing package or type'}), 400

    try:
        if install_type == 'apt':
            # For demo, just check if package exists
            result = subprocess.run(['apt', 'list', '--installed', pkg],
                                  capture_output=True, text=True, timeout=10)
            if pkg in result.stdout:
                return jsonify({'status': 'already installed'})
            else:
                # Actually install
                subprocess.run(['sudo', 'apt', 'update'], capture_output=True)
                result = subprocess.run(['sudo', 'apt', 'install', '-y', pkg],
                                      capture_output=True, text=True, timeout=300)
                if result.returncode == 0:
                    return jsonify({'status': 'installed'})
                else:
                    return jsonify({'error': result.stderr}), 500

        elif install_type == 'flatpak':
            # Check if already installed (system-wide)
            result = subprocess.run(['flatpak', 'list', '--system', '--app'],
                                  capture_output=True, text=True)
            if pkg in result.stdout:
                return jsonify({'status': 'already installed'})
            else:
                # Install to system
                subprocess.run(['flatpak', 'remote-add', '--system', '--if-not-exists', 'flathub',
                              'https://flathub.org/repo/flathub.flatpakrepo'],
                             capture_output=True)
                result = subprocess.run(['flatpak', 'install', '--system', '-y', 'flathub', pkg],
                                      capture_output=True, text=True, timeout=300)
                if result.returncode == 0:
                    return jsonify({'status': 'installed'})
                else:
                    return jsonify({'error': result.stderr}), 500

        elif install_type == 'extension':
            # Install GNOME extension automatically
            import tempfile
            import os
            import zipfile
            import shutil
            import json
            
            extension_uuid = pkg
            
            # Check if already installed
            check_result = subprocess.run(['gnome-extensions', 'info', extension_uuid],
                                        capture_output=True, text=True)
            if check_result.returncode == 0:
                # Already installed, just enable it
                subprocess.run(['gnome-extensions', 'enable', extension_uuid],
                             capture_output=True)
                return jsonify({'status': 'already installed and enabled'})
            
            # Get GNOME Shell version
            shell_version_result = subprocess.run(['gnome-shell', '--version'],
                                                 capture_output=True, text=True)
            shell_version = shell_version_result.stdout.strip().split()[-1]
            major_version = shell_version.split('.')[0]
            
            # Download extension info from extensions.gnome.org
            info_url = f'https://extensions.gnome.org/extension-info/?uuid={extension_uuid}&shell_version={major_version}'
            info_result = subprocess.run(['curl', '-s', info_url],
                                        capture_output=True, text=True, timeout=30)
            
            if info_result.returncode != 0 or not info_result.stdout:
                return jsonify({'error': 'Could not fetch extension info. Install Extension Manager to browse extensions.'}), 500
            
            try:
                ext_info = json.loads(info_result.stdout)
                
                if 'download_url' not in ext_info:
                    return jsonify({'error': f'Extension not compatible with GNOME {major_version}. Try Extension Manager for other versions.'}), 400
                
                download_url = f"https://extensions.gnome.org{ext_info['download_url']}"
                
                # Download and install
                with tempfile.TemporaryDirectory() as tmpdir:
                    zip_path = os.path.join(tmpdir, 'extension.zip')
                    subprocess.run(['wget', '-q', '-O', zip_path, download_url],
                                 check=True, timeout=60)
                    
                    # Extract
                    extract_dir = os.path.join(tmpdir, 'extracted')
                    os.makedirs(extract_dir)
                    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                        zip_ref.extractall(extract_dir)
                    
                    # Install to user extensions directory
                    extensions_dir = os.path.expanduser(f'~/.local/share/gnome-shell/extensions/{extension_uuid}')
                    os.makedirs(os.path.dirname(extensions_dir), exist_ok=True)
                    
                    if os.path.exists(extensions_dir):
                        shutil.rmtree(extensions_dir)
                    shutil.copytree(extract_dir, extensions_dir)
                    
                    # Enable the extension
                    enable_result = subprocess.run(['gnome-extensions', 'enable', extension_uuid],
                                                  capture_output=True, text=True)
                    
                    return jsonify({'status': 'installed'})
                    
            except json.JSONDecodeError:
                return jsonify({'error': 'Extension not found. Install Extension Manager to browse available extensions.'}), 400
            except Exception as e:
                return jsonify({'error': f'Installation failed: {str(e)}'}), 500

        return jsonify({'error': 'Unknown install type'}), 400

    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Installation timed out'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
