#!/usr/bin/env python3
"""
Article generator for acalise.com app blogs.

Reads a per-app THEME + a list of article dicts and emits
<app>/blog/<slug>/index.html, matching the template already used across
the site (nav, article shell, answer boxes, FAQ, CTA, footer) and
emitting Article + FAQPage + WebSite + BreadcrumbList JSON-LD.

The CSS / nav / footer skeletons live next to this file in _style.css,
_nav.html and _footer.html; they were lifted verbatim from a shipped
article so generated pages are byte-comparable with hand-written ones.

Usage:  python3 tools/genarticle.py content_chartcheck.py
"""
import html
import importlib.util
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parent
STYLE = (HERE / '_style.css').read_text()

# The github.io -> acalise.com mirror guard every page on the site carries.
# Kept as a constant so its braces don't collide with f-string interpolation.
MIRROR_GUARD = (
    '<script>if(location.hostname==="acalise.github.io")'
    '{document.write(\'<meta name="robots" content="noindex,nofollow">\');'
    'location.replace("https://acalise.com"+location.pathname+location.search+location.hash);}</script>'
)

APPLE_SVG = (
    '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">'
    '<path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.8-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.83 1.94-1.46 2.94-1.5.13 1.17-.34 2.35-1.04 3.19-.69.85-1.83 1.51-2.95 1.42-.15-1.15.41-2.35 1.05-3.11z"/></svg>'
)


def e(s):
    """Escape for an HTML attribute / JSON string context."""
    return html.escape(s, quote=True)


def nav(app):
    if app['appstore_url']:
        cta = (
            f'<a href="{app["appstore_url"]}" class="nav-cta" rel="noopener">\n'
            f'      {APPLE_SVG}\n      {app["cta_label"]}\n    </a>'
        )
    else:
        # App not shipped yet - render the chip without a dead link.
        cta = f'<span class="nav-cta" aria-disabled="true">\n      {APPLE_SVG}\n      {app["cta_label"]}\n    </span>'
    return f'''<nav>
    <a href="/{app['slug']}/" class="nav-brand">
      <img src="../../icon.png" alt="{e(app['name'])} app icon">
      <span>{e(app['name'])}</span>
    </a>
    {cta}
  </nav>'''


def footer(app):
    store = (
        f'<a href="{app["appstore_url"]}" rel="noopener">App Store</a> &nbsp;&middot;&nbsp;\n      '
        if app['appstore_url'] else ''
    )
    return f'''<footer>
    <p>
      &copy; 2026 {e(app['name'])} &nbsp;&middot;&nbsp;
      {store}<a href="/{app['slug']}/blog/">Blog</a> &nbsp;&middot;&nbsp;
      <a href="https://acalise.com/privacy/{app['slug']}/">Privacy</a> &nbsp;&middot;&nbsp;
      <a href="https://acalise.com">acalise.com</a>
    </p>
    <p class="kw">{e(app['kw_footer'])}</p>
  </footer>'''


def cta_banner(app, a):
    label = a.get('cta_title') or app['cta_title']
    body = a.get('cta_body') or app['cta_body']
    if app['appstore_url']:
        btn = (f'<a href="{app["appstore_url"]}" class="btn" rel="noopener">{APPLE_SVG} {app["cta_label"]}</a>')
    else:
        btn = f'<span class="btn" aria-disabled="true">{APPLE_SVG} {app["cta_label"]}</span>'
    return f'''<div class="cta-banner">
      <h3>{e(label)}</h3>
      <p>{body}</p>
      {btn}
    </div>'''


def faq_html(faqs):
    out = ['<h2>Frequently asked questions</h2>']
    for q, ans in faqs:
        out.append(f'''<div class="faq-item">
      <h3>{e(q)}</h3>
      <p>{ans}</p>
    </div>''')
    return '\n    '.join(out)


def related_html(app, related, by_slug):
    if not related:
        return ''
    items = []
    for slug in related:
        title = by_slug.get(slug)
        if not title:
            raise SystemExit(f'related slug not found in this content set: {slug}')
        items.append(f'<li><a href="/{app["slug"]}/blog/{slug}/">{e(title)}</a></li>')
    inner = '\n      '.join(items)
    return f'<h2>Related Articles</h2>\n    <ul>\n      {inner}\n    </ul>'


