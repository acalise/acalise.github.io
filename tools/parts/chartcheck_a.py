# -*- coding: utf-8 -*-
"""
ChartCheck blog content, part A (October 2026 batch).

Eight articles: the product-matched "ai chart analysis *" cluster (best apps,
free options, prompts, stocks, gold, trading bots) plus two method pieces
(multi-timeframe analysis, volume). Same dict shape as content_chartcheck.py,
with card_title / card_desc included inline.
"""

ARTICLES = []

# ---------------------------------------------------------------- A1
ARTICLES.append({
    'slug': 'best-ai-chart-analysis-apps',
    'seo_title': 'Best AI Chart Analysis Apps: An Honest Guide | ChartCheck',
    'seo_h1': 'The Best AI Chart Analysis Apps, Grouped by What They Actually Do',
    'og_title': 'The Best AI Chart Analysis Apps',
    'meta_desc': 'An honest guide to AI chart analysis apps: chatbots with vision, charting platforms with automated pattern tools, and dedicated screenshot analysers.',
    'og_desc': 'Chatbots, charting platforms and screenshot analysers: what each kind of AI chart tool is good at, and who it suits.',
    'keywords': 'best ai chart analysis app, ai trading chart analyzer, ai stock chart analysis app, ai chart analyzer, chart analysis app, ai technical analysis app',
    'badge': 'Comparison',
    'published': '2026-10-01', 'published_label': 'October 1, 2026',
    'card_title': 'The Best AI Chart Analysis Apps',
    'card_desc': 'Three very different kinds of tool sell under the same label. What each one is good at, and how to pick.',
    'intro': 'Search for an AI chart analysis app and you get three very different kinds of product under the same label: general chatbots that can read an image, charting platforms with automated pattern detection, and dedicated apps that read a screenshot. They solve different problems. Picking the right one is mostly a matter of knowing which problem you have.',
    'quick_answer': 'If you read a few charts a week, a general-purpose chatbot with vision and a good prompt is enough. If you live inside a charting platform and want trendlines and patterns detected automatically on live data, use the automated tools built into that platform. If you want a consistent, structured read of a screenshot from any app, in the same shape every time, a dedicated screenshot analyser such as ChartCheck (made by the author of this site) is built for that. None of them predicts price, and any that claims to should be treated with suspicion.',
    'body': '''<h2>Disclosure first</h2>

    <p>ChartCheck is made by the author of this site, so treat its section below as a description from the maker rather than an independent review. The rest of this guide describes categories of tool and the public, well-known products in them. It does not rank anything on accuracy, because nobody has a fair, public benchmark for "chart read quality", and any list that claims to is guessing.</p>

    <h2>The three kinds of AI chart tool</h2>

    <table class="comparison-table">
      <thead>
        <tr><th>Kind</th><th>Input</th><th>Strongest at</th><th>Weakest at</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>General chatbot with vision</td>
          <td>Any image you upload</td>
          <td>Explaining concepts, follow-up conversation</td>
          <td>Consistent output, remembering your context</td>
        </tr>
        <tr>
          <td>Charting platform automation</td>
          <td>Live price data on the platform</td>
          <td>Exact levels, scanning many symbols</td>
          <td>Only works inside that platform</td>
        </tr>
        <tr class="highlight-row">
          <td>Dedicated screenshot analyser</td>
          <td>A screenshot from any app</td>
          <td>Same structured read every time</td>
          <td>Limited to what is in the frame</td>
        </tr>
      </tbody>
    </table>

    <h2>1. General-purpose chatbots with vision</h2>

    <p>ChatGPT, Claude and Gemini all accept images and will describe a chart you upload. For a free or already-paid-for tool, the read is often surprisingly good: trend direction, the sequence of highs and lows, obvious horizontal levels and the common named patterns.</p>

    <p>Where they struggle is consistency and context. Each answer is shaped differently, so two charts are hard to compare side by side. They do not know your timeframe, your indicator settings or how long you hold a trade unless you type it every time. They also tend to agree with whatever framing you give them, which is the subject of our piece on <a href="/chartcheck/blog/chart-analysis-with-chatgpt/">using ChatGPT for chart analysis</a>.</p>

    <div class="info-card">
      <h4>Best for</h4>
      <p>Occasional reads, learning vocabulary, and asking "why" questions about a specific candle or pattern. Pair it with a fixed prompt from our <a href="/chartcheck/blog/ai-stock-analysis-prompt/">prompt templates</a> and you remove most of the inconsistency.</p>
    </div>

    <h2>2. Charting platforms with automated analysis</h2>

    <p>Major charting platforms have their own automation. TradingView offers built-in automatic pattern and trendline indicators alongside a very large library of community-written scripts. TrendSpider is built specifically around automated trendline and pattern detection on live data, with scanning across many symbols.</p>

    <p>The structural advantage here is that these tools work on the underlying price data rather than a picture of it. Levels are exact, not read off an axis. They can scan a whole watchlist in a way an image-based tool cannot.</p>

    <p>The tradeoff is that you have to be inside that platform. If your charts live in a broker app, a crypto exchange or MetaTrader, the automation does not follow you there. Detection rules are also mechanical: a script finds whatever shape its parameters describe, which is precise but literal.</p>

    <div class="info-card">
      <h4>Best for</h4>
      <p>Active traders who already chart on one platform and want scanning and exact, data-derived levels across many symbols.</p>
    </div>

    <h2>3. Dedicated screenshot analysers</h2>

    <p>This is the category ChartCheck sits in. You screenshot a chart from whatever app you already use and get a structured technical read back. The idea is not that a vision model is smarter than a chatbot; it is that the workflow is built around chart reading specifically.</p>

    <p>In ChartCheck's case that means every read comes back in the same order: trend and structure, support and resistance zones described by where they formed, chart and candlestick patterns marked complete or still forming, whatever indicators are visible, a plain-language summary, a confidence level describing how legible the chart was, and an explicit list of what it could not see. You can then ask follow-up questions in a thread attached to that read, and earlier reads of the same asset stay with it.</p>

    <p>The limits are the limits of any picture. It cannot see the level from six months ago if you cropped it out, it has no order book, fundamentals or news, and it does not predict price.</p>

    <div class="info-card">
      <h4>Best for</h4>
      <p>People who chart across several apps, want comparable reads on many charts, and prefer not to retype context every time.</p>
    </div>

    <h2>How to judge any AI chart analyser</h2>

    <p>Marketing in this category is loud. These checks cut through it quickly.</p>

    <ol>
      <li><strong>Does it describe or does it predict?</strong> A tool that describes structure, levels and patterns is doing something achievable. A tool that tells you where price is going, or labels charts "buy" and "sell", is claiming something nothing can reliably do.</li>
      <li><strong>Does it admit what it cannot see?</strong> A good read names its blind spots: cropped history, unreadable axis labels, missing volume. A read that never says "I could not tell" is filling gaps silently.</li>
      <li><strong>What does its confidence score measure?</strong> It should measure how clearly the chart could be read. If it is presented as a probability that the trade works, that is a red flag.</li>
      <li><strong>Is the output the same shape every time?</strong> Comparing reads across charts is most of the value. Free-form prose makes that hard.</li>
      <li><strong>Does it promise returns?</strong> Win rates, "accuracy" percentages and profit screenshots are not evidence of anything. Walk away.</li>
    </ol>

    <h2>Test any of them in five minutes</h2>

    <p>Take three screenshots you already understand well: a clean trending daily chart, a choppy sideways one, and a deliberately bad capture with the price axis cropped off. Run all three through the tool.</p>

    <ul>
      <li>The trending chart should get a correct structural description and a high legibility score.</li>
      <li>The choppy chart should be described as range-bound or unclear, not forced into a pattern.</li>
      <li>The cropped chart should get a low confidence and a clear note that the price axis is missing. If the tool confidently quotes price levels off a chart with no price axis, you have learned what you needed to know.</li>
    </ul>

    <p>That third test is the most revealing one. How a tool behaves on a bad input tells you more about it than how it behaves on a textbook chart, and it takes about a minute. Our guide to <a href="/chartcheck/blog/screenshot-a-chart-for-analysis/">screenshotting a chart properly</a> covers what a good input looks like.</p>

    <h2>Which one should you use?</h2>

    <p>Honestly, many people need only one, and it is often the cheapest one. If you look at charts occasionally, use a chatbot with a structured prompt. If you scan dozens of symbols on one platform, use that platform's automation. If you read a steady flow of charts from different apps and want them in a consistent, comparable format, that is the problem a dedicated analyser is built to solve. Whichever you choose, keep the output in its place: a fast, unbiased second read of what already happened, never a signal.</p>''',
    'faqs': [
        ('What is the best AI chart analysis app?',
         'It depends on the problem. A chatbot with vision is enough for occasional reads, charting-platform automation is best for scanning on live data, and a dedicated screenshot analyser suits people who want consistent structured reads from any app. There is no public benchmark of read accuracy, so be wary of any ranking that claims one is "most accurate".'),
        ('Can an AI chart analyzer predict stock prices?',
         'No. AI chart analysis describes what a chart has already done: trend, levels, patterns and indicator readings. It does not know the future, and tools that present their output as price predictions or buy and sell signals are overstating what is possible.'),
        ('Is ChartCheck independent of this blog?',
         'No. ChartCheck is made by the author of this site. That is why this guide sticks to describing categories and well-known public products instead of ranking accuracy.'),
        ('Do AI chart analysis apps work on crypto and forex?',
         'Image-based tools work on any chart that is legible as a picture, including stocks, ETFs, crypto, forex and futures. Market quirks still matter, such as crypto having no daily close and spot forex having no centralised volume.'),
    ],
    'related': ['ai-chart-analysis', 'chart-analysis-with-chatgpt', 'ai-chart-analysis-free'],
})

