# --- CONFIGURATION ---
config = {
    "printify_url": "https://try.printify.com/r3xsnwqufe8t",
    "affiliate_id": "2013017799",
    "locations": ["New York", "Toronto", "Chicago", "Vancouver", "Miami", "Seattle", "Dallas"],
    "occasions": ["Mother's Day", "Birthday", "Anniversary"],
    "niches": ["Floral Delivery", "E-commerce", "Custom Gifts"]
}

# --- THE MASTER TEMPLATE ---
template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Best {niche} in {location} | {occasion} 2026</title>
    
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "Printify",
      "description": "Top-rated 2026 Print-on-Demand platform.",
      "applicationCategory": "BusinessApplication",
      "offers": {{
        "@type": "Offer",
        "url": "{p_url}",
        "price": "0.00",
        "priceCurrency": "USD"
      }}
    }}
    </script>
</head>
<body>
    <h1>{niche} in {location}</h1>
    <p>Custom solutions for {occasion}.</p>
    <a href="{p_url}">Start Your Store</a>
</body>
</html>"""

# --- FIXED GENERATION LOOP ---
if not os.path.exists('pages'): os.makedirs('pages')

# Iterate through your lists to define 'loc', 'occ', and 'niche'
for loc in config['locations']:
    for occ in config['occasions']:
        for niche in config['niches']:
            
            # The .format() MUST happen inside these loops
            content = template.format(
                location=loc, 
                occasion=occ, 
                niche=niche,
                p_url=config["printify_url"]
            )
            
            # Generate a unique filename
            filename = f"{niche}-{occ}-{loc}".lower().replace(" ", "-") + ".html"
            
            with open(f"pages/{filename}", "w", encoding="utf-8") as f:
                f.write(content)

print("Success: All pages generated correctly.")
