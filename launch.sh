#!/bin/bash

# C0LL1N-1Z3R - Kid Power Edition Launcher
# Uncle Lee's Christmas Present for Collin

echo "🔥 Starting C0LL1N-1Z3R... 🔥"
echo ""

# Check if Python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed. Please install Python3 first."
    exit 1
fi

# Check if Flask is installed
if ! python3 -c "import flask" &> /dev/null; then
    echo "📦 Installing Flask..."
    pip3 install flask --user
fi

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Launch the app
cd "$SCRIPT_DIR"
echo "🚀 Launching web interface at http://localhost:5000"
echo ""
echo "✨ Open your browser to: http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop"
echo ""

python3 coll1n1z3r_gui.py