# ---------------------------------------------------------------- A2
ARTICLES.append({
    'slug': 'ai-chart-analysis-free',
    'seo_title': 'Free AI Chart Analysis: What You Get and What It Costs',
    'seo_h1': 'Free AI Chart Analysis: What You Actually Get, and the Hidden Costs',
    'og_title': 'Free AI Chart Analysis: What You Actually Get',
    'meta_desc': 'The genuinely free ways to get AI chart analysis, what each one does well, the hidden costs of free tools, and the red flags that mean free is a funnel.',
    'og_desc': 'The genuinely free ways to get an AI read on a trading chart, and the red flags that mean free is really a funnel.',
    'keywords': 'ai chart analysis free, ai trading chart analysis free, ai stock chart analysis free, free ai chart analyzer, free ai technical analysis',
    'badge': 'Guide',
    'published': '2026-10-01', 'published_label': 'October 1, 2026',
    'card_title': 'Free AI Chart Analysis',
    'card_desc': 'The genuinely free options, what they do well, and the red flags that mean free is really a sales funnel.',
    'intro': 'You can get a competent AI read on a trading chart without paying anything. The free options are real and useful. They also come with costs that are not on a price tag: your time, inconsistency, and in some corners of this market, a funnel built to sell you something much worse than a subscription.',
    'quick_answer': 'The most capable free option is the free tier of a general-purpose chatbot that accepts images, combined with a structured prompt. Charting platforms also include free automated pattern and trendline tools on live data. What free tools cost you is consistency and context: you retype your setup every time and get differently-shaped answers. Be wary of "free AI signals" offered through Telegram, Discord or social media, which are frequently funnels to paid groups, brokers or outright scams.',
    'body': '''<h2>The genuinely free options</h2>

    <p>There are three honest routes to a free AI read of a chart. None of them requires a credit card, and each is good at something different.</p>

    <h2>1. Free tiers of general chatbots</h2>

    <p>Most general-purpose assistants now accept image uploads on their free tiers, usually with limits on how many images or messages you can send in a period. Upload a chart and ask for a description and you will typically get trend direction, a description of recent highs and lows, obvious support and resistance areas, named patterns and a reading of any visible indicators.</p>

    <p>The quality is real. The weakness is that a free-form question gets a free-form answer, and that answer leans toward agreeing with however you framed the question. Fix both with a fixed prompt. We publish several in <a href="/chartcheck/blog/ai-stock-analysis-prompt/">AI stock analysis prompts</a>, ready to paste.</p>

    <h2>2. Built-in automation on charting platforms</h2>

    <p>Charting platforms commonly include automatic pattern and trendline tools, and community-written indicators that do similar jobs, at no cost on their free plans. Because these work on the actual price data rather than a picture, the levels they mark are exact.</p>

    <p>They are not "AI" in the chatbot sense: they apply fixed detection rules. That makes them precise and literal. A script will find a triangle wherever its parameters say one exists, whether or not a human would call it meaningful. They also explain nothing, which matters if you are learning.</p>

    <h2>3. Free trials of dedicated tools</h2>

    <p>Dedicated chart analysis apps commonly offer a trial or a limited free allowance, because each analysis costs real compute to run. A trial is the right way to judge one: run the five-minute test in our guide to the <a href="/chartcheck/blog/best-ai-chart-analysis-apps/">best AI chart analysis apps</a> on charts you already understand before paying for anything.</p>

    <h2>Getting a good read from a free chatbot</h2>

    <p>Most of the gap between a free chatbot and a paid tool is the input and the prompt, not the model. These four habits close most of it.</p>

    <ol>
      <li><strong>Send a clean screenshot.</strong> Price axis visible, timeframe visible, enough bars for context, no overlapping drawings. A bad capture produces a vague or wrong read regardless of the tool. See <a href="/chartcheck/blog/screenshot-a-chart-for-analysis/">how to screenshot a chart</a>.</li>
      <li><strong>State what it cannot see.</strong> Symbol, timeframe and indicator settings. The model reads the image; it does not know your RSI is set to 21 periods unless you say so.</li>
      <li><strong>Ask for a fixed structure.</strong> Trend, levels, patterns, indicators, then "what you cannot see". Same order every time, so reads are comparable.</li>
      <li><strong>Ask neutrally.</strong> "Describe this chart" not "this is about to break out, right?" Leading questions get agreeable answers.</li>
    </ol>

    <h2>What free actually costs</h2>

    <div class="info-card">
      <h4>The costs that are not on the price tag</h4>
      <p><strong>Time.</strong> Retyping symbol, timeframe, settings and trading style for every chart. Fine for two charts a week, a real friction at twenty.</p>
      <p><strong>Consistency.</strong> Free-form answers vary in shape, so comparing this week's read with last week's is harder than it should be.</p>
      <p><strong>Memory.</strong> Free chats rarely keep a tidy history per asset, so you lose the ability to see how your read of one chart changed over time.</p>
      <p><strong>Limits.</strong> Free tiers cap image uploads. When you hit the cap mid-session, you either stop or switch tools, and the reads stop being comparable.</p>
    </div>

    <p>None of these are reasons to pay. They are reasons to decide based on volume. If the free route is enough for how often you look at charts, it is the correct choice.</p>

    <h2>Red flags: when free is a funnel</h2>

    <p>A separate corner of this market uses "free AI chart analysis" or "free AI signals" as bait. It usually lives in Telegram channels, Discord servers, and social media accounts with screenshots of winning trades. The pattern is consistent enough to recognise:</p>

    <ul>
      <li><strong>Directional calls, not descriptions.</strong> "AI says BUY at this price, target here, stop there." Description of a chart is achievable. Reliable directional calls are not, from anyone.</li>
      <li><strong>Accuracy percentages.</strong> A claimed win rate with no audited, verifiable record behind it means nothing. Selective screenshots of winners prove only that the account has winners to screenshot.</li>
      <li><strong>A referral link to a specific broker.</strong> Free signals that require you to open an account at one particular broker are often paid for by that broker, sometimes per deposit.</li>
      <li><strong>Upsell to a "VIP" group.</strong> The free tier exists to sell the paid one, and the paid one is the same content with more urgency.</li>
      <li><strong>Pressure.</strong> Countdown timers, "last spots", requests to move to private messages. Legitimate educational tools do not need urgency.</li>
    </ul>

    <p>Regulators in several countries have published warnings about AI trading claims of this kind. If a free tool is telling you what to buy, ask what it is really selling.</p>

    <h2>What a free read can and cannot tell you</h2>

    <p>Whether the tool is free or paid, the structural limits are the same, and they are covered in <a href="/chartcheck/blog/ai-chart-analysis/">what AI chart analysis can and cannot do</a>. A picture of a chart contains no order book, no fundamentals, no news, and nothing outside the frame. Paying more does not change that. What paying buys, at best, is a better workflow around the same underlying capability.</p>

    <h2>A sensible way to start</h2>

    <p>Start free. Use a chatbot with a structured prompt on a handful of charts you already understand, so you can judge whether the reads are correct. Notice where the friction is. If it is retyping and inconsistency, a dedicated tool may be worth a trial. If it is that you cannot judge whether a read is right, the better investment is learning to <a href="/chartcheck/blog/how-to-read-a-stock-chart/">read a chart yourself</a> first, because any tool is only as useful as your ability to evaluate it.</p>''',
    'faqs': [
        ('Is there a completely free AI chart analysis tool?',
         'Yes. The free tiers of general-purpose chatbots that accept images will analyse a chart screenshot, usually with limits on uploads. Charting platforms also include free automated pattern and trendline indicators. Neither requires a payment method.'),
        ('Is free AI chart analysis as good as paid?',
         'The underlying reading capability can be similar. What dedicated paid tools typically add is workflow: a stored trading profile, the same output structure every time, and a history of reads per asset. If you only analyse a few charts a week, free is usually enough.'),
        ('Are free AI trading signals legit?',
         'Treat them with heavy suspicion. Channels offering free AI buy and sell signals are frequently funnels to paid groups or specific brokers, and some are scams. No tool reliably predicts price, so a free service claiming to is overstating its ability.'),
        ('Can I use a free AI tool for crypto charts?',
         'Yes. Image-based analysis works on any legible chart. Crypto has its own quirks, such as no daily close and exchange-specific volume, which are covered in our crypto chart analysis guide.'),
    ],
    'related': ['best-ai-chart-analysis-apps', 'ai-stock-analysis-prompt', 'chart-analysis-with-chatgpt'],
})

