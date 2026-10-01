# -*- coding: utf-8 -*-
"""
Coach Dink blog content, part A (8 articles): video analysis, filming,
ratings, mistakes, improvement, film review, drills by level.

Demand source: Google autocomplete harvest, Oct 2026 (pickleball video
analysis / rating levels / self rating / beginner mistakes / drills for
3.0-4.0 clusters). Never name the trademarked rating system; Coach Dink's
rating is its own estimate.
"""

ARTICLES = []

# ---------------------------------------------------------------- 1
ARTICLES.append({
    'slug': 'pickleball-video-analysis-app',
    'seo_title': 'Pickleball Video Analysis: Apps, Coaches, or DIY?',
    'seo_h1': 'Pickleball Video Analysis: Apps, Coaches, or Reviewing It Yourself',
    'og_title': 'Pickleball Video Analysis: Which Approach Actually Helps',
    'meta_desc': 'The three ways to get pickleball video analysis, compared honestly: your own film review, a coach, and AI apps. What each one catches and misses.',
    'og_desc': 'Self review, coach review, or an AI app: what each kind of pickleball video analysis catches and what it misses.',
    'keywords': 'pickleball video analysis, ai pickleball video analysis, pickleball video analysis app, pickleball video analysis software, best pickleball video app, pickleball analysis app',
    'badge': 'Comparison',
    'published': '2026-10-01', 'published_label': 'October 1, 2026',
    'card_title': 'Pickleball video analysis: apps, coaches, or DIY',
    'card_desc': 'What each kind of video review catches, what it misses, and which one fits where you are.',
    'intro': 'Filming your games is the fastest way to find out what is actually costing you points, because what you remember about a rally and what happened in it are usually different things. The harder question is who, or what, watches the video. There are three real options, and they are good at different things.',
    'quick_answer': 'Reviewing your own film is free and builds the most understanding, but it is slow and you tend to see what you expect. A coach reviewing your video catches the most, including the "why" behind a habit, but it costs money and takes days. AI video analysis apps give you a report in minutes and are consistent from game to game, but they are best at patterns you repeat (positioning, kitchen arrival, serve depth) and weaker at precise counting. Most improving players get the most from combining an app for every game with a coach or self review now and then.',
    'body': '''<h2>Why video beats memory</h2>

    <p>Ask any player what lost them a game and you will hear about the two or three rallies that stung: the easy put-away into the net, the lob that went over their head. Video almost always tells a different story. The points that actually decide recreational games are usually quieter: a third shot that floated, a step back from the kitchen after a dink, a partner and you both drifting to the middle and leaving the sideline open.</p>

    <p>None of those feel like mistakes in the moment. They only show up when you can watch the rally again from outside your own head. That is the whole value of video analysis, regardless of who does the watching.</p>

    <h2>Option 1: reviewing your own film</h2>

    <p>You prop a phone on the fence, play a game, and watch it back on the couch. It costs nothing and it is the option that teaches you the most about the game, because you are forced to name what you see.</p>

    <div class="info-card">
      <h4>What self review does well</h4>
      <p><strong>Builds your eye.</strong> Once you have watched yourself stand flat-footed at the baseline after a return a dozen times, you start feeling it during play.</p>
      <p><strong>Shows obvious positioning.</strong> Where you stand after the serve, the return, and the third shot is easy to see from a wide shot.</p>
      <p><strong>Free and repeatable.</strong> You can do it after every session if you have the time.</p>
    </div>

    <p>The weaknesses are real, though. It is slow: a 15 minute game can take 30 to 45 minutes to review properly once you pause and rewind. It is also biased. Most players watch the ball and their own highlight shots instead of their feet and their partner, and they rarely know what "correct" looks like at the level above them. If you do not know that you should be at the kitchen line by the fifth shot, you will not notice that you never get there.</p>

    <p>If you go this route, use a checklist. Our <a href="/coachdink/blog/pickleball-film-review/">guide to reviewing your own pickleball film</a> walks through what to watch for in each phase of a rally.</p>

    <h2>Option 2: a coach reviews your video</h2>

    <p>Many teaching pros offer remote video review: you send a game, they send back notes or a voiced-over breakdown. Some do it live in a lesson.</p>

    <p>This is the deepest kind of analysis available. A good coach sees the cause behind the symptom. You might think your problem is popping up dinks; a coach may see that your paddle face opens because your grip slides during fast exchanges. They can also tell you which one thing to fix first, which is something players are generally bad at choosing for themselves.</p>

    <p>The tradeoffs are cost and speed. Paid video review is priced per session, turnaround is often a few days, and it does not scale to every game you play. Quality also varies a lot between coaches. That is not a criticism of coaching; it is just that a single detailed review every few weeks is a different tool from feedback after every game.</p>

    <h2>Option 3: AI video analysis apps</h2>

    <p>The newest option is software that watches the video for you. You upload or record a game, the app works out which player you are, and it returns a report about your play. Approaches differ: some use dedicated court tracking to produce stat sheets, others use a vision model that watches the game and writes coaching notes.</p>

    <p>The obvious advantages are speed and consistency. A report arrives in minutes, it uses the same standards after every game, and it does not get tired or politely skip the thing you do not want to hear.</p>

    <p>It is worth being clear about what these tools are good and less good at, because the marketing rarely is.</p>

    <table class="comparison-table">
      <thead>
        <tr><th>Kind of insight</th><th>How reliably AI handles it</th><th>Why</th></tr>
      </thead>
      <tbody>
        <tr class="highlight-row">
          <td>Recurring positioning habits (staying back, drifting, spacing with partner)</td>
          <td>Strong</td>
          <td>Patterns that repeat across many rallies are visible and hard to miss.</td>
        </tr>
        <tr>
          <td>Serve and return depth tendencies</td>
          <td>Good, if you serve enough in the clip</td>
          <td>Depth is visible on a full-court view, but needs a decent sample.</td>
        </tr>
        <tr>
          <td>Shot selection in common situations</td>
          <td>Good</td>
          <td>Driving a low ball versus dropping it is easy to see from the wide angle.</td>
        </tr>
        <tr>
          <td>Exact counts (shots per rally, percentages)</td>
          <td>Variable</td>
          <td>Counting every shot in a fast game from one phone angle is genuinely hard; treat precise numbers cautiously.</td>
        </tr>
        <tr>
          <td>Fine technique (grip, wrist, paddle face)</td>
          <td>Limited from a corner camera</td>
          <td>A full-court shot makes each player small. Technique needs a close angle.</td>
        </tr>
      </tbody>
    </table>

    <p>That last row is the honest limit. A wide shot from the corner is the right angle for strategy and positioning, which is where most recreational points are lost, but it is the wrong angle for analysing a backhand stroke in detail. If technique is your issue, a close camera and a coach are still the better combination.</p>

    <h2>Coach Dink, disclosed</h2>

    <p>Coach Dink is an AI video analysis app made by the author of this site, so weigh this section accordingly. You film a full game from a corner of the court, choose which player you are (or "Me + my partner" for a doubles team report), and get a report that names the habits costing you points, explains why each one matters, points to the moments in the video where it happened, and ranks drills to fix them.</p>

    <p>A deliberate design choice: it does not show stats it cannot reproduce. When the same game was run through the analysis repeatedly during development, things like rally counts and per-rally shot counts came back different each time, so those were dropped. What remains is the coaching itself plus measurements that held steady run to run, like serve depth and court spacing. It also gives a rating estimate that moves only when you film a game. That rating is Coach Dink's own estimate for tracking progress, not an official rating from any organisation.</p>

    <h2>Which one should you use?</h2>

    <ul>
      <li><strong>Newer players (roughly 2.5 to 3.0):</strong> self review with a simple checklist plus an app is plenty. Your biggest gains are positional and an app will spot them every game.</li>
      <li><strong>Players stuck around 3.5:</strong> this is where an app earns its keep, because the plateau is usually two or three habits you repeat without noticing. See <a href="/coachdink/blog/how-to-improve-at-pickleball/">how to get unstuck</a>.</li>
      <li><strong>4.0 and above:</strong> use an app for game-to-game tracking and add a coach for technique, because your remaining problems are increasingly about stroke detail and decision speed.</li>
    </ul>

    <p>Whichever you choose, the camera setup matters more than the software. A shaky, zoomed-in clip that misses half the court defeats every method. Start with <a href="/coachdink/blog/how-to-film-pickleball/">how to film a pickleball game properly</a>.</p>

    <h2>Questions to ask before choosing an app</h2>

    <p>If you are comparing AI video analysis apps, the feature lists tend to look similar. These questions separate them more usefully.</p>

    <ol>
      <li><strong>What camera setup does it need?</strong> Some tools expect a specific mount or a camera at a particular height; others work from a phone propped in the corner. The easier the setup, the more often you will actually film.</li>
      <li><strong>Does it coach, or just count?</strong> A stat sheet tells you what happened. Coaching tells you why it matters and what to do about it. Both can be useful, but if you only get numbers, you still have to work out the fix yourself.</li>
      <li><strong>Does it point to the moments?</strong> Feedback like "you stayed back after returning" is far more convincing when you can tap through to the exact rallies where it happened. It also lets you check the app is right.</li>
      <li><strong>Does it handle doubles properly?</strong> Most recreational pickleball is doubles. Check that the app can identify which player you are among four, and ideally analyse you and your partner together.</li>
      <li><strong>Does it link findings to practice?</strong> The step after "here is your habit" is "here is how to fix it". Drills tied to the findings save you building a practice plan from scratch.</li>
      <li><strong>Is it honest about uncertainty?</strong> Be wary of tools that produce very precise numbers from a single phone angle without explaining their limits. Consistency from game to game matters more than decimal places.</li>
    </ol>

    <h2>A realistic weekly routine</h2>

    <p>Whatever mix of methods you choose, a simple rhythm keeps video analysis useful instead of becoming another chore.</p>

    <div class="info-card">
      <h4>One week, three steps</h4>
      <p><strong>Film one competitive game.</strong> Not a warm-up, not a blowout. A game where you were genuinely trying to win is where your habits show up.</p>
      <p><strong>Get the analysis and pick two things.</strong> From an app, a coach, or your own review. Write them down in plain language.</p>
      <p><strong>Practise those two before your next game.</strong> Even one short focused session helps. Then film again and see whether they changed.</p>
    </div>

    <p>Over a couple of months, this routine produces something open play never does: a record of what you fixed and how your game changed. That record is also the best motivation to keep going, because progress in pickleball is otherwise hard to see from week to week.</p>

    <h2>What none of them replace</h2>

    <p>Video analysis tells you what to work on. It does not do the work. The improvement comes from taking the one or two things your review found and drilling them until they hold up in games, then filming again to check. Players who film every week but never change what they practise do not improve faster than players who never film at all.</p>''',
    'faqs': [
        ('Is AI pickleball video analysis accurate?',
         'It is accurate at spotting habits that repeat across a game, such as staying back after the return or leaving a gap with your partner. It is less reliable at precise counting from a single phone angle, like exact shots per rally. Judge a tool by whether its coaching matches what you see when you rewatch the moment it points to.'),
        ('What camera do I need for pickleball video analysis?',
         'Your phone is enough. What matters is placement: a corner of the court, about five feet up, on the wide (0.5x) lens, with all four corners of the court in frame and the phone left untouched for the whole game.'),
        ('Can video analysis give me an official pickleball rating?',
         'No. Official ratings come from match results tracked by rating systems used by clubs and tournaments. App ratings, including Coach Dink\'s, are estimates for tracking your own progress.'),
        ('How often should I film my games?',
         'Once a week is a good rhythm for most recreational players. It gives you time to drill what the last review found before checking whether it changed.'),
        ('Does video analysis work for doubles?',
         'Yes, and doubles is where it helps most, because positioning with your partner is hard to judge from inside the rally. Coach Dink can analyse you alone or you and your partner as a team.'),
    ],
    'related': ['how-to-film-pickleball', 'pickleball-film-review', 'how-to-improve-at-pickleball'],
})

