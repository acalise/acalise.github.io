# -*- coding: utf-8 -*-
"""
Coach Dink blog content set.

Topic selection is demand-driven (Google autocomplete harvest, Oct 2026):
the product-matched "pickleball video analysis" / film-review cluster, the
rating-level cluster ("3.0 meaning", "self rating guide", "rating chart"),
and the shot/strategy terms a filmed-game report actually diagnoses (third
shot drop, dinking, resets, serve faults, kitchen, doubles, stacking).

Never write the trademarked rating brand anywhere in this set. Coach Dink's
rating is its own estimate, never official.

Articles live in tools/parts/coachdink_{a,b}.py with card copy inline.
APP['appstore_url'] is None until the app is live (renders "Coming soon").
"""
import importlib.util as _u
import pathlib as _p

APP = {
    'slug': 'coachdink',
    'name': 'Coach Dink',
    'appstore_url': None,
    'cta_label': 'Coming soon to the App Store',
    'cta_title': 'Film a game. Get coached.',
    'cta_body': 'Coach Dink watches video of your pickleball games and tells you the habits costing you points, why they matter, and the drills that fix them. Singles and doubles, on iPhone.',
    'kw_footer': 'ai pickleball coach · pickleball video analysis · pickleball drills · pickleball rating levels · third shot drop · pickleball doubles strategy',
    'root_css': ''':root {
      --bg: #0a100c; --bg2: #0f1712; --card: #141e18;
      --border: rgba(90,155,104,0.24); --border-soft: rgba(236,244,238,0.09);
      --accent: #5a9b68; --accent2: #3d7a4e; --accent-light: #c5e35a; --accent-glow: rgba(90,155,104,0.16);
      --text: #ecf4ee; --muted: #a2b3a7; --muted2: #6b7d70;
    }''',
    'scope': 'This article is general pickleball instruction for recreational players. Rules references follow the USA Pickleball rulebook as generally applied; check the current official rulebook and your local tournament or league rules for edge cases. Ratings discussed here are descriptive skill levels, and Coach Dink\'s rating is its own estimate for tracking progress, not an official rating from any pickleball organization. Coach Dink is made by the author of this site.',
}

ARTICLES = []
for _name in ('coachdink_a', 'coachdink_b'):
    _spec = _u.spec_from_file_location(_name, _p.Path(__file__).parent / 'parts' / f'{_name}.py')
    _mod = _u.module_from_spec(_spec)
    _spec.loader.exec_module(_mod)
    ARTICLES.extend(_mod.ARTICLES)

CLUSTERS = [
    ('Film and Improve', [
        'pickleball-video-analysis-app',
        'how-to-film-pickleball',
        'pickleball-film-review',
        'how-to-improve-at-pickleball',
        'beginner-pickleball-mistakes',
    ]),
    ('Ratings and Drills', [
        'pickleball-rating-levels-explained',
        'pickleball-self-rating-guide',
        'pickleball-drills-by-level',
    ]),
    ('Shots', [
        'third-shot-drop',
        'pickleball-dinking-tips',
        'pickleball-reset-shot',
        'pickleball-serve-tips',
    ]),
    ('Strategy and Rules', [
        'pickleball-kitchen-rules',
        'pickleball-doubles-strategy',
        'pickleball-stacking',
    ]),
]

INDEX = {
    'title': 'The Coach Dink Blog - Pickleball Tips, Drills and Video Analysis',
    'og_title': 'The Coach Dink Blog',
    'badge': 'The Coach Dink Blog',
    'h1': 'Film it. Fix it. Play better.',
    'blurb': 'Pickleball guides for recreational players: how to film and review your games, what the rating levels mean, and how to fix the shots and habits that cost the most points.',
    'meta_desc': 'Pickleball guides on filming and reviewing your games, rating levels, drills by level, the third shot drop, dinking, resets, serving, kitchen rules and doubles strategy.',
}
