import os, re

DOMAIN = "https://sellmyhousefastcocoa.com"
PHONE = "321-450-7457"

# 1. CREATE robots.txt
robots = f"""User-agent: *
Allow: /
Disallow: /test-ctrl.html

Sitemap: {DOMAIN}/sitemap.xml
"""
with open('robots.txt', 'w') as f:
    f.write(robots)
print("Created robots.txt")

# 2. CREATE .htaccess with security headers
htaccess = """# Security Headers
<IfModule mod_headers.c>
    Header always set X-Frame-Options "SAMEORIGIN"
    Header always set X-Content-Type-Options "nosniff"
    Header always set Referrer-Policy "strict-origin-when-cross-origin"
    Header always set Permissions-Policy "geolocation=(), microphone=(), camera=()"
    Header always set Strict-Transport-Security "max-age=63072000; includeSubDomains; preload"
    Header always set Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline' https://www.googletagmanager.com https://www.google-analytics.com https://assets.leadconnectorhq.com https://api.leadconnectorhq.com; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; font-src 'self'; frame-src https://api.leadconnectorhq.com https://www.google.com; connect-src 'self' https://www.google-analytics.com https://api.leadconnectorhq.com;"
    <FilesMatch "\\.(png|jpg|jpeg|gif|ico|svg|webp|pdf|css|js)$">
        Header always set X-Frame-Options "SAMEORIGIN"
        Header always set X-Content-Type-Options "nosniff"
        Header always set Referrer-Policy "strict-origin-when-cross-origin"
        Header always set Strict-Transport-Security "max-age=63072000; includeSubDomains; preload"
    </FilesMatch>
</IfModule>

# Enable compression
<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/html text/css text/javascript application/javascript application/json
</IfModule>

# Cache control for static assets
<IfModule mod_expires.c>
    ExpiresActive On
    ExpiresByType image/jpeg "access plus 1 year"
    ExpiresByType image/png "access plus 1 year"
    ExpiresByType image/webp "access plus 1 year"
    ExpiresByType text/css "access plus 1 month"
    ExpiresByType application/javascript "access plus 1 month"
</IfModule>
"""
with open('.htaccess', 'w') as f:
    f.write(htaccess)
print("Created .htaccess")

# 3. FIX sitemap.xml
with open('sitemap.xml', 'r') as f:
    sitemap_content = f.read()

existing_urls = set(re.findall(r'<loc>([^<]+)</loc>', sitemap_content))
html_files = sorted([f for f in os.listdir('.') if f.endswith('.html')])

url_entries = []
for fname in html_files:
    if fname == 'test-ctrl.html':
        continue
    if fname == 'index.html':
        url = f"{DOMAIN}/"
        priority = "1.0"
        changefreq = "weekly"
    elif fname.startswith('blog-'):
        url = f"{DOMAIN}/{fname.replace('.html', '')}"
        priority = "0.6"
        changefreq = "monthly"
    elif fname == 'blog.html':
        url = f"{DOMAIN}/blog"
        priority = "0.7"
        changefreq = "weekly"
    elif fname in ['privacy.html', 'terms.html']:
        url = f"{DOMAIN}/{fname.replace('.html', '')}"
        priority = "0.3"
        changefreq = "yearly"
    elif fname.startswith('sell-my-house-fast-'):
        url = f"{DOMAIN}/{fname.replace('.html', '')}"
        priority = "0.8"
        changefreq = "monthly"
    else:
        url = f"{DOMAIN}/{fname.replace('.html', '')}"
        priority = "0.8"
        changefreq = "monthly"
    url_entries.append(f"  <url><loc>{url}</loc><lastmod>2026-09-04</lastmod><changefreq>{changefreq}</changefreq><priority>{priority}</priority></url>")

url_lines = "\n".join(url_entries)
sitemap = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n" + url_lines + "\n</urlset>"

with open('sitemap.xml', 'w') as f:
    f.write(sitemap)
print(f"Updated sitemap.xml with {len(url_entries)} URLs")