# ---------------------------------------------------------------- 2
ARTICLES.append({
    'slug': 'how-to-film-pickleball',
    'seo_title': 'How to Film Pickleball: Phone Position and Camera Angle',
    'seo_h1': 'How to Film Your Pickleball Games: Phone Position, Angle, and Setup',
    'og_title': 'How to Film Your Pickleball Games',
    'meta_desc': 'Where to put your phone to film a pickleball game, which lens to use, how high to mount it, and the five mistakes that ruin a clip before you watch it.',
    'og_desc': 'Where to put your phone, which lens to use, and the mistakes that ruin a pickleball clip.',
    'keywords': 'how to film pickleball, filming pickleball games, pickleball camera angle, best camera angle for pickleball, pickleball phone mount, record pickleball game',
    'badge': 'How-To',
    'published': '2026-10-01', 'published_label': 'October 1, 2026',
    'card_title': 'How to film your pickleball games',
    'card_desc': 'Phone position, lens, height, and the five mistakes that ruin a clip.',
    'intro': 'Most pickleball video is filmed from the wrong place. A phone leaning on a water bottle behind the baseline shows you the back of your own head and very little else. Fifteen seconds of setup gets you a clip you can actually learn from, whether you review it yourself, send it to a coach, or run it through an app.',
    'quick_answer': 'Put your phone in a corner of the court, about five feet off the ground, on the ultra-wide (0.5x) lens. Frame it so all four corners of the court and the server standing behind the far baseline are visible. Keep the sun behind the camera, start recording before the first serve, and do not touch the phone again until the game is over: no panning, no zooming.',
    'body': '''<h2>Why the corner, not the baseline</h2>

    <p>The instinct is to film from directly behind your own baseline, because that is how pickleball looks on TV. Broadcast cameras, though, are mounted high, and from ground level that angle has two problems.</p>

    <p>First, depth is almost invisible. From behind and low down, a ball landing a foot from the kitchen and one landing a foot from the baseline look very similar, so you cannot judge third shots, serve depth, or whether a dink was attackable. Second, the near players block the far players. In doubles you often cannot see what the opponents did, which is half of every rally.</p>

    <p>A corner angle fixes both. You see the length of the court at a diagonal, so depth shows up as distance along the court, and all four players stay visible because nobody stands between the camera and the far side.</p>

    <h2>The setup, step by step</h2>

    <div class="info-card">
      <h4>Fifteen-second setup</h4>
      <p><strong>1. Pick a corner.</strong> Any corner works. Stand just outside the court, off the corner where the baseline meets the sideline.</p>
      <p><strong>2. Get it about five feet up.</strong> Roughly chest to head height. A small tripod, a fence clamp, or a phone propped on a bag on a bench all work. Height is what turns a flat, squashed court into one you can read.</p>
      <p><strong>3. Switch to the ultra-wide lens.</strong> Tap 0.5x in the camera app. The standard 1x lens will not fit a full court from the corner.</p>
      <p><strong>4. Check all four corners.</strong> Every corner of the court should be in frame, plus room behind the far baseline so the server is visible.</p>
      <p><strong>5. Start recording and walk away.</strong> No panning, no zooming, no picking it up between points.</p>
    </div>

    <h2>How high is high enough?</h2>

    <p>Five feet is a practical target, not a magic number. The higher the camera, the more the court opens up and the easier it is to see where the ball landed. Below about three feet, the court compresses into a thin strip and the far kitchen almost disappears. If all you have is a bench, put a bag on the bench and lean the phone against it; that alone often gets you to a workable height.</p>

    <p>A fence clamp is the neatest option on courts with chain-link fencing. Clip it at head height near the corner, angle it diagonally across the court, and you are done.</p>

    <h2>Landscape or portrait?</h2>

    <p>Landscape for analysis. A court is wider than it is tall from a corner view, and portrait wastes most of the frame on sky and ground while cutting off a sideline. Shoot portrait only if the clip is going straight to social media and you do not care about reviewing it.</p>

    <h2>The five things that ruin a clip</h2>

    <p>Almost every unusable pickleball video fails in one of these ways.</p>

    <ol>
      <li><strong>Touching the phone.</strong> Someone picks it up to check it is recording, or nudges it while grabbing a ball. The angle shifts and part of the court is gone for the rest of the game. Start it and leave it.</li>
      <li><strong>Missing a corner.</strong> If the far baseline or one sideline is cut off, any ball landing there is invisible, and so is any player standing there. Check the frame before the first serve.</li>
      <li><strong>Shooting into the sun.</strong> A low sun in the frame turns players into silhouettes and makes the ball vanish. Keep the sun behind the camera, even if that means choosing a different corner.</li>
      <li><strong>Too low, too far.</strong> A phone on the ground behind the fence makes every player tiny and flattens depth. Get it up and as close to the court corner as is safe.</li>
      <li><strong>Zooming.</strong> Pinch-zoom crops the frame and lowers quality. Use the wide lens and stay at the default zoom.</li>
    </ol>

    <h2>Will the camera get hit?</h2>

    <p>Occasionally, which is another reason the corner works well: most balls that leave the court go long or wide near the middle, not into the corner post area. Keep the phone just outside the court rather than on the line, and if you use a tripod, choose a short, stable one that will not topple if a player chases a ball nearby. Let the other players know it is there.</p>

    <h2>How long should you film?</h2>

    <p>One full game is ideal. It is long enough for patterns to show up (you will serve, return, and dink many times) and short enough to review. Coach Dink accepts videos up to 20 minutes, which comfortably covers a game to 11. Filming a whole session is fine for your own records, but for review, pick one game and watch that properly.</p>

    <h2>Battery and storage</h2>

    <p>Wide-angle video at default settings uses storage quickly, and recording drains the battery. Start a session with a charged phone, close other apps, and clear space if your phone is nearly full. You do not need 4K: standard 1080p is more than enough to see positioning and ball placement, and the files are much smaller.</p>

    <h2>Filming for doubles versus singles</h2>

    <p>The same setup works for both. Doubles benefits most from the corner angle, because the thing you most want to see, how you and your partner move together, is only visible when both of you and both opponents stay in frame. If you are filming for a team review, check that both sidelines are visible on your side of the net, since gaps along the sideline are among the most common doubles positioning problems.</p>

    <h2>Indoor courts and fenceless courts</h2>

    <p>Indoor gyms often have no fence to clamp to and walls set well back from the court. A small tripod with an extending leg is the easiest answer: set it just off the corner, extend it to around head height, and keep the legs out of the way of anyone running for a wide ball. Gym lighting is usually even, which helps, but watch for bright windows in the frame behind the far court; point the camera so windows are behind it or to the side.</p>

    <p>On outdoor courts with no fence, a tripod is again the simplest option. If you only have a bench, put it near the corner, stack a bag on it, and lean the phone in a case against the bag. Test the angle by recording five seconds and checking the frame before you start the game.</p>

    <h2>Multiple courts and crowded sessions</h2>

    <p>At busy open play, the corner of your court might be right next to the corner of another one. That is fine as long as your phone is not on the neighbouring court's line. Players on the next court will appear at the edge of your frame; that does not matter. What matters is that your four corners are visible and nobody walks in front of the lens for long stretches. If people regularly walk along one side of the court, use the corner on the other side.</p>

    <h2>Getting permission</h2>

    <p>Before you film, let the other three players know. Most people are happy to be in the clip, especially if you offer to share it. If someone would rather not be filmed, respect that and film a different game. A quick "mind if I record this one? It is just for my own practice" covers it in almost every case.</p>

    <h2>A quick pre-game checklist</h2>

    <div class="info-card">
      <h4>Before the first serve</h4>
      <p><strong>Lens:</strong> 0.5x selected, not 1x, not zoomed.</p>
      <p><strong>Frame:</strong> all four court corners visible, plus space behind the far baseline.</p>
      <p><strong>Height:</strong> roughly chest to head height, angled slightly down across the court.</p>
      <p><strong>Light:</strong> sun behind or beside the camera, never in front.</p>
      <p><strong>Stability:</strong> tripod or clamp tight, phone will not tip if the fence is hit.</p>
      <p><strong>Battery and storage:</strong> enough for the whole game.</p>
      <p><strong>Recording:</strong> started, with the red indicator confirmed, before the first serve.</p>
    </div>

    <h2>What to do with the footage</h2>

    <p>A good clip is the starting point, not the result. You can <a href="/coachdink/blog/pickleball-film-review/">review it yourself with a checklist</a>, send it to a coach, or run it through an app. If you are weighing those options, our <a href="/coachdink/blog/pickleball-video-analysis-app/">comparison of video analysis approaches</a> covers what each one catches.</p>

    <p>In Coach Dink, you pick the video, choose which player you are from the wide frame, and the report comes back in a few minutes, pointing to the moments in the game where each habit showed up. Whatever you use, the camera placement above is what makes the analysis possible.</p>''',
    'faqs': [
        ('Where is the best place to put a camera for pickleball?',
         'A corner of the court, just outside the lines, about five feet up, on the 0.5x wide lens, with all four court corners and the far server in frame.'),
        ('Do I need a tripod to film pickleball?',
         'A tripod or fence clamp makes it easier, but it is not required. A phone propped securely on a bag on a bench works, as long as it is high enough and nobody moves it during the game.'),
        ('Should I film pickleball in 4K?',
         'No. 1080p is plenty for seeing positioning and where shots land, and the files are much smaller and faster to upload.'),
        ('Why does my pickleball video look flat?',
         'The camera is too low. From ground level the court compresses and depth is hard to judge. Raise the phone to around head height and the court opens up.'),
        ('Can I film from behind the baseline instead?',
         'You can, but at ground level you lose depth and the near players block the far ones. A corner angle shows all four players and where every ball lands.'),
    ],
    'related': ['pickleball-video-analysis-app', 'pickleball-film-review', 'pickleball-doubles-strategy'],
})