# ---------------------------------------------------------------- A3
ARTICLES.append({
    'slug': 'ai-stock-analysis-prompt',
    'seo_title': 'AI Stock Analysis Prompts: 6 Copy-Paste Templates',
    'seo_h1': 'AI Stock Analysis Prompts: Six Copy-Paste Templates That Avoid the Usual Traps',
    'og_title': 'AI Stock Analysis Prompts: 6 Templates',
    'meta_desc': 'Six copy-paste prompts for AI stock chart analysis in ChatGPT, Claude or Gemini: first read, levels, patterns, timeframes, devil\'s advocate and journaling.',
    'og_desc': 'Six copy-paste prompts for analysing a stock chart with ChatGPT, Claude or Gemini, and why each line is there.',
    'keywords': 'ai stock analysis prompt, ai stock market analysis prompt, chatgpt stock analysis prompt, chatgpt prompt for chart analysis, ai trading prompt, stock analysis prompt',
    'badge': 'Templates',
    'published': '2026-10-01', 'published_label': 'October 1, 2026',
    'card_title': 'AI Stock Analysis Prompts',
    'card_desc': 'Six copy-paste templates for chart analysis in any chatbot, and why each line is in there.',
    'intro': 'Most bad AI stock analysis comes from a bad prompt, not a bad model. A vague question gets a vague, agreeable, differently-shaped answer every time. These six templates are built to get description instead of prediction, a fixed structure you can compare across charts, and an honest list of what the model could not see.',
    'quick_answer': 'A good chart analysis prompt does four things: it gives the model the context it cannot see (symbol, timeframe, indicator settings), it demands a fixed output order, it bans predictions and trade suggestions, and it asks the model to list what it could not see. The six templates below cover a first read, levels, pattern checks, two-timeframe comparison, a devil\'s advocate review, and a journaling summary. Paste them into ChatGPT, Claude or Gemini with a chart screenshot attached.',
    'body': '''<h2>Why the prompt matters so much</h2>

    <p>General-purpose models are good at reading a chart image and bad at three things that a prompt can fix. They answer in a different shape every time. They do not know what is not in the picture. And they lean toward agreeing with the framing of the question. A prompt that addresses all three turns a chatty assistant into a fairly disciplined first-pass technician.</p>

    <p>Each template below uses square brackets for the parts you fill in. Attach the chart screenshot in the same message. If you have not already, read <a href="/chartcheck/blog/screenshot-a-chart-for-analysis/">how to screenshot a chart</a>; no prompt rescues a capture with the price axis cropped off.</p>

    <h2>1. The structured first read</h2>

    <p>Use this as your default. It is the template to save somewhere you can paste from.</p>

    <div class="script-box">
      <span class="who">Prompt</span>
      <p>Analyse the attached chart. Describe it; do not tell me what to do with it.</p>
      <p>Context: [SYMBOL], [TIMEFRAME] candles, roughly [NUMBER] bars visible. Indicators shown: [LIST WITH SETTINGS, e.g. 50 and 200 SMA, RSI 14].</p>
      <p>Answer in exactly this order, with these headings:<br>
      1. Trend and structure: the sequence of highs and lows, and whether it is intact or has broken.<br>
      2. Key levels: each zone described by where it formed and how many times it was tested. Approximate prices only, labelled approximate.<br>
      3. Patterns: name any chart or candlestick patterns, and say whether each is complete or still forming.<br>
      4. Indicators: read only what is visible in the image.<br>
      5. Legibility: how clearly could you read this chart, low, medium or high, and why.<br>
      6. What you cannot see: anything cropped, unreadable or missing.</p>
      <p>Do not predict direction. Do not suggest entries, exits, stops or targets.</p>
    </div>

    <p>The legibility line keeps the confidence honest: it asks how clear the picture is, not how likely a trade is to work. The last section is the most important. It forces the model to surface blind spots instead of quietly filling them in.</p>

    <h2>2. Levels only</h2>

    <p>When you want a focused list of support and resistance zones without a full read.</p>

    <div class="script-box">
      <span class="who">Prompt</span>
      <p>From the attached [TIMEFRAME] chart of [SYMBOL], list the horizontal zones where price has reacted more than once.</p>
      <p>For each zone give: approximate price range, whether it acted as support, resistance or both, roughly how many reactions, and how recent the last reaction was.</p>
      <p>Order them from nearest to current price to furthest. If you cannot read the price axis precisely, say so and describe zones by position instead (for example "the March lows").</p>
    </div>

    <p>Asking for a range rather than a single number matches how levels actually behave, as covered in <a href="/chartcheck/blog/support-and-resistance/">how to draw support and resistance</a>.</p>

    <h2>3. Pattern check</h2>

    <p>When you think you see a pattern and want an independent opinion. Note that you do not name the pattern in the prompt.</p>

    <div class="script-box">
      <span class="who">Prompt</span>
      <p>Look at the attached chart of [SYMBOL] on the [TIMEFRAME]. Are there any recognised chart patterns or candlestick patterns in the most recent [NUMBER] bars?</p>
      <p>For each one: name it, describe exactly which swings or candles form it, say whether it is complete, and state what would invalidate it. If nothing qualifies cleanly, say that rather than forcing a pattern.</p>
    </div>

    <p>"If nothing qualifies, say that" is the key line. Without it, models tend to find a pattern because you asked for one.</p>

    <h2>4. Two-timeframe comparison</h2>

    <p>Attach two screenshots of the same symbol: one higher timeframe, one lower. This is the AI version of the top-down method in <a href="/chartcheck/blog/multi-timeframe-analysis/">multi-timeframe analysis</a>.</p>

    <div class="script-box">
      <span class="who">Prompt</span>
      <p>Image 1 is [SYMBOL] on the [HIGHER TIMEFRAME]. Image 2 is the same symbol on the [LOWER TIMEFRAME].</p>
      <p>1. Describe the trend and structure on each separately.<br>
      2. Say whether they agree or conflict.<br>
      3. Identify which higher-timeframe level, if any, the lower-timeframe chart is currently trading near.<br>
      4. List anything visible on one chart that is invisible on the other.</p>
      <p>Description only, no trade suggestions.</p>
    </div>

    <h2>5. Devil's advocate</h2>

    <p>The most useful prompt for someone who already has a view. It counters the model's tendency to agree with you.</p>

    <div class="script-box">
      <span class="who">Prompt</span>
      <p>I have a [BULLISH / BEARISH] read on the attached [SYMBOL] [TIMEFRAME] chart because [YOUR REASONS].</p>
      <p>Argue the opposite case as strongly as the chart allows. What on this chart contradicts my read? Which of my reasons is weakest? What would I expect to see if I were wrong?</p>
      <p>Base everything on what is visible in the image.</p>
    </div>

    <p>Here you deliberately state your view, but you ask the model to attack it rather than confirm it. That reverses the agreeableness problem and turns it into something useful.</p>

    <h2>6. Journal summary</h2>

    <p>For keeping a trading journal of what charts looked like at the time you looked at them.</p>

    <div class="script-box">
      <span class="who">Prompt</span>
      <p>Summarise the attached [SYMBOL] [TIMEFRAME] chart in five bullet points for a trading journal: trend, nearest level above, nearest level below, any pattern in progress, and one thing that is unclear. Keep each bullet under fifteen words. Include today's date: [DATE].</p>
    </div>

    <p>Short, dated, fixed-format notes are what make a journal useful later. You can look back and compare what you thought the chart showed with what happened next, which is the fastest honest feedback loop available.</p>

    <h2>Lines to never put in a prompt</h2>

    <ul>
      <li><strong>"Should I buy?"</strong> It pushes the model from description into prediction, where it will still answer confidently.</li>
      <li><strong>"Give me a price target."</strong> Same problem, with a specific number attached, which feels more authoritative and is not.</li>
      <li><strong>"This is bullish, right?"</strong> A leading question. You will get reasons you are right.</li>
      <li><strong>"Be accurate."</strong> It changes nothing. Asking it to list what it cannot see does far more.</li>
    </ul>

    <h2>When typing prompts stops being worth it</h2>

    <p>Templates work well for a handful of charts. The friction appears at volume: filling in brackets, re-attaching context, and keeping reads in a consistent format across sessions. That workflow problem, rather than any extra intelligence, is what dedicated tools such as ChartCheck are built around: you set up how you trade once, and every screenshot comes back in the same structure with a legibility-based confidence level and a "what I couldn't see" list. If you only read a few charts a week, the prompts above are enough.</p>''',
    'faqs': [
        ('What is the best prompt for AI stock chart analysis?',
         'One that supplies context the model cannot see (symbol, timeframe, indicator settings), asks for a fixed output order, bans predictions and trade suggestions, and asks the model to list what it could not see. Template 1 above does all four.'),
        ('Do these prompts work in ChatGPT, Claude and Gemini?',
         'Yes. They are plain-language instructions and work in any assistant that accepts an image. Output quality depends mostly on the screenshot: price axis visible, timeframe visible, and enough bars for context.'),
        ('Can a prompt make AI predict stock prices accurately?',
         'No. A prompt can make the description of a chart more structured and more honest, but it cannot give the model information about the future that is not in the image. Prompts that ask for predictions get confident answers, not reliable ones.'),
        ('Why should I avoid telling the AI my position?',
         'General-purpose assistants lean toward agreeing with the framing of a question. If you say you are long, the analysis tends to find reasons to support that. Ask neutrally, or use the devil\'s advocate template to have it argue against your view.'),
    ],
    'related': ['chart-analysis-with-chatgpt', 'ai-chart-analysis-free', 'screenshot-a-chart-for-analysis'],
})

