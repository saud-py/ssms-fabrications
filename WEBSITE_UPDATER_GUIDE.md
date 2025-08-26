# Website Content Updater Guide

This guide explains how to easily update your SS & MS Fabrication website content using the provided scripts.

## 📁 Available Scripts

### 1. Interactive Python Script (`update_website.py`)
**Best for**: First-time setup or major changes
**Features**: 
- Interactive prompts for all content
- Automatic backup creation
- Comprehensive content updates

### 2. Shell Script (`update_website.sh`)
**Best for**: Quick updates on Mac/Linux
**Features**:
- Simple command-line interface
- Fast updates for basic information

### 3. Configuration-based (`apply_config.py` + `website_config.json`)
**Best for**: Repeated updates or team collaboration
**Features**:
- Edit JSON file with your content
- Apply all changes at once
- Version control friendly

## 🚀 Quick Start

### Method 1: Interactive Python Script

```bash
python3 update_website.py
```

Follow the prompts to update:
- Company name and branding
- Contact information (address, phone, email)
- Hero section (main headline and subtitle)
- About section content
- Service descriptions

### Method 2: Shell Script (Mac/Linux)

```bash
./update_website.sh
```

Enter your information when prompted. Press Enter to skip fields you don't want to change.

### Method 3: Configuration File

1. **Edit the config file**:
```bash
nano website_config.json
# or use any text editor
```

2. **Apply the changes**:
```bash
python3 apply_config.py
```

## 📝 Configuration File Format

Edit `website_config.json` to customize your website:

```json
{
  "company": {
    "name": "Your Company Name",
    "tagline": "Your Company Tagline",
    "experience_years": "15 years"
  },
  "contact": {
    "address": "Your Full Address",
    "phone": "Your Phone Number", 
    "email": "your@email.com",
    "business_hours": "Your Business Hours"
  },
  "hero": {
    "title": "Your Main Headline",
    "subtitle": "Your company description"
  },
  "about": {
    "main_description": "Your company story...",
    "secondary_description": "Additional details..."
  },
  "services": {
    "gates": {
      "title": "Custom Service Name",
      "description": "Service description..."
    }
    // ... more services
  }
}
```

## 🔧 What Each Script Updates

### Company Information
- Company name in header and throughout site
- Page title
- Footer text

### Contact Details
- Business address
- Phone number
- Email address
- Business hours

### Hero Section
- Main headline
- Subtitle/description
- Call-to-action text

### About Section
- Company description
- Experience years
- Mission statement

### Services
- Service titles
- Service descriptions
- All 4 service cards

## 📋 Step-by-Step Example

### Using Interactive Script:

1. **Run the script**:
```bash
python3 update_website.py
```

2. **Follow prompts**:
```
Company Name: ABC Steel Works
Full Address: 456 Industrial Road, Mumbai, Maharashtra 400001
Phone Number: +91 98765 12345
Email: info@abcsteel.com
Main Headline: Expert Steel Fabrication Services
```

3. **Confirm changes**:
```
Proceed with updates? (y/N): y
```

4. **Done!** Your website is updated with a backup created.

## 🛡️ Safety Features

### Automatic Backups
All scripts create timestamped backups:
- `index_backup_20241226_143022.html`
- Restore anytime if needed

### Validation
- Scripts check for required files
- Handle missing or invalid input gracefully
- Preserve website structure

## 🎯 Best Practices

### 1. Test Locally First
```bash
# Open in browser to test
open index.html
# or
python3 -m http.server 8000
```

### 2. Keep Backups
- Scripts auto-create backups
- Keep important versions manually
- Test changes before deploying

### 3. Update in Stages
- Update basic info first
- Test thoroughly
- Add advanced customizations later

### 4. Use Version Control
```bash
git add .
git commit -m "Update company information"
```

## 🔄 Common Update Workflows

### Initial Setup
1. Run `python3 update_website.py`
2. Update all company information
3. Add images to `images/` folder
4. Test locally
5. Deploy to Netlify

### Regular Updates
1. Edit `website_config.json`
2. Run `python3 apply_config.py`
3. Deploy changes

### Quick Contact Update
1. Run `./update_website.sh`
2. Update only contact fields
3. Deploy

## 🚨 Troubleshooting

### Script Won't Run
```bash
# Make sure Python is installed
python3 --version

# Make shell script executable
chmod +x update_website.sh
```

### Changes Not Showing
- Clear browser cache
- Check file was actually updated
- Verify backup was created

### Restore from Backup
```bash
cp index_backup_YYYYMMDD_HHMMSS.html index.html
```

## 📱 Mobile Testing

After updates, test on mobile:
```bash
# Start local server
python3 -m http.server 8000

# Visit on mobile browser
http://your-computer-ip:8000
```

## 🌐 Deployment

After updating content:

1. **Test locally**
2. **Commit to Git**:
```bash
git add .
git commit -m "Update website content"
git push
```
3. **Netlify auto-deploys** from your repository

## 💡 Pro Tips

1. **Batch Updates**: Use config file for multiple changes
2. **Content Planning**: Write content in a document first
3. **SEO**: Include keywords in descriptions
4. **Consistency**: Keep tone and style consistent
5. **Mobile First**: Always test on mobile devices

## 🆘 Need Help?

1. Check this guide first
2. Look at backup files for reference
3. Test with small changes first
4. Keep original content as reference