# ---------------------------------------------------------------- 3
ARTICLES.append({
    'slug': 'pickleball-rating-levels-explained',
    'seo_title': 'Pickleball Rating Levels Explained: 2.5 to 5.0 | Coach Dink',
    'seo_h1': 'Pickleball Rating Levels Explained: What 2.5, 3.0, 3.5, 4.0 and 5.0 Mean',
    'og_title': 'Pickleball Rating Levels Explained',
    'meta_desc': 'What pickleball rating levels mean from 2.5 to 5.0: the skills that define each level, the real gap between 3.5 and 4.0, and how ratings are assigned.',
    'og_desc': 'What each pickleball rating level means, and the real difference between 3.5 and 4.0.',
    'keywords': 'pickleball rating levels explained, pickleball rating chart, pickleball rating system, 3.0 pickleball rating meaning, 3.5 vs 4.0 pickleball, pickleball skill levels',
    'badge': 'Explainer',
    'published': '2026-10-01', 'published_label': 'October 1, 2026',
    'card_title': 'Pickleball rating levels explained',
    'card_desc': 'What 2.5 through 5.0 actually look like on court, and what separates 3.5 from 4.0.',
    'intro': 'Pickleball ratings get thrown around at every open play, but very few people can say what separates a 3.0 from a 3.5. The numbers describe a fairly specific set of skills and habits. Once you know what they are, the scale stops being mysterious and starts being a map of what to work on next.',
    'quick_answer': 'Pickleball skill ratings typically run from about 1.0 to 5.5 or higher. Roughly: 2.0 to 2.5 is learning the rules and keeping the ball in play; 3.0 can rally and knows basic positioning but is inconsistent; 3.5 has a developing soft game and gets to the kitchen, but errors under pressure; 4.0 is consistent, dinks patiently, has a reliable third shot, and plays as a team; 4.5 and up adds pace control, shot variety and few unforced errors. Official ratings come from match results; self ratings are estimates.',
    'body': '''<h2>How the scale works</h2>

    <p>Pickleball uses a numeric scale, usually in half-point steps for self rating and decimals for results-based systems. Lower numbers mean newer players. Two kinds of rating exist side by side:</p>

    <ul>
      <li><strong>Skill-based ratings</strong> describe what you can do: which shots you have, how consistent you are, and how well you understand positioning. USA Pickleball publishes skill descriptions that clubs and players use for self rating.</li>
      <li><strong>Results-based ratings</strong> are calculated from match results against other rated players. Rating systems used by clubs and tournaments work this way, which is why they are considered official: they measure outcomes, not opinions.</li>
    </ul>

    <p>The descriptions below are the commonly understood skill picture at each level. Use them as a guide, not a ruling. If you want help placing yourself, the <a href="/coachdink/blog/pickleball-self-rating-guide/">self rating guide</a> turns these into questions.</p>

    <h2>Level by level</h2>

    <table class="comparison-table">
      <thead>
        <tr><th>Level</th><th>What it usually looks like</th><th>The typical limiter</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>2.0 to 2.5</td>
          <td>Knows the basic rules and scoring, can serve and return most of the time, rallies are short.</td>
          <td>Keeping the ball in play.</td>
        </tr>
        <tr>
          <td>3.0</td>
          <td>Can sustain a rally at moderate pace, serves reliably, starting to learn the two-bounce rule in practice and to move toward the kitchen.</td>
          <td>Consistency, and standing in no man's land.</td>
        </tr>
        <tr class="highlight-row">
          <td>3.5</td>
          <td>Gets to the kitchen line, can dink, attempts third shot drops, understands stacking and basic doubles positioning.</td>
          <td>Errors under pressure and impatience in dink rallies.</td>
        </tr>
        <tr class="highlight-row">
          <td>4.0</td>
          <td>Consistent third shots, patient dinking, resets hard balls, moves with partner, chooses when to speed up.</td>
          <td>Pace control and shot variety.</td>
        </tr>
        <tr>
          <td>4.5</td>
          <td>Few unforced errors, varied spins and placement, strong hands in fast exchanges, deliberate strategy.</td>
          <td>Forcing errors from equally consistent opponents.</td>
        </tr>
        <tr>
          <td>5.0+</td>
          <td>Tournament level. Every shot is available and controlled under pressure.</td>
          <td>Margins measured in inches and tenths of a second.</td>
        </tr>
      </tbody>
    </table>

    <h2>What a 3.0 rating means</h2>

    <p>3.0 is the most common level in recreational play, and the one people most often underrate or overrate themselves around. A 3.0 player can rally, serves in most of the time, and knows the basic rules well, including the non-volley zone. What holds them back is consistency and court position. They often hit a good shot, then a loose one, and they frequently stay near the baseline or stop halfway in, where the ball arrives at their feet.</p>

    <p>The fastest way out of 3.0 is almost never a new shot. It is getting to the kitchen line reliably and keeping the ball in play one or two shots longer. Our <a href="/coachdink/blog/beginner-pickleball-mistakes/">beginner mistakes guide</a> covers the habits that keep players here.</p>

    <h2>The real difference between 3.5 and 4.0</h2>

    <p>This is the gap most players get stuck in, and it is mostly not about power or athleticism. Watch a 3.5 game and a 4.0 game side by side and the differences are about patience and percentages.</p>

    <div class="info-card">
      <h4>What 4.0 players do that 3.5 players usually do not</h4>
      <p><strong>They get to the kitchen together.</strong> Both partners arrive at the line, at roughly the same time, and stay level with each other.</p>
      <p><strong>Their third shot lets them come in.</strong> Whether it is a drop or a drive followed by a fifth-shot drop, it buys time to move forward. See the <a href="/coachdink/blog/third-shot-drop/">third shot drop guide</a>.</p>
      <p><strong>They dink to wait, not to win.</strong> A 3.5 tends to speed up the first ball that feels attackable. A 4.0 dinks until the ball is genuinely high, then attacks.</p>
      <p><strong>They can reset.</strong> When a hard ball comes at their feet, they soften it back into the kitchen instead of swinging. That one skill ends many rallies early at 3.5.</p>
      <p><strong>They make fewer unforced errors.</strong> Not zero, just fewer, and the gap compounds over a game to 11.</p>
    </div>

    <p>If you are stuck around 3.5, film a game and count how often you are not at the kitchen line when the dinking starts, and how many rallies you end with a speed-up from below net height. Those two numbers usually explain the plateau. We go deeper in <a href="/coachdink/blog/how-to-improve-at-pickleball/">how to improve at pickleball</a>.</p>

    <h2>What separates 2.5 from 3.0</h2>

    <p>At 2.5, players are still building the basics: the serve goes in most of the time but not reliably, rallies rarely last more than a few shots, and the non-volley zone rules are still being learned. The jump to 3.0 is mostly about consistency. A 3.0 can serve and return dependably, keep a moderate-pace rally going, and has started to understand that the goal is to move forward toward the kitchen rather than stay at the baseline.</p>

    <p>Practically, the fastest route from 2.5 to 3.0 is volume on two shots: the serve and the return, both aimed deep. If those two shots go in nine times out of ten, a surprising number of games are won simply by not giving points away at the start of each rally.</p>

    <h2>What separates 4.0 from 4.5</h2>

    <p>Above 4.0, the differences become finer and harder to see from the side of the court. A 4.0 player has every basic shot and uses them sensibly. A 4.5 player uses them deliberately. They move opponents with placement, disguise their shots, change pace on purpose, and win fast exchanges at the kitchen more often than not. Unforced errors become rare enough that points are usually won by forcing the opponent into a weak ball rather than waiting for a mistake.</p>

    <p>Players at this stage often benefit most from technique work with a coach, because the remaining gains are in paddle control and timing, which a wide video angle shows less clearly than positioning.</p>

    <h2>A quick reference chart</h2>

    <div class="stat-row">
      <div class="stat-card"><div class="stat-number">2.5</div><div class="stat-label">Learning to keep the ball in play</div></div>
      <div class="stat-card"><div class="stat-number">3.0</div><div class="stat-label">Consistent rallies, moving forward</div></div>
      <div class="stat-card"><div class="stat-number">3.5</div><div class="stat-label">At the kitchen, developing soft game</div></div>
      <div class="stat-card"><div class="stat-number">4.0</div><div class="stat-label">Patient, consistent, plays as a team</div></div>
    </div>

    <h2>Why your rating seems to change depending on where you play</h2>

    <p>A "3.5" at one club can look like a 3.0 at another. Self ratings drift because people rate themselves against the players around them. Results-based ratings correct for this over time because every result is measured against opponents with known ratings, but they need a decent number of recorded matches to settle. If you have only played a few rated matches, your number can move a lot.</p>

    <h2>Singles and doubles ratings</h2>

    <p>Many results-based systems track singles and doubles separately, and for good reason. The two formats reward different skills. Singles leans on movement, serve and return depth, and passing shots, because one player has to cover the whole court. Doubles leans on patience, dinking, and teamwork. It is common for a player to be half a point or more apart between the two. If someone tells you their rating, it is usually their doubles number, since that is the format most recreational players play.</p>

    <h2>Using your rating to choose games and events</h2>

    <p>The practical point of a rating is matching you with games where everyone has a chance to win. That is better for learning: games that are too easy teach you nothing, and games that are far too hard mostly teach you to defend. Many clubs run sessions by rating band, and tournaments split brackets by rating. When you are between levels, it is usually better to play in the higher band for open play and the lower one for your first few tournaments, where nerves tend to cost players a little of their usual level.</p>

    <h2>Does age or fitness change your rating?</h2>

    <p>Not directly. Ratings measure play, not athleticism. A fit, fast player with poor shot selection will often lose to an older, patient player who keeps the ball low and stays at the kitchen. That is part of what makes pickleball appealing, and it is why the levels above are written in terms of decisions and consistency rather than speed.</p>

    <h2>How Coach Dink's rating fits in</h2>

    <p>Coach Dink gives you a rating estimate from your filmed games, and it only moves when you film a game, not when you finish drills. It is the app's own estimate for tracking your progress over time. It is not an official rating, and it will not replace a results-based rating for tournament entry. Its job is to show whether the habits you are drilling are actually changing how you play.</p>''',
    'faqs': [
        ('What is a good pickleball rating?',
         'It depends on where you play, but 3.5 is a solid recreational level, 4.0 is a strong club player, and 4.5 and above is advanced. Most recreational players are between 2.5 and 3.5.'),
        ('How long does it take to go from 3.0 to 3.5?',
         'It varies widely with how often you play and whether you practise deliberately. Players who drill specific weaknesses and review their games tend to move faster than players who only play open play.'),
        ('Is 3.5 an intermediate pickleball player?',
         'Yes. 3.0 to 3.5 is usually described as intermediate, with 4.0 as advanced intermediate and 4.5 and above as advanced.'),
        ('How do I get an official pickleball rating?',
         'Official ratings come from recorded match results, usually through leagues, tournaments, or clubs that report results to a rating system. Self ratings and app estimates are not official.'),
    ],
    'related': ['pickleball-self-rating-guide', 'how-to-improve-at-pickleball', 'pickleball-drills-by-level'],
})

