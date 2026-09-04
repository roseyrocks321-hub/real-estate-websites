# GTR (Golden Ticket Realty) — Schema Markup Templates
**Site:** https://goldenticketrealty.com  
**Purpose:** Add structured data for real estate agent / local business, FAQs, breadcrumbs, and articles  
**Created:** 2026-09-04  

---

## Current State

GTR currently uses Yoast SEO’s default `Organization` + `WebPage` schema.  
**Missing:** `RealEstateAgent` (or `LocalBusiness`), `FAQPage`, `BreadcrumbList` on inner pages, `Article` on blog posts, `HowTo`, `Review`, `AggregateRating`.

---

## 1. Homepage Schema: RealEstateAgent + LocalBusiness

Replace the existing `Organization` block with `RealEstateAgent` (which inherits from `LocalBusiness`). Add this via a custom plugin, `functions.php`, or a schema plugin like Schema Pro / Rank Math.

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "RealEstateAgent",
      "@id": "https://goldenticketrealty.com/#realestateagent",
      "name": "Golden Ticket Realty",
      "alternateName": "GTR",
      "url": "https://goldenticketrealty.com/",
      "logo": {
        "@type": "ImageObject",
        "url": "https://goldenticketrealty.com/wp-content/uploads/2024/08/1.png",
        "width": 981,
        "height": 333
      },
      "image": {
        "@type": "ImageObject",
        "url": "https://goldenticketrealty.com/wp-content/uploads/2024/08/1.png"
      },
      "description": "Golden Ticket Realty is a trusted cash home buyer in Melbourne, FL. We buy houses in any condition throughout Brevard County. No repairs, no fees, no commissions — just fair cash offers and fast closings.",
      "telephone": "+13213412201",
      "email": "info@goldenticketrealty.com",
      "priceRange": "$$$",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "",
        "addressLocality": "Melbourne",
        "addressRegion": "FL",
        "postalCode": "32901",
        "addressCountry": "US"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": "28.0836",
        "longitude": "-80.6081"
      },
      "areaServed": [
        {
          "@type": "City",
          "name": "Melbourne",
          "containedInPlace": {
            "@type": "State",
            "name": "Florida"
          }
        },
        {
          "@type": "City",
          "name": "Palm Bay"
        },
        {
          "@type": "City",
          "name": "Cocoa"
        },
        {
          "@type": "City",
          "name": "Cocoa Beach"
        },
        {
          "@type": "City",
          "name": "Rockledge"
        },
        {
          "@type": "City",
          "name": "Titusville"
        },
        {
          "@type": "City",
          "name": "Merritt Island"
        },
        {
          "@type": "City",
          "name": "Satellite Beach"
        },
        {
          "@type": "City",
          "name": "Viera"
        },
        {
          "@type": "City",
          "name": "Indialantic"
        },
        {
          "@type": "City",
          "name": "Indian Harbour Beach"
        },
        {
          "@type": "City",
          "name": "Cape Canaveral"
        },
        {
          "@type": "City",
          "name": "Melbourne Beach"
        }
      ],
      "openingHoursSpecification": [
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
          "opens": "08:00",
          "closes": "20:00"
        },
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": "Saturday",
          "opens": "09:00",
          "closes": "17:00"
        }
      ],
      "sameAs": [
        "https://www.facebook.com/goldenticketrealty",
        "https://www.instagram.com/golden_ticket_realty",
        "https://www.linkedin.com/company/golden-ticket-realty/"
      ],
      "hasOfferCatalog": {
        "@type": "OfferCatalog",
        "name": "Cash Home Buying Services",
        "itemListElement": [
          {
            "@type": "Offer",
            "itemOffered": {
              "@type": "Service",
              "name": "Cash Home Purchase",
              "description": "We buy houses in Melbourne FL and Brevard County for cash, as-is, with no repairs or commissions."
            }
          },
          {
            "@type": "Offer",
            "itemOffered": {
              "@type": "Service",
              "name": "Foreclosure Assistance",
              "description": "Fast cash sales to help homeowners avoid foreclosure in Brevard County."
            }
          },
          {
            "@type": "Offer",
            "itemOffered": {
              "@type": "Service",
              "name": "Inherited Property Sales",
              "description": "Quick and hassle-free sales for inherited homes in Melbourne and surrounding areas."
            }
          }
        ]
      }
    },
    {
      "@type": "WebSite",
      "@id": "https://goldenticketrealty.com/#website",
      "url": "https://goldenticketrealty.com/",
      "name": "Golden Ticket Realty",
      "publisher": {
        "@id": "https://goldenticketrealty.com/#realestateagent"
      }
    },
    {
      "@type": "WebPage",
      "@id": "https://goldenticketrealty.com/",
      "url": "https://goldenticketrealty.com/",
      "name": "Sell Your House Fast in Melbourne, FL | Golden Ticket Realty",
      "isPartOf": {
        "@id": "https://goldenticketrealty.com/#website"
      },
      "about": {
        "@id": "https://goldenticketrealty.com/#realestateagent"
      },
      "description": "Sell your house fast in Melbourne, FL with Golden Ticket Realty – trusted local cash homebuyers. Avoid repairs, fees, and delays—quick and hassle-free."
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://goldenticketrealty.com/#breadcrumb",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://goldenticketrealty.com/"
        }
      ]
    }
  ]
}
```

---

## 2. Service Page Schema: HowTo + FAQPage

Use on `/how-we-buy-houses/` or `/sell-your-house/`:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "HowTo",
      "name": "How to Sell Your House Fast in Melbourne, FL",
      "description": "A simple 4-step guide to selling your Melbourne home for cash with Golden Ticket Realty.",
      "totalTime": "P14D",
      "estimatedCost": {
        "@type": "MonetaryAmount",
        "currency": "USD",
        "value": "0"
      },
      "step": [
        {
          "@type": "HowToStep",
          "position": 1,
          "name": "Contact Us",
          "text": "Call (321) 341-2201 or fill out our online form with your property address and contact information.",
          "url": "https://goldenticketrealty.com/sell-your-house/#step1"
        },
        {
          "@type": "HowToStep",
          "position": 2,
          "name": "Property Walkthrough",
          "text": "We schedule a convenient time to view your home. No cleaning, repairs, or staging required.",
          "url": "https://goldenticketrealty.com/sell-your-house/#step2"
        },
        {
          "@type": "HowToStep",
          "position": 3,
          "name": "Receive Cash Offer",
          "text": "Get a fair, no-obligation cash offer within 24 hours of our visit.",
          "url": "https://goldenticketrealty.com/sell-your-house/#step3"
        },
        {
          "@type": "HowToStep",
          "position": 4,
          "name": "Close and Get Paid",
          "text": "Choose your closing date. We handle all paperwork and you walk away with cash.",
          "url": "https://goldenticketrealty.com/sell-your-house/#step4"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How fast can I sell my house in Melbourne, FL?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "With Golden Ticket Realty, you can close in as little as 7 to 14 days. We make a cash offer within 24 hours of viewing your property and let you choose the closing date that works best for you."
          }
        },
        {
          "@type": "Question",
          "name": "Do I need to make repairs before selling?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No. We buy houses as-is in any condition. You do not need to clean, repair, or stage your home. We handle everything after purchase."
          }
        },
        {
          "@type": "Question",
          "name": "Are there any fees or commissions?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No. There are zero agent commissions, closing costs, or hidden fees when you sell to Golden Ticket Realty. The offer we make is the amount you receive at closing."
          }
        },
        {
          "@type": "Question",
          "name": "What areas in Brevard County do you buy in?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "We buy houses throughout Brevard County including Melbourne, Palm Bay, Cocoa, Cocoa Beach, Rockledge, Titusville, Merritt Island, Satellite Beach, Viera, Indialantic, Indian Harbour Beach, Cape Canaveral, and Melbourne Beach."
          }
        }
      ]
    }
  ]
}
```

