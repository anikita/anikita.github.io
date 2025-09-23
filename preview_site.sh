#!/bin/bash

echo "🔍 Building and previewing Jekyll site locally..."
echo ""

# Check if Jekyll is available
if ! command -v jekyll &> /dev/null; then
    echo "❌ Jekyll not found. Install with: gem install jekyll bundler"
    exit 1
fi

# Clean previous build
echo "🧹 Cleaning previous build..."
rm -rf _site

# Build the site
echo "🔨 Building site..."
if jekyll build; then
    echo "✅ Site built successfully!"
    echo ""
    echo "📂 Site files are in: _site/"
    echo ""

    # Check if Python is available for serving
    if command -v python3 &> /dev/null; then
        echo "🌐 Starting local server at http://localhost:8000"
        echo "🛑 Press Ctrl+C to stop"
        echo ""
        cd _site && python3 -m http.server 8000
    else
        echo "✅ Site built! Open _site/index.html in your browser to preview."
        echo "💡 Or install Python and run: cd _site && python3 -m http.server 8000"
    fi
else
    echo "❌ Site build failed!"
    echo "💡 Try running: ./toggle_theme.sh  # Switch theme off for local dev"
    exit 1
fi