# ---------------------------------------------------------------- 4
ARTICLES.append({
    'slug': 'pickleball-self-rating-guide',
    'seo_title': 'Pickleball Self Rating Guide: 12 Questions | Coach Dink',
    'seo_h1': 'Pickleball Self Rating Guide: 12 Honest Questions to Find Your Level',
    'og_title': 'Pickleball Self Rating Guide',
    'meta_desc': 'How to rate yourself at pickleball honestly: twelve yes-or-no questions that place you between 2.5 and 4.5, and the biases that make players rate too high.',
    'og_desc': 'Twelve honest questions that place you between 2.5 and 4.5 at pickleball.',
    'keywords': 'pickleball self rating guide, pickleball self rating quiz, how to know your pickleball rating, how to rate pickleball level, pickleball skill rating quiz, what is my pickleball rating',
    'badge': 'Guide',
    'published': '2026-10-01', 'published_label': 'October 1, 2026',
    'card_title': 'Pickleball self rating guide',
    'card_desc': 'Twelve yes-or-no questions that place you honestly between 2.5 and 4.5.',
    'intro': 'Signing up for a league, a clinic, or a ladder usually means picking a number for yourself. Most players guess based on who they beat last week. A better approach is to check yourself against specific skills, answered honestly, which is what this guide does.',
    'quick_answer': 'Answer the twelve questions below with what you do in real games, not your best shot ever. Count your "yes" answers in each block. If you answer yes to most of the 3.0 block, you are at least 3.0; most of the 3.5 block, at least 3.5; and so on. Stop at the first block where you answer no to more than one question. That is roughly your level. For an accurate number, use results-based ratings or film a game and check yourself against what you see.',
    'body': '''<h2>Before you start: three rules</h2>

    <ol>
      <li><strong>Answer for real games.</strong> Not drills, not warm-up, not the one great shot you hit last month. What happens in a competitive game to 11.</li>
      <li><strong>"Most of the time" means most of the time.</strong> If you hit your third shot drop well about half the time, that is a no.</li>
      <li><strong>When in doubt, it is a no.</strong> The cost of rating slightly low is a few easy games. The cost of rating high is a season of losing and learning very little.</li>
    </ol>

    <h2>Block 1: are you at least 3.0?</h2>

    <div class="info-card">
      <h4>3.0 questions</h4>
      <p><strong>1.</strong> Do you get your serve in most of the time, deep enough that the returner cannot step in and attack it?</p>
      <p><strong>2.</strong> Can you sustain a rally at moderate pace from the baseline without the ball going into the net or long every few shots?</p>
      <p><strong>3.</strong> Do you know the non-volley zone rules well enough that you rarely commit a kitchen fault, including stepping in after a volley?</p>
    </div>

    <p>If you answered no to two or more, you are most likely in the 2.0 to 2.5 range, and that is fine. Your focus is consistency and rules. Our <a href="/coachdink/blog/pickleball-kitchen-rules/">kitchen rules guide</a> is a good next read.</p>

    <h2>Block 2: are you at least 3.5?</h2>

    <div class="info-card">
      <h4>3.5 questions</h4>
      <p><strong>4.</strong> After you return serve, do you get all the way to the kitchen line, not just partway, in most rallies?</p>
      <p><strong>5.</strong> Can you keep a dink rally going for five or more shots without popping the ball up or netting it?</p>
      <p><strong>6.</strong> Do you attempt a third shot drop when serving, and does it land in or near the kitchen at least some of the time?</p>
    </div>

    <h2>Block 3: are you at least 4.0?</h2>

    <div class="info-card">
      <h4>4.0 questions</h4>
      <p><strong>7.</strong> Is your third shot (drop, or drive then drop) reliable enough that you and your partner usually make it to the kitchen?</p>
      <p><strong>8.</strong> When an opponent drives a hard ball at your feet while you are moving in, can you reset it softly into the kitchen most of the time?</p>
      <p><strong>9.</strong> In dink rallies, do you wait for a genuinely high ball before speeding up, instead of attacking from below the net?</p>
    </div>

    <h2>Block 4: are you at least 4.5?</h2>

    <div class="info-card">
      <h4>4.5 questions</h4>
      <p><strong>10.</strong> Do you win most fast hand battles at the kitchen against 4.0 players?</p>
      <p><strong>11.</strong> Can you deliberately use spin, pace changes, and placement to set up a point, rather than just keeping the ball in?</p>
      <p><strong>12.</strong> Are your unforced errors rare enough that most of your lost points are won by the opponent, not given away?</p>
    </div>

    <h2>How to read your results</h2>

    <p>Work through the blocks in order and stop at the first one where you answered no to two or more questions. Your level is the one before it. If you passed Block 2 but failed Block 3, you are around 3.5. If you passed every question in a block but only one in the next, you are probably a "plus" at your level, like a strong 3.5 knocking on 4.0.</p>

    <p>For a fuller description of each level, see <a href="/coachdink/blog/pickleball-rating-levels-explained/">pickleball rating levels explained</a>.</p>

    <h2>The three biases that make players rate too high</h2>

    <h2>1. Rating your best shots instead of your typical ones</h2>

    <p>Everybody remembers the perfect drop that died in the kitchen. Nobody remembers the four that floated. Ratings are about what happens most of the time, and memory is a terrible sampler.</p>

    <h2>2. Rating against your local group</h2>

    <p>If you are the best player at a small club, you may be a 3.0 in a 3.0 room. Players who move clubs or enter their first tournament often find their self rating was half a point high. That is not a character flaw; it is just what happens without an outside reference.</p>

    <h2>3. Confusing athleticism with level</h2>

    <p>Fast, fit players can chase down a lot of balls and win rallies through effort, especially against newer players. That stops working around 3.5, where opponents keep the ball low and make you hit up. Ratings reward control and positioning more than speed.</p>

    <h2>The most honest check: film a game</h2>

    <p>Every question above is easier to answer from video than from memory. Questions 4, 5, 7, and 9 in particular are almost impossible to judge from inside a rally, because you do not see where you were standing or how high the ball was when you attacked.</p>

    <p>Set up a phone in the corner of the court (our <a href="/coachdink/blog/how-to-film-pickleball/">filming guide</a> shows how), play one game, and go back through the twelve questions while watching. Most players drop half a point the first time they do this, then gain it back quickly because they now know exactly what to fix.</p>

    <p>Coach Dink starts with a short quiz like this one to give you an initial estimate, then adjusts your rating from your filmed games. That estimate is the app's own, for tracking progress; it is not an official rating.</p>

    <h2>Worked examples</h2>

    <p>A few common patterns, to show how the blocks play out in practice.</p>

    <div class="info-card">
      <h4>The athletic newcomer</h4>
      <p>Six months in, fit, wins a lot of open play games with pace. Passes Block 1 easily. In Block 2, answers yes to question 6 (attempts drops) but no to question 4 (stays back after returning) and no to question 5 (dink rallies end quickly because they speed up). Two no answers in Block 2 means roughly 3.0, possibly a strong 3.0. Their fastest gains are positional, not technical.</p>
    </div>

    <div class="info-card">
      <h4>The steady club regular</h4>
      <p>Two years in, rarely misses a serve or return, gets to the kitchen, dinks patiently. Passes Blocks 1 and 2. In Block 3, yes to question 9 (patient) but no to 7 (third shot inconsistent) and no to 8 (struggles with hard balls at the feet). That is a solid 3.5. The work is the third shot and the reset.</p>
    </div>

    <div class="info-card">
      <h4>The ex-tennis player</h4>
      <p>Strong drives, good footwork, great at the baseline. Often surprised by the self rating, because Block 2 and 3 questions are about soft play and patience. Many former tennis players land around 3.5 at first, then move up quickly once their soft game catches up with their groundstrokes.</p>
    </div>

    <h2>When different formats give different answers</h2>

    <p>If you play both singles and doubles, run the questions separately for each. Questions 4 through 9 are written with doubles in mind, so for singles, swap in the equivalent: do you recover to the middle of the baseline after each shot, can you hit approach shots deep enough to come forward behind them, and can you pass an opponent who has reached the kitchen? It is normal to land at different levels in the two formats.</p>

    <h2>Re-rating yourself over time</h2>

    <p>A self rating is a snapshot. It is worth repeating every couple of months, especially if you are practising deliberately. The questions you answered no to are, in effect, your practice plan: each one maps to a skill you can drill. When a no becomes a reliable yes in real games (not just drills), your level has moved.</p>

    <p>To make this concrete, keep a short note with the date and your answers. Three months later, answer again. It is one of the few ways to see progress in a sport where your opponents tend to improve alongside you, which can make it feel like you are standing still even when you are not.</p>

    <h2>Self rating versus official ratings</h2>

    <p>Self ratings are used for open play, clinics, and some recreational leagues. Tournaments and many competitive leagues use results-based ratings, calculated from your match outcomes against other rated players. If you play in events that use one, your results will correct your self rating over time, up or down. Until then, an honest self rating is how you find games that are competitive enough to help you improve.</p>''',
    'faqs': [
        ('How do I know my pickleball rating?',
         'Either rate yourself honestly against skill descriptions, like the questions above, or play recorded matches in a results-based rating system used by clubs and tournaments. Filming a game makes a self rating much more accurate.'),
        ('Is it better to rate yourself high or low in pickleball?',
         'Slightly low. You will have some easy games, but you will also win enough to build confidence and learn. Rating high usually means losing most games without understanding why.'),
        ('Can I be a 3.5 in singles and a 3.0 in doubles?',
         'Yes. Singles rewards movement and passing shots; doubles rewards patience, dinking, and teamwork. Many players are noticeably stronger in one format.'),
        ('How accurate are pickleball self rating quizzes?',
         'They are a reasonable starting point, but they depend on honest answers. Most players overrate themselves slightly. Checking your answers against video of a real game makes them much more reliable.'),
    ],
    'related': ['pickleball-rating-levels-explained', 'how-to-film-pickleball', 'how-to-improve-at-pickleball'],
})