# 4. FIX H1s and canonicals on service pages
def add_h1_and_canonical(filepath, h1_text, canonical_path):
    with open(filepath, 'r', errors='ignore') as f:
        content = f.read()
    
    if 'rel="canonical"' not in content:
        canonical_tag = f'<link rel="canonical" href="{DOMAIN}/{canonical_path}">'
        content = content.replace('<meta name="viewport" content="width=device-width, initial-scale=1.0">', 
                                  f'<meta name="viewport" content="width=device-width, initial-scale=1.0">\n{canonical_tag}')
        print(f"  Added canonical to {filepath}")
    
    if '<h1' not in content.lower():
        h1_html = f'''<section class="section" style="padding-bottom:0;">
<div class="container">
<h1 style="color:var(--primary);font-size:2.2rem;margin-bottom:0.5rem;">{h1_text}</h1>
</div>
</section>
'''
        match = re.search(r'(</div>\s*</div>\s*</div>\s*<section class="section">)', content)
        if match:
            content = content.replace(match.group(1), f'{h1_html}<section class="section">')
        else:
            content = re.sub(r'(<section class="section">)', h1_html + r'\1', content, count=1)
        print(f"  Added H1 to {filepath}")
    
    with open(filepath, 'w') as f:
        f.write(content)

add_h1_and_canonical('divorce.html', 'Sell Your House Fast During Divorce in Cocoa, FL', 'divorce')
add_h1_and_canonical('job-relocation.html', 'Sell Your House Fast for Job Relocation in Cocoa, FL', 'job-relocation')
add_h1_and_canonical('tired-landlords.html', 'Sell Your Rental Property Fast in Cocoa, FL', 'tired-landlords')

# 5. FIX test-ctrl.html canonical
with open('test-ctrl.html', 'r', errors='ignore') as f:
    content = f.read()
if 'rel="canonical"' not in content:
    canonical_tag = f'<link rel="canonical" href="{DOMAIN}/tired-landlords">'
    content = content.replace('<meta name="viewport" content="width=device-width, initial-scale=1.0">', 
                              f'<meta name="viewport" content="width=device-width, initial-scale=1.0">\n{canonical_tag}')
    with open('test-ctrl.html', 'w') as f:
        f.write(content)
    print("Added canonical to test-ctrl.html")