# ---------------------------------------------------------------- A4
ARTICLES.append({
    'slug': 'ai-technical-analysis-stocks',
    'seo_title': 'AI Technical Analysis of Stocks: What It Reads | ChartCheck',
    'seo_h1': 'AI Technical Analysis of Stocks: What It Reads, and What Stocks Add',
    'og_title': 'AI Technical Analysis of Stocks',
    'meta_desc': 'How AI technical analysis works on stock charts, the stock-specific details that change the read (gaps, earnings, volume, splits), and how to use it well.',
    'og_desc': 'How AI reads a stock chart, and the stock-specific details like gaps, earnings and splits that change the read.',
    'keywords': 'ai technical analysis of stocks, ai stock technical analysis, ai stock chart analysis, ai technical analysis for stocks, ai stock chart reader, stock chart ai',
    'badge': 'By Market',
    'published': '2026-10-01', 'published_label': 'October 1, 2026',
    'card_title': 'AI Technical Analysis of Stocks',
    'card_desc': 'Gaps, earnings, real volume and splits: what is specific to stock charts and how it changes an AI read.',
    'intro': 'Stocks are the market technical analysis was originally written for, and in some ways the easiest for AI to read: they have real sessions, real closes and centralised volume. They also carry quirks that a picture of a chart cannot explain on its own, such as earnings gaps and stock splits. Knowing those quirks is the difference between a useful AI read and a confidently wrong one.',
    'quick_answer': 'AI technical analysis of a stock reads the same things a technician would from a screenshot: trend and structure, support and resistance, patterns, moving averages, RSI, MACD and volume. Stocks are well suited to it because they have defined sessions, real closes and exchange-reported volume. The stock-specific traps are gaps (especially around earnings, which the chart cannot explain), split-adjusted versus unadjusted history, pre-market and after-hours bars, and the difference between a single stock and the broader market. Supply that context and the read improves substantially.',
    'body': '''<h2>Why stocks suit chart analysis</h2>

    <p>Classical technical analysis grew up on stock charts, and the conventions show it. Several features of a typical stock chart make the picture more informative than charts of other markets.</p>

    <ul>
      <li><strong>Real sessions.</strong> A trading day opens and closes, so each daily candle summarises a defined period. The close is a meaningful price, not an arbitrary midnight in one time zone.</li>
      <li><strong>Exchange-reported volume.</strong> Volume on a stock chart reflects reported trading, rather than a single broker's tick count, so it carries information about participation. See <a href="/chartcheck/blog/volume-analysis-trading/">how to read volume</a>.</li>
      <li><strong>Widely watched conventions.</strong> The 50 and 200 day moving averages, prior highs and round numbers are watched by enough participants that price often reacts around them.</li>
    </ul>

    <p>That combination means a clean daily stock chart is usually a high-legibility input for any AI reader.</p>

    <h2>What an AI read covers</h2>

    <p>A good read of a stock chart runs a consistent first-pass checklist, the same one described in <a href="/chartcheck/blog/how-to-read-a-stock-chart/">how to read a stock chart</a>:</p>

    <ol>
      <li><strong>Trend and structure.</strong> Higher highs and higher lows, or lower highs and lower lows, and where that sequence last broke.</li>
      <li><strong>Levels.</strong> Price zones that have been tested more than once, prior highs and lows, and gap edges.</li>
      <li><strong>Patterns.</strong> Bases, flags, wedges, triangles, head and shoulders, double tops and bottoms, and candlestick formations at those levels.</li>
      <li><strong>Moving averages.</strong> Where price sits relative to visible averages, and whether the averages slope up, down or flat.</li>
      <li><strong>Momentum indicators.</strong> RSI and MACD readings if those panels are in the screenshot.</li>
      <li><strong>Volume.</strong> Whether moves happened on expanding or contracting participation.</li>
    </ol>

    <h2>The stock-specific traps</h2>

    <p>These are things a picture of a stock chart shows without explaining. An AI reader will see them; it cannot know their cause unless you tell it.</p>

    <h2>Earnings gaps</h2>

    <p>A stock that reports earnings can open far from the prior close, leaving a gap on the chart. On the image, a gap from an earnings surprise looks like any other gap. The reason it happened, and whether the news behind it is still being digested, is invisible. If a large gap is on your chart, tell the model what caused it.</p>

    <p>A related trap is upcoming earnings. A clean pattern that is days away from an earnings report is a different situation from the same pattern in a quiet month, because the report can override any chart structure overnight. Nothing in the image tells the model a report is coming.</p>

    <h2>Split-adjusted history</h2>

    <p>When a company splits its stock, charting platforms normally adjust historical prices so the chart stays continuous. Some views or data sources show unadjusted prices, which produce an apparent collapse on the split date that never happened economically. If you see a sudden vertical drop to a fraction of the prior price with no matching news, check whether the chart is adjusted before asking anyone, human or AI, to read it.</p>

    <h2>Extended-hours bars</h2>

    <p>Pre-market and after-hours trading can be shown or hidden. With extended hours on, intraday charts include thin, often erratic bars that create highs and lows the regular session never printed. Be consistent, and tell the model which you are showing, because a "level" formed in thin pre-market trade is not the same as one formed in the regular session.</p>

    <h2>The market behind the stock</h2>

    <p>Individual stocks tend to move with their sector and the broad market. A breakout on a single-stock chart while the whole market falls is a different picture from the same breakout in a rising market. A screenshot of one ticker contains none of that. Looking at an index chart alongside is cheap and often clarifying.</p>

    <div class="info-card">
      <h4>Context worth typing every time</h4>
      <p>Symbol and timeframe. Indicator settings. Whether extended hours are shown. Whether earnings are due soon, and the cause of any large recent gap. Whether the broad market is trending up, down or sideways. Five short lines that fix most stock-specific misreads.</p>
    </div>

    <h2>Daily, weekly or intraday?</h2>

    <p>For most stock analysis the daily chart is the anchor. It has a meaningful close, well-defined levels and enough bars for a pattern to mean something. The weekly chart puts the daily in context, and intraday charts are where the most noise lives. The ratio approach in <a href="/chartcheck/blog/multi-timeframe-analysis/">multi-timeframe analysis</a> applies directly: decide which timeframe carries your decision and read one above it for context.</p>

    <h2>What AI cannot add on stocks</h2>

    <p>Fundamentals are the obvious gap. Valuation, earnings quality, balance sheets, guidance and competitive position are not on a price chart. Chart analysis describes behaviour of the price; it says nothing about whether the business is worth that price. For long-term investors in particular, a chart read is at most one input alongside the fundamentals, not a substitute.</p>

    <p>The same structural limits apply as everywhere: no order book, no news, nothing outside the frame, and no knowledge of the future. These are covered in <a href="/chartcheck/blog/ai-chart-analysis/">what AI chart analysis can and cannot do</a>.</p>

    <h2>Using it well</h2>

    <p>The productive pattern is the same as for any market. Look at the chart and form your own read. Run an AI read with context supplied. Compare. Where they agree, you have at least confirmed the picture is legible. Where they disagree, look for the reason, which is often a level just outside your attention or a gap you had stopped noticing. Tools such as ChartCheck are built to make that comparison fast and consistent, returning the same structure for every screenshot along with an explicit list of what could not be seen. None of it tells you what to buy.</p>''',
    'faqs': [
        ('Can AI do technical analysis on stocks?',
         'Yes. A vision model can read a stock chart screenshot for trend and structure, support and resistance, patterns, moving averages, RSI, MACD and volume. It describes what the chart shows; it does not predict where the stock goes next.'),
        ('Why does AI misread stock charts around earnings?',
         'An earnings gap looks like any other gap in the image, so the model sees the gap but not its cause. It also cannot know that a report is due soon. Tell it about recent or upcoming earnings and the read becomes much more useful.'),
        ('What timeframe is best for AI stock chart analysis?',
         'The daily chart is the usual anchor for stocks, because the daily close is meaningful and levels are well defined. Add a weekly chart for context. Intraday charts work but carry more noise.'),
        ('Does AI technical analysis include fundamentals?',
         'No. A price chart contains no information about valuation, earnings or the business. Chart analysis and fundamental analysis answer different questions, and an AI read of a chart covers only the first.'),
    ],
    'related': ['how-to-read-a-stock-chart', 'ai-chart-analysis', 'volume-analysis-trading'],
})

