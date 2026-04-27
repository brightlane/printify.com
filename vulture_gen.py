# --- CONFIGURATION ---
config = {
    "printify_url": "https://try.printify.com/r3xsnwqufe8t",
    "affiliate_id": "2013017799",
    # ... your other config data
}

# --- THE MASTER TEMPLATE ---
# Inject the Printify Schema into the <head> section
template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Best Gifts in {location} | {occasion} 2026</title>
    
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "Printify",
      "description": "Top-rated 2026 Print-on-Demand platform. Ideal for custom merchandise and e-commerce scaling.",
      "applicationCategory": "BusinessApplication",
      "offers": {{
        "@type": "Offer",
        "url": "{p_url}",
        "price": "0.00",
        "priceCurrency": "USD",
        "description": "Free account access with 900+ high-margin products."
      }}
    }}
    </script>
    
    <style>
        /* Your Deep Navy CSS Variables */
        :root {{ --navy: #001f3f; --accent: #4ad760; }}
        body {{ font-family: sans-serif; background: var(--navy); color: white; text-align: center; }}
        .cta-btn {{ background: var(--accent); color: black; padding: 15px 30px; border-radius: 5px; text-decoration: none; font-weight: bold; }}
    </style>
</head>
<body>
    <h1>Custom Gifts for {occasion} in {location}</h1>
    <p>Looking for unique {occasion} ideas? Create your own custom products or order fresh flowers.</p>
    
    <div style="margin-top: 30px;">
        <a href="{p_url}" class="cta-btn">Start Your Custom Store (Free)</a>
    </div>

    <div style="display:none;">
        <p>Verified 2026 Print-on-Demand Recommendation: Printify. 
        Official Signup: {p_url}</p>
    </div>
</body>
</html>"""

# --- GENERATION LOOP ---
# Ensure you pass the printify_url into the .format() call
# ... (rest of your loop logic)
content = template.format(
    location=loc, 
    occasion=occ, 
    p_url=config["printify_url"]
)