# ---------------------------------------------------------------- 5
ARTICLES.append({
    'slug': 'beginner-pickleball-mistakes',
    'seo_title': '12 Beginner Pickleball Mistakes (and How to Fix Each One)',
    'seo_h1': '12 Beginner Pickleball Mistakes and How to Fix Each One',
    'og_title': '12 Beginner Pickleball Mistakes and the Fixes',
    'meta_desc': 'The twelve mistakes that keep new pickleball players stuck at 2.5 and 3.0, why each one costs points, and a simple fix or drill for every one of them.',
    'og_desc': 'The twelve habits that keep new players stuck, and a simple fix for each.',
    'keywords': 'beginner pickleball mistakes, pickleball beginner mistakes fix, common pickleball mistakes, pickleball tips for beginners, pickleball mistakes to avoid, new pickleball player tips',
    'badge': 'Guide',
    'published': '2026-10-01', 'published_label': 'October 1, 2026',
    'card_title': '12 beginner pickleball mistakes and the fixes',
    'card_desc': 'The habits that keep new players stuck at 2.5 and 3.0, with a fix for each.',
    'intro': 'Most beginner pickleball mistakes are not about technique. They are about where you stand, when you move, and which shot you choose. That is good news, because positioning and decisions are much faster to fix than a stroke. Here are the twelve that cost new players the most points, roughly in order of how often they show up.',
    'quick_answer': 'The biggest beginner mistakes are rushing forward after serving (the two-bounce rule means the return must bounce, so stay back), staying back after returning (you should be moving to the kitchen line), standing in no man\'s land, hitting every ball hard, swinging big at the kitchen, and backing up during dink rallies. Most of them are fixed by learning where to stand at each stage of the rally rather than by changing your stroke.',
    'body': '''<h2>Mistakes in the first three shots</h2>

    <h2>1. Rushing forward after you serve</h2>

    <p>The two-bounce rule says the return of serve must bounce, and then the serving team's next shot (the third shot) must bounce too. Beginners often serve and jog forward, then get the return bouncing at their feet or behind them.</p>

    <p><strong>Fix:</strong> after serving, stay behind the baseline until you see where the return is going. Your third shot is hit off the bounce, so you want the ball in front of you.</p>

    <h2>2. Staying back after you return</h2>

    <p>This is the mirror image, and it is even more costly. The returning team has the positional advantage: once the return is hit, the returner can move straight to the kitchen line while the serving team is stuck at the back waiting for a bounce. Beginners often return and stay put, giving that advantage away.</p>

    <p><strong>Fix:</strong> hit a deep, high-ish return, then walk forward to the kitchen line. A slower, deeper return gives you more time to get there. "Return and come in" should become automatic.</p>

    <h2>3. Short serves and short returns</h2>

    <p>A short serve or return lets the other side step into the court and attack, and a short return in particular lets the serving team move forward early. Depth matters far more than pace on these two shots.</p>

    <p><strong>Fix:</strong> aim serves and returns at the back third of the court. Missing long occasionally is acceptable while you calibrate. See <a href="/coachdink/blog/pickleball-serve-tips/">serve tips</a> for more.</p>

    <h2>Mistakes in court position</h2>

    <h2>4. Living in no man's land</h2>

    <p>The area between the baseline and the kitchen, often called the transition zone or no man's land, is where balls land at your feet. Beginners stop there because it feels like progress. Opponents at the kitchen can hit down at you, and you have to hit up.</p>

    <p><strong>Fix:</strong> be either back (waiting for a bounce) or at the kitchen line. If you have to pass through the middle, split-step when the opponent hits, play the ball, and keep moving forward. Learning a <a href="/coachdink/blog/pickleball-reset-shot/">reset shot</a> helps when you are caught there.</p>

    <h2>5. Standing too far back from the kitchen line</h2>

    <p>Even when beginners reach the front, they often stand a couple of feet behind the line. That turns dinks into half-volleys at their feet and gives opponents a target.</p>

    <p><strong>Fix:</strong> toes just behind the line. Being close lets you take more balls out of the air and keep them low.</p>

    <h2>6. Not moving with your partner</h2>

    <p>In doubles, partners should move as a pair: forward together, sideways together. Beginners often leave a big gap down the middle or one player charges while the other stays back, which creates an easy angle for opponents.</p>

    <p><strong>Fix:</strong> imagine a rope between you, about the width of a few paddles. When the ball goes to one side, both of you shift that way. More on this in <a href="/coachdink/blog/pickleball-doubles-strategy/">doubles strategy</a>.</p>

    <h2>Mistakes in shot choice</h2>

    <h2>7. Hitting every ball hard</h2>

    <p>Power wins points against other beginners, which is why it is so tempting. It stops working as soon as opponents are at the kitchen and can block your drive back at your feet.</p>

    <p><strong>Fix:</strong> ask "is this ball above the net?" before you attack. If the answer is no, play it soft. That one question changes a lot.</p>

    <h2>8. Never trying a soft third shot</h2>

    <p>The <a href="/coachdink/blog/third-shot-drop/">third shot drop</a> is the shot that gets the serving team to the kitchen. Many beginners avoid it because it feels hard and they miss it often at first.</p>

    <p><strong>Fix:</strong> practise it in drills and attempt it in casual games. Missing drops is part of learning them; avoiding them forever caps your level.</p>

    <h2>9. Speeding up from below the net</h2>

    <p>A dink rally gets tense, and someone hits hard at a low ball. Because the ball is below net height, the shot has to go up, and an opponent at the line punishes it.</p>

    <p><strong>Fix:</strong> keep dinking until a ball comes up above the net, then attack. Patience wins dink rallies. See <a href="/coachdink/blog/pickleball-dinking-tips/">dinking tips</a>.</p>

    <h2>Mistakes in technique and habits</h2>

    <h2>10. Big swings at the kitchen</h2>

    <p>At the kitchen line the ball arrives fast and there is no time for a full backswing. Big swings lead to late contact and mishits.</p>

    <p><strong>Fix:</strong> paddle up, out in front of your body, with short compact punches for volleys and a smooth lifting motion for dinks.</p>

    <h2>11. Paddle down between shots</h2>

    <p>Letting the paddle drop to knee height after each shot means you are late to every fast ball at your body.</p>

    <p><strong>Fix:</strong> after every shot, return to a ready position with the paddle in front of your chest. It feels fussy at first and becomes natural in a few sessions.</p>

    <h2>12. Watching your own shot</h2>

    <p>Beginners often admire a good shot and stay frozen while the opponent hits back. By the time they react, the ball is past them.</p>

    <p><strong>Fix:</strong> hit, then immediately recover to position and watch the opponent's paddle. Split-step as they make contact.</p>

    <h2>Why you will not notice most of these yourself</h2>

    <p>Nearly every item on this list is invisible from inside the rally. You do not feel yourself stopping in no man's land, standing two feet off the line, or leaving a gap with your partner. You only see it on video.</p>

    <p>That is the case for filming. A phone in the corner of the court for one game (see <a href="/coachdink/blog/how-to-film-pickleball/">how to film pickleball</a>) shows you which three or four of these twelve you actually do. Fix those first; ignore the rest for now. Coach Dink automates that step: it watches the game, names the habits costing you points, and ranks drills for them, but the same checklist works if you review the video yourself.</p>

    <h2>Two bonus mistakes that are about mindset</h2>

    <h2>Playing only with stronger players</h2>

    <p>Playing up is valuable, but if every game is against players a full level above you, you mostly defend and rarely get to practise building a point. Mix it up: some games against stronger players to see what good looks like, some against equals where you can try new shots without being punished instantly.</p>

    <h2>Changing everything at once</h2>

    <p>After a bad session or a helpful video, it is tempting to try to fix your grip, your footwork, your third shot, and your dinking in the same week. That rarely works, because you cannot concentrate on four things during a fast rally. Pick one or two, give them a few weeks, then move on.</p>

    <h2>A one-week plan for beginners</h2>

    <div class="info-card">
      <h4>Seven days, three sessions</h4>
      <p><strong>Session 1, drill:</strong> 20 deep serves and 20 deep returns to a target in the back third. Then return-and-move 20 times, walking all the way to the kitchen line after every return.</p>
      <p><strong>Session 2, play:</strong> open play with one rule for yourself: after every return, get to the kitchen line. Do not worry about anything else.</p>
      <p><strong>Session 3, drill and play:</strong> 10 minutes of cooperative dinking with toes at the line, then play with a second rule: no hard shots at balls below the net.</p>
    </div>

    <p>At the end of the week, film a game and count how often you reached the kitchen line by the time dinking started. Compare with the next week. It is a simple number, and it moves faster than almost anything else in your game.</p>

    <h2>Which to fix first</h2>

    <p>If you are newer than 3.0, start with numbers 2 and 4: return and come in, and stop living in no man's land. Those two alone change how rallies feel, because you start playing from the front of the court. Then work on 7 and 9, the shot selection mistakes. Technique habits like 10 and 11 tend to improve on their own once you are spending more time at the line.</p>''',
    'faqs': [
        ('What is the most common mistake in pickleball?',
         'Staying back after returning serve, or stopping in no man\'s land between the baseline and the kitchen. Both leave you hitting up at opponents who can hit down.'),
        ('Why do I keep hitting the ball into the net in pickleball?',
         'Usually because you are hitting balls that are below net height too hard, or making contact late and behind your body. Play low balls softly with a lifting motion and meet the ball out in front.'),
        ('Should beginners hit the ball hard in pickleball?',
         'Only when the ball is above the net. Hitting everything hard works against other beginners but becomes a liability once opponents reach the kitchen line.'),
        ('How long does it take to stop making beginner mistakes?',
         'Positioning habits can change within a few weeks of focused attention, especially if you film your games and check. Shot selection takes longer because it relies on judgment under pressure.'),
    ],
    'related': ['how-to-improve-at-pickleball', 'pickleball-kitchen-rules', 'third-shot-drop'],
})

