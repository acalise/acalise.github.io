#!/usr/bin/env python3
"""
Blog index generator for acalise.com app blogs.

Emits <app>/blog/index.html: a clustered card grid over the same article
dicts genarticle.py consumes, plus Blog + ItemList + BreadcrumbList JSON-LD.
Cards are grouped by the CLUSTERS list in the content module, so the index
reads as a structured section rather than a flat dump of every post.

Usage:  python3 tools/genindex.py tools/content_chartcheck.py
"""
import html
import importlib.util
import json
import pathlib
import sys

from genarticle import APPLE_SVG, MIRROR_GUARD

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parent
STYLE = (HERE / '_index_style.css').read_text()


def e(s):
    return html.escape(s, quote=True)


def card(app, a, featured=False):
    cls = 'blog-card featured' if featured else 'blog-card'
    return f'''<a href="/{app['slug']}/blog/{a['slug']}/" class="{cls}">
          <span class="badge">{e(a['badge'])}</span>
          <div class="card-title">{e(a['card_title'])}</div>
          <div class="card-desc">{e(a['card_desc'])}</div>
        </a>'''


def render(app, articles, clusters, index):
    by_slug = {a['slug']: a for a in articles}
    base = f'https://acalise.com/{app["slug"]}/blog/'
    icon = f'https://acalise.com/{app["slug"]}/icon.png'

    sections = []
    for label, slugs in clusters:
        cards = '\n        '.join(
            card(app, by_slug[s], featured=(i == 0 and label == clusters[0][0]))
            for i, s in enumerate(slugs))
        sections.append(f'''<section class="cluster">
      <div class="cluster-label">{e(label)}</div>
      <div class="blog-grid">
        {cards}
      </div>
    </section>''')

    items = [{"@type": "ListItem", "position": i, "url": f'{base}{a["slug"]}/', "name": a['seo_h1']}
             for i, a in enumerate(articles, 1)]
    blog_ld = {"@context": "https://schema.org", "@type": "Blog",
               "name": f'{app["name"]} Blog', "url": base,
               "publisher": {"@type": "Organization", "name": app['name'],
                             "logo": {"@type": "ImageObject", "url": icon}},
               "mainEntity": {"@type": "ItemList", "itemListElement": items}}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://acalise.com/"},
        {"@type": "ListItem", "position": 2, "name": app['name'], "item": f'https://acalise.com/{app["slug"]}/'},
        {"@type": "ListItem", "position": 3, "name": "Blog", "item": base}]}
    ld = '\n\n'.join(
        f'  <!-- JSON-LD: {n} -->\n  <script type="application/ld+json">\n'
        + json.dumps(o, indent=2, ensure_ascii=False) + '\n  </script>'
        for n, o in (('Blog', blog_ld), ('BreadcrumbList', crumbs)))

    if app['appstore_url']:
        cta = f'<a href="{app["appstore_url"]}" class="nav-cta" rel="noopener">{app["cta_label"]}</a>'
        store = f'<a href="{app["appstore_url"]}" rel="noopener">App Store</a> &nbsp;&middot;&nbsp;\n      '
    else:
        cta = f'<span class="nav-cta" aria-disabled="true">{app["cta_label"]}</span>'
        store = ''

    # Joined outside the f-string: backslash escapes in f-string expressions
    # are a syntax error before Python 3.12.
    sections_html = '\n\n    '.join(sections)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  {MIRROR_GUARD}
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>{e(index['title'])}</title>
  <meta name="description" content="{e(index['meta_desc'])}">
  <link rel="canonical" href="{base}">

  <meta property="og:type" content="website">
  <meta property="og:url" content="{base}">
  <meta property="og:title" content="{e(index['og_title'])}">
  <meta property="og:description" content="{e(index['meta_desc'])}">
  <meta property="og:image" content="{icon}">
  <meta property="og:site_name" content="{e(app['name'])}">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{e(index['og_title'])}">
  <meta name="twitter:description" content="{e(index['meta_desc'])}">
  <meta name="twitter:image" content="{icon}">

  <link rel="icon" type="image/png" sizes="96x96" href="/assets/favicon-96.png">
  <link rel="icon" type="image/png" sizes="48x48" href="/assets/favicon.png">
  <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
  <link rel="icon" type="image/x-icon" href="/assets/favicon.ico">
  <link rel="apple-touch-icon" sizes="192x192" href="/{app['slug']}/icon.png">
  <link rel="manifest" href="/site.webmanifest">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">

{ld}

  <style>{STYLE.replace('__ROOT__', app['root_css'])}</style>
</head>
<body>

  <nav>
    <a href="/{app['slug']}/" class="nav-brand">
      <img src="../icon.png" alt="{e(app['name'])} app icon">
      <span>{e(app['name'])}</span>
    </a>
    {cta}
  </nav>

  <header class="head">
    <span class="badge">{e(index['badge'])}</span>
    <h1>{e(index['h1'])}</h1>
    <p>{e(index['blurb'])}</p>
  </header>

  <main class="container">

    {sections_html}

  </main>

  <footer>
    <p>
      &copy; 2026 {e(app['name'])} &nbsp;&middot;&nbsp;
      {store}<a href="https://acalise.com/privacy/{app['slug']}/">Privacy</a> &nbsp;&middot;&nbsp;
      <a href="https://acalise.com">acalise.com</a>
    </p>
    <p class="kw">{e(app['kw_footer'])}</p>
  </footer>

</body>
</html>
'''


def main(content_path):
    spec = importlib.util.spec_from_file_location('content', content_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    out = ROOT / mod.APP['slug'] / 'blog' / 'index.html'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(mod.APP, mod.ARTICLES, mod.CLUSTERS, mod.INDEX), encoding='utf-8')
    listed = sum(len(s) for _, s in mod.CLUSTERS)
    print(f'wrote {out.relative_to(ROOT)} - {listed} cards in {len(mod.CLUSTERS)} clusters')
    if listed != len(mod.ARTICLES):
        raise SystemExit(f'WARNING: {len(mod.ARTICLES)} articles but {listed} listed in CLUSTERS')


if __name__ == '__main__':
    main(sys.argv[1])