# ---------------------------------------------------------------- A5
ARTICLES.append({
    'slug': 'ai-chart-analysis-gold',
    'seo_title': 'AI Chart Analysis for Gold (XAUUSD) | ChartCheck',
    'seo_h1': 'AI Chart Analysis for Gold (XAUUSD): What Changes When the Chart Is Gold',
    'og_title': 'AI Chart Analysis for Gold (XAUUSD)',
    'meta_desc': 'How to get a useful AI read of a gold chart: spot XAUUSD vs futures, tick volume, round-number levels, news spikes and the dollar link the chart cannot show.',
    'og_desc': 'Spot vs futures, tick volume, round numbers and news spikes: what is specific to reading a gold chart with AI.',
    'keywords': 'ai chart analysis xauusd, gold chart analysis, xauusd chart analysis, ai gold analysis, gold technical analysis, xauusd technical analysis',
    'badge': 'By Market',
    'published': '2026-10-01', 'published_label': 'October 1, 2026',
    'card_title': 'AI Chart Analysis for Gold (XAUUSD)',
    'card_desc': 'Spot vs futures, tick volume, round numbers and news spikes: what a gold chart adds to an AI read.',
    'intro': 'Gold is one of the most screenshotted charts in retail trading, usually as XAUUSD on a forex or CFD platform. An AI reads it the same way it reads any candlestick chart. But a gold chart has particular features, from what its volume bar actually measures to how violently it reacts to scheduled data, that change how much of the read you should trust.',
    'quick_answer': 'AI chart analysis works on gold charts like any other: trend, structure, levels, patterns and visible indicators. The gold-specific points are that spot XAUUSD has no centralised volume (the bars are usually broker tick volume, unlike COMEX futures), that round numbers are heavily watched, that scheduled US data and central bank decisions can produce spikes that cut through any level, and that gold is priced in dollars, so the dollar and interest rates move it in ways the chart cannot show. Supply that context, and read volume on spot charts cautiously.',
    'body': '''<h2>Which gold chart are you looking at?</h2>

    <p>"Gold" on a screen can mean different instruments, and they are not interchangeable for analysis.</p>

    <table class="comparison-table">
      <thead>
        <tr><th>Instrument</th><th>Where you see it</th><th>Volume shown</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>Spot gold (XAUUSD)</td>
          <td>Forex and CFD platforms, MetaTrader</td>
          <td>Usually tick volume from your broker&#39;s feed</td>
        </tr>
        <tr>
          <td>Gold futures (GC)</td>
          <td>Futures platforms, many charting sites</td>
          <td>Exchange-reported contract volume</td>
        </tr>
        <tr>
          <td>Gold ETFs</td>
          <td>Stock brokers</td>
          <td>Exchange-reported share volume, regular sessions</td>
        </tr>
      </tbody>
    </table>

    <p>Prices track closely, but the charts differ in session structure, gaps and above all volume. Tell the model which one your screenshot shows. The difference matters most for the volume panel, below.</p>

    <h2>Volume on XAUUSD is not what it looks like</h2>

    <p>Spot gold trades over the counter, not on a single exchange, so there is no single reported volume figure. The volume bars under an XAUUSD chart on most retail platforms are tick volume: a count of price changes in your broker's feed during each bar. Tick volume tends to rise when activity rises, so it is not useless, but it is one broker's view and not the same thing as contract volume.</p>

    <p>That has a direct consequence for AI reads. Classic volume reasoning, such as "breakout on high volume", carries less weight on a spot chart. If you want volume-based reasoning on gold, a futures chart is the better input. The general principles are covered in <a href="/chartcheck/blog/volume-analysis-trading/">how to read volume</a>, and the same caveat about OTC volume appears in our <a href="/chartcheck/blog/ai-chart-analysis-forex/">forex guide</a>.</p>

    <h2>Round numbers carry real weight</h2>

    <p>Gold is quoted in dollars per troy ounce, and round numbers in that price get a lot of attention: hundred-dollar marks especially, and fifty-dollar marks on shorter timeframes. Orders and alerts cluster around them, so price often stalls, overshoots or whipsaws near them.</p>

    <p>A vision model marks levels from how price behaved on the chart. It will catch a round number if price has reacted there visibly, but it may not flag an untested round number just above or below the visible range. Worth adding yourself.</p>

    <h2>News spikes and scheduled data</h2>

    <p>Gold reacts sharply to scheduled US economic releases and central bank decisions, such as inflation data, employment reports and interest rate announcements. On a short-timeframe chart that shows up as a single enormous candle, often with long wicks in both directions, that slices through levels which had held for days.</p>

    <div class="info-card">
      <h4>What this does to an AI read</h4>
      <p><strong>Wicks distort levels.</strong> A news wick can create a "high" or "low" that was traded for seconds. Treating it as a key level is often a mistake.</p>
      <p><strong>Patterns break on schedule.</strong> A tidy triangle on the 15-minute chart an hour before a major release is not the same setup as one in a quiet session.</p>
      <p><strong>Spreads widen.</strong> Around releases, and around the daily rollover, spot spreads can widen sharply, so the price on your chart may differ meaningfully from the price you could have traded.</p>
    </div>

    <p>None of this is visible as cause in the image. The model sees the candle, not the calendar. Mention any major release inside or just after your chart window.</p>

    <h2>The dollar and rates are off-chart</h2>

    <p>Gold is priced in US dollars, so a stronger dollar tends to weigh on its dollar price and a weaker one tends to support it, other things equal. Gold pays no yield, so changes in real interest rates also influence it. Neither the dollar index nor bond yields appear on an XAUUSD screenshot. A breakout on gold that coincides with a sharp move in the dollar is a different story from one that does not, and the image alone cannot tell them apart.</p>

    <h2>Sessions and the shape of a gold day</h2>

    <p>Spot gold trades almost around the clock on weekdays, and activity shifts through Asian, London and New York hours. Quiet Asian-hours ranges are commonly broken when London and then New York open. On intraday charts this creates a familiar shape: tight overnight range, then expansion. An AI will describe the range and the break correctly; it will not know which session each bar belongs to unless the time axis is legible and in a known time zone.</p>

    <h2>A screenshot checklist for gold</h2>

    <ol>
      <li>Say whether it is spot XAUUSD, futures or an ETF.</li>
      <li>Keep the price axis and the time axis readable, and note your chart's time zone.</li>
      <li>Include enough bars to see the last few days on intraday charts, or several months on the daily.</li>
      <li>Mention any major data release or central bank decision inside the window.</li>
      <li>If volume matters to your read, use a futures chart rather than spot.</li>
    </ol>

    <p>The general capture rules are in <a href="/chartcheck/blog/screenshot-a-chart-for-analysis/">how to screenshot a chart</a>.</p>

    <h2>What a good gold read looks like</h2>

    <p>A useful AI read of a gold chart describes the structure (trending, ranging, or breaking a range), marks the zones that have been tested more than once while treating single news wicks with caution, names any pattern and whether it is complete, and says clearly what it could not judge: tick volume reliability, the dollar, upcoming data. That last part is the one to look for. ChartCheck, for example, returns an explicit list of what could not be seen alongside its confidence level, which on gold usually includes the macro drivers. A read that sounds certain about gold's next move is telling you about its tone, not about gold.</p>''',
    'faqs': [
        ('Can AI analyse XAUUSD charts?',
         'Yes. A gold chart is a candlestick chart like any other, so an AI can read trend, structure, levels, patterns and visible indicators. The gold-specific caveats are tick volume on spot charts, news spikes, and macro drivers like the dollar that are not on the chart.'),
        ('Is volume reliable on a gold chart?',
         'On spot XAUUSD, the volume bars are usually tick volume from your broker, not exchange-reported volume, so treat them as a rough activity gauge. Gold futures charts show exchange-reported contract volume and are better for volume-based analysis.'),
        ('Why do gold charts spike so much?',
         'Gold reacts strongly to scheduled US economic data and central bank decisions. On short timeframes those releases can produce very large candles with long wicks that cut through levels. The chart shows the spike but not the news that caused it.'),
        ('What timeframe is best for gold chart analysis?',
         'There is no single best timeframe. Many traders anchor on the daily or 4-hour chart for structure and use a lower timeframe for detail. Reading one timeframe above your decision timeframe adds useful context.'),
        ('Does AI know what the dollar is doing when it reads a gold chart?',
         'No. It only sees the image. If the dollar or interest rates moved sharply during the period on your chart, mention it in your prompt.'),
    ],
    'related': ['ai-chart-analysis-forex', 'volume-analysis-trading', 'ai-chart-analysis'],
})

