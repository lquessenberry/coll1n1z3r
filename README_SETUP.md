# 🔥 C0LL1N-1Z3R - Kid Power Edition 🔥

**Uncle Lee's Christmas Present for Collin**

The ultimate app installer for creative tools, games, and awesome desktop effects!

---

## 🎁 What's Inside

**26+ Apps & Extensions Including:**

- 🎨 **Creative Tools:** GIMP, Inkscape, Krita, Blender, Pinta, Tux Paint, LibreOffice
- ⚔️ **Games:** FreeCiv, 0 A.D., Hedgewars, Wesnoth
- 💻 **Coding:** Scratch
- 🔧 **Desktop:** GNOME Tweaks, Extension Manager
- ✨ **Effects:** Burn My Windows, Blur My Shell, Desktop Cube, Gnomelets, Impatience

---

## 🚀 Quick Start (Easy Way)

### 1. Double-click `launch.sh`

That's it! Your browser will open to http://localhost:5000

### 2. Or run from terminal:

```bash
cd "/home/lquessenberry/Custom Apps/coll1n1z3r"
./launch.sh
```

---

## 🖥️ Add to Applications Menu (Optional)

To add C0LL1N-1Z3R to your Applications menu:

```bash
cp C0LL1N-1Z3R.desktop ~/.local/share/applications/
```

Now you can find it in your app launcher!

---

## 📋 Requirements

- **Ubuntu/Linux** with GNOME desktop
- **Python 3** (already installed on Ubuntu)
- **Flask** (auto-installs when you run launch.sh)
- **Internet connection** (for downloading apps)

---

## 🎯 How to Use

1. **Launch the app** using `launch.sh`
2. **Open your browser** to http://localhost:5000
3. **Browse categories** using the tabs at the top:
   - 📦 All
   - 🎨 Creative
   - ⚔️ Games
   - 💻 Coding
   - 🔧 Desktop
   - ✨ Effects
4. **Click Install** on any app you want
5. **Click Launch** after installation to open the app!

---

## ⚠️ Important Notes

### For APT Packages (GIMP, Inkscape, etc.)
- You'll need to enter your **sudo password**
- This is normal and safe - it's installing system packages

### For GNOME Extensions (Effects)
- After installing extensions, **restart GNOME Shell**:
  - Press **Alt + F2**
  - Type **r**
  - Press **Enter**
- Or just log out and log back in

### For Flatpaks (Krita, Blender)
- First installation might take a few minutes
- They install to system-wide location

---

## 🎨 Pro Tips

1. **Install Extension Manager first** (in Desktop or Effects tab)
   - Makes managing extensions easier
   
2. **Try the cool effects:**
   - Burn My Windows = Fire effects when closing windows
   - Desktop Cube = 3D desktop cube
   - Blur My Shell = Beautiful blur effects
   - Gnomelets = Desktop pets!

3. **Launch buttons appear after install**
   - Click to open apps instantly from the interface

---

## 🐛 Troubleshooting

**Q: Apps won't install?**
- Make sure you have internet connection
- Check if you entered the correct sudo password

**Q: Extensions not working?**
- Restart GNOME Shell (Alt+F2, type "r")
- Or log out and log back in

**Q: Can't launch the app?**
- Make sure launch.sh is executable: `chmod +x launch.sh`
- Check Python3 is installed: `python3 --version`

**Q: Browser doesn't open automatically?**
- Manually go to: http://localhost:5000

---

## 🎄 Merry Christmas, Collin!

This app was made with ❤️ by Uncle Lee to help you discover awesome creative tools, fun games, and make your computer LEGENDARY!

Have fun exploring and creating amazing things! 🚀

---

## 📝 Technical Details

- **Backend:** Python Flask
- **Frontend:** HTML/CSS/JavaScript
- **Installs:** APT packages, Flatpak apps, GNOME extensions
- **Auto-downloads** extensions from extensions.gnome.org
- **Launches apps** directly from the interface

Built December 2025
