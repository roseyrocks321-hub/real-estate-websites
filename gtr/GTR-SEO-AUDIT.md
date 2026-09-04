# GTR (Golden Ticket Realty) — Technical SEO Audit & Fix Log
**Site:** https://goldenticketrealty.com  
**Platform:** WordPress (PHP 8.2, Elementor, Hello Theme, Yoast SEO)  
**Audit Date:** 2026-09-04  
**Auditor:** Hermes Agent  

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Pages Crawled | 21 (12 pages + 9 posts) |
| Critical Issues | 1 (4xx/403 on xmlrpc.php) |
| High Priority | 3 (oversized images, low content, broken links) |
| Medium Priority | 5 (titles, meta, headings, security) |
| Low Priority | 4 (H2 dupes, schema gaps, cross-origin links) |

---

## 1. CRITICAL ISSUES

### 1.1 Response Codes: Internal Client Error (4xx)
- **Count:** 1 page (HIGH — 0.83%)
- **Issue:** `https://goldenticketrealty.com/xmlrpc.php?rsd` returns **403 Forbidden**
- **Impact:** Screaming Frog flags this as a 4xx. XML-RPC is a known attack vector and should be blocked, but the RSD link in `<head>` creates a crawl error.
- **Fix:** Remove the `<link rel="EditURI" type="application/rsd+xml" ...>` tag from the WordPress theme or use a security plugin to disable XML-RPC and remove the RSD link.
  - **WordPress Action:** Install/disable XML-RPC via `add_filter('xmlrpc_enabled', '__return_false');` in `functions.php` or use a security plugin (Wordfence, Sucuri) to block XML-RPC and remove RSD/WLW manifest links.

---

## 2. MEDIUM PRIORITY ISSUES

### 2.1 Images: Over 100 kB (15 pages — 38.46%)
**Oversized images found on live crawl:**

| Page | Image | Size | Fix |
|------|-------|------|-----|
| `/our-projects/` | `IMG_5353-1-scaled.jpg` | 634 KB | Compress to WebP, max 1200px width |
| `/our-projects/` | `IMG-9538-1024x768.jpg` | 108 KB | Compress to WebP |
| `/our-projects/` | `IMG_8788-1-1024x768.jpg` | 119 KB | Compress to WebP |
| `/our-projects/` | `kitchen_before_matched.png` | 457 KB | Compress PNG, or convert to WebP |
| `/our-projects/` | `living_room_before_matched.png` | 455 KB | Compress PNG, or convert to WebP |
| `/our-projects/` | `bedroom_before_matched.png` | 514 KB | Compress PNG, or convert to WebP |
| `/our-projects/` | `008_i77a5716-edit-1024x683.jpg` | 109 KB | Compress to WebP |
| `/our-projects/` | `4th-bedroom-after.png` | 833 KB | Compress PNG, or convert to WebP |
| `/our-projects/` | `enhanced_image_1edit_kitchen-768x573.png` | 485 KB | Compress PNG, or convert to WebP |
| `/our-projects/` | `bathroom_resized.png` | 634 KB | Compress PNG, or convert to WebP |
| `/our-projects/` | `backyard_resized.png` | 822 KB | Compress PNG, or convert to WebP |
| `/our-projects/` | `kitchen-after-1-1.png` | 408 KB | Compress PNG, or convert to WebP |
| `/our-projects/` | `bathroom-1-after-1024x629.png` | 796 KB | Compress PNG, or convert to WebP |
| `/our-projects/` | `backyard-after-1.png` | **1,630 KB** | Compress PNG, or convert to WebP |
| `/sell-your-house/` | `happy-couple-1024x676.jpg` | 105 KB | Compress to WebP |

**Recommended Action:**
1. Use a WordPress image optimization plugin (ShortPixel, Imagify, or Smush) to bulk-compress existing images.
2. Convert PNG before/after images to WebP format.
3. Set max image width to 1200px.
4. Enable lazy loading on all images (already partially enabled via Elementor).
5. Add explicit `width` and `height` attributes to prevent CLS.

