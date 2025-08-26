#!/usr/bin/env python3
"""
Configuration-based Website Updater
Updates the website using the website_config.json file
"""

import json
import re
import os
from datetime import datetime

def load_config():
    """Load configuration from JSON file"""
    with open('website_config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def create_backup():
    """Create backup of current HTML file"""
    backup_file = f"index_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    if os.path.exists('index.html'):
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
        with open(backup_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Backup created: {backup_file}")
        return backup_file
    return None

def apply_config_to_html(config):
    """Apply configuration to HTML file"""
    
    # Read current HTML
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Company information
    company = config.get('company', {})
    if company.get('name'):
        content = re.sub(r'SS & MS FABRICATION', company['name'], content)
        content = re.sub(r'SS and MS Fabrication Works', company['name'], content)
        content = re.sub(r'<title>.*?</title>', f'<title>{company["name"]} - Quality Steel Fabrication</title>', content)
    
    if company.get('tagline'):
        content = re.sub(r'Crafting Excellence in Steel Since 2010', company['tagline'], content)
    
    # Contact information
    contact = config.get('contact', {})
    if contact.get('address'):
        content = re.sub(r'123 Fabrication Street, Industrial Area, City, State 12345', contact['address'], content)
    
    if contact.get('phone'):
        content = re.sub(r'\+91 98765 43210', contact['phone'], content)
    
    if contact.get('email'):
        content = re.sub(r'contact@ssmsfab\.com', contact['email'], content)
    
    if contact.get('business_hours'):
        content = re.sub(r'Monday - Saturday: 9:00 AM - 6:00 PM', contact['business_hours'], content)
    
    # Hero section
    hero = config.get('hero', {})
    if hero.get('title'):
        content = re.sub(r'Precision in Steel Fabrication', hero['title'], content)
    
    if hero.get('subtitle'):
        old_subtitle = r'Delivering high-quality Stainless Steel \(SS\) and Mild Steel \(MS\) solutions for all your construction and design needs\.'
        content = re.sub(old_subtitle, hero['subtitle'], content)
    
    # About section
    about = config.get('about', {})
    if about.get('main_description'):
        old_desc = r'With over a decade of experience in the metal fabrication industry, we pride ourselves on delivering exceptional craftsmanship and durable products\. Our team of skilled professionals is dedicated to turning your vision into reality\.'
        content = re.sub(old_desc, about['main_description'], content)
    
    if about.get('secondary_description'):
        old_desc2 = r'We use only the highest quality materials and state-of-the-art equipment to ensure every project meets our rigorous standards of quality, safety, and precision\.'
        content = re.sub(old_desc2, about['secondary_description'], content)
    
    # Services
    services = config.get('services', {})
    service_mappings = {
        'gates': ('Custom Gates & Grills', 'Designer SS and MS gates, window grills, and safety doors for homes and businesses.'),
        'railings': ('Staircase & Railings', 'Elegant and sturdy staircase railings, balcony railings, and handrails in various designs.'),
        'structural': ('Structural Fabrication', 'MS structures for sheds, warehouses, and other industrial and commercial applications.'),
        'custom': ('Bespoke Projects', 'Custom fabrication work based on your specific designs and requirements.')
    }
    
    for key, (old_title, old_desc) in service_mappings.items():
        if key in services:
            service = services[key]
            if service.get('title'):
                content = re.sub(re.escape(old_title), service['title'], content)
            if service.get('description'):
                content = re.sub(re.escape(old_desc), service['description'], content)
    
    # Write updated content
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Website updated successfully!")

def main():
    """Main function"""
    print("🔧 Configuration-based Website Updater")
    print("=" * 40)
    
    # Check if files exist
    if not os.path.exists('index.html'):
        print("❌ Error: index.html not found!")
        return
    
    if not os.path.exists('website_config.json'):
        print("❌ Error: website_config.json not found!")
        return
    
    try:
        # Load configuration
        config = load_config()
        print("✅ Configuration loaded")
        
        # Create backup
        backup_file = create_backup()
        
        # Apply configuration
        apply_config_to_html(config)
        
        print("\n🎉 Website updated successfully!")
        if backup_file:
            print(f"📁 Backup saved as: {backup_file}")
        
        print("\n💡 To customize further:")
        print("1. Edit website_config.json with your details")
        print("2. Run this script again")
        print("3. Add your images to the 'images/' folder")
        
    except json.JSONDecodeError:
        print("❌ Error: Invalid JSON in website_config.json")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()