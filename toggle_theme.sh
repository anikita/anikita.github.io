#!/bin/bash

# Toggle Jekyll theme for local development vs GitHub Pages deployment
# GitHub Pages themes don't work locally, so we comment/uncomment them

CONFIG_FILE="_config.yml"

if [ ! -f "$CONFIG_FILE" ]; then
    echo "❌ _config.yml not found!"
    exit 1
fi

if grep -q "^theme:" "$CONFIG_FILE"; then
    echo "🔄 Switching to LOCAL DEVELOPMENT mode (commenting out theme)..."
    sed -i '' 's/^theme:/# theme:/' "$CONFIG_FILE"
    echo "✅ Theme commented out for local development"
    echo "💡 Run: ./dev_server.sh"
elif grep -q "^# theme:" "$CONFIG_FILE"; then
    echo "🔄 Switching to PRODUCTION mode (uncommenting theme)..."
    # Remove the entire commented line and replace with uncommented version
    sed -i '' 's/^# theme: jekyll-theme-tactile.*$/theme: jekyll-theme-tactile/' "$CONFIG_FILE"
    echo "✅ Theme enabled for GitHub Pages deployment"
    echo "💡 Ready to commit and push!"
else
    echo "❓ No theme line found in _config.yml"
fi

echo ""
echo "📄 Current theme setting:"
grep -E "^(# )?theme:" "$CONFIG_FILE"