# ---------------------------------------------------------------- A6
ARTICLES.append({
    'slug': 'ai-trading-bots-explained',
    'seo_title': 'Do AI Trading Bots Work? An Honest Explainer',
    'seo_h1': 'Do AI Trading Bots Work? An Honest Look at What They Are and What They Promise',
    'og_title': 'Do AI Trading Bots Work?',
    'meta_desc': 'What AI trading bots actually do, why backtests mislead, the red flags in bot marketing, and how a bot differs from AI chart analysis that only describes.',
    'og_desc': 'What AI trading bots really do, why their backtests mislead, and how they differ from chart analysis that only describes.',
    'keywords': 'ai trading bot does it work, ai trading good or bad, ai trading bot vs chart analysis, do ai trading bots work, ai trading bot scam, is ai trading legit',
    'badge': 'Explainer',
    'published': '2026-10-01', 'published_label': 'October 1, 2026',
    'card_title': 'Do AI Trading Bots Work?',
    'card_desc': 'What bots actually do, why backtests mislead, the marketing red flags, and how a bot differs from chart analysis.',
    'intro': '"AI trading bot" is one of the most heavily marketed phrases in retail finance, and one of the least defined. Some products labelled that way are ordinary rule-based automation. Some are genuine machine learning models. Some are scams with a dashboard. Here is how to tell them apart, why the evidence offered for them is usually weak, and how a bot differs from a tool that only reads a chart.',
    'quick_answer': 'An AI trading bot is software that places trades automatically according to a model or a set of rules. Whether one "works" depends on whether its edge survives real costs and changing markets, and that is very hard to show. Backtests are easy to overfit, published performance is often selective, and fees, slippage and regime changes erode results. Be very wary of bots promising consistent returns. AI chart analysis is a different thing: it describes what a chart shows and leaves every decision with you.',
    'body': '''<h2>What the phrase actually covers</h2>

    <p>Products sold as AI trading bots fall roughly into four groups. Knowing which one you are looking at answers most of the question.</p>

    <ol>
      <li><strong>Rule-based automation.</strong> "Buy when the fast moving average crosses above the slow one, sell when it crosses back." Plain if-then logic, often relabelled as AI. Transparent, testable, and only as good as the rule.</li>
      <li><strong>Grid and DCA bots.</strong> Common on crypto exchanges. They buy and sell at preset intervals or price steps. Mechanical, predictable, and they can perform very badly when a market trends hard in one direction.</li>
      <li><strong>Machine learning models.</strong> Systems trained on historical data to find patterns. Genuinely "AI", and genuinely hard: markets are noisy, change over time, and punish models that learned the past too well.</li>
      <li><strong>Fronts for something else.</strong> A slick dashboard showing returns that are not real, sold to collect deposits, subscriptions or broker referral fees. This group does a lot of the advertising.</li>
    </ol>

    <h2>Why "does it work?" is so hard to answer</h2>

    <h2>Backtests flatter everything</h2>

    <p>A backtest runs a strategy over historical data to see how it would have done. The problem is that you can adjust a strategy until it fits the past almost perfectly. Try enough parameter combinations and one of them will look excellent by chance. This is called overfitting, and a strategy fitted to the past this way often fails as soon as it meets data it has not seen.</p>

    <p>A beautiful equity curve in a bot advert is therefore weak evidence on its own. What would be stronger: results on data held back from development, live results over a long period, and figures that include every cost.</p>

    <h2>Costs eat thin edges</h2>

    <p>Every trade pays something: commissions or fees, the spread, and slippage between the price you expected and the price you got. A bot that trades frequently pays these constantly. A small theoretical edge can be wiped out entirely by costs that the marketing chart left out. Then there is the bot's own subscription fee on top.</p>

    <h2>Markets change regime</h2>

    <p>A strategy that did well in a steady trend can do badly in a choppy range, and vice versa. A bot trained or tuned during one kind of market has no guarantee of behaving well in the next. Performance that looks stable over a short window may just reflect one regime.</p>

    <h2>Red flags in AI bot marketing</h2>

    <div class="info-card">
      <h4>Walk away if you see</h4>
      <p><strong>Guaranteed or "consistent" returns.</strong> No legitimate trading product can guarantee returns.</p>
      <p><strong>Specific monthly percentages.</strong> "Earn 10% a month" is a sales claim, not a property of any market.</p>
      <p><strong>Unverifiable track records.</strong> Screenshots and testimonials instead of independently verifiable results.</p>
      <p><strong>Requirements to deposit with one specific broker or platform.</strong> Often how the seller is really paid.</p>
      <p><strong>Pressure and secrecy.</strong> "Limited spots", private messages, and refusal to explain how the strategy works.</p>
      <p><strong>Withdrawal friction.</strong> Fees or delays to withdraw "profits". A hallmark of outright fraud.</p>
    </div>

    <p>US regulators, including the CFTC, have published customer advisories warning specifically about AI trading bot claims, and regulators elsewhere have issued similar warnings. Their consistent message is that "AI" in the pitch is not evidence of anything.</p>

    <h2>Bots versus chart analysis</h2>

    <p>These two things are often lumped together, but they do fundamentally different jobs.</p>

    <table class="comparison-table">
      <thead>
        <tr><th></th><th>AI trading bot</th><th>AI chart analysis</th></tr>
      </thead>
      <tbody>
        <tr><td>What it does</td><td>Places trades automatically</td><td>Describes what a chart shows</td></tr>
        <tr><td>Who decides</td><td>The software</td><td>You</td></tr>
        <tr><td>Claim it makes</td><td>Usually about returns</td><td>About structure, levels and patterns</td></tr>
        <tr><td>How you check it</td><td>Hard: needs long, honest, cost-inclusive records</td><td>Easy: compare the description to the chart</td></tr>
        <tr><td>Main risk</td><td>Losing money automatically</td><td>Over-trusting a read</td></tr>
      </tbody>
    </table>

    <p>The key row is "how you check it". Whether a chart description is right can be judged on the spot: is the trend described correctly, are the levels where price actually reacted, is the pattern really there? Whether a bot has a real edge can only be judged over a long time, with honest data, after costs. That asymmetry is why a description tool can be useful to someone learning, while a bot is a much bigger bet.</p>

    <p>ChartCheck sits firmly on the description side. It reads a screenshot and returns trend, levels, patterns, indicators, a confidence level about legibility and a list of what it could not see. It does not place trades and it does not tell you what to buy or sell.</p>

    <h2>If you are still considering a bot</h2>

    <ul>
      <li>Understand the strategy in plain words. If nobody can explain what it does, do not run it.</li>
      <li>Ask for results on unseen data and over a long live period, with all costs included.</li>
      <li>Start on a demo or paper account, then only with money you can afford to lose entirely.</li>
      <li>Check that the seller and any broker involved are registered with the relevant regulator.</li>
      <li>Set a hard stop on the experiment in advance, in money and in time.</li>
    </ul>

    <h2>The honest bottom line</h2>

    <p>Some automated strategies exist that work for some people for some periods, mostly built and monitored by people who understand them deeply. The products advertised most loudly to retail traders are, on the evidence they offer, a poor bet. "AI" is a word on the box, not a property of the results. If what you actually want is to understand charts better, a tool that describes them, which you can check against your own eyes, is a far smaller and more honest step. Start with <a href="/chartcheck/blog/ai-chart-analysis/">what AI chart analysis can and cannot do</a>.</p>''',
    'faqs': [
        ('Do AI trading bots actually work?',
         'Some automated strategies work for some people for some periods, but most bots marketed to retail traders offer weak evidence: overfitted backtests, selective results and returns that ignore costs. Treat any bot promising consistent returns with great suspicion.'),
        ('Is AI trading good or bad?',
         'It depends what is meant. Automation and analysis tools can be useful. Products that promise guaranteed or steady profits from AI are a red flag, and regulators have issued warnings about AI trading bot claims.'),
        ('What is the difference between an AI trading bot and AI chart analysis?',
         'A bot places trades automatically. Chart analysis describes what a chart shows (trend, levels, patterns, indicators) and leaves every decision with you. A description can be checked against the chart immediately; a bot\'s edge can only be judged over a long period after costs.'),
        ('How can I tell if an AI trading bot is a scam?',
         'Common warning signs include guaranteed returns, specific monthly percentages, unverifiable track records, pressure to deposit with a particular broker, secrecy about the strategy and difficulty withdrawing funds. Check whether the seller is registered with a financial regulator.'),
    ],
    'related': ['ai-chart-analysis', 'why-ai-chart-analysis-is-wrong', 'ai-chart-analysis-free'],
})

