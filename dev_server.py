#!/usr/bin/env python3
"""
Jekyll Development Server Launcher
Helps set up and run local Jekyll server for testing before pushing to GitHub Pages.
"""

import subprocess
import sys
import os
from pathlib import Path

def check_jekyll_installed():
    """Check if Jekyll is installed"""
    try:
        result = subprocess.run(['jekyll', '--version'],
                              capture_output=True, text=True, check=True)
        print(f"✅ Jekyll found: {result.stdout.strip()}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Jekyll not found. Install with: gem install jekyll bundler")
        return False

def run_validation():
    """Run validation before starting server"""
    print("🛡️  Running pre-deployment validation...")
    try:
        result = subprocess.run(['python3', 'validate_blog.py'],
                              capture_output=True, text=True, check=True)
        print("✅ Validation passed!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Validation failed:\n{e.stdout}")
        return False

def start_jekyll_server():
    """Start Jekyll development server"""
    print("🚀 Starting Jekyll development server...")
    print("📍 Your site will be available at: http://localhost:4000")
    print("🛑 Press Ctrl+C to stop the server")

    try:
        # Run jekyll serve with live reload
        subprocess.run(['jekyll', 'serve', '--livereload'],
                      cwd='.', check=True)
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to start Jekyll server: {e}")

def show_instructions():
    """Show setup instructions"""
    print("📚 Jekyll Local Development Setup")
    print("=" * 40)
    print()
    print("1️⃣ Install Jekyll (Ruby required):")
    print("   macOS: brew install ruby")
    print("   Then:  gem install jekyll bundler")
    print()
    print("2️⃣ Test your setup:")
    print("   python3 dev_server.py")
    print()
    print("3️⃣ Development workflow:")
    print("   - Make changes to posts or pages")
    print("   - Run: python3 dev_server.py")
    print("   - View at: http://localhost:4000")
    print("   - Changes auto-reload in browser")
    print("   - When ready: git add . && git commit && git push")
    print()
    print("4️⃣ Validation:")
    print("   - Automatic validation on commit")
    print("   - Manual validation: python3 validate_blog.py")
    print()

def main():
    """Main function"""
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        show_instructions()
        return

    print("🎯 Jekyll Development Server Launcher")
    print()

    # Check Jekyll installation
    if not check_jekyll_installed():
        print("\n💡 Run: python3 dev_server.py --help")
        sys.exit(1)

    # Run validation
    if not run_validation():
        print("\n🛑 Fix validation errors before starting server")
        sys.exit(1)

    # Start server
    start_jekyll_server()

if __name__ == "__main__":
    main()
