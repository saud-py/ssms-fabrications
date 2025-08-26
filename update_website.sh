#!/bin/bash

# Website Content Updater for SS & MS Fabrication Works
# Simple shell script version

echo "🔧 SS & MS Fabrication Website Updater"
echo "======================================"
echo "This script will help you update your website content."
echo "Press Enter to skip any field you don't want to change."
echo ""

# Create backup
BACKUP_FILE="index_backup_$(date +%Y%m%d_%H%M%S).html"
cp index.html "$BACKUP_FILE"
echo "✅ Backup created: $BACKUP_FILE"
echo ""

# Company Name
echo "📋 COMPANY INFORMATION"
echo "---------------------"
read -p "Company Name (current: SS & MS FABRICATION): " COMPANY_NAME

# Contact Information
echo ""
echo "📞 CONTACT INFORMATION"
echo "---------------------"
read -p "Full Address: " ADDRESS
read -p "Phone Number: " PHONE
read -p "Email Address: " EMAIL
read -p "Business Hours: " HOURS

# Hero Section
echo ""
echo "🎯 HERO SECTION"
echo "---------------"
read -p "Main Headline (current: Precision in Steel Fabrication): " HERO_TITLE
read -p "Subtitle/Description: " HERO_SUBTITLE

# Apply updates using sed
if [ ! -z "$COMPANY_NAME" ]; then
    sed -i.bak "s/SS & MS FABRICATION/$COMPANY_NAME/g" index.html
    sed -i.bak "s/SS and MS Fabrication Works/$COMPANY_NAME/g" index.html
    echo "✅ Company name updated"
fi

if [ ! -z "$ADDRESS" ]; then
    sed -i.bak "s/123 Fabrication Street, Industrial Area, City, State 12345/$ADDRESS/g" index.html
    echo "✅ Address updated"
fi

if [ ! -z "$PHONE" ]; then
    sed -i.bak "s/+91 98765 43210/$PHONE/g" index.html
    echo "✅ Phone number updated"
fi

if [ ! -z "$EMAIL" ]; then
    sed -i.bak "s/contact@ssmsfab\.com/$EMAIL/g" index.html
    echo "✅ Email updated"
fi

if [ ! -z "$HOURS" ]; then
    sed -i.bak "s/Monday - Saturday: 9:00 AM - 6:00 PM/$HOURS/g" index.html
    echo "✅ Business hours updated"
fi

if [ ! -z "$HERO_TITLE" ]; then
    sed -i.bak "s/Precision in Steel Fabrication/$HERO_TITLE/g" index.html
    echo "✅ Hero title updated"
fi

if [ ! -z "$HERO_SUBTITLE" ]; then
    sed -i.bak "s/Delivering high-quality Stainless Steel (SS) and Mild Steel (MS) solutions for all your construction and design needs\./$HERO_SUBTITLE/g" index.html
    echo "✅ Hero subtitle updated"
fi

# Clean up temporary files
rm -f index.html.bak

echo ""
echo "🎉 Website updated successfully!"
echo "📁 Backup saved as: $BACKUP_FILE"
echo ""
echo "💡 Next steps:"
echo "1. Review the changes in your browser"
echo "2. Add your images to the 'images/' folder"
echo "3. Deploy to Netlify"