# ---------------------------------------------------------------- A7
ARTICLES.append({
    'slug': 'multi-timeframe-analysis',
    'seo_title': 'Multi-Timeframe Analysis: Picking Your Chart Timeframes',
    'seo_h1': 'Multi-Timeframe Analysis: How to Pick Your Timeframes and Read Them Together',
    'og_title': 'Multi-Timeframe Analysis Explained',
    'meta_desc': 'How multi-timeframe analysis works, how to choose a set of timeframes for day trading or swing trading, and how to resolve conflicts between them.',
    'og_desc': 'How to choose a set of chart timeframes, read them top-down, and handle the moments they disagree.',
    'keywords': 'multi timeframe analysis, best timeframe for day trading, multiple timeframe analysis, top down analysis trading, which timeframe to trade, best chart timeframe',
    'badge': 'Reading Charts',
    'published': '2026-10-01', 'published_label': 'October 1, 2026',
    'card_title': 'Multi-Timeframe Analysis',
    'card_desc': 'How to choose a set of timeframes, read them top-down, and what to do when they disagree.',
    'intro': 'The same chart can be in an uptrend, a downtrend and a range all at once, depending on which timeframe you look at. That is not a contradiction; each timeframe answers a different question. Multi-timeframe analysis is the habit of reading them in a deliberate order so the bigger picture frames the smaller one, instead of the other way round.',
    'quick_answer': 'Multi-timeframe analysis means reading a higher timeframe for context and a lower one for detail. Start from the timeframe on which you actually make decisions, then add one roughly four to six times longer for trend and key levels, and optionally one roughly four to six times shorter for timing. There is no single best timeframe for day trading; it depends on how long you hold. A common day-trading set is 1-hour, 15-minute and 5-minute. When timeframes conflict, the higher one usually defines the backdrop, and conflict itself is useful information.',
    'body': '''<h2>Why one timeframe is not enough</h2>

    <p>Picture a stock in a steady uptrend on the daily chart. On the 15-minute chart, today, it is falling hard. Both statements are true. A trader looking only at the 15-minute chart sees a downtrend. A trader looking only at the daily sees a pullback inside an uptrend. Neither has the full picture, and they will interpret the same move very differently.</p>

    <p>Multi-timeframe analysis is simply the discipline of looking at both, in order, so that you know which situation you are in. It is also the single most common thing missing from an AI read, because a screenshot is one timeframe by definition, as explained in <a href="/chartcheck/blog/ai-chart-analysis/">what AI chart analysis cannot see</a>.</p>

    <h2>The three roles</h2>

    <div class="info-card">
      <h4>Context, decision, detail</h4>
      <p><strong>Context timeframe (higher).</strong> Defines the prevailing trend and the major support and resistance zones. Answers: what kind of market is this?</p>
      <p><strong>Decision timeframe (middle).</strong> Where you actually form your view and would plan any trade. Answers: what is the setup?</p>
      <p><strong>Detail timeframe (lower, optional).</strong> Shows how price is behaving right now around the level you care about. Answers: what is happening at this moment?</p>
    </div>

    <h2>How to choose the timeframes</h2>

    <p>Start with your decision timeframe, because it follows from how long you typically hold. Then step up and down by a consistent factor. A widely used rule of thumb, associated with Alexander Elder's triple screen approach, is a ratio of roughly four to six between adjacent timeframes. Too close together and they show nearly the same thing; too far apart and the lower one stops relating to the higher one.</p>

    <table class="comparison-table">
      <thead>
        <tr><th>Style (typical hold)</th><th>Context</th><th>Decision</th><th>Detail</th></tr>
      </thead>
      <tbody>
        <tr><td>Scalping (minutes)</td><td>15-minute</td><td>5-minute</td><td>1-minute</td></tr>
        <tr class="highlight-row"><td>Day trading (hours)</td><td>1-hour</td><td>15-minute</td><td>5-minute</td></tr>
        <tr><td>Swing trading (days to weeks)</td><td>Daily or weekly</td><td>4-hour or daily</td><td>1-hour</td></tr>
        <tr><td>Position trading (weeks to months)</td><td>Monthly</td><td>Weekly</td><td>Daily</td></tr>
      </tbody>
    </table>

    <p>These are starting points, not rules. What matters is consistency. Pick a set and use it every time, so that your reads are comparable from one chart to the next.</p>

    <h2>"What is the best timeframe for day trading?"</h2>

    <p>There is no single answer, which is why the question gets so many conflicting replies. A day trader holding for an hour and one holding for five minutes need different charts. The more useful question is: how long do I usually hold, and what timeframe shows a meaningful number of bars over that period? If you hold for about an hour, a 15-minute decision chart shows four bars per hold, and a 1-hour context chart shows the day's structure. That is why 1-hour, 15-minute and 5-minute is such a common day-trading set.</p>

    <p>Very short timeframes also carry more noise relative to signal. Random fluctuation dominates a 1-minute chart in a way it does not on an hourly one. Lower is not more precise; it is more detailed, which is a different thing.</p>

    <h2>Reading top-down, step by step</h2>

    <ol>
      <li><strong>Context first.</strong> On the higher timeframe, identify trend and structure, and mark the two or three most important zones. See <a href="/chartcheck/blog/support-and-resistance/">support and resistance</a>.</li>
      <li><strong>Locate yourself.</strong> Where is current price relative to those zones? In the middle of nowhere, or near something important?</li>
      <li><strong>Decision timeframe.</strong> Read structure and patterns here, keeping the higher-timeframe zones in view. A pattern forming right at a higher-timeframe level means more than the same pattern in open space.</li>
      <li><strong>Detail, if used.</strong> Look at how price is behaving at the level: rejecting, grinding, or slicing through.</li>
      <li><strong>Write it down.</strong> One line per timeframe. It makes conflicts obvious.</li>
    </ol>

    <h2>When timeframes disagree</h2>

    <p>They often will. That is not a failure of the method; it is the method telling you something.</p>

    <ul>
      <li><strong>Higher up, lower down.</strong> Commonly a pullback within a larger uptrend. The question is whether the pullback is reaching a meaningful higher-timeframe level.</li>
      <li><strong>Higher down, lower up.</strong> Commonly a bounce within a larger downtrend. Same question, inverted.</li>
      <li><strong>Higher ranging.</strong> Lower-timeframe trends inside a range tend to stall at the range edges. The range boundaries matter more than the small trend.</li>
    </ul>

    <p>The general principle is that the higher timeframe sets the backdrop and the lower timeframe operates inside it. A conflict is a reason for caution and smaller conclusions, not a reason to pick whichever chart agrees with you.</p>

    <h2>Common mistakes</h2>

    <ul>
      <li><strong>Timeframe shopping.</strong> Flipping between charts until one shows the pattern you hoped for. If you look at enough timeframes, every view is supported somewhere.</li>
      <li><strong>Too many timeframes.</strong> Five charts produce five opinions and no decision. Two or three is enough.</li>
      <li><strong>Inconsistent sets.</strong> Daily and 4-hour today, weekly and 15-minute tomorrow. Reads stop being comparable.</li>
      <li><strong>Ignoring the higher timeframe entirely.</strong> The most common one, and the reason so many lower-timeframe breakouts run straight into a level that was obvious one chart up.</li>
    </ul>

    <h2>Doing it with AI chart analysis</h2>

    <p>An AI read of one screenshot is a single-timeframe read. For a multi-timeframe view, take one screenshot per timeframe and analyse each, then compare them yourself, or attach both to a chatbot with the two-timeframe template in our <a href="/chartcheck/blog/ai-stock-analysis-prompt/">AI stock analysis prompts</a>. In ChartCheck, earlier reads of the same asset stay with it, which makes it straightforward to look at a daily read and a 1-hour read of the same symbol side by side. In every case, the tool reads each picture; putting them together is your job.</p>''',
    'faqs': [
        ('What is multi-timeframe analysis?',
         'Reading the same instrument on two or three timeframes in a set order: a higher timeframe for trend and key levels, a middle one for decisions, and optionally a lower one for detail. It prevents mistaking a pullback in a bigger trend for a new trend.'),
        ('What is the best timeframe for day trading?',
         'There is no single best timeframe. Choose a decision timeframe that suits how long you hold, then add one about four to six times higher for context. A common day-trading set is 1-hour, 15-minute and 5-minute charts.'),
        ('How many timeframes should I use?',
         'Two or three. More than that tends to produce conflicting views and makes it tempting to pick whichever chart supports what you already wanted to do.'),
        ('What should I do when timeframes conflict?',
         'Treat the higher timeframe as the backdrop and the lower one as what is happening inside it. Conflict is information: it usually means a pullback or bounce within a larger move, and it is a reason for caution rather than a signal.'),
    ],
    'related': ['how-to-read-a-stock-chart', 'support-and-resistance', 'screenshot-a-chart-for-analysis'],
})

