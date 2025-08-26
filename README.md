# SS and MS Fabrication Works Website

A modern, responsive single-page website for SS and MS Fabrication Works, optimized for Netlify deployment.

## Features

- **Responsive Design**: Works perfectly on all devices
- **Optimized Performance**: Fast loading with minimal dependencies
- **Image Carousel**: Swiper.js powered gallery with smooth transitions
- **Contact Form**: Netlify Forms integration for easy inquiries
- **SEO Optimized**: Proper meta tags and semantic HTML
- **Smooth Animations**: Intersection Observer API for scroll animations

## Deployment on Netlify

1. **Connect Repository**: Link your Git repository to Netlify
2. **Build Settings**: 
   - Build command: (leave empty)
   - Publish directory: `.` (root)
3. **Deploy**: Netlify will automatically deploy your site

## Customization

### Adding Your Images

Replace the placeholder images in the gallery section with your actual project photos:

1. Create an `images` folder in your project
2. Add your images (recommended: WebP format for best performance)
3. Update the image sources in `index.html`:

```html
<!-- Replace this -->
<div class="bg-gray-300 w-full h-96 rounded-lg flex items-center justify-center">
    <span class="text-gray-600 text-lg">Custom Gate Project</span>
</div>

<!-- With this -->
<img src="images/your-project-1.webp" alt="Custom Gate Project" class="w-full h-96 object-cover rounded-lg">
```

### Updating Contact Information

Edit the contact details in the Contact section:
- Address
- Phone number
- Email
- Business hours

### Customizing Colors

The website uses Tailwind CSS. You can easily change colors by modifying the class names:
- Primary color: `blue-600` (change to your preferred color)
- Text colors: `gray-800`, `gray-600`
- Background colors: `gray-50`, `gray-100`

## Performance Tips

1. **Optimize Images**: Use WebP format and compress images
2. **Lazy Loading**: Images load as users scroll
3. **Minimal Dependencies**: Only essential libraries included
4. **Caching**: Netlify.toml configured for optimal caching

## Form Handling

The contact form uses Netlify Forms (free tier includes 100 submissions/month):
- No backend required
- Spam protection included
- Email notifications available in Netlify dashboard

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## File Structure

```
├── index.html          # Main website file
├── netlify.toml        # Netlify configuration
├── README.md          # This file
└── images/            # Your project images (create this folder)
```

## Need Help?

For customizations or issues:
1. Check the Netlify documentation
2. Validate HTML at validator.w3.org
3. Test responsiveness using browser dev tools