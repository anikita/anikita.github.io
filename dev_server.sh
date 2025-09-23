#!/bin/bash

echo "🚀 Starting Jekyll development server..."
echo "📍 Your site will be available at: http://localhost:4000"
echo "🛑 Press Ctrl+C to stop the server"
echo ""

# Check if Jekyll is available
if ! command -v jekyll &> /dev/null; then
    echo "❌ Jekyll not found. Install with: gem install jekyll bundler"
    exit 1
fi

echo "🔧 Using Jekyll without theme for local dev (theme works on GitHub Pages)..."
echo "💡 Theme is commented out in _config.yml for local development"
echo ""

# Run Jekyll without live reload (more stable)
jekyll serve