# ---------------------------------------------------------------- 6
ARTICLES.append({
    'slug': 'how-to-improve-at-pickleball',
    'seo_title': 'How to Improve at Pickleball (and Get Unstuck at 3.5)',
    'seo_h1': 'How to Improve at Pickleball When You Feel Stuck',
    'og_title': 'How to Improve at Pickleball When You Are Stuck',
    'meta_desc': 'More open play rarely breaks a pickleball plateau. The four-step loop that does: film a game, find two habits, drill them, then film again to check.',
    'og_desc': 'Why more open play rarely breaks a plateau, and the four-step loop that does.',
    'keywords': 'how to improve your pickleball skills, how to improve at pickleball, stuck at 3.5 pickleball, pickleball improvement guide, pickleball tips to improve your game, get better at pickleball',
    'badge': 'Guide',
    'published': '2026-10-01', 'published_label': 'October 1, 2026',
    'card_title': 'How to improve at pickleball when you feel stuck',
    'card_desc': 'Why more open play rarely breaks a plateau, and the four-step loop that does.',
    'intro': 'Most pickleball players improve quickly for the first few months, then hit a wall somewhere around 3.0 to 3.5. They keep playing three or four times a week and stay the same. The reason is simple: open play rehearses the habits you already have. Breaking a plateau needs a different loop.',
    'quick_answer': 'To improve at pickleball, stop trying to fix everything. Film one game, find the two habits that cost you the most points, drill those two specifically for a week or two, then film again to check they changed in real play. Repeat. Most plateaus around 3.5 come from a small number of repeated habits (not getting to the kitchen, attacking from below the net, weak third shots), and playing more without targeting them just reinforces them.',
    'body': '''<h2>Why open play stops making you better</h2>

    <p>Early on, every game teaches you something new: a rule, a shot, a position. After a few months, that runs out. You have a way of playing, and every game is another repetition of it, including the parts that lose points.</p>

    <p>Open play also gives poor feedback. You lose a rally and blame the last shot, but the point was often lost two or three shots earlier, when you stopped short of the kitchen or floated a third shot. Without seeing the whole rally again, you keep fixing the wrong thing.</p>

    <h2>The improvement loop</h2>

    <div class="info-card">
      <h4>Four steps, repeated</h4>
      <p><strong>1. Film one game.</strong> A phone in the corner of the court, about five feet up, wide lens, all four corners in frame. <a href="/coachdink/blog/how-to-film-pickleball/">Full setup guide</a>.</p>
      <p><strong>2. Find two habits.</strong> Not ten. The two that cost the most points. Review it yourself with a checklist, ask a coach, or use an app.</p>
      <p><strong>3. Drill only those two.</strong> One or two focused practice sessions per week, with a specific drill for each habit.</p>
      <p><strong>4. Film again.</strong> Check whether the habit changed in an actual game, not just in the drill. If it did, pick the next one.</p>
    </div>

    <p>The loop is simple, but each step has a common way to go wrong.</p>

    <h2>Step 2: choosing the right two habits</h2>

    <p>The temptation is to pick the most embarrassing moments: the overhead into the net, the missed easy volley. Those feel important but are usually rare. What matters is frequency multiplied by cost. A habit that loses you a point in one rally out of five is worth far more attention than a dramatic miss that happens once a game.</p>

    <p>At 3.0 to 3.5, the high-frequency habits are almost always some of these:</p>

    <ul>
      <li>Not getting all the way to the kitchen line after the return, or arriving late after the third shot.</li>
      <li>Third shots that float high or land deep in the transition zone, letting opponents attack.</li>
      <li>Speeding up dinks from below net height.</li>
      <li>Partners leaving a gap in the middle or moving independently.</li>
      <li>Short returns of serve that let the serving team come in early.</li>
    </ul>

    <p>If you review the video yourself, our <a href="/coachdink/blog/pickleball-film-review/">film review guide</a> has a phase-by-phase checklist. The goal is a short, concrete list: "I stop at the transition line after returning" is actionable; "I need to be more consistent" is not.</p>

    <h2>Step 3: drill the habit, not the shot</h2>

    <p>If your problem is not reaching the kitchen after the return, a dinking drill will not fix it. You need a drill where you return and walk in every single time until it is automatic. Match the drill to the habit.</p>

    <table class="comparison-table">
      <thead>
        <tr><th>Habit found on film</th><th>Drill that targets it</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>Stopping short after the return</td>
          <td>Return-and-move: partner serves, you return deep, walk to the line and split-step before their third shot. Repeat 20 times.</td>
        </tr>
        <tr>
          <td>Floating third shots</td>
          <td>Drop ladder from the baseline: partner at the kitchen feeds, you drop. Move forward a step after every five good drops.</td>
        </tr>
        <tr>
          <td>Attacking low balls</td>
          <td>Dink rally with a rule: you may only speed up a ball above net height. Any other speed-up loses the point.</td>
        </tr>
        <tr>
          <td>Getting caught in transition</td>
          <td>Reset drill: partner at the line drives at your feet while you are in the middle; your only job is to soften it into the kitchen.</td>
        </tr>
      </tbody>
    </table>

    <p>More options for each level are in <a href="/coachdink/blog/pickleball-drills-by-level/">pickleball drills by level</a>.</p>

    <h2>Step 4: check it changed in a game</h2>

    <p>This is the step almost everyone skips, and it is the one that matters. Habits that look fixed in drills often reappear under the pressure of a real game. Filming again tells you whether the change transferred. If it did, move to the next habit. If not, keep drilling, or try a drill that adds more game-like pressure.</p>

    <h2>Why "stuck at 3.5" is so common</h2>

    <p>3.5 is the level where the game changes character. Below it, you can win points with pace and athleticism. Above it, opponents keep the ball low and punish anything you hit up. The skills that got you to 3.5 are not the ones that get you to 4.0.</p>

    <p>The specific skills that make the jump are covered in detail in <a href="/coachdink/blog/pickleball-rating-levels-explained/">pickleball rating levels explained</a>. In short: getting to the kitchen as a team, a third shot that lets you come in, patience in dink rallies, and being able to reset hard balls. None of those are about power. All of them show up clearly on video.</p>

    <h2>A sample four-week plan</h2>

    <table class="comparison-table">
      <thead>
        <tr><th>Week</th><th>Focus</th></tr>
      </thead>
      <tbody>
        <tr><td>1</td><td>Film one competitive game. Review it and write down the two habits that cost the most points.</td></tr>
        <tr><td>2</td><td>Two short drill sessions on habit one, plus open play with one personal rule tied to it.</td></tr>
        <tr><td>3</td><td>Same for habit two. Keep the rule from week 2 in open play.</td></tr>
        <tr><td>4</td><td>Film another game. Compare. Keep what changed, carry forward what did not, and pick the next habit.</td></tr>
      </tbody>
    </table>

    <p>Four weeks per cycle is slow enough for habits to actually change and fast enough that you see progress within a season.</p>

    <h2>Other things that help (and some that do not)</h2>

    <h2>Playing with intention in open play</h2>

    <p>You do not have to give up open play to improve. Turn each session into practice by carrying one rule into it: "I will get to the kitchen after every return", or "I will drop every third shot today, even if I miss". You may lose a few more games while the habit forms. That is the price of changing it.</p>

    <h2>Lessons and clinics</h2>

    <p>A good lesson can shortcut weeks of trial and error, especially for technique. Lessons are most effective when you arrive with a specific problem from your own game ("my drops float when I am under pressure") rather than a general request to get better. Film review gives you exactly that kind of specific problem.</p>

    <h2>New paddles</h2>

    <p>Equipment changes can help at the margins, and a paddle that suits your style is nice to have. But a new paddle rarely breaks a plateau, because plateaus are almost always about habits and decisions. If your problem is not getting to the kitchen, a different paddle will not change it.</p>

    <h2>Watching pro matches</h2>

    <p>Professional matches are fun and occasionally instructive, especially for positioning and patience. Be careful copying their shot choices, though: pros attack balls and take risks that only work with their level of control. Watching recreational players one level above you can teach you more about the shots that will work in your games.</p>

    <h2>Fitness and movement</h2>

    <p>Better movement helps at every level: a quicker split-step, faster recovery, and the ability to get low for dinks and resets. If you are short of breath late in games or your legs feel heavy at the kitchen, a little conditioning can make your technique hold up longer. It just rarely solves a plateau on its own.</p>

    <h2>How much practice versus play?</h2>

    <p>There is no single right ratio, but many improving recreational players find that one focused practice session for every two or three sessions of play works well. Practice does not have to be long. Thirty minutes of a targeted drill with a partner, before open play starts, is often enough to move one habit.</p>

    <h2>Using an app for the loop</h2>

    <p>Coach Dink (made by the author of this site) is built around exactly this loop. You film a game, it identifies the habits costing you points with the moments in the video where they happened, ranks drills that target them, and updates your rating estimate only when you film another game. The point of that last rule is that drills do not move the number; only a change in how you actually play does. The rating is the app's own estimate for tracking progress, not an official one.</p>

    <p>You can run the same loop with a notebook and a phone. What matters is the structure: film, pick two, drill two, film again.</p>''',
    'faqs': [
        ('What is the fastest way to improve at pickleball?',
         'Find out which two habits cost you the most points, ideally by filming a game, then drill those two specifically and check on video that they changed. Targeted practice beats more open play.'),
        ('Why am I not getting better at pickleball?',
         'Usually because you are repeating the same habits in every game without seeing them. Open play rehearses your current way of playing. Filming and targeted drilling break that cycle.'),
        ('How do I get from 3.5 to 4.0 in pickleball?',
         'Focus on getting to the kitchen as a team, a reliable third shot, patience in dink rallies, and resetting hard balls. These matter more than power at this level.'),
        ('How often should I practise versus play pickleball?',
         'A common rhythm is one focused practice session for every two or three play sessions. Even 30 minutes of targeted drilling before open play makes a difference.'),
    ],
    'related': ['pickleball-film-review', 'pickleball-drills-by-level', 'pickleball-rating-levels-explained'],
})