### 2.2 Content: Low Content Pages (2 pages — 18.18%)
Pages with very thin content (< 200 words of meaningful text):

| Page | Word Count | Issue | Recommendation |
|------|-----------|-------|----------------|
| `/thank-you/` | ~150 | Thin thank-you page | Add next steps, related links, testimonials, social proof |
| `/our-company/` | ~200 | Thin about page | Expand to 500+ words: founder story, mission, team photos, community involvement |

### 2.3 Page Titles: Over 60 Characters (2 pages — 18.18%)
| Page | Current Title | Length | Recommended Title |
|------|--------------|--------|-------------------|
| `/contact/` | Contact Golden Ticket Realty | All-Cash Offers & Foreclosure Help | 69 | Contact Golden Ticket Realty | Melbourne Cash Offers |
| `/comparison/` | Sell Your House Fast in Brevard County, FL – Compare Direct Sale | 64 | Sell Your House Fast Brevard County | Direct Sale vs Agent |

### 2.4 Page Titles: Over 561 Pixels (2 pages — 18.18%)
Same as above — titles over 60 chars typically exceed 561px in SERPs.

### 2.5 Meta Description: Over 155 Characters (1 page — 9.09%)
| Page | Current Meta | Length | Recommended Meta |
|------|-------------|--------|-----------------|
| `/contact/` | Reach out to Golden Ticket Realty at (321) 341-2201 for answers to your questions about all-cash offers, stopping foreclosure, or learning about our company. | 157 | Contact Golden Ticket Realty in Melbourne FL. Call (321) 341-2201 for cash offers, foreclosure help, and fast closings. |

---

## 3. LOW PRIORITY ISSUES

### 3.1 H2: Missing on 3 Pages (27.27%)
Pages with H1 but no H2 headings:

| Page | H1 Count | H2 Count | Fix |
|------|---------|---------|-----|
| `/our-company/` | 1 | 0 | Add H2 sections: "Our Mission", "Meet Martin Pacheco", "Why We Buy Houses", "Our Process" |
| `/terms-conditions/` | 1 | 0 | Add H2 sections for each major clause |
| `/privacy-policy/` | 1 | 0 | Add H2 sections for data collection, cookies, third parties, contact |

### 3.2 H2: Duplicate on 3 Pages (27.27%)
Multiple pages use identical or near-identical H2 text:
- "How To Sell Your House For Cash In Melbourne, FL" appears on both homepage and `/sell-your-house/`
- "We Buy Houses in Melbourne in ANY Situation" and similar situational H2s are repeated
- **Fix:** Make H2s unique per page. Use page-specific variations.

### 3.3 H1: Non-Sequential on 3 Pages (27.27%)
Some pages skip from H1 → H3 without H2, or have H3 before H2:
- `/how-we-buy-houses/` has H3 sections without preceding H2s
- `/sell-your-house/` has H3s nested without H2 hierarchy
- **Fix:** Re-structure headings so H1 → H2 → H3 is logical and sequential.

### 3.4 Security: Unsafe Cross-Origin Links (11 URLs — 10.28%)
External links found without `rel="noopener noreferrer"`:

| Target | Found On | Fix |
|--------|---------|-----|
| `linkedin.com/in/winwithpacheco/` | Multiple pages | Add `rel="noopener noreferrer"` |
| `facebook.com/goldenticketrealty` | Multiple pages | Add `rel="noopener noreferrer"` |
| `instagram.com/golden_ticket_realty` | Multiple pages | Add `rel="noopener noreferrer"` |
| `fasthomeofferutah.com` | Homepage, Our Company | Add `rel="noopener noreferrer nofollow"` |
| `melbourneflorida.org` | Homepage | Add `rel="noopener noreferrer nofollow"` |
| `nar.realtor/...` | Homepage | Add `rel="noopener noreferrer nofollow"` |
| `en.wikipedia.org/...` | Contact, Comparison | Add `rel="noopener noreferrer nofollow"` |