# 6. FIX titles
title_fixes = {
    'blog-august-pcs-patrick-sfb-cocoa.html': (
        'August PCS Rush at Patrick SFB: How Cocoa Military Families Can Sell Fast',
        'August PCS: Sell Fast in Cocoa, FL | Military Families'
    ),
    'blog-divorce-home-sale-cocoa.html': (
        'Divorce and Home Sale in Cocoa, FL: Protecting Your Equity During Separation',
        'Divorce Home Sale Cocoa, FL | Protect Equity Fast'
    ),
    'blog-divorce-mediation-property-cocoa.html': (
        'Divorce Mediation and Property Sale in Cocoa, FL: What to Expect',
        'Divorce Mediation Property Sale Cocoa, FL | Guide'
    ),
    'blog-job-relocation-sell-fast-cocoa.html': (
        'Job Relocation in Cocoa, FL: How to Sell Your House in 30 Days or Less',
        'Job Relocation Cocoa, FL | Sell in 30 Days'
    ),
    'blog-military-divorce-home-sale-cocoa.html': (
        'Military Divorce and Home Sales in Brevard County: A Dual Challenge',
        'Military Divorce Home Sale Brevard | Cash Buyers'
    ),
    'blog-pcs-patrick-sfb-cocoa.html': (
        'PCS from Patrick SFB: Military Home Sale Guide for Cocoa Families',
        'PCS Patrick SFB | Military Home Sale Guide Cocoa'
    ),
    'blog-pcs-sell-house-cocoa.html': (
        'PCS from Patrick SFB: How to Sell Your House in 14 Days | Cocoa Cash Home Buyers | 321-450-7457',
        'PCS Patrick SFB | Sell House in 14 Days Cocoa'
    ),
    'blog-pcs-timeline-cocoa.html': (
        'PCS Timeline: When to List Your Cocoa Home Before Your Transfer Date',
        'PCS Timeline Cocoa, FL | When to List Home'
    ),
    'blog-relocate-new-job-cocoa.html': (
        'Relocating for a New Job? Sell Your Cocoa House Before You Start',
        'Relocating for New Job? Sell Cocoa House Fast'
    ),
    'blog-rental-property-taxes-cocoa.html': (
        'Rental Property Taxes in Cocoa, FL: What Landlords Need to Know Before Selling',
        'Rental Property Taxes Cocoa, FL | Landlord Guide'
    ),
    'blog-sell-house-during-divorce-cocoa.html': (
        'How to Sell Your House During a Divorce in Cocoa, FL: Step-by-Step',
        'Sell House During Divorce Cocoa, FL | Step Guide'
    ),
    'blog-sell-rental-cocoa.html': (
        'How to Sell a Rental Property in Cocoa, FL | Tired Landlord Guide | July 2026',
        'Sell Rental Property Cocoa, FL | Landlord Guide'
    ),
    'blog-sell-rental-tenants-cocoa.html': (
        "Selling a Rental Property with Tenants in Cocoa, FL: A Landlord's Complete Guide",
        'Sell Rental with Tenants Cocoa, FL | Guide'
    ),
    'blog-separation-home-sale-cocoa.html': (
        'Selling a House in Cocoa During a Separation: Legal and Financial Tips',
        'Sell House During Separation Cocoa, FL | Tips'
    ),
    'blog-tired-landlord-no-eviction-cocoa.html': (
        'Tired Landlord in Cocoa? How to Sell Without Evicting Your Tenants',
        'Tired Landlord Cocoa, FL | Sell Without Eviction'
    ),
    'blog-year-end-sell-rental-cocoa.html': (
        'Year-End Tax Benefits of Selling a Rental Property in Cocoa, FL',
        'Year-End Tax Benefits | Sell Rental Cocoa, FL'
    ),
    'divorce.html': (
        'Sell House During Divorce Cocoa, FL | Fast Cash Sale | 321-450-7457',
        'Sell House During Divorce Cocoa, FL | Cash Sale'
    ),
    'faq.html': (
        'FAQ | Sell My House Fast Cocoa, FL | Cash Home Buyers',
        'FAQ | Sell My House Fast Cocoa, FL | Buyers'
    ),
    'index.html': (
        'Sell My House Fast Cocoa, FL | Cash Home Buyers | 321-450-7457',
        'Sell My House Fast Cocoa, FL | Cash Buyers'
    ),
    'job-relocation.html': (
        'Sell House Fast Job Relocation Cocoa, FL | Cash Buyers | 321-450-7457',
        'Sell House Fast Job Relocation Cocoa, FL | Buyers'
    ),
    'pricing.html': (
        'How Much Do Cash Buyers Pay in Cocoa, FL? | 321-450-7457',
        'How Much Do Cash Buyers Pay in Cocoa, FL?'
    ),
    'sell-my-house-fast-cape-canaveral.html': (
        'Sell My House Fast Cape Canaveral, FL | Cash Buyers | 321-450-7457',
        'Sell My House Fast Cape Canaveral, FL | Buyers'
    ),
    'sell-my-house-fast-cocoa-beach.html': (
        'Sell My House Fast Cocoa Beach, FL | Cash Buyers | 321-450-7457',
        'Sell My House Fast Cocoa Beach, FL | Buyers'
    ),
    'sell-my-house-fast-cocoa.html': (
        'Sell My House Fast Cocoa, FL | Cash Buyers | 321-450-7457',
        'Sell My House Fast Cocoa, FL | Cash Buyers'
    ),
    'sell-my-house-fast-melbourne.html': (
        'Sell My House Fast Melbourne, FL | Cash Buyers | 321-450-7457',
        'Sell My House Fast Melbourne, FL | Buyers'
    ),
    'sell-my-house-fast-merritt-island.html': (
        'Sell My House Fast Merritt Island, FL | Cash Buyers | 321-450-7457',
        'Sell My House Fast Merritt Island, FL | Buyers'
    ),
    'sell-my-house-fast-palm-bay.html': (
        'Sell My House Fast Palm Bay, FL | Cash Buyers | 321-450-7457',
        'Sell My House Fast Palm Bay, FL | Buyers'
    ),
    'sell-my-house-fast-rockledge.html': (
        'Sell My House Fast Rockledge, FL | Cash Buyers | 321-450-7457',
        'Sell My House Fast Rockledge, FL | Buyers'
    ),
    'sell-my-house-fast-satellite-beach.html': (
        'Sell My House Fast Satellite Beach, FL | Cash Buyers | 321-450-7457',
        'Sell My House Fast Satellite Beach, FL | Buyers'
    ),
    'sell-my-house-fast-titusville.html': (
        'Sell My House Fast Titusville, FL | Cash Buyers | 321-450-7457',
        'Sell My House Fast Titusville, FL | Buyers'
    ),
    'sell-my-house-fast-viera.html': (
        'Sell My House Fast Viera, FL | Cash Buyers | 321-450-7457',
        'Sell My House Fast Viera, FL | Buyers'
    ),
    'test-ctrl.html': (
        'Sell My Rental Property Cocoa, FL | Tired Landlord Cash Buyers | 321-555-0199',
        'Sell My Rental Property Cocoa, FL | Buyers'
    ),
    'testimonials.html': (
        'Reviews | Cocoa Cash Home Buyers | 321-450-7457',
        'Reviews | Cocoa Cash Home Buyers | 321-450-7457'
    ),
    'tired-landlords.html': (
        'Sell My Rental Property Cocoa, FL | Tired Landlord Cash Buyers | 321-450-7457',
        'Sell My Rental Property Cocoa, FL | Buyers'
    ),
}