# ---------------------------------------------------------------- 7
ARTICLES.append({
    'slug': 'pickleball-film-review',
    'seo_title': 'Pickleball Film Review: What to Look For | Coach Dink',
    'seo_h1': 'Pickleball Film Review: How to Watch Your Own Games and What to Look For',
    'og_title': 'Pickleball Film Review: What to Look For',
    'meta_desc': 'How to review video of your own pickleball games: a three-pass checklist for position, shot choice and teamwork, what to ignore, and how to practise it.',
    'og_desc': 'A phase-by-phase checklist for reviewing your own pickleball video.',
    'keywords': 'pickleball film review, pickleball video review, how to review pickleball video, analyze my pickleball game, watch pickleball game video, pickleball game analysis',
    'badge': 'How-To',
    'published': '2026-10-01', 'published_label': 'October 1, 2026',
    'card_title': 'Pickleball film review: what to look for',
    'card_desc': 'A phase-by-phase checklist for watching your own games, and what to ignore.',
    'intro': 'Watching yourself play pickleball is uncomfortable the first time and incredibly useful after that. The trap is watching it like a highlight reel: following the ball, wincing at misses, and learning nothing. Good film review is structured. You watch for specific things in a specific order.',
    'quick_answer': 'Review one game, not a whole session. Watch it three times with a different focus each time: first your position (where you are standing on every shot), then your shot choices (soft or hard, and whether the ball was above the net), then your partner and team movement. Ignore technique on the first pass. Write down the two habits that show up most often and cost points, then pick drills for those two.',
    'body': '''<h2>Before you watch</h2>

    <p>Start with a usable clip. A wide, stable view from a corner of the court, with all four corners in frame, makes everything below possible. If your video is zoomed in or the phone moved, see <a href="/coachdink/blog/how-to-film-pickleball/">how to film pickleball</a> first.</p>

    <p>Pick one game to 11. It is long enough for patterns and short enough that you will actually finish reviewing it. Have something to write on. Pause often.</p>

    <h2>Pass 1: watch your feet, not the ball</h2>

    <p>This is the most valuable pass and the hardest one, because your eyes want to follow the ball. Force yourself to watch only where you are standing.</p>

    <div class="info-card">
      <h4>Position checklist</h4>
      <p><strong>When you serve:</strong> do you stay back for the return, or drift forward and get the ball at your feet?</p>
      <p><strong>When you return:</strong> do you move all the way to the kitchen line after hitting? How many shots does it take you to get there?</p>
      <p><strong>After your third shot:</strong> do you move in behind a good drop, or stay at the baseline? Do you stop in the middle?</p>
      <p><strong>At the kitchen:</strong> are your toes near the line, or are you a few feet back?</p>
      <p><strong>During dinks:</strong> do you drift backward as the rally goes on?</p>
    </div>

    <p>A simple way to score this: for each rally, note whether you were at the kitchen line by the time the dinking started. If the answer is no in more than a couple of rallies, you have found your first habit.</p>

    <h2>Pass 2: shot choices</h2>

    <p>Now watch the ball, but only to judge decisions, not execution. A missed shot that was the right choice is fine. A made shot that was the wrong choice is a habit to fix.</p>

    <ul>
      <li><strong>Every hard shot:</strong> was the ball above the net when you hit it? Speeding up from below the net is one of the most common point-losers at 3.0 to 3.5.</li>
      <li><strong>Every third shot:</strong> drop or drive? If drive, did you follow it with a drop on the fifth? Did your drops land in the kitchen or float into the middle?</li>
      <li><strong>Every return:</strong> deep or short? Short returns let the serving team come in.</li>
      <li><strong>Lobs:</strong> did they work, or did they set up the opponent? Lobs from bad positions often become put-aways.</li>
    </ul>

    <p>Some of these connect to specific shots covered elsewhere: the <a href="/coachdink/blog/third-shot-drop/">third shot drop</a>, <a href="/coachdink/blog/pickleball-dinking-tips/">dinking</a>, and the <a href="/coachdink/blog/pickleball-reset-shot/">reset</a>.</p>

    <h2>Pass 3: the team</h2>

    <p>In doubles, watch the two of you as a unit.</p>

    <ul>
      <li>Do you move forward together, or does one partner charge while the other stays back?</li>
      <li>When the ball goes to one sideline, do you both shift toward it?</li>
      <li>Is there a gap down the middle that opponents keep hitting through?</li>
      <li>Who takes the middle ball? Is it consistent, or do you both go for it (or neither)?</li>
    </ul>

    <p>Team problems are nearly invisible during play, because each player only sees their own half. They are obvious on video. The <a href="/coachdink/blog/pickleball-doubles-strategy/">doubles strategy guide</a> covers the usual fixes.</p>

    <h2>What to ignore, at least at first</h2>

    <p>Technique details like grip, wrist angle, and swing path are hard to judge from a wide corner camera, where each player is small in the frame. They also matter less than position and decisions at most recreational levels. Leave them for later or for a close-up clip and a coach.</p>

    <p>Also ignore the one-off disasters. The ball that clipped the net cord, the overhead you shanked. They are memorable but rarely the pattern.</p>

    <h2>A simple scoring sheet</h2>

    <p>Writing tallies as you go keeps the review honest and makes it easy to compare games over time. A sheet with these columns works well:</p>

    <table class="comparison-table">
      <thead>
        <tr><th>Column</th><th>What to tally</th></tr>
      </thead>
      <tbody>
        <tr><td>At the line</td><td>Rallies where you reached the kitchen line before dinking started, out of total rallies.</td></tr>
        <tr><td>Low attacks</td><td>Times you sped up a ball below net height.</td></tr>
        <tr><td>Third shots</td><td>Drops that landed in or near the kitchen versus drops that floated.</td></tr>
        <tr><td>Return depth</td><td>Returns that landed deep versus short.</td></tr>
        <tr><td>Team gaps</td><td>Points lost through the middle or down a sideline your team left open.</td></tr>
      </tbody>
    </table>

    <p>Five columns, one game. The column with the worst numbers usually points straight at your first habit to fix.</p>

    <h2>Common mistakes when reviewing</h2>

    <ul>
      <li><strong>Watching at full speed only.</strong> Slow down or pause on each shot during your positional pass; you will miss most of it at normal speed.</li>
      <li><strong>Focusing only on yourself in doubles.</strong> Half of your problems may be how the two of you move together.</li>
      <li><strong>Judging shots by outcome.</strong> An attack from below the net that happened to win is still a risky choice; a well-chosen drop that clipped the tape is still the right shot.</li>
      <li><strong>Reviewing too many games.</strong> One reviewed properly beats three skimmed.</li>
      <li><strong>Not writing anything down.</strong> Without notes, the review turns back into memory, which is what you were trying to get away from.</li>
    </ul>

    <h2>Turning notes into practice</h2>

    <p>By the end of three passes you will have a list. Cut it to two items, chosen by how often each happened multiplied by how many points it cost. Then pick one drill for each. Our <a href="/coachdink/blog/how-to-improve-at-pickleball/">improvement guide</a> explains this loop and has a table matching common habits to drills.</p>

    <h2>Reviewing a singles game</h2>

    <p>Singles review uses the same three passes, with different emphasis. Position still comes first, but the question changes: instead of "did I reach the kitchen", ask "did I recover to the middle of my baseline after each shot, and did I come forward behind approach shots that were deep enough to allow it?" Shot choice in singles is more about depth and passing angles than about patience in dink rallies, so on the second pass, note how often your shots landed short and gave the opponent an easy approach. Skip the team pass entirely, and spend the time on movement instead: how quickly you split-step and how often you are caught leaning the wrong way.</p>

    <h2>Comparing games over time</h2>

    <p>The first review tells you what is wrong. The second and third tell you whether you fixed it, which is where film review becomes genuinely motivating. Keep your tally sheets, or at least the two numbers that matter most to you, and look at them side by side every month. A move from reaching the kitchen in half your rallies to most of them is a real change in how you play, even if your win rate has not caught up yet. Wins tend to follow a few weeks behind habit changes, because opponents adapt and because a new habit is shaky under pressure at first.</p>

    <h2>Getting your partner involved</h2>

    <p>If you play regularly with the same partner, watch the video together. You will each notice things about the other that the other cannot see, and you will agree on team habits much faster than you would by talking about them between points. Keep it constructive: the goal is two specific things to work on as a team, not a list of each other's errors.</p>

    <h2>How long film review takes</h2>

    <p>Done properly, three passes of a 15 minute game can easily take 45 minutes or more. That time cost is the main reason players stop doing it. Two ways to make it sustainable: review one game every week or two rather than every session, and focus on one pass (usually position) when you are short on time.</p>

    <h2>Letting software do the first pass</h2>

    <p>AI video analysis apps automate much of this. Coach Dink, made by the author of this site, watches the full game, identifies which player you are, and returns the habits costing you points with the moments in the video where each happened, so you can jump straight to them instead of scrubbing through 15 minutes. It then ranks drills for those habits.</p>

    <p>It is still worth watching the moments it points to yourself. Seeing your own habit on screen is what makes the fix stick. For a broader look at the options, see our <a href="/coachdink/blog/pickleball-video-analysis-app/">comparison of video analysis approaches</a>.</p>''',
    'faqs': [
        ('What should I look for when reviewing pickleball video?',
         'Your position on every shot first, especially whether you reach the kitchen line. Then shot choices, such as whether you attacked balls below the net. Then how you and your partner move as a team.'),
        ('How long should a pickleball film review take?',
         'Allow two to three times the length of the game if you pause and rewatch properly. Reviewing one game per week is a sustainable rhythm.'),
        ('Can I see technique problems on game video?',
         'Some, but a wide corner camera makes players small. Position and decisions show up clearly; grip and swing details are better judged from a close camera.'),
        ('Should I review wins or losses?',
         'Both are useful, but a close loss is often the most informative, because it shows the habits that cost you points against opponents at your level.'),
    ],
    'related': ['pickleball-video-analysis-app', 'how-to-film-pickleball', 'how-to-improve-at-pickleball'],
})

