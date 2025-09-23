#!/usr/bin/env python3
"""
Jekyll Blog Validator
Validates blog posts and configuration before committing to prevent common errors.
"""

import os
import re
import yaml
import sys
from pathlib import Path
from typing import List, Dict, Any

class JekyllValidator:
    def __init__(self, site_root: str = "."):
        self.site_root = Path(site_root)
        self.errors: List[str] = []
        self.warnings: List[str] = []

    def validate_post_filename(self, filepath: Path) -> bool:
        """Validate Jekyll post filename format: YYYY-MM-DD-title.md"""
        filename = filepath.name
        pattern = r'^\d{4}-\d{2}-\d{2}-[a-zA-Z0-9\-]+\.md$'

        if not re.match(pattern, filename):
            self.errors.append(f"Invalid post filename: {filename}")
            self.errors.append("  Format should be: YYYY-MM-DD-title-with-hyphens.md")
            return False

        # Check for underscores (common mistake)
        if '_' in filename:
            self.errors.append(f"Post filename contains underscores: {filename}")
            self.errors.append("  Use hyphens (-) instead of underscores (_) in filenames")
            return False

        return True

    def validate_front_matter(self, filepath: Path) -> bool:
        """Validate Jekyll front matter"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            self.errors.append(f"Cannot read file {filepath}: {e}")
            return False

        # Check for front matter delimiters
        if not content.startswith('---'):
            self.errors.append(f"No front matter found in {filepath}")
            return False

        # Split front matter from content
        parts = content.split('---', 2)
        if len(parts) < 3:
            self.errors.append(f"Incomplete front matter in {filepath}")
            return False

        front_matter_text = parts[1]

        try:
            front_matter = yaml.safe_load(front_matter_text)
        except yaml.YAMLError as e:
            self.errors.append(f"Invalid YAML in front matter of {filepath}: {e}")
            return False

        # Required fields for posts
        required_fields = ['title', 'date', 'author']
        for field in required_fields:
            if field not in front_matter:
                self.errors.append(f"Missing required field '{field}' in {filepath}")

        # Validate date format
        if 'date' in front_matter:
            date_str = str(front_matter['date'])
            if not re.match(r'^\d{4}-\d{2}-\d{2}', date_str):
                self.errors.append(f"Invalid date format in {filepath}: {date_str}")
                self.errors.append("  Use format: YYYY-MM-DD")

        # Validate layout
        if 'layout' in front_matter:
            valid_layouts = ['post', 'default', 'page']
            if front_matter['layout'] not in valid_layouts:
                self.warnings.append(f"Unknown layout '{front_matter['layout']}' in {filepath}")

        return len(self.errors) == 0

    def validate_config(self) -> bool:
        """Validate _config.yml"""
        config_file = self.site_root / '_config.yml'
        if not config_file.exists():
            self.errors.append("Missing _config.yml file")
            return False

        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
        except Exception as e:
            self.errors.append(f"Invalid _config.yml: {e}")
            return False

        # Check for required fields
        if 'title' not in config:
            self.warnings.append("_config.yml missing 'title' field")

        # Validate theme
        if 'theme' in config:
            theme = config['theme']
            supported_themes = [
                'jekyll-theme-minimal', 'jekyll-theme-modernist',
                'jekyll-theme-slate', 'jekyll-theme-tactile',
                'jekyll-theme-cayman', 'jekyll-theme-hacker',
                'jekyll-theme-leap-day', 'jekyll-theme-merlot',
                'jekyll-theme-midnight', 'jekyll-theme-minimal',
                'jekyll-theme-modernist', 'jekyll-theme-slate',
                'jekyll-theme-tactile', 'jekyll-theme-time-machine'
            ]
            if theme not in supported_themes:
                self.warnings.append(f"Theme '{theme}' may not be supported by GitHub Pages")

        return True

    def validate_posts(self) -> bool:
        """Validate all posts in _posts directory"""
        posts_dir = self.site_root / '_posts'
        if not posts_dir.exists():
            self.warnings.append("No _posts directory found")
            return True

        valid = True
        for post_file in posts_dir.glob('*.md'):
            if not self.validate_post_filename(post_file):
                valid = False
            if not self.validate_front_matter(post_file):
                valid = False

        return valid

    def run_validation(self) -> bool:
        """Run all validations"""
        print("🔍 Validating Jekyll blog...")

        self.validate_config()
        self.validate_posts()

        # Report results
        if self.errors:
            print("\n❌ Errors found:")
            for error in self.errors:
                print(f"  {error}")

        if self.warnings:
            print("\n⚠️  Warnings:")
            for warning in self.warnings:
                print(f"  {warning}")

        if not self.errors:
            print("\n✅ Validation passed! Your blog looks good to go.")
            return True
        else:
            print(f"\n❌ Validation failed with {len(self.errors)} errors.")
            return False

def main():
    """Main validation function"""
    validator = JekyllValidator()

    if validator.run_validation():
        print("\n🚀 Ready to commit and push!")
        sys.exit(0)
    else:
        print("\n🛑 Please fix the errors before committing.")
        sys.exit(1)

if __name__ == "__main__":
    main()