# ---------------------------------------------------------------- A8
ARTICLES.append({
    'slug': 'volume-analysis-trading',
    'seo_title': 'How to Read Volume on a Stock Chart | ChartCheck',
    'seo_h1': 'How to Read Volume on a Stock Chart: Volume Analysis for Beginners',
    'og_title': 'How to Read Volume on a Stock Chart',
    'meta_desc': 'A practical guide to volume analysis: reading volume bars, breakouts, climaxes and dry-ups, relative volume, OBV and volume profile, and where volume misleads.',
    'og_desc': 'Reading volume bars, breakouts, climaxes, relative volume and volume profile, plus the markets where volume misleads.',
    'keywords': 'how to read volume on a stock chart, volume analysis, volume analysis trading, trading volume explained, relative volume, volume profile, on balance volume',
    'badge': 'Reading Charts',
    'published': '2026-10-01', 'published_label': 'October 1, 2026',
    'card_title': 'How to Read Volume on a Chart',
    'card_desc': 'Breakouts, climaxes, dry-ups, relative volume and volume profile, and the markets where volume misleads.',
    'intro': 'Price tells you where a market went. Volume tells you how much participation it took to get there. Read together, they help separate moves with broad conviction behind them from moves that happened in thin trade. Volume is also one of the most misread panels on a chart, mostly because people expect it to predict direction, which it does not.',
    'quick_answer': 'Each volume bar shows how many shares or contracts traded during that candle. Read it relative to its own recent average rather than as an absolute number. The core ideas: breakouts on clearly higher-than-average volume suggest broader participation than breakouts on low volume; trends that continue on fading volume may be losing participation; very high volume after a long move can mark exhaustion; and quiet volume during a consolidation is normal. Volume shows participation, not direction. On spot forex and spot gold, the volume shown is usually broker tick volume, so read it more cautiously.',
    'body': '''<h2>What a volume bar actually shows</h2>

    <p>The bars along the bottom of most charts show how many units traded during each candle: shares for a stock, contracts for a future, coins for a crypto pair on that exchange. Many platforms colour each bar to match its candle, green for an up candle and red for a down candle. That colour describes the candle, not whether buyers or sellers "won" the volume. Every trade has both a buyer and a seller.</p>

    <p>The single most important habit is to read volume relative to itself. A bar is high or low compared with the bars around it. Many charts can overlay a moving average on volume, typically 20 or 50 periods, which makes "higher than usual" easy to see at a glance.</p>

    <h2>The five situations worth recognising</h2>

    <h2>1. Breakout volume</h2>

    <p>When price breaks out of a range or through a well-tested level, look at the volume on the breakout bar and the bars right after. A break on clearly above-average volume shows that many participants were involved. A break on below-average volume shows a move that happened without much participation. Neither guarantees the outcome, but low-volume breakouts are widely regarded as more prone to failing back into the range. Levels themselves are covered in <a href="/chartcheck/blog/support-and-resistance/">support and resistance</a>.</p>

    <h2>2. Trend volume</h2>

    <p>In a healthy-looking uptrend, volume often expands on up moves and contracts on pullbacks. When a trend keeps making new highs but volume on each push gets smaller, participation behind the move may be fading. That is not a reversal signal on its own; trends can run for a long time on modest volume. It is context.</p>

    <h2>3. Climax volume</h2>

    <p>After a long, steep move, an unusually huge volume bar, often with a wide candle or a long wick, can mark a point of exhaustion: a final burst of panic selling or euphoric buying. Climaxes are much easier to identify afterwards than in real time, so treat a big bar as a reason to watch closely, not as a conclusion.</p>

    <h2>4. Dry-up volume</h2>

    <p>Volume often declines during consolidations such as flags, triangles and bases. Quiet trade while price tightens is normal, and many chart pattern descriptions include it. A sudden expansion out of a quiet period is what makes the subsequent move noticeable. See the <a href="/chartcheck/blog/chart-patterns-cheat-sheet/">chart patterns cheat sheet</a> for which patterns typically include a volume component.</p>

    <h2>5. Volume at levels</h2>

    <p>High volume around a support or resistance zone means a lot of trading happened there, which is one reason that zone may matter again later: many participants have positions anchored to it.</p>

    <table class="comparison-table">
      <thead>
        <tr><th>Price does</th><th>Volume does</th><th>A common reading</th></tr>
      </thead>
      <tbody>
        <tr><td>Breaks a level</td><td>Well above average</td><td>Broad participation in the break</td></tr>
        <tr><td>Breaks a level</td><td>Below average</td><td>Thin break, more caution warranted</td></tr>
        <tr><td>Trend continues</td><td>Fades push by push</td><td>Participation may be thinning</td></tr>
        <tr><td>Long move, final spike</td><td>Extreme bar</td><td>Possible exhaustion, confirmed only later</td></tr>
        <tr><td>Tight consolidation</td><td>Low and declining</td><td>Normal quiet before a range resolves</td></tr>
      </tbody>
    </table>

    <h2>Volume tools beyond the bars</h2>

    <div class="info-card">
      <h4>Relative volume</h4>
      <p>Current volume divided by average volume for the same period. A reading of 2 means twice as much trading as usual. Popular with day traders for spotting unusually active stocks.</p>
    </div>

    <div class="info-card">
      <h4>On-balance volume (OBV)</h4>
      <p>A running total that adds a bar's volume when price closes up and subtracts it when price closes down. Traders watch whether OBV confirms price, such as making new highs with it, or diverges from it.</p>
    </div>

    <div class="info-card">
      <h4>Volume profile</h4>
      <p>A horizontal histogram showing how much traded at each price, rather than in each time period. The price with the most trading is often called the point of control. Useful for seeing where in a range activity actually concentrated.</p>
    </div>

    <h2>Where volume misleads</h2>

    <ul>
      <li><strong>Spot forex and spot gold.</strong> These trade over the counter with no central exchange, so the "volume" on most retail charts is tick volume from one broker's feed. It roughly tracks activity but is not reported trading volume. See our guides on <a href="/chartcheck/blog/ai-chart-analysis-forex/">forex</a> and <a href="/chartcheck/blog/ai-chart-analysis-gold/">gold</a>.</li>
      <li><strong>Crypto.</strong> Volume is per exchange. The same pair on two exchanges can show very different volume, and no single chart shows total market volume.</li>
      <li><strong>Calendar effects.</strong> Holidays, half-days and index rebalancing days produce unusual volume unrelated to the chart's story.</li>
      <li><strong>Earnings and news days.</strong> Volume spikes on news reflect the news. That is real participation, but its cause is off the chart.</li>
      <li><strong>Extended hours.</strong> Pre-market and after-hours volume is far thinner than the regular session and should not be compared directly with it.</li>
    </ul>

    <h2>The mistake to avoid</h2>

    <p>Volume does not tell you direction. A huge red bar can be a capitulation low or the start of a much larger decline. A huge green bar can be the start of a run or a blow-off top. Volume tells you that a lot of people were involved in what price did. You still have to read what price did, in context, and accept that the read can be wrong.</p>

    <h2>Volume in an AI chart read</h2>

    <p>If the volume panel is in your screenshot, an AI reader can describe it: whether a breakout came on high or low volume relative to recent bars, whether volume has faded through a trend, whether there was a climactic bar. If the panel is cropped out, the read simply has no volume information, and a good tool should say so. ChartCheck reads whatever indicators are visible, volume included, and lists anything it could not see. Including the volume panel is one of the easiest ways to make any read, human or AI, more complete; the rest is in <a href="/chartcheck/blog/screenshot-a-chart-for-analysis/">how to screenshot a chart</a>.</p>''',
    'faqs': [
        ('How do you read volume on a stock chart?',
         'Each bar shows how many shares traded during that candle. Compare each bar with its recent average rather than reading the raw number, and read it alongside price: breakouts, trends, climaxes and consolidations each have typical volume behaviour.'),
        ('Does high volume mean the price will go up?',
         'No. Volume measures participation, not direction. High volume can accompany a strong rise, a sharp fall or an exhaustion point. You have to read price action to know what the volume was attached to.'),
        ('What is a good volume for a breakout?',
         'There is no fixed number. Traders usually look for volume clearly above its recent average, for example compared with a 20 or 50 period volume average. Breakouts on below-average volume are widely regarded as more likely to fail.'),
        ('Is volume reliable in forex and crypto?',
         'Less so than on stocks. Spot forex volume on retail platforms is usually broker tick volume, and crypto volume is specific to each exchange. Both are rough activity gauges rather than total market volume.'),
    ],
    'related': ['support-and-resistance', 'chart-patterns-cheat-sheet', 'how-to-read-a-stock-chart'],
})