---

## 3. FAQ Page Schema

Use on `/faqs/`:

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How does Golden Ticket Realty differ from a traditional real estate agent?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Unlike traditional agents who list your home and charge 5-6% in commissions, Golden Ticket Realty buys your home directly for cash. There are no showings, no open houses, no repairs, and no waiting for buyer financing."
      }
    },
    {
      "@type": "Question",
      "name": "What types of houses do you buy in Melbourne?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We buy all types of residential properties in Melbourne and Brevard County: single-family homes, condos, townhomes, duplexes, and even properties in need of major repairs."
      }
    },
    {
      "@type": "Question",
      "name": "How is the cash offer calculated?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Our cash offers are based on current Melbourne market conditions, comparable sales, the property’s condition, and estimated repair costs. We aim to make fair, transparent offers that reflect true market value."
      }
    },
    {
      "@type": "Question",
      "name": "Can I sell if my house is in foreclosure?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Selling to a cash buyer can stop foreclosure proceedings if the sale closes before the auction date. We work with tight timelines and can close in as little as 7 days."
      }
    },
    {
      "@type": "Question",
      "name": "What if I already have a tenant in the property?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We buy rental properties with tenants in place. You do not need to evict or wait for a lease to end. We handle the transition and honor existing lease terms when applicable."
      }
    }
  ]
}
```

---

## 4. Blog Post Schema: Article

Use on every blog post:

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "How to Sell Your House Fast in Melbourne, FL — A Homeowner’s Guide",
  "description": "Learn how to sell your house fast in Melbourne, FL with Golden Ticket Realty. No repairs, no fees, fair cash offers in 24 hours.",
  "image": "https://goldenticketrealty.com/wp-content/uploads/2024/08/blog-featured-image.jpg",
  "author": {
    "@type": "Person",
    "name": "Martin Pacheco",
    "url": "https://goldenticketrealty.com/our-company/"
  },
  "publisher": {
    "@type": "RealEstateAgent",
    "name": "Golden Ticket Realty",
    "logo": {
      "@type": "ImageObject",
      "url": "https://goldenticketrealty.com/wp-content/uploads/2024/08/1.png"
    }
  },
  "datePublished": "2026-09-17T09:00:00-04:00",
  "dateModified": "2026-09-17T09:00:00-04:00",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://goldenticketrealty.com/blog/sell-house-fast-melbourne/"
  }
}
```