fixed_count = 0
for fname, (old_title, new_title) in title_fixes.items():
    if not os.path.exists(fname):
        continue
    with open(fname, 'r', errors='ignore') as f:
        content = f.read()
    if old_title in content and len(new_title) <= 60:
        content = content.replace(f'<title>{old_title}</title>', f'<title>{new_title}</title>')
        with open(fname, 'w') as f:
            f.write(content)
        fixed_count += 1
        print(f"  Fixed title: {fname} ({len(new_title)} chars)")
    elif old_title in content and len(new_title) > 60:
        print(f"  WARNING: New title still too long for {fname}: {new_title} ({len(new_title)} chars)")

# 7. FIX meta descriptions
meta_fixes = {
    'divorce.html': (
        'Divorcing in Brevard County? Sell your house fast during divorce without fighting over repairs, showings, or commissions. Cash offer in 24 hrs. Call 321-450-7457.',
        'Divorcing in Brevard County? Sell fast without repairs or commissions. Cash offer in 24 hrs. Call 321-450-7457.'
    ),
    'job-relocation.html': (
        'Relocating from Cocoa or Brevard County? Sell your house fast before you move. Cash buyers, no repairs, close in 7-14 days. Call 321-450-7457 for a fair offer.',
        'Relocating from Cocoa? Sell fast before you move. No repairs, close in 7-14 days. Call 321-450-7457.'
    ),
    'index.html': (
        'Sell your house fast in Cocoa, FL. We buy homes from tired landlords, divorcing couples, relocating families & inherited properties. Fair cash offer in 24 hours. Call 321-450-7457.',
        'Sell your house fast in Cocoa, FL. We buy homes as-is. Fair cash offer in 24 hours. Call 321-450-7457.'
    ),
    'pricing.html': (
        "Wondering how much cash buyers pay for houses in Cocoa, FL? We explain our pricing formula, compare cash vs. retail sale & show you how much you'll actually net. Call 321-450-7457.",
        'How much do cash buyers pay in Cocoa, FL? See our pricing formula & compare cash vs. retail. Call 321-450-7457.'
    ),
    'blog-sell-rental-cocoa.html': (
        'Thinking about selling a rental property in Cocoa, FL? This guide covers your options, tax implications, tenant rights & how to sell fast for cash. Call 321-450-7457.',
        'Selling a rental property in Cocoa, FL? Guide to options, taxes & fast cash sales. Call 321-450-7457.'
    ),
    'test-ctrl.html': (
        'Burned out landlord in Cocoa, FL? We buy rental properties with tenants inside. No evictions, no repairs, no hassle. Fair cash offer in 24 hours. Close in 7-14 days. Call 321-555-0199.',
        'Burned out landlord in Cocoa, FL? We buy rental properties as-is. Cash offer in 24 hrs. Close in 7-14 days.'
    ),
    'tired-landlords.html': (
        'Burned out landlord in Cocoa, FL? We buy rental properties with tenants inside. No evictions, no repairs, no hassle. Fair cash offer in 24 hours. Close in 7-14 days. Call 321-450-7457.',
        'Burned out landlord in Cocoa, FL? We buy rentals with tenants inside. No evictions or repairs. Call 321-450-7457.'
    ),
    'blog-tired-landlord-no-eviction-cocoa.html': (
        'Burned out landlord in Cocoa, FL? Learn how to sell your rental property without evicting tenants \u2014 including selling to cash buyers who honor existing leases.',
        'Burned out landlord in Cocoa, FL? Learn how to sell without evicting tenants. Cash buyers honor leases.'
    ),
    'blog-year-end-sell-rental-cocoa.html': (
        'Thinking about selling a rental property in Cocoa before year-end? Learn the tax benefits, depreciation recapture rules & how to close before December 31. Call 321-450-7457.',
        'Selling a rental in Cocoa before year-end? Learn tax benefits & depreciation rules. Call 321-450-7457.'
    ),
    'blog-pcs-sell-house-cocoa.html': (
        'PCS orders from Patrick Space Force Base? Learn how military families in Cocoa, FL can sell fast in 14 days without repairs, showings, or agent fees. Call 321-450-7457.',
        'PCS from Patrick SFB? Sell your Cocoa house in 14 days. No repairs or fees. Call 321-450-7457.'
    ),
    'blog-divorce-mediation-property-cocoa.html': (
        'Going through divorce mediation in Cocoa, FL? Learn how property sales are handled, who gets what & how a cash sale simplifies splitting assets. Call 321-450-7457.',
        'Divorce mediation in Cocoa, FL? Learn how property sales work & how cash sales simplify splitting assets.'
    ),
    'blog-military-divorce-home-sale-cocoa.html': (
        'Facing military divorce in Brevard County? Learn how SCRA protections, VA loans & BAH affect your home sale. Sell fast for cash in Cocoa. Call 321-450-7457.',
        'Military divorce in Brevard County? Learn how SCRA & VA loans affect your home sale. Call 321-450-7457.'
    ),
    'terms.html': (
        'Terms and conditions for Cocoa Cash Home Buyers website and services.',
        'Terms and conditions for Cocoa Cash Home Buyers website and services. Read our policies before using the site.'
    ),
}

