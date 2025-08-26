# Image Setup Guide for SS & MS Fabrication Website

## Required Images

Place all images in the `images/` folder with these exact names:

### 1. Company Logo
- **File**: `images/logo.png`
- **Recommended size**: 200x80px (or similar ratio)
- **Format**: PNG with transparent background preferred
- **Usage**: Appears in the navigation header

### 2. Hero Background
- **File**: `images/hero-bg.jpg`
- **Recommended size**: 1920x1080px
- **Format**: JPG
- **Usage**: Background image for the main hero section
- **Tip**: Choose an image of your workshop, team, or impressive fabrication work

### 3. Workshop Image
- **File**: `images/workshop.jpg`
- **Recommended size**: 600x400px
- **Format**: JPG
- **Usage**: Shows in the "About Us" section
- **Tip**: Interior shot of your workshop or team at work

### 4. Project Gallery Images
Add 6 project images with these names:
- `images/project-1.jpg` - Custom Gate Project
- `images/project-2.jpg` - Staircase Railing
- `images/project-3.jpg` - Industrial Structure
- `images/project-4.jpg` - Window Grills
- `images/project-5.jpg` - Balcony Railing
- `images/project-6.jpg` - Custom Fabrication

**Recommended specs for project images:**
- **Size**: 800x600px
- **Format**: JPG
- **Quality**: High quality but compressed for web

## Image Optimization Tips

### 1. Compress Images
Use tools like:
- **Online**: TinyPNG, Squoosh.app
- **Software**: Photoshop, GIMP
- **Target**: Keep file sizes under 500KB each

### 2. Recommended Formats
- **Logo**: PNG (supports transparency)
- **Photos**: JPG (better compression for photos)
- **Modern option**: WebP (smaller file sizes, good browser support)

### 3. Image Dimensions
```
Logo: 200x80px (2.5:1 ratio)
Hero: 1920x1080px (16:9 ratio)
Workshop: 600x400px (3:2 ratio)
Projects: 800x600px (4:3 ratio)
```

## Adding Your Images

### Method 1: Direct Upload
1. Create the `images` folder in your project root
2. Add your images with the exact names listed above
3. Deploy to Netlify

### Method 2: Using Netlify Dashboard
1. Go to your Netlify site dashboard
2. Click "Site settings" → "Asset optimization"
3. Upload images directly through the file manager

## Fallback Behavior

The website includes automatic fallbacks:
- If logo fails to load: Shows text-only company name
- If project images fail: Shows gray placeholder with project name
- If workshop image fails: Shows placeholder box

## File Structure
```
your-project/
├── images/
│   ├── logo.png
│   ├── hero-bg.jpg
│   ├── workshop.jpg
│   ├── project-1.jpg
│   ├── project-2.jpg
│   ├── project-3.jpg
│   ├── project-4.jpg
│   ├── project-5.jpg
│   └── project-6.jpg
├── index.html
├── netlify.toml
└── README.md
```

## Testing Your Images

1. **Local Testing**: Open `index.html` in your browser
2. **Check Loading**: Ensure all images load properly
3. **Mobile Test**: Test on mobile devices or browser dev tools
4. **Performance**: Check loading speed

## Troubleshooting

### Images Not Showing?
1. Check file names match exactly (case-sensitive)
2. Verify images are in the `images/` folder
3. Check file formats (JPG/PNG)
4. Ensure files aren't corrupted

### Slow Loading?
1. Compress images further
2. Consider WebP format
3. Check file sizes (aim for <500KB each)

### Logo Issues?
1. Ensure transparent background for PNG
2. Check dimensions aren't too large
3. Verify contrast against header background

## Pro Tips

1. **Consistent Style**: Use similar lighting/style for project images
2. **High Quality**: Use your best work for the gallery
3. **Mobile First**: Test how images look on mobile devices
4. **SEO**: Use descriptive file names (e.g., `stainless-steel-gate.jpg`)
5. **Backup**: Keep original high-res versions for future use