---

## 5. BreadcrumbList Schema (Inner Pages)

Add to every inner page. Example for `/sell-your-house/`:

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://goldenticketrealty.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Sell Your House",
      "item": "https://goldenticketrealty.com/sell-your-house/"
    }
  ]
}
```

---

## 6. Review / AggregateRating Schema

Add to `/testimonials/`:

```json
{
  "@context": "https://schema.org",
  "@type": "RealEstateAgent",
  "name": "Golden Ticket Realty",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "5.0",
    "reviewCount": "12",
    "bestRating": "5",
    "worstRating": "1"
  },
  "review": [
    {
      "@type": "Review",
      "author": {
        "@type": "Person",
        "name": "Homeowner in Melbourne"
      },
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": "5"
      },
      "reviewBody": "Golden Ticket Realty made selling our inherited home incredibly easy. They handled everything and we closed in 10 days. Highly recommend!"
    }
  ]
}
```

---

## 7. ImageObject Schema (For Local SEO / AI Citation)

Add to pages with hero/city images:

```json
{
  "@context": "https://schema.org",
  "@type": "ImageObject",
  "contentUrl": "https://goldenticketrealty.com/wp-content/uploads/2024/08/melbourne-hero.webp",
  "description": "Golden Ticket Realty buys houses in Melbourne FL — Downtown Melbourne skyline",
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "28.0836",
    "longitude": "-80.6081"
  }
}
```

---

## Implementation Instructions

### Option A: Custom Plugin (Recommended)
1. Create a plugin folder: `wp-content/plugins/gtr-schema/`
2. Add `gtr-schema.php` with `wp_head` hooks that output the JSON-LD
3. Use conditional logic: `is_front_page()`, `is_page('faqs')`, `is_single()`, etc.
4. Activate plugin in WordPress admin

### Option B: functions.php
Add JSON-LD output functions to the child theme `functions.php`.  
**Risk:** Theme updates may overwrite changes. Use a child theme.

### Option C: Schema Plugin
- **Schema Pro** or **Rank Math** can handle RealEstateAgent schema
- Configure business details in plugin settings
- Map schema types to page templates

### Validation
After deployment, test every page:
- [ ] Google Rich Results Test: https://search.google.com/test/rich-results
- [ ] Schema.org Validator: https://validator.schema.org/
- [ ] GSC → Enhancements → check for errors