# ---------------------------------------------------------------- 8
ARTICLES.append({
    'slug': 'pickleball-drills-by-level',
    'seo_title': 'Best Pickleball Drills for 3.0, 3.5 and 4.0 Players',
    'seo_h1': 'The Best Pickleball Drills for 3.0, 3.5 and 4.0 Players',
    'og_title': 'Pickleball Drills for 3.0, 3.5 and 4.0 Players',
    'meta_desc': 'Pickleball drills matched to your level: what 3.0, 3.5 and 4.0 players should practise, how to run each drill with a partner, and how to know when to move up.',
    'og_desc': 'Drills matched to 3.0, 3.5 and 4.0 players, with how to run each one.',
    'keywords': 'best pickleball drills for 3.0 players, best pickleball drills for 3.5 players, best pickleball drills for 4.0 players, pickleball drills by level, pickleball drills for intermediate players, pickleball drills to improve your game',
    'badge': 'Drills',
    'published': '2026-10-01', 'published_label': 'October 1, 2026',
    'card_title': 'Pickleball drills for 3.0, 3.5 and 4.0 players',
    'card_desc': 'What to practise at each level, how to run each drill, and when to move up.',
    'intro': 'A drill is only useful if it targets something you actually do wrong in games. That depends heavily on your level: a 3.0 player and a 4.0 player lose points in very different ways. Here are the drills that tend to matter most at each stage, with how to run them with one partner.',
    'quick_answer': 'At 3.0, drill consistency and getting to the kitchen: deep serve and return targets, return-and-move, and cooperative dinking. At 3.5, drill the shots that let you come forward and stay there: third shot drop ladders, dink patience games, and transition resets. At 4.0, drill pressure and decisions: hands battles, speed-up and counter, and drop-or-drive decision drills. At every level, the best drill is the one that targets the habit your game video shows most often.',
    'body': '''<h2>How to use this guide</h2>

    <p>Start at your level, but be honest. If you are not sure where you are, our <a href="/coachdink/blog/pickleball-self-rating-guide/">self rating guide</a> will place you. And if a drill from the level below exposes a weakness, do it. Levels are a guide, not a fence.</p>

    <p>All drills below need one partner and a court. A few mention a third player as an option.</p>

    <h2>Drills for 3.0 players</h2>

    <p>At 3.0, most lost points come from errors and from staying back. The focus is consistency and position.</p>

    <div class="info-card">
      <h4>1. Deep target serves and returns</h4>
      <p>Place a towel or cone in the back third of the service box. Take turns serving to it, then returning to the back third. Count how many land deep out of 20. Depth matters more than pace on both shots.</p>
    </div>

    <div class="info-card">
      <h4>2. Return and move</h4>
      <p>Partner serves; you return deep and walk all the way to the kitchen line, split-stepping as your partner hits the third shot. Your partner does not need to play it out. Repeat 20 times until moving forward after the return is automatic.</p>
    </div>

    <div class="info-card">
      <h4>3. Cooperative dinking</h4>
      <p>Both players at the kitchen line, dinking cross-court and then straight, trying to keep the rally going as long as possible. Count your longest rally and try to beat it. The goal is control and soft hands, not winning.</p>
    </div>

    <div class="info-card">
      <h4>4. Volley-to-volley control</h4>
      <p>Stand a few feet behind the kitchen line facing each other and volley gently back and forth, paddle up and in front. This builds the ready position and compact strokes beginners often lack.</p>
    </div>

    <h2>Drills for 3.5 players</h2>

    <p>At 3.5, players usually have the shots but not the reliability, especially in the transition from baseline to kitchen. Drill the shots that get you forward and the patience that keeps you there.</p>

    <div class="info-card">
      <h4>5. Third shot drop ladder</h4>
      <p>Partner at the kitchen line feeds; you start at the baseline and hit drops into the kitchen. After every five good drops, take one step forward. If a drop floats high, your partner attacks it, which makes the feedback honest. See the full <a href="/coachdink/blog/third-shot-drop/">third shot drop guide</a>.</p>
    </div>

    <div class="info-card">
      <h4>6. Dink with a speed-up rule</h4>
      <p>Play out dink rallies to a point, with one rule: you may speed up only a ball that is above net height. Any speed-up from below loses the point immediately. This trains the patience that separates 3.5 from 4.0. More in <a href="/coachdink/blog/pickleball-dinking-tips/">dinking tips</a>.</p>
    </div>

    <div class="info-card">
      <h4>7. Transition reset</h4>
      <p>You stand in the middle of the court; partner at the kitchen hits firm balls at your feet. Your only job is to soften each one back into the kitchen. After a good reset, take a step forward. The <a href="/coachdink/blog/pickleball-reset-shot/">reset shot guide</a> covers the technique.</p>
    </div>

    <div class="info-card">
      <h4>8. Skinny singles</h4>
      <p>Play half-court games (one service box width) with all the normal rules, including the two-bounce rule. You have to drop, move in, and dink to win. It is the most game-like solo-partner drill there is.</p>
    </div>

    <h2>Drills for 4.0 players</h2>

    <p>At 4.0, consistency is mostly there. Points are decided by pressure, decisions, and fast exchanges. Drill those.</p>

    <div class="info-card">
      <h4>9. Hands battles</h4>
      <p>Both at the kitchen line, start with a dink, then either player may speed up a high ball. Play it out with fast volleys. This builds reaction speed and counter-attacking from a compact ready position.</p>
    </div>

    <div class="info-card">
      <h4>10. Drop or drive decision drill</h4>
      <p>Partner feeds you a mix of returns from the kitchen: some deep and low, some short or high. You decide each time whether to drop or drive, then play the next shot to the kitchen. The skill is reading the ball, not the shot itself.</p>
    </div>

    <div class="info-card">
      <h4>11. Speed-up and counter</h4>
      <p>From a dink rally, one player is assigned as the attacker and must speed up the first attackable ball; the other must counter or reset. Swap roles. It builds both sides of the most important exchange at 4.0.</p>
    </div>

    <div class="info-card">
      <h4>12. Two-on-one patterns</h4>
      <p>With a third player, two players at the kitchen dink against one, who must defend the whole width. The single player gets intense footwork and reset practice; the pair practises moving the ball to create an opening.</p>
    </div>

    <h2>Drills you can do alone</h2>

    <p>No partner? A wall or a backboard still gives you useful reps.</p>

    <div class="info-card">
      <h4>Solo options</h4>
      <p><strong>Wall dinks:</strong> stand a few feet from a wall and hit soft shots that would clear a net-height line taped on the wall. Builds touch and a consistent lifting motion.</p>
      <p><strong>Wall volleys:</strong> stand further back and volley continuously with the paddle up and in front. Great for hands and the ready position.</p>
      <p><strong>Serve targets:</strong> on an empty court, serve to cones in the back third of each service box. Count your hits out of 20 and track it over weeks.</p>
      <p><strong>Footwork:</strong> shadow the return-and-move pattern without a ball: return motion, walk forward, split-step at the line, recover. It sounds silly and works.</p>
    </div>

    <h2>Signs you are ready to move up a level of drills</h2>

    <ul>
      <li>You can complete the drill at your level with few errors, even when you add scoring.</li>
      <li>The habit the drill targets no longer shows up when you film a game.</li>
      <li>Your partner has to work hard to make the drill difficult for you.</li>
    </ul>

    <p>When two of those are true, take the next drill from the level above, or add pressure to the current one by playing it to points.</p>

    <h2>How to structure a practice session</h2>

    <ul>
      <li><strong>Warm up (5 minutes):</strong> cooperative dinking and volleys.</li>
      <li><strong>Main drill (15 to 20 minutes):</strong> one drill that targets your biggest habit.</li>
      <li><strong>Pressure version (5 to 10 minutes):</strong> the same drill with scoring.</li>
      <li><strong>Game (optional):</strong> skinny singles or a regular game, focusing on that one thing.</li>
    </ul>

    <p>Thirty to forty minutes is plenty. One habit per session is more effective than rotating through every drill on this page.</p>

    <h2>Making drills feel like games</h2>

    <p>The biggest weakness of most drills is that they are too comfortable. You hit the same ball from the same spot, it goes well, and then the habit vanishes the moment a real opponent is trying to beat you. A few simple tweaks make practice transfer better.</p>

    <ul>
      <li><strong>Add scoring.</strong> Play the drill to 11 points. The moment there is something to lose, you will feel the same tension you feel in games.</li>
      <li><strong>Add a consequence.</strong> If a drop floats, your partner attacks it. If you speed up a low ball, you lose the point. Honest feedback is what makes the drill teach.</li>
      <li><strong>Randomise the feed.</strong> Instead of the same ball every time, your partner mixes depth, height and direction. Real games never give you the same ball twice.</li>
      <li><strong>Finish with a live ball.</strong> End each repetition by playing the point out, so the drilled shot is followed by the decision that comes next in a real rally.</li>
    </ul>

    <h2>Common drilling mistakes</h2>

    <p>The most common is drilling what you are already good at. It feels productive because it goes well. The second is drilling without a reason: running through a list of drills from a video without knowing whether any of them target your actual problems. The third is stopping too soon. A habit usually needs several sessions, spread over a couple of weeks, before it holds up in games. If you change drills every session, nothing quite sticks.</p>

    <h2>Choosing the right drill</h2>

    <p>The drills above are grouped by level because that is how players search for them, but the best way to pick is from your own games. If video shows you stopping in the transition zone, drill 2 or 7 will do more than any dinking drill, whatever your level. Our <a href="/coachdink/blog/how-to-improve-at-pickleball/">improvement guide</a> lays out the loop: film, find two habits, drill them, film again.</p>

    <p>Coach Dink, made by the author of this site, has a library of around 50 drills organised by shot and skill, and after each filmed game it ranks the ones that target what the report found. Whether you use an app or a notebook, matching the drill to the habit is what makes practice count.</p>''',
    'faqs': [
        ('What are the best pickleball drills for 3.0 players?',
         'Deep serve and return targets, return-and-move to the kitchen line, cooperative dinking, and volley control. The focus at 3.0 is consistency and getting to the front of the court.'),
        ('What drills help a 3.5 pickleball player get to 4.0?',
         'Third shot drop ladders, dink rallies with a rule against speeding up low balls, transition reset drills, and skinny singles. These build the patience and transition play that 4.0 requires.'),
        ('Can you do pickleball drills alone?',
         'Some, with a wall or ball machine, such as wall dinking and volley control. Most drills that build game skills, like drops and resets, work best with a partner.'),
        ('How long should a pickleball drill session be?',
         'Thirty to forty minutes focused on one habit is usually enough. Longer sessions tend to lose focus.'),
        ('How often should I drill instead of playing?',
         'Many players do well with one focused drill session for every two or three play sessions.'),
    ],
    'related': ['how-to-improve-at-pickleball', 'third-shot-drop', 'pickleball-reset-shot'],
})
