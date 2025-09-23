#!/bin/bash

echo "🔨 Building Jekyll site locally (no server)..."
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
    echo "🌐 To preview: Open _site/index.html in your browser"
    echo "🚀 To serve:   cd _site && python3 -m http.server 8000"
    echo ""
    echo "📊 Build summary:"
    echo "   - $(find _site -name "*.html" | wc -l) HTML pages"
    echo "   - $(find _site -name "*.css" | wc -l) CSS files"
    echo "   - $(find _site -name "*.js" | wc -l) JS files"
else
    echo "❌ Site build failed!"
    echo "💡 Try running: ./toggle_theme.sh  # Switch theme off for local dev"
    exit 1
fi