**Note:** LinkedIn returns HTTP 999 to crawlers, which Screaming Frog may flag as a broken link. This is expected LinkedIn behavior.

### 3.5 Security: Bad Content Type on 8 URLs (7.48%)
Some resource URLs may return incorrect `Content-Type` headers. Audit via:
```bash
curl -sI https://goldenticketrealty.com/wp-content/uploads/... | grep -i content-type
```

### 3.6 Security Headers Missing on Most Pages
Current headers on homepage:
```
X-Frame-Options: SAMEORIGIN
Content-Security-Policy: frame-ancestors 'self';
```

**Missing headers:**
- `Strict-Transport-Security` (HSTS)
- `X-Content-Type-Options: nosniff`
- `Referrer-Policy`
- Full `Content-Security-Policy`

**WordPress Action:** Add via `.htaccess` (if Apache/LiteSpeed) or a security plugin:
```apache
<IfModule mod_headers.c>
    Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
    Header always set X-Frame-Options "SAMEORIGIN"
    Header always set X-Content-Type-Options "nosniff"
    Header always set Referrer-Policy "strict-origin-when-cross-origin"
    Header always set Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline' https://www.googletagmanager.com https://goldenticketrealty.com; style-src 'self' 'unsafe-inline'; img-src 'self' data: https://goldenticketrealty.com; font-src 'self'; connect-src 'self' https://www.google-analytics.com; frame-ancestors 'self';"
</IfModule>
```

---

## 4. ADDITIONAL FINDINGS

### 4.1 Phone Number Inconsistency
- Homepage snapshot shows `tel:%20321-294-2081` (with encoded space)
- Contact page meta references `(321) 341-2201`
- **Fix:** Standardize to one number across all pages. Ensure `tel:` links have no spaces: `href="tel:3213412201"`

### 4.2 Draft/Trashed Content in Sitemap
- `https://goldenticketrealty.com/__trashed-2/` — post slug contains "__trashed" but returns 200 and has real content
- `https://goldenticketrealty.com/elementor-1590/` — generic Elementor draft slug, thin content (1,172 words but low quality)
- **Fix:** Permanently delete or properly publish these posts. Remove from sitemap if trashed.

### 4.3 Sitemap Issues
- Post sitemap contains 9 posts, some with poor slugs (`elementor-1590`, `__trashed-2`)
- **Fix:** Clean up post slugs, remove trashed/draft content from sitemap, resubmit to GSC.

### 4.4 Missing RealEstateAgent / LocalBusiness Schema
Current schema is `Organization` only. For real estate SEO, upgrade to `RealEstateAgent` with:
- `address` (Melbourne, FL)
- `geo` coordinates
- `telephone`
- `areaServed` (Brevard County cities)
- `priceRange` (e.g., "$$$")
- `openingHoursSpecification`

See `GTR-SCHEMA-MARKUP.md` for complete JSON-LD templates.

### 4.5 Missing FAQPage Schema on `/faqs/`
The FAQs page has H2 FAQ headings but no `FAQPage` structured data.
- **Fix:** Add `FAQPage` JSON-LD. See schema markup document.

### 4.6 Missing BreadcrumbList Schema on Inner Pages
Only the homepage has breadcrumbs in schema. Inner pages lack `BreadcrumbList`.

---

## 5. VERIFICATION CHECKLIST

After fixes are deployed:
- [ ] Re-run Screaming Frog crawl
- [ ] Verify 4xx count = 0
- [ ] Verify all images < 100 KB (or < 200 KB for hero/retina)
- [ ] Verify all titles ≤ 60 chars
- [ ] Verify all meta descriptions ≤ 155 chars
- [ ] Verify every page has at least 1 H2
- [ ] Verify heading sequence is h1 → h2 → h3 (no skips)
- [ ] Verify all external links have `rel="noopener noreferrer"`
- [ ] Verify security headers with `curl -I`
- [ ] Verify schema with Google's Rich Results Test
- [ ] Request indexing for updated pages in GSC
