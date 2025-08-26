#!/usr/bin/env python3
"""
Website Content Updater for SS & MS Fabrication Works
This script allows you to update website content through interactive prompts.
"""

import re
import os
import json
from datetime import datetime

class WebsiteUpdater:
    def __init__(self):
        self.html_file = "index.html"
        self.backup_file = f"index_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
        
    def backup_html(self):
        """Create a backup of the current HTML file"""
        if os.path.exists(self.html_file):
            with open(self.html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            with open(self.backup_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Backup created: {self.backup_file}")
        
    def read_html(self):
        """Read the current HTML content"""
        with open(self.html_file, 'r', encoding='utf-8') as f:
            return f.read()
    
    def write_html(self, content):
        """Write updated content to HTML file"""
        with open(self.html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ Website updated successfully!")
    
    def update_company_name(self, content, new_name):
        """Update company name throughout the website"""
        patterns = [
            (r'<title>.*?</title>', f'<title>{new_name} - Quality Steel Fabrication</title>'),
            (r'SS & MS FABRICATION', new_name),
            (r'SS and MS Fabrication Works', new_name),
            (r'SS & MS Fabrication Works', new_name)
        ]
        
        for pattern, replacement in patterns:
            content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
        
        return content
    
    def update_contact_info(self, content, contact_data):
        """Update contact information"""
        # Update address
        if contact_data.get('address'):
            content = re.sub(
                r'123 Fabrication Street, Industrial Area, City, State 12345',
                contact_data['address'],
                content
            )
        
        # Update phone
        if contact_data.get('phone'):
            content = re.sub(
                r'\+91 98765 43210',
                contact_data['phone'],
                content
            )
        
        # Update email
        if contact_data.get('email'):
            content = re.sub(
                r'contact@ssmsfab\.com',
                contact_data['email'],
                content
            )
        
        # Update business hours
        if contact_data.get('hours'):
            hours_pattern = r'Monday - Saturday: 9:00 AM - 6:00 PM'
            content = re.sub(hours_pattern, contact_data['hours'], content)
        
        return content
    
    def update_hero_content(self, content, hero_data):
        """Update hero section content"""
        if hero_data.get('title'):
            content = re.sub(
                r'Precision in Steel Fabrication',
                hero_data['title'],
                content
            )
        
        if hero_data.get('subtitle'):
            content = re.sub(
                r'Delivering high-quality Stainless Steel \(SS\) and Mild Steel \(MS\) solutions for all your construction and design needs\.',
                hero_data['subtitle'],
                content
            )
        
        return content
    
    def update_about_section(self, content, about_data):
        """Update about section content"""
        if about_data.get('description'):
            # Update main description
            old_desc = r'With over a decade of experience in the metal fabrication industry, we pride ourselves on delivering exceptional craftsmanship and durable products\. Our team of skilled professionals is dedicated to turning your vision into reality\.'
            content = re.sub(old_desc, about_data['description'], content)
        
        if about_data.get('experience'):
            content = re.sub(
                r'over a decade of experience',
                f"over {about_data['experience']} of experience",
                content
            )
        
        return content
    
    def update_services(self, content, services_data):
        """Update services section"""
        service_mappings = {
            'gates': ('Custom Gates & Grills', 'Designer SS and MS gates, window grills, and safety doors for homes and businesses.'),
            'railings': ('Staircase & Railings', 'Elegant and sturdy staircase railings, balcony railings, and handrails in various designs.'),
            'structural': ('Structural Fabrication', 'MS structures for sheds, warehouses, and other industrial and commercial applications.'),
            'custom': ('Bespoke Projects', 'Custom fabrication work based on your specific designs and requirements.')
        }
        
        for key, (title, desc) in service_mappings.items():
            if services_data.get(key):
                new_title, new_desc = services_data[key]
                content = re.sub(re.escape(title), new_title, content)
                content = re.sub(re.escape(desc), new_desc, content)
        
        return content

def get_user_input():
    """Collect user input for website updates"""
    print("🔧 SS & MS Fabrication Website Updater")
    print("=" * 50)
    print("Press Enter to skip any field you don't want to change.\n")
    
    data = {}
    
    # Company Information
    print("📋 COMPANY INFORMATION")
    print("-" * 25)
    company_name = input("Company Name (current: SS & MS FABRICATION): ").strip()
    if company_name:
        data['company_name'] = company_name
    
    # Contact Information
    print("\n📞 CONTACT INFORMATION")
    print("-" * 25)
    address = input("Full Address: ").strip()
    phone = input("Phone Number: ").strip()
    email = input("Email Address: ").strip()
    hours = input("Business Hours (e.g., Monday - Saturday: 9:00 AM - 6:00 PM): ").strip()
    
    if any([address, phone, email, hours]):
        data['contact'] = {}
        if address: data['contact']['address'] = address
        if phone: data['contact']['phone'] = phone
        if email: data['contact']['email'] = email
        if hours: data['contact']['hours'] = hours
    
    # Hero Section
    print("\n🎯 HERO SECTION")
    print("-" * 15)
    hero_title = input("Main Headline (current: Precision in Steel Fabrication): ").strip()
    hero_subtitle = input("Subtitle/Description: ").strip()
    
    if hero_title or hero_subtitle:
        data['hero'] = {}
        if hero_title: data['hero']['title'] = hero_title
        if hero_subtitle: data['hero']['subtitle'] = hero_subtitle
    
    # About Section
    print("\n📖 ABOUT SECTION")
    print("-" * 17)
    experience = input("Years of Experience (e.g., '15 years'): ").strip()
    description = input("Company Description (main paragraph): ").strip()
    
    if experience or description:
        data['about'] = {}
        if experience: data['about']['experience'] = experience
        if description: data['about']['description'] = description
    
    # Services
    print("\n🔨 SERVICES")
    print("-" * 12)
    print("Update service titles and descriptions (format: Title | Description)")
    
    services = {}
    service_names = [
        ('gates', 'Gates & Grills'),
        ('railings', 'Staircase & Railings'),
        ('structural', 'Structural Fabrication'),
        ('custom', 'Custom/Bespoke Projects')
    ]
    
    for key, name in service_names:
        service_input = input(f"{name}: ").strip()
        if service_input and '|' in service_input:
            title, desc = service_input.split('|', 1)
            services[key] = (title.strip(), desc.strip())
    
    if services:
        data['services'] = services
    
    return data

def main():
    """Main function to run the website updater"""
    updater = WebsiteUpdater()
    
    # Check if HTML file exists
    if not os.path.exists(updater.html_file):
        print(f"❌ Error: {updater.html_file} not found!")
        print("Make sure you're running this script in the same directory as your website files.")
        return
    
    # Get user input
    data = get_user_input()
    
    if not data:
        print("\n⚠️  No changes specified. Exiting...")
        return
    
    # Confirm changes
    print("\n📋 SUMMARY OF CHANGES")
    print("=" * 25)
    for section, values in data.items():
        print(f"• {section.upper()}: {len(values) if isinstance(values, dict) else 1} field(s)")
    
    confirm = input("\nProceed with updates? (y/N): ").strip().lower()
    if confirm != 'y':
        print("❌ Update cancelled.")
        return
    
    # Create backup
    updater.backup_html()
    
    # Read current content
    content = updater.read_html()
    
    # Apply updates
    if 'company_name' in data:
        content = updater.update_company_name(content, data['company_name'])
    
    if 'contact' in data:
        content = updater.update_contact_info(content, data['contact'])
    
    if 'hero' in data:
        content = updater.update_hero_content(content, data['hero'])
    
    if 'about' in data:
        content = updater.update_about_section(content, data['about'])
    
    if 'services' in data:
        content = updater.update_services(content, data['services'])
    
    # Write updated content
    updater.write_html(content)
    
    print(f"\n🎉 Website updated successfully!")
    print(f"📁 Backup saved as: {updater.backup_file}")
    print("\n💡 Next steps:")
    print("1. Review the changes in your browser")
    print("2. Add your images to the 'images/' folder")
    print("3. Deploy to Netlify")

if __name__ == "__main__":
    main()