def jsonld(app, a):
    url = f'https://acalise.com/{app["slug"]}/blog/{a["slug"]}/'
    icon = f'https://acalise.com/{app["slug"]}/icon.png'
    article = {
        "@context": "https://schema.org", "@type": "Article",
        "headline": a['seo_h1'], "description": a['meta_desc'],
        "author": {"@type": "Person", "name": "Anthony Calise", "url": "https://acalise.com"},
        "publisher": {"@type": "Organization", "name": app['name'],
                      "logo": {"@type": "ImageObject", "url": icon}},
        "datePublished": a['published'], "dateModified": a.get('modified', a['published']),
        "image": icon, "mainEntityOfPage": url,
    }
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": re.sub(r'<[^>]+>', '', ans)}}
        for q, ans in a['faqs']]}
    site = {"@context": "https://schema.org", "@type": "WebSite", "name": app['name'],
            "url": f'https://acalise.com/{app["slug"]}/'}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://acalise.com/"},
        {"@type": "ListItem", "position": 2, "name": app['name'], "item": f'https://acalise.com/{app["slug"]}/'},
        {"@type": "ListItem", "position": 3, "name": "Blog", "item": f'https://acalise.com/{app["slug"]}/blog/'},
        {"@type": "ListItem", "position": 4, "name": a['seo_h1'], "item": url}]}
    blocks = []
    for label, obj in (('Article', article), ('FAQPage', faq), ('WebSite', site), ('BreadcrumbList', crumbs)):
        blocks.append(f'  <!-- JSON-LD: {label} -->\n  <script type="application/ld+json">\n'
                      + json.dumps(obj, indent=2, ensure_ascii=False) + '\n  </script>')
    return '\n\n'.join(blocks)


def render(app, a, by_slug):
    url = f'https://acalise.com/{app["slug"]}/blog/{a["slug"]}/'
    icon = f'https://acalise.com/{app["slug"]}/icon.png'
    css = STYLE.replace('__ROOT__', app['root_css'])
    scope = (f'<section class="answer-box" aria-labelledby="scope">\n'
             f'      <h2 id="scope">Scope</h2>\n      <p>{a.get("scope") or app["scope"]}</p>\n    </section>')
    rel = related_html(app, a.get('related', []), by_slug)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  {MIRROR_GUARD}
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Primary SEO -->
  <title>{e(a['seo_title'])}</title>
  <meta name="description" content="{e(a['meta_desc'])}">
  <meta name="keywords" content="{e(a['keywords'])}">
  <link rel="canonical" href="{url}">

  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:url" content="{url}">
  <meta property="og:title" content="{e(a['og_title'])}">
  <meta property="og:description" content="{e(a['og_desc'])}">
  <meta property="og:image" content="{icon}">
  <meta property="og:site_name" content="{e(app['name'])}">
  <meta property="article:published_time" content="{a['published']}">
  <meta property="article:modified_time" content="{a.get('modified', a['published'])}">
  <meta property="article:author" content="Anthony Calise">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{e(a['og_title'])}">
  <meta name="twitter:description" content="{e(a['og_desc'])}">
  <meta name="twitter:image" content="{icon}">

  <!-- Favicon -->
  <link rel="icon" type="image/png" sizes="96x96" href="/assets/favicon-96.png">
  <link rel="icon" type="image/png" sizes="48x48" href="/assets/favicon.png">
  <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
  <link rel="icon" type="image/x-icon" href="/assets/favicon.ico">
  <link rel="apple-touch-icon" sizes="192x192" href="/{app['slug']}/icon.png">
  <link rel="manifest" href="/site.webmanifest">

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">

{jsonld(app, a)}

  <style>{css}</style>
</head>
<body>

  {nav(app)}

  <article class="article-wrapper">
    <div class="article-meta">
      <span class="badge">{e(a['badge'])}</span>
      <span class="date">Published {a['published_label']}</span>
    </div>

    <h1>{e(a['seo_h1'])}</h1>

    <p class="article-intro">{a['intro']}</p>

    <section class="answer-box" aria-labelledby="quick">
      <h2 id="quick">{e(a.get('quick_title', 'The short answer'))}</h2>
      <p>{a['quick_answer']}</p>
    </section>

    {a['body']}

    {cta_banner(app, a)}

    {faq_html(a['faqs'])}

    {rel}

    {scope}
  </article>

  {footer(app)}

</body>
</html>
'''


def main(content_path):
    spec = importlib.util.spec_from_file_location('content', content_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    app, articles = mod.APP, mod.ARTICLES
    by_slug = {a['slug']: a['seo_h1'] for a in articles}
    # Articles already on disk that this set links to but does not regenerate.
    by_slug.update(getattr(mod, 'EXTRA_TITLES', {}))
    written = []
    for a in articles:
        out = ROOT / app['slug'] / 'blog' / a['slug'] / 'index.html'
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(app, a, by_slug), encoding='utf-8')
        words = len(re.sub(r'<[^>]+>', ' ', a['body']).split())
        written.append((str(out.relative_to(ROOT)), words))
    for p, w in written:
        print(f'{w:5d} body words  {p}')
    print(f'\n{len(written)} articles written for {app["name"]}')


if __name__ == '__main__':
    main(sys.argv[1])