for fname, (old_meta, new_meta) in meta_fixes.items():
    if not os.path.exists(fname):
        continue
    with open(fname, 'r', errors='ignore') as f:
        content = f.read()
    if old_meta in content and len(new_meta) <= 155:
        content = content.replace(f'<meta name="description" content="{old_meta}">', 
                                  f'<meta name="description" content="{new_meta}">')
        with open(fname, 'w') as f:
            f.write(content)
        fixed_count += 1
        print(f"  Fixed meta: {fname} ({len(new_meta)} chars)")
    elif old_meta in content and len(new_meta) > 155:
        print(f"  WARNING: New meta still too long for {fname}: {len(new_meta)} chars")

print(f"Fixed {fixed_count} title/meta issues")

# 8. ADD favicon to pages missing it
favicon_tag = '<link rel="icon" type="image/png" href="/favicon.png" sizes="48x48">'
for fname in html_files:
    if fname == 'test-ctrl.html':
        continue
    with open(fname, 'r', errors='ignore') as f:
        content = f.read()
    if 'rel="icon"' not in content and '<head>' in content:
        content = content.replace('<meta name="viewport" content="width=device-width, initial-scale=1.0">',
                                  f'<meta name="viewport" content="width=device-width, initial-scale=1.0">\n{favicon_tag}')
        with open(fname, 'w') as f:
            f.write(content)
        print(f"  Added favicon to {fname}")

print("Done with batch 1 fixes!")
