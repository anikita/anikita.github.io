# Antonis Nikitakis Personal Blog

A Jekyll-powered blog hosted on GitHub Pages, featuring technical writing and systems engineering philosophy.

## 🚀 Quick Start

### Prerequisites
- Ruby (for Jekyll)
- Python 3 (for validation tools)

### Local Development Setup

1. **Clone the repository** (if not already done)
   ```bash
   git clone https://github.com/anikita/anikita.github.io.git
   cd anikita.github.io
   ```

2. **Set up Python environment**
   ```bash
   ./setup_dev_env.sh
   ```
   This creates a virtual environment and installs validation dependencies.

3. **Install Jekyll** (if not already installed)
   ```bash
   gem install jekyll bundler
   gem install jekyll-theme-tactile jekyll-feed
   ```

4. **Start development server**
   ```bash
   python3 dev_server.py
   ```
   Open http://localhost:4000 to view your site locally.

## 📝 Writing Posts

1. **Create a new post** in `_posts/` folder with format: `YYYY-MM-DD-post-title.md`
2. **Add front matter**:
   ```yaml
   ---
   layout: default
   title: "Your Post Title"
   date: 2025-09-23
   author: Antonis Nikitakis
   categories: [blog]
   ---
   ```

3. **Write your content** in Markdown below the front matter.

## 🛡️ Validation & Quality Assurance

### Automatic Validation
The pre-commit hook automatically validates your changes:
- Post filename format
- Front matter completeness
- YAML syntax
- Theme compatibility

### Manual Validation
```bash
# Activate virtual environment
source venv/bin/activate

# Run validation
python validate_blog.py
```

## 🎨 Changing Themes

Edit `_config.yml` and change the theme:
```yaml
theme: jekyll-theme-minimal  # Try different themes
```

Available themes: `jekyll-theme-tactile`, `jekyll-theme-slate`, `jekyll-theme-minimal`, etc.

## 📤 Publishing Changes

```bash
git add .
git commit -m "Your commit message"
git push
```

Changes automatically deploy to https://anikita.github.io/

## 🏗️ Project Structure

```
├── _config.yml          # Jekyll configuration
├── _posts/              # Blog posts
├── index.md             # Homepage
├── Gemfile              # Ruby dependencies
├── requirements.txt     # Python dependencies
├── validate_blog.py     # Validation script
├── dev_server.py       # Development server launcher
└── setup_dev_env.sh     # Environment setup script
```

## 🐛 Troubleshooting

### Jekyll not found locally
```bash
gem install jekyll bundler
gem install jekyll-theme-tactile jekyll-feed
```

### Validation fails
```bash
source venv/bin/activate
python validate_blog.py
```

### Permission issues
```bash
chmod +x setup_dev_env.sh
chmod +x dev_server.py
```

## 📚 Resources

- [Jekyll Documentation](https://jekyllrb.com/)
- [GitHub Pages](https://pages.github.com/)
- [Markdown Guide](https://www.markdownguide.org/)

---

*Built with Jekyll and hosted on GitHub Pages*
