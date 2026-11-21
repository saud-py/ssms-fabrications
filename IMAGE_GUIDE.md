# Image Guide

How photos are organised on the SS & MS FABRICATION website, and how to add or replace them.

## Where the photos are

```
images/
├── logo.png            # Logo in the header, thank-you, privacy and 404 pages (144 × 144 px PNG)
├── 2025-04-09.webp     # Workshop photo in the home page "About" section
├── gates/              # gates-01.webp ... gates-14.webp     → gates.html
├── railings/           # railings-01.webp ... railings-03.webp → railings.html
├── sheds/              # sheds-01.webp ... sheds-14.webp     → sheds-structures.html
├── office/             # office-01.webp ... office-03.webp   → office-partitions.html
└── custom/             # custom-01.webp ... custom-07.webp   → custom-fabrication.html
```

Photos are numbered in the order they appear in that page's gallery. The office page also reuses two photos from
`custom/` (the jali partition and the display shelving).

## Special photos

Some photos are used in more than one place. If you replace one of these, check each place it appears.

| Photo | Used for |
|---|---|
| `gates/gates-01.webp` | Home page banner, gates page banner, link-preview image when the site is shared on WhatsApp or Facebook |
| `railings/railings-01.webp` | Railings page banner, home page "Railings" card |
| `sheds/sheds-01.webp` | Sheds page banner |
| `sheds/sheds-02.webp` | Home page "Truss Work, Sheds & Structures" card |
| `office/office-01.webp` | Office page banner, home page "Office Partitions" card and photo tile |
| `custom/custom-01.webp` | Custom page banner, home page "Custom Fabrication" card |

The home page "Our Work" section shows 8 photos picked from the service folders. Each one links to its service page.

## Adding a photo to a service page

1. **Prepare the photo.**
   - Format: **WebP** (smallest files). JPG also works.
   - Size: about 1,000–1,400 px on the longest side.
   - File size: aim for under 200 KB. [Squoosh](https://squoosh.app) can convert to WebP and compress.
   - Content: the finished work, in good light, without people, clutter or watermarks in the way.
2. **Name it** with the next number in that folder, for example `images/railings/railings-04.webp`.
3. **Add it to the page's gallery.** Open the service page, find the `work-grid` section under "Our recent work",
   and copy an existing line, changing the file name and description in both places:

   ```html
   <a href="images/railings/railings-04.webp" data-caption="SS balcony railing with glass panels"><img src="images/railings/railings-04.webp" alt="SS balcony railing with glass panels" loading="lazy" width="400" height="300"></a>
   ```

   - `href` and `src`: the photo's path.
   - `data-caption` and `alt`: a short, factual description, for example "Black MS sliding main gate with vertical bars".
     It is shown under the enlarged photo, read out by screen readers, and helps Google understand the image.

Tapping a gallery photo opens it enlarged; visitors can swipe or use the arrow keys to move through the gallery.

## Replacing a page banner

The banner photo is set in the page's `page-hero` section (service pages) or in `css/site.css` under `.hero`
(home page). Wide (landscape) photos work best. The banner has a dark overlay so the white text stays readable.

If you change the home page banner, also update the `preload` link and the `og:image` link-preview tag in the
`<head>` of `index.html`.

## Checking your changes

1. Preview the site locally (see README.md) and open the page you changed.
2. Check the photo shows in the gallery and enlarges when tapped.
3. Check on a phone-sized screen (in Chrome: right-click → Inspect → device toolbar).
