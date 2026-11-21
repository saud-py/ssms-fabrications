# SS & MS FABRICATION Website

Website for SS & MS FABRICATION, a steel fabrication business in BEML Layout, Bagalur, Bengaluru (since 2010).
It is the landing site for the business's Google Ads campaigns.

- **Live site:** https://ssms-fabricatiion-works.netlify.app/
- **Hosting:** Netlify. Every push to `main` is deployed automatically. There is no build step.
- **Tech:** plain HTML, CSS and JavaScript. No frameworks and no build tools.

## Pages

| File | What it is | Use as the landing page for |
|---|---|---|
| `index.html` | Home page: all services, photos, reviews, areas served, map and contact form | General / brand campaigns |
| `gates.html` | Gates, grills and safety doors | Gate, grill and safety door ads |
| `railings.html` | Staircase and balcony railings | Railing ads |
| `sheds-structures.html` | Truss work, roofing sheds and steel structures | Heavy steel / truss / shed campaign |
| `office-partitions.html` | Office partitions, cabins, server room cages, planters | Office and IT work campaign |
| `custom-fabrication.html` | Custom SS and MS work | Custom work ads |
| `success.html` | Thank-you page shown after the contact form is sent | Not linked from ads |
| `privacy.html` | Privacy policy (required by Google Ads because the form collects personal details) | Not linked from ads |
| `404.html` | Shown by Netlify for any page that doesn't exist | Not linked from ads |

Every service page has the same sections: banner with Quote and Call buttons, a "what we make" list, photo gallery,
"How it works", customer reviews, areas served, the contact form and links to the other services.

## Folder layout

```
├── index.html, gates.html, railings.html, ...   # The pages (see table above)
├── css/
│   ├── site.css      # Styles for the home page and all service pages
│   └── page.css      # Styles for the thank-you, privacy and 404 pages
├── js/
│   └── main.js       # Phone menu, photo pop-up, scroll animations, form flag for conversion tracking
├── images/
│   ├── logo.png
│   ├── 2025-04-09.webp   # Workshop photo in the home page "About" section
│   ├── gates/  railings/  sheds/  office/  custom/   # Project photos per service
├── netlify.toml      # Netlify headers, caching and the /thank-you redirect
├── robots.txt        # Search engine rules (keeps the thank-you page out of search)
├── sitemap.xml       # List of pages for Google Search Console
└── IMAGE_GUIDE.md    # How to add or replace photos
```

## Making common changes

The header (menu), contact section, reviews, areas served and footer are repeated in each of the 6 main pages
(`index.html` and the 5 service pages). **When you change one of these, make the same change in all 6 pages.**
Search the project for the text you want to change to find every copy.

### Phone number, email or address

The phone number appears in several formats. Search for each one and update all of them:

- `+919481347471` (call links and the business details for Google)
- `919481347471` (WhatsApp links)
- `+91 94813 47471` (text shown on the page)
- `+91-94813-47471` (business details for Google)

The address and email are in the contact section, footer and business details of each page, and in `privacy.html`.

### WhatsApp messages

Each service page opens WhatsApp with a ready-made first message, for example
"Hi, I need a quote for a gate / grill work." The message is part of the link after `?text=`, written with
`%20` for spaces. The home page and thank-you page use a general enquiry message.

### Reviews

The 3 reviews and the "Rated 5.0 on Google from 16 reviews" line are typed into each page. They don't update
automatically. Update the rating and review count when they change.

### Photos

See [IMAGE_GUIDE.md](IMAGE_GUIDE.md).

## Contact form

The form uses Netlify Forms. Submissions appear in the Netlify dashboard under **Forms → contact**.

- Turn on email notifications in Netlify (**Forms → Notifications**) so every enquiry reaches you quickly.
- Fields: name and phone (required), service (required), area, email and details (optional).
- Spam protection: a hidden "honeypot" field that bots fill in and people don't.
- The form must keep the same name (`contact`) and the same fields on every page, or Netlify will reject submissions.
- After sending, visitors see `success.html`.

## Google Ads conversion tracking

The Google Ads tag (`AW-957726947`) is in the `<head>` of every page. Conversions:

| Conversion | When it fires | Where it's set up |
|---|---|---|
| Contact form | Only when `success.html` loads after a real form submission (not on reloads or direct visits) | `success.html`, plus the flag set in `js/main.js` |
| Call | Any "Call" link or button is clicked | `trackConversion('call')` in each page |
| WhatsApp | Any WhatsApp link or button is clicked | `trackConversion('whatsapp')` in each page |

Clicks are tracked without delaying the link, so a blocked or slow Google tag never stops a call or chat.

## Search engines

- `sitemap.xml` lists all public pages. If you add a page, add it here and resubmit the sitemap in Google Search Console.
- Each page has a canonical link and business details for Google (structured data) in its `<head>`.
- If the site moves to its own domain, replace `https://ssms-fabricatiion-works.netlify.app/` everywhere
  (pages, `sitemap.xml` and `robots.txt`).

## Previewing locally

From the project folder, run:

```bash
python3 -m http.server 8765
```

Then open http://localhost:8765. The contact form only works on Netlify, not in a local preview.

## Deploying

Push or merge your changes into `main`. Netlify deploys them within a minute or two.
After a deploy that touches the form or tracking, submit one test enquiry on the live site and check it arrives in Netlify.
