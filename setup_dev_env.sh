#!/bin/bash

# Jekyll Blog Development Environment Setup Script
# This script sets up the Python virtual environment for blog validation tools

echo "🚀 Setting up Jekyll blog development environment..."

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3 first."
    exit 1
fi

echo "✅ Python 3 found"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "❌ Failed to create virtual environment"
        exit 1
    fi
fi

echo "✅ Virtual environment ready"

# Activate virtual environment and install dependencies
echo "📥 Installing Python dependencies..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 Setup complete!"
    echo ""
    echo "📋 Available commands:"
    echo "  • Run validation:    source venv/bin/activate && python validate_blog.py"
    echo "  • Start dev server:  python3 dev_server.py"
    echo "  • Activate venv:     source venv/bin/activate"
    echo ""
    echo "💡 Pro tip: Add 'source venv/bin/activate' to your shell startup for convenience"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi
