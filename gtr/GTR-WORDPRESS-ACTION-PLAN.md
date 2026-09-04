# GTR (Golden Ticket Realty) — WordPress Action Plan
**Site:** https://goldenticketrealty.com  
**Platform:** WordPress (PHP 8.2, Elementor 4.2.4, Hello Theme 3.5.1, Yoast SEO 28.4)  
**Created:** 2026-09-04  

---

## Overview

Because GTR is a live WordPress site hosted remotely, many fixes must be implemented via the WordPress admin dashboard, plugins, or server-level configuration rather than direct file edits. This document provides step-by-step instructions for each fix category.

---

## 1. SECURITY & SERVER CONFIGURATION

### 1.1 Block XML-RPC and Remove RSD Link
**Issue:** `xmlrpc.php?rsd` returns 403 and creates a 4xx crawl error.

**Actions:**
1. Install **Wordfence Security** or **Sucuri Security** plugin
2. Go to **Wordfence → Login Security → Settings → XML-RPC**
3. Enable **"Disable XML-RPC"**
4. Alternatively, add to `functions.php` of child theme:
   ```php
   add_filter('xmlrpc_enabled', '__return_false');
   remove_action('wp_head', 'rsd_link');
   remove_action('wp_head', 'wlwmanifest_link');
   ```
5. Verify fix: `curl -sI https://goldenticketrealty.com/xmlrpc.php` should return 403 or 405

### 1.2 Add Security Headers
**Issue:** Missing HSTS, X-Content-Type-Options, Referrer-Policy, CSP.

**Actions:**
1. If server uses **Apache/LiteSpeed**, edit `.htaccess` via cPanel File Manager or FTP:
   ```apache
   <IfModule mod_headers.c>
       Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
       Header always set X-Frame-Options "SAMEORIGIN"
       Header always set X-Content-Type-Options "nosniff"
       Header always set Referrer-Policy "strict-origin-when-cross-origin"
       Header always set Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline' https://www.googletagmanager.com https://goldenticketrealty.com; style-src 'self' 'unsafe-inline'; img-src 'self' data: https://goldenticketrealty.com; font-src 'self'; connect-src 'self' https://www.google-analytics.com; frame-ancestors 'self';"
   </IfModule>
   ```
2. If `.htaccess` is locked (permission denied), use a plugin instead:
   - Install **Redirection** or **HTTP Headers** plugin
   - Add headers via plugin UI
3. Verify with: `curl -sI https://goldenticketrealty.com/ | grep -i "strict-transport\|x-content\|referrer\|content-security"`

### 1.3 Fix Unsafe Cross-Origin Links
**Issue:** External links lack `rel="noopener noreferrer"`.

**Actions:**
1. In **Elementor**, edit each page with external links
2. Select the link widget → **Advanced → Attributes**
3. Add attribute: `rel|noopener noreferrer`
4. For social profile links, add: `rel|noopener noreferrer`
5. For affiliate/partner links (`fasthomeofferutah.com`), add: `rel|noopener noreferrer nofollow`
6. Alternative: Use a plugin like **External Links** to auto-add `rel` attributes sitewide

---

## 2. IMAGE OPTIMIZATION

### 2.1 Bulk Compress Existing Images
**Issue:** 15+ images over 100 KB, several PNGs over 400 KB, one over 1.6 MB.

**Actions:**
1. Install **ShortPixel Image Optimizer** (recommended) or **Imagify**
2. Go to **ShortPixel → Settings**
3. Configure:
   - **Compression type:** Lossy (or Glossy for better quality)
   - **WebP delivery:** Enable (via .htaccess rewrite or `<picture>` tags)
   - **Resize large images:** Max width 1200px, max height 1200px
   - **CMYK to RGB conversion:** Enable
4. Run **Bulk Optimization** on existing Media Library
5. Expected savings: 60–80% file size reduction

### 2.2 Convert PNG Before/After Images to WebP
**Issue:** `/our-projects/` page has large PNG files (408 KB – 1,630 KB).

**Actions:**
1. In ShortPixel settings, enable **"Create WebP versions"**
2. After bulk optimization, verify WebP files exist in `/wp-content/uploads/`
3. If server supports `.htaccess` rewrite, enable ShortPixel’s **"Deliver WebP"** option
4. Alternative: Manually convert critical PNGs using an online converter (Squoosh, CloudConvert) and re-upload

### 2.3 Add Explicit Width/Height to Images
**Issue:** Missing `width`/`height` causes Cumulative Layout Shift (CLS).

**Actions:**
1. In **Elementor**, select each image widget
2. Ensure **Width** and **Height** are set (or use responsive units)
3. For theme images, add `width` and `height` attributes in HTML
4. Enable **"Add missing image dimensions"** in WP Rocket or similar performance plugin

---

## 3. CONTENT & HEADING FIXES

### 3.1 Expand Low-Content Pages
**Issue:** `/thank-you/` and `/our-company/` have thin content.

**Actions for `/thank-you/`:**
1. Edit page in Elementor
2. Add sections:
   - "What Happens Next?" (H2) — explain timeline (24-48 hours)
   - "While You Wait" (H2) — link to FAQs, testimonials, blog
   - "Have Questions?" (H2) — phone number, email, live chat
   - "Read Success Stories" (H2) — 2–3 testimonial snippets with links
3. Target: 400+ words total

**Actions for `/our-company/`:**
1. Edit page in Elementor
2. Add sections:
   - "Our Mission" (H2) — 150+ words
   - "Meet Martin Pacheco" (H2) — founder bio, photo, credentials
   - "Why We Buy Houses in Melbourne" (H2) — community connection
   - "Our Process" (H2) — step-by-step with icons
   - "Community Involvement" (H2) — local partnerships, charity
3. Target: 600+ words total

### 3.2 Fix Missing H2 Headings
**Issue:** `/our-company/`, `/terms-conditions/`, `/privacy-policy/` have 0 H2s.

**Actions:**
1. Edit each page in Elementor
2. Change existing text headings from `<p>` or `<h3>` to `<h2>` where appropriate
3. For legal pages, use H2 for major sections:
   - Terms: "Acceptance of Terms", "User Conduct", "Limitation of Liability", "Contact"
   - Privacy: "Information We Collect", "How We Use Your Data", "Cookies", "Third Parties", "Your Rights"

### 3.3 Fix Non-Sequential Headings
**Issue:** Some pages skip H1 → H3 without H2.

**Actions:**
1. Audit `/how-we-buy-houses/` and `/sell-your-house/`
2. Change any `<h3>` that is a top-level section heading to `<h2>`
3. Use `<h3>` only for subsections under an `<h2>`
4. Ensure visual hierarchy in Elementor matches HTML heading hierarchy

### 3.4 Fix Duplicate H2s Across Pages
**Issue:** "How To Sell Your House For Cash In Melbourne, FL" appears on multiple pages.

**Actions:**
1. Audit all pages for identical H2 text
2. Make each H2 unique:
   - Homepage: "How To Sell Your House For Cash In Melbourne, FL"
   - `/sell-your-house/`: "Get a Fair Cash Offer for Your Melbourne Home Today"
   - `/how-we-buy-houses/`: "Our Simple 4-Step Home Buying Process in Melbourne"

---

## 4. TITLE & META DESCRIPTION FIXES

### 4.1 Fix Titles Over 60 Characters

| Page | Current Title | Fix in Yoast |
|------|--------------|--------------|
| `/contact/` | Contact Golden Ticket Realty \| All-Cash Offers & Foreclosure Help (69 chars) | Contact Golden Ticket Realty \| Melbourne Cash Offers (55 chars) |
| `/comparison/` | Sell Your House Fast in Brevard County, FL – Compare Direct Sale (64 chars) | Sell Your House Fast Brevard County \| Direct Sale vs Agent (58 chars) |

**Actions:**
1. Edit each page → scroll to **Yoast SEO** box
2. Update **SEO Title** field
3. Ensure green indicator (good length)

### 4.2 Fix Meta Description Over 155 Characters

| Page | Current Meta | Fix in Yoast |
|------|-------------|--------------|
| `/contact/` | Reach out to Golden Ticket Realty at (321) 341-2201 for answers to your questions about all-cash offers, stopping foreclosure, or learning about our company. (157 chars) | Contact Golden Ticket Realty in Melbourne FL. Call (321) 341-2201 for cash offers, foreclosure help, and fast closings. (117 chars) |

**Actions:**
1. Edit page → **Yoast SEO** box → **Meta Description**
2. Update text and ensure green indicator

---

## 5. SCHEMA MARKUP

### 5.1 Upgrade Organization to RealEstateAgent
**Issue:** Current schema is generic `Organization`. Missing local business signals.

**Actions:**
1. **Option A (Plugin):** Install **Schema Pro** or switch to **Rank Math**
   - Configure business type as **Real Estate Agent**
   - Fill in address, phone, geo coordinates, hours, area served
2. **Option B (Custom Code):** Add to child theme `functions.php`:
   ```php
   add_action('wp_head', 'gtr_realestateagent_schema');
   function gtr_realestateagent_schema() {
       if (!is_front_page()) return;
       // Output JSON-LD from GTR-SCHEMA-MARKUP.md
   }
   ```
3. Validate with Google Rich Results Test

### 5.2 Add FAQPage Schema to `/faqs/`
**Actions:**
1. In Yoast SEO → **FAQ** block is available in Gutenberg
2. Or add custom JSON-LD in page template
3. See `GTR-SCHEMA-MARKUP.md` for full template

### 5.3 Add BreadcrumbList to Inner Pages
**Actions:**
1. Enable breadcrumbs in **Yoast SEO → Settings → Breadcrumbs**
2. Or add custom breadcrumb schema via plugin

---

## 6. SITEMAP & INDEXING

### 6.1 Clean Up Sitemap
**Issue:** Post sitemap contains `__trashed-2` and `elementor-1590` slugs.

**Actions:**
1. Go to **Posts → All Posts**
2. Find the post with slug `__trashed-2`
   - If it should be live: edit slug to something SEO-friendly (e.g., `top-reasons-fast-home-sale-melbourne`)
   - If it should be deleted: move to Trash, then empty Trash
3. Find the post with slug `elementor-1590`
   - This is a draft/auto-generated slug. Either publish with a proper slug or delete
4. Go to **Yoast SEO → Settings → Site Features → API**
   - Ensure XML sitemaps are enabled
5. Purge cache (NitroPack, Cloudflare, or server cache)
6. Verify clean sitemap: `curl -s https://goldenticketrealty.com/post-sitemap.xml`

### 6.2 Resubmit Sitemap to GSC
**Actions:**
1. Go to **Google Search Console → Sitemaps**
2. Remove old sitemap submission if stale
3. Submit: `https://goldenticketrealty.com/sitemap_index.xml`
4. Check "Last read" date

---

## 7. PHONE NUMBER STANDARDIZATION

**Issue:** Inconsistent phone numbers across site.

**Actions:**
1. Decide on primary number (e.g., 321-341-2201)
2. Use **Better Search Replace** plugin to bulk-replace old numbers
3. Search for: `321-294-2081` and `321-341-2201`
4. Ensure all `tel:` links use format: `tel:3213412201` (no spaces, no dashes in href)
5. Update:
   - Header CTA
   - Footer
   - Contact page
   - Meta descriptions
   - Schema markup
   - GMB listing

---

## 8. BLOG SETUP

### 8.1 Create Blog Index Page
**Actions:**
1. Create a new page: **Pages → Add New**
2. Title: "Blog" or "Real Estate Insights"
3. Use Elementor to add a **Posts Grid** widget
4. Configure grid to show blog posts, 6 per page
5. Set page slug to `/blog/`
6. Add to main navigation: **Appearance → Menus → Main Menu**

### 8.2 Set Up Blog Post Template
**Actions:**
1. In **Elementor → Templates → Single Post**
2. Create a "Single Post" template
3. Include: header, breadcrumbs, post title, featured image, content, author box, related posts, CTA section, footer
4. Set display conditions: **All Posts**

---

## 9. PERFORMANCE & CACHING

### 9.1 Review Caching Setup
**Issue:** NitroPack is installed. Verify it's configured correctly.

**Actions:**
1. Go to **NitroPack** dashboard
2. Ensure caching mode is **"Strong"** or **"Ludicrous"**
3. Enable image lazy loading
4. Enable CSS/JS minification
5. Exclude critical CSS for above-the-fold content
6. After making SEO changes, purge NitroPack cache

### 9.2 Enable GZIP / Brotli Compression
**Actions:**
1. Check if server has compression enabled:
   ```bash
   curl -sI -H "Accept-Encoding: gzip" https://goldenticketrealty.com/ | grep -i content-encoding
   ```
2. If missing, add to `.htaccess`:
   ```apache
   <IfModule mod_deflate.c>
       AddOutputFilterByType DEFLATE text/html text/css text/javascript application/javascript application/json
   </IfModule>
   ```

---

## 10. VERIFICATION CHECKLIST

After completing all WordPress actions:
- [ ] XML-RPC blocked and RSD link removed
- [ ] Security headers present on all pages
- [ ] All external links have `rel="noopener noreferrer"`
- [ ] All images under 100 KB (or 200 KB for hero)
- [ ] All titles ≤ 60 characters
- [ ] All meta descriptions ≤ 155 characters
- [ ] Every page has at least 1 H2
- [ ] Heading hierarchy is sequential (h1 → h2 → h3)
- [ ] RealEstateAgent schema validates in Rich Results Test
- [ ] FAQPage schema on `/faqs/`
- [ ] BreadcrumbList on inner pages
- [ ] Sitemap is clean (no trashed/draft URLs)
- [ ] Phone number is consistent sitewide
- [ ] Blog index page live and in navigation
- [ ] NitroPack cache purged
- [ ] GSC sitemap resubmitted
