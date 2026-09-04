import os, re

# Fix remaining titles and meta descriptions with EXACT matches

# Titles
fixes = [
    ('blog-pcs-sell-house-cocoa.html',
     '<title>PCS from Patrick SFB: How to Sell Your House in 14 Days | Cocoa Cash Home Buyers | July 2026</title>',
     '<title>PCS Patrick SFB | Sell House in 14 Days Cocoa</title>'),
]

for fname, old, new in fixes:
    if not os.path.exists(fname):
        continue
    with open(fname, 'r', errors='ignore') as f:
        content = f.read()
    if old in content:
        content = content.replace(old, new)
        with open(fname, 'w') as f:
            f.write(content)
        print(f"Fixed title: {fname}")

# Meta descriptions
meta_fixes = [
    ('blog-august-pcs-patrick-sfb-cocoa.html',
     '<meta name="description" content="August is peak PCS season at Patrick Space Force Base. Learn how military families in Cocoa, FL can sell their homes in 14 days or less before reporting date.">',
     '<meta name="description" content="August PCS season at Patrick SFB. Learn how military families in Cocoa, FL can sell homes in 14 days or less. Call 321-450-7457.">'),
    ('blog-divorce-mediation-property-cocoa.html',
     '<meta name="description" content="Going through divorce mediation in Cocoa, FL? Learn how property sales are handled in mediation, what agreements cover, and how to sell fast if mediation succeeds.">',
     '<meta name="description" content="Divorce mediation in Cocoa, FL? Learn how property sales work, what agreements cover, and how to sell fast. Call 321-450-7457.">'),
    ('blog-military-divorce-home-sale-cocoa.html',
     '<meta name="description" content="Facing military divorce in Brevard County? Learn how SCRA protections, VA loans, and property division work when selling your home during a military divorce.">',
     '<meta name="description" content="Military divorce in Brevard County? Learn how SCRA, VA loans, and property division work when selling. Call 321-450-7457.">'),
    ('blog-pcs-timeline-cocoa.html',
     '<meta name="description" content="PCS from Patrick SFB? Learn exactly when to list your Cocoa home before your transfer date, how to time the sale, and why cash buyers fit military timelines.">',
     '<meta name="description" content="PCS from Patrick SFB? Learn when to list your Cocoa home before transfer, and why cash buyers fit military timelines. Call 321-450-7457.">'),
    ('blog-sell-rental-cocoa.html',
     '<meta name="description" content="Thinking about selling a rental property in Cocoa, FL? This guide covers your options as a tired landlord, from listing with a realtor to selling for cash. Call 321-450-7457 for a fair cash offer.">',
     '<meta name="description" content="Selling a rental in Cocoa, FL? This guide covers your options from listing to cash sale. Call 321-450-7457 for a fair offer.">'),
    ('blog-year-end-sell-rental-cocoa.html',
     '<meta name="description" content="Thinking about selling a rental property in Cocoa before year-end? Learn the tax benefits, depreciation recapture strategies, and how to maximize your after-tax proceeds.">',
     '<meta name="description" content="Selling a rental in Cocoa before year-end? Learn tax benefits, depreciation recapture, and how to maximize proceeds. Call 321-450-7457.">'),
    ('blog.html',
     '<meta name="description" content="Real estate tips for Cocoa homeowners. Learn about selling rental properties, divorce home sales, military PCS moves, and cash buyer options in Brevard County.">',
     '<meta name="description" content="Real estate tips for Cocoa homeowners. Learn about selling rentals, divorce sales, PCS moves, and cash buyers in Brevard County.">'),
    ('divorce.html',
     '<meta name="description" content="Divorcing in Brevard County? Sell your house fast during divorce without fighting over repairs, showings, or listing delays. Fair cash offer. Close in 7-14 days. Both parties get paid. Call 321-450-7457.">',
     '<meta name="description" content="Divorcing in Brevard County? Sell fast without repairs or showings. Fair cash offer, close in 7-14 days. Call 321-450-7457.">'),
    ('index.html',
     '<meta name="description" content="Sell your house fast in Cocoa, FL. We buy homes from tired landlords, divorcing couples, and relocating families. Fair cash offers. Close in 7-14 days. No repairs, no fees. Call 321-450-7457.">',
     '<meta name="description" content="Sell your house fast in Cocoa, FL. We buy homes as-is. Fair cash offers, close in 7-14 days. No repairs or fees. Call 321-450-7457.">'),
    ('job-relocation.html',
     '<meta name="description" content="Relocating from Cocoa or Brevard County? Sell your house fast before you move. Cash offers in 24 hours. Close in 7-14 days. No repairs, no showings, no double mortgage. Call 321-450-7457.">',
     '<meta name="description" content="Relocating from Cocoa? Sell fast before you move. Cash offers in 24 hrs, close in 7-14 days. No repairs or showings. Call 321-450-7457.">'),
    ('pricing.html',
     '<meta name="description" content="Wondering how much cash buyers pay for houses in Cocoa, FL? We explain our pricing formula, compare cash vs. traditional sales, and show you exactly what to expect. Call 321-450-7457.">',
     '<meta name="description" content="How much do cash buyers pay in Cocoa, FL? We explain our pricing formula and compare cash vs. traditional sales. Call 321-450-7457.">'),
]

for fname, old, new in meta_fixes:
    if not os.path.exists(fname):
        continue
    with open(fname, 'r', errors='ignore') as f:
        content = f.read()
    if old in content:
        content = content.replace(old, new)
        with open(fname, 'w') as f:
            f.write(content)
        print(f"Fixed meta: {fname}")

print("Done with batch 2 fixes!")
