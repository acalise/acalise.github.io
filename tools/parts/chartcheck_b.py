# -*- coding: utf-8 -*-
"""
ChartCheck blog content, part B (October 2026 batch): indicators, drawing
tools and the classic reversal / continuation patterns.

Merged into content_chartcheck.py's ARTICLES by the parent. Each dict carries
card_title / card_desc for the blog index.
"""

ARTICLES = []

# ---------------------------------------------------------------- B1
ARTICLES.append({
    'slug': 'rsi-indicator-explained',
    'seo_title': 'RSI Indicator Explained: How to Read RSI | ChartCheck',
    'seo_h1': 'The RSI Indicator Explained: How to Read It Without Fooling Yourself',
    'og_title': 'The RSI Indicator Explained',
    'meta_desc': 'How to read the RSI indicator: what the number measures, why 70 and 30 are not sell and buy signals, how RSI divergence works, and where it misleads you.',
    'og_desc': 'What RSI actually measures, why 70/30 are not signals, and how divergence really works.',
    'keywords': 'rsi indicator explained, how to read rsi, rsi divergence, relative strength index, rsi overbought oversold, rsi settings',
    'badge': 'Indicators',
    'published': '2026-10-01', 'published_label': 'October 1, 2026',
    'card_title': 'The RSI Indicator Explained',
    'card_desc': 'What the number measures, why 70 and 30 are not signals, and how divergence really works.',
    'intro': 'RSI is probably the most widely displayed indicator on retail charts and one of the most consistently misread. The standard explanation - above 70 is overbought, below 30 is oversold - is technically true and practically misleading, and understanding why is most of what there is to learn about it.',
    'quick_answer': 'RSI (Relative Strength Index) compares the size of recent up-moves to recent down-moves over a lookback window, usually 14 periods, and scales the result from 0 to 100. A high reading means recent gains have been large relative to recent losses; a low reading means the reverse. It measures momentum, not value, so "overbought" does not mean "about to fall". Strong trends can hold RSI above 70 for long stretches. The more useful reads are where RSI sits relative to 50, and divergence between RSI and price at a level that already matters.',
    'body': '''<h2>What the number actually measures</h2>

    <p>RSI takes the last N periods (14 by default), averages the size of the up-closes and the size of the down-closes separately, and turns their ratio into a number between 0 and 100. If every recent close was higher than the one before, RSI approaches 100. If every recent close was lower, it approaches 0. A balanced mix lands near 50.</p>

    <p>That is all it is. It does not know about volume, fundamentals, levels or anything else. It is a smoothed answer to one question: <em>over the last few periods, have the up-moves been bigger than the down-moves?</em></p>

    <p>Keeping that definition in mind fixes most RSI mistakes, because it tells you what the indicator cannot possibly tell you. It cannot tell you price is "too high". It can only tell you price has been rising with more force than it has been falling.</p>

    <h2>Why 70 and 30 are not sell and buy signals</h2>

    <p>The overbought / oversold framing comes from the indicator's original use as a mean-reversion tool, and it works acceptably in sideways markets. In trending markets it is close to backwards.</p>

    <p>Think about what a strong uptrend is: a sustained period where up-moves are larger than down-moves. That is precisely the condition that pushes RSI above 70 and keeps it there. Selling every time RSI crosses 70 in a real trend means repeatedly selling the strongest part of the move.</p>

    <div class="info-card">
      <h4>A more honest reading of the zones</h4>
      <p><strong>Above 70.</strong> Momentum is strong to the upside. In a range, the move may be stretched. In a trend, it is often just confirmation that the trend is healthy.</p>
      <p><strong>Below 30.</strong> Momentum is strong to the downside. The same caveat applies in reverse.</p>
      <p><strong>Around 50.</strong> No clear momentum edge either way. Often the most informative zone to watch, because a trend that keeps bouncing off 50 is intact and one that keeps failing at 50 is weakening.</p>
    </div>

    <h2>The 50 line is underrated</h2>

    <p>Many technicians find the midline more useful than the extremes. In a healthy uptrend, RSI pullbacks tend to hold somewhere in the 40 to 50 area rather than dropping to 30. In a healthy downtrend, rallies tend to stall somewhere in the 50 to 60 area.</p>

    <p>The practical consequence is a regime read. If RSI spends weeks oscillating between roughly 40 and 80, momentum has a bullish character. If it oscillates between roughly 20 and 60, it has a bearish character. When that range shifts - an uptrend's RSI pullback breaking well below 40, say - something about the character of the move has changed, which is often worth noticing before price itself makes it obvious.</p>

    <p>Those ranges are rules of thumb, not thresholds. Different instruments and timeframes have different typical RSI ranges, and the useful habit is to observe where a particular chart's RSI normally lives rather than impose fixed numbers.</p>

    <h2>RSI divergence</h2>

    <p>Divergence is the most discussed RSI signal and deserves the most care.</p>

    <p><strong>Bearish divergence</strong>: price makes a higher high, but RSI makes a lower high. The new price peak was reached with less momentum than the previous one.</p>

    <p><strong>Bullish divergence</strong>: price makes a lower low, but RSI makes a higher low. Sellers pushed price to a new low but with less force than last time.</p>

    <p>What divergence genuinely tells you is that momentum is fading relative to price. What it does not tell you is when, or whether, price will turn. Momentum can fade for a long time while price keeps grinding in the same direction, producing divergence after divergence before anything happens. Trading every divergence as a reversal is one of the more reliable ways to fight a trend repeatedly.</p>

    <h2>Making divergence more meaningful</h2>

    <ol>
      <li><strong>Location first.</strong> Divergence at a well-tested <a href="/chartcheck/blog/support-and-resistance/">support or resistance zone</a> combines two pieces of evidence. Divergence in the middle of nowhere is one weak piece.</li>
      <li><strong>Compare clear swings.</strong> Divergence should be drawn between two obvious swing highs or swing lows, not between arbitrary bars you chose because the lines diverge.</li>
      <li><strong>Wait for structure.</strong> A divergence followed by a break of the most recent swing low (for bearish) or swing high (for bullish) has been confirmed by price itself. Before that, it is a warning, not an event.</li>
      <li><strong>Higher timeframes carry more weight.</strong> A divergence on the daily chart reflects weeks of trading. One on the 1-minute chart reflects minutes.</li>
    </ol>

    <h2>Hidden divergence</h2>

    <p>The mirror concept is sometimes called hidden divergence and is read as a continuation hint rather than a reversal hint. In an uptrend, price makes a higher low while RSI makes a lower low: the pullback was sharp on the momentum reading but price held structure. It is worth knowing the term exists, mostly so you do not mistake it for a regular divergence pointing the other way.</p>

    <h2>Settings</h2>

    <p>Fourteen periods is the default and remains the most common choice. Shorter settings make RSI faster and noisier, reaching extremes more often. Longer settings make it slower and smoother. There is no correct setting; there is only consistency. Changing the period until the indicator agrees with the view you already hold is a form of curve-fitting that feels like analysis.</p>

    <h2>Reading RSI from a screenshot</h2>

    <p>If your chart screenshot includes the RSI panel, an AI read can pick out the current level, whether it is near the extremes or the midline, and obvious divergences between visible swings. That is straightforward visual work.</p>

    <p>What a screenshot read cannot know is your setting, unless the label is legible in the image - a 7-period RSI and a 21-period RSI look similar but mean different things. And it can only judge divergence between swings that are actually in frame. If the prior high you care about is off the left edge, it does not exist for the analysis. The <a href="/chartcheck/blog/screenshot-a-chart-for-analysis/">screenshot guide</a> covers how to keep the right context visible.</p>

    <h2>RSI in ranges versus trends</h2>

    <p>The single most useful thing you can decide before reading RSI is what kind of market you are looking at, because the same reading means different things in each.</p>

    <table class="comparison-table">
      <thead>
        <tr><th>Reading</th><th>In a sideways range</th><th>In a strong trend</th></tr>
      </thead>
      <tbody>
        <tr><td>RSI above 70</td><td>Price is near the top of its recent behaviour; a pullback toward the middle of the range is plausible.</td><td>Normal. The trend is doing what trends do.</td></tr>
        <tr><td>RSI below 30</td><td>Price is near the bottom of its recent behaviour.</td><td>Normal in a downtrend. Not evidence of a bottom.</td></tr>
        <tr class="highlight-row"><td>RSI around 50</td><td>Unremarkable.</td><td>Worth watching. Pullbacks holding near 40 to 50 in an uptrend suggest the trend is intact; repeated failures there suggest it is tiring.</td></tr>
        <tr><td>Divergence</td><td>Can mark the edges of the range.</td><td>Common and often early. Needs structure to confirm it.</td></tr>
      </tbody>
    </table>

    <p>Deciding the regime is the job of price structure, not RSI. Look at the swings first: rising highs and lows, falling highs and lows, or neither. The <a href="/chartcheck/blog/how-to-read-a-stock-chart/">chart reading guide</a> walks through that first pass. Then interpret RSI inside that context.</p>

    <h2>A worked reading, in words</h2>

    <p>Imagine a daily chart where price has been climbing for two months in a clear sequence of higher highs and higher lows. RSI has spent most of that time between roughly 45 and 75, touching the low end on each pullback and pushing above 70 on each new high.</p>

    <p>Now price makes another new high, but RSI only reaches the mid-60s. That is bearish divergence. The tempting conclusion is "the top is in". The more careful reading is: "the latest push higher had less force than the previous one." Then you ask what would confirm it. If the next pullback drops RSI well below its usual 45 floor and price breaks the most recent swing low, momentum and structure now agree that the character of the move has changed. If instead the pullback holds the usual area and price pushes to another high, the divergence was simply a quieter leg in an ongoing trend.</p>

    <p>Neither outcome was knowable from the divergence alone. That is the point: RSI gives you the question, and price structure gives you the answer.</p>

    <h2>Common RSI mistakes</h2>

    <ul>
      <li><strong>Treating 70 and 30 as instructions.</strong> They are descriptions of momentum, and in trends they are often signs of strength rather than exhaustion.</li>
      <li><strong>Trading divergence without structure.</strong> Divergence can stack up several times before price turns, or never lead to a turn at all.</li>
      <li><strong>Reading RSI on one timeframe in isolation.</strong> A 15-minute RSI at 25 inside a daily uptrend is describing a short pullback, not a reversal. The <a href="/chartcheck/blog/multi-timeframe-analysis/">multi-timeframe guide</a> covers how to stack timeframes sensibly.</li>
      <li><strong>Stacking near-identical oscillators.</strong> RSI, stochastics and similar momentum tools often agree because they are built from the same price data. Agreement between them is not independent confirmation.</li>
      <li><strong>Constantly changing the period.</strong> If the setting changes every time the indicator disagrees with you, the indicator is no longer telling you anything.</li>
    </ul>

    <h2>Where RSI fits</h2>

    <p>RSI is a momentum gauge. It is useful for describing the character of a move and for flagging when that character is changing. It is not a timing tool, and it is at its least reliable exactly when it feels most persuasive: at an extreme reading during a strong trend. Use it to ask better questions about the chart, not to answer them.</p>''',
    'faqs': [
        ('What is a good RSI setting?',
         'Fourteen periods is the standard and a sensible default. Shorter settings reach overbought and oversold far more often and produce more noise; longer settings react slowly. The more important thing than the exact number is picking one and keeping it, rather than adjusting it until the indicator agrees with what you already believe.'),
        ('Does RSI above 70 mean the price will drop?',
         'No. It means recent up-moves have been large relative to down-moves, which is what a strong uptrend looks like. In sideways markets an extreme reading can precede a pullback, but in trending markets RSI can stay above 70 for long periods while price keeps rising. Treat it as a description of momentum, not a reversal signal.'),
        ('What is RSI divergence?',
         'Divergence is when price and RSI disagree: price makes a higher high while RSI makes a lower high (bearish), or price makes a lower low while RSI makes a higher low (bullish). It signals that momentum is weakening relative to price. It does not say when, or whether, price will reverse, and divergences can repeat several times before anything happens.'),
        ('Is RSI better for stocks, crypto or forex?',
         'The calculation is identical in every market, so it works the same way mechanically. What differs is behaviour: markets that trend strongly will hold RSI at extremes longer, and very volatile instruments hit extremes more often. Observe where a particular chart\'s RSI usually ranges rather than applying fixed thresholds everywhere.'),
        ('Can AI read RSI off a chart image?',
         'If the RSI panel is visible, yes - reading the current level and spotting divergence between visible swings is simple visual work. It cannot know the period setting unless the label is readable, and it can only compare swings that are inside the screenshot.'),
    ],
    'related': ['macd-indicator-explained', 'support-and-resistance', 'multi-timeframe-analysis'],
})

# ---------------------------------------------------------------- B2
ARTICLES.append({
    'slug': 'macd-indicator-explained',
    'seo_title': 'MACD Explained: How to Read MACD Crossovers | ChartCheck',
    'seo_h1': 'MACD Explained: How to Read the Lines, the Histogram and the Crossovers',
    'og_title': 'MACD Explained',
    'meta_desc': 'How to read MACD: what the two lines and the histogram actually calculate, why crossovers lag, what the zero line tells you, and where MACD misleads.',
    'og_desc': 'What the MACD lines and histogram calculate, why crossovers lag, and what the zero line means.',
    'keywords': 'macd explained, how to read macd, macd crossover, macd histogram, macd indicator, macd divergence, macd settings 12 26 9',
    'badge': 'Indicators',
    'published': '2026-10-01', 'published_label': 'October 1, 2026',
    'card_title': 'MACD Explained',
    'card_desc': 'The two lines, the histogram, the zero line, and why every crossover arrives late.',
    'intro': 'MACD looks more complicated than RSI - two lines, a histogram, a zero line - but it is built entirely out of moving averages, and once you see that, every part of it becomes readable. The most important thing to understand about it is also the least advertised: everything it shows you is late, by design.',
    'quick_answer': 'MACD is the difference between a fast and a slow exponential moving average of price (12 and 26 periods by default). The signal line is a 9-period average of that difference, and the histogram is the gap between the two lines. Above zero, the fast average is above the slow one, so recent price has been stronger than the longer-term average. Crossovers mark changes in that relationship, but because they are averages of averages, they arrive after the move has already started. Read MACD as a description of trend and momentum, not a trigger.',
    'body': '''<h2>What MACD is built from</h2>

    <p>MACD stands for Moving Average Convergence Divergence. The name describes the mechanics directly.</p>

    <div class="info-card">
      <h4>The three parts</h4>
      <p><strong>The MACD line.</strong> The 12-period exponential moving average minus the 26-period exponential moving average. When short-term price is running above the longer-term average, this is positive. When it is running below, negative.</p>
      <p><strong>The signal line.</strong> A 9-period exponential moving average of the MACD line itself - a smoothed version of the first line.</p>
      <p><strong>The histogram.</strong> The MACD line minus the signal line, drawn as bars. It shows how far apart the two lines are, and whether that gap is growing or shrinking.</p>
    </div>

    <p>Because every component is derived from moving averages of price, MACD contains no information that is not already in the price chart. It reorganises that information in a way that makes changes in trend and momentum easier to see. That is genuinely useful, but it is a lens, not a new data source.</p>

    <h2>The zero line</h2>

    <p>The simplest MACD read is also one of the most robust: which side of zero is the MACD line on?</p>

    <p>Above zero, the fast average is above the slow average, which is another way of saying price has recently been stronger than its longer-term trend. Below zero, the reverse. A MACD line that has spent weeks above zero describes an uptrend; one that keeps crossing back and forth describes a market without a clear direction.</p>

    <p>A cross of the zero line is the same event as the two underlying moving averages crossing each other. That is a slow signal by nature - by the time a 12-period average overtakes a 26-period one, price has usually been moving for a while.</p>

    <h2>Signal-line crossovers</h2>

    <p>The crossover most people mean when they say "MACD crossover" is the MACD line crossing its signal line.</p>

    <ul>
      <li><strong>Bullish crossover</strong>: MACD line crosses above the signal line. Short-term momentum has turned up relative to its own recent average.</li>
      <li><strong>Bearish crossover</strong>: MACD line crosses below the signal line. Short-term momentum has turned down.</li>
    </ul>

    <p>These happen frequently, and in sideways markets most of them lead nowhere: the lines weave around each other while price chops in a range. Crossovers are much more coherent in trending markets, which creates the obvious problem - you only know the market was trending after the fact.</p>

    <h2>Why everything arrives late</h2>

    <p>It is worth being explicit about the lag, because it is structural. The MACD line is a difference of two averages. The signal line is an average of that. A crossover is therefore an average-of-an-average event, and it will always confirm a turn after the turn began.</p>

    <p>That is not a flaw in the indicator; it is the price of smoothing. Smoothing removes noise, and removing noise necessarily delays the signal. Faster settings reduce lag and add noise. Slower settings do the opposite. There is no setting that is both early and clean.</p>

    <p>The practical consequence: MACD is better at telling you what kind of market you are in than at telling you when to act.</p>

    <h2>Reading the histogram</h2>

    <p>The histogram is the most responsive part of MACD, because it measures the gap between the two lines rather than the lines themselves. Before the lines cross, the gap has to shrink - so the histogram bars get shorter before the crossover happens.</p>

    <p>That gives a simple read:</p>

    <table class="comparison-table">
      <thead>
        <tr><th>Histogram</th><th>What it describes</th></tr>
      </thead>
      <tbody>
        <tr><td>Above zero and growing</td><td>Upside momentum is accelerating.</td></tr>
        <tr class="highlight-row"><td>Above zero and shrinking</td><td>Still positive, but momentum is fading. A bearish signal-line cross may follow.</td></tr>
        <tr><td>Below zero and growing (more negative)</td><td>Downside momentum is accelerating.</td></tr>
        <tr class="highlight-row"><td>Below zero and shrinking</td><td>Still negative, but selling pressure is fading.</td></tr>
      </tbody>
    </table>

    <p>Shrinking bars are an early hint, not a confirmed turn. Momentum can fade and re-accelerate without any crossover at all.</p>

    <h2>MACD divergence</h2>

    <p>The same divergence logic used for <a href="/chartcheck/blog/rsi-indicator-explained/">RSI</a> applies. If price makes a higher high while the MACD line or histogram makes a lower high, momentum behind the new high was weaker. The reverse applies at lows.</p>

    <p>The same caveats apply too. Divergence describes fading momentum, not an imminent reversal, and it can persist through several more swings in the trend direction. It carries more weight at a level that already matters and on a higher timeframe.</p>

    <h2>Settings</h2>

    <p>12, 26 and 9 are the defaults and by far the most commonly used, which is itself a reason to keep them: they are the settings most other participants are looking at. Some traders use faster settings on short timeframes. As with any indicator, changing settings until past signals look good is curve-fitting, and it rarely survives contact with the next stretch of data.</p>

    <h2>MACD versus RSI</h2>

    <p>They are often shown together and often treated as redundant. They are related but not identical. RSI is bounded between 0 and 100 and answers "how forceful have recent up-moves been compared to down-moves". MACD is unbounded and answers "how far is short-term price trending away from the longer-term trend, and is that gap widening". RSI tends to be more useful for spotting stretched moves in ranges; MACD tends to be more useful for describing trend direction and its changes. Neither one predicts.</p>

    <h2>A worked reading, in words</h2>

    <p>Picture a daily chart where price has been falling for several weeks. MACD has been below zero the whole time, and the histogram has been printing long negative bars.</p>

    <p>Then the histogram bars start getting shorter. Selling momentum is fading, though MACD is still below zero and the trend is still down. A few days later the MACD line crosses above the signal line: a bullish signal-line crossover, below zero. That tells you short-term momentum has turned up relative to its recent average. It does not tell you the downtrend is over, because the fast average is still below the slow one.</p>

    <p>What would make the picture more convincing? Price breaking its most recent swing high, ending the sequence of lower highs. MACD eventually crossing above zero, meaning the 12-period average has overtaken the 26-period one. Ideally, both of those happening near a level that has mattered before. Each step adds evidence; none of them alone is a verdict. And at every step, the indicator is describing price behaviour that has already happened.</p>

    <h2>Common MACD mistakes</h2>

    <ul>
      <li><strong>Treating every crossover as a signal.</strong> In ranges, the lines cross constantly and most crossovers lead nowhere.</li>
      <li><strong>Ignoring which side of zero the crossover happened on.</strong> A bullish crossover deep below zero is a bounce in momentum during a downtrend. A bullish crossover above zero is momentum resuming inside an uptrend. They are not the same event.</li>
      <li><strong>Reading the histogram as a forecast.</strong> Shrinking bars mean momentum is fading. They do not mean a reversal is coming.</li>
      <li><strong>Comparing MACD values across instruments.</strong> MACD is measured in price units, so its values depend on the price level and volatility of the instrument. A MACD of 2 means something very different on a stock trading at 20 than on one trading at 2,000. Compare MACD to its own history on the same chart.</li>
      <li><strong>Using it as independent confirmation of a moving average crossover.</strong> MACD crossing zero is a moving average crossover. Counting both as separate evidence is double-counting.</li>
    </ul>

    <h2>Where MACD is most useful</h2>

    <p>MACD tends to earn its place as a trend-character gauge. Is the market trending, and is that trend strengthening or weakening? Those are the questions it answers clearly. It is least useful in tight sideways markets, where it generates a stream of crossovers with no follow-through, and as an entry trigger, where its built-in lag works against you. Pair it with price structure and <a href="/chartcheck/blog/support-and-resistance/">levels</a> rather than reading it alone.</p>

    <h2>Reading MACD from a screenshot</h2>

    <p>An AI read of a chart screenshot can describe where the MACD line sits relative to zero, whether the lines have recently crossed, and whether the histogram is expanding or contracting - all visible features of the image. It cannot reliably know the settings unless they are labelled on the chart, and it cannot see crossovers that happened off the edge of the frame. If MACD is central to how you read a chart, make sure the panel and its label are clearly visible before you analyse it.</p>''',
    'faqs': [
        ('What do the MACD settings 12, 26, 9 mean?',
         '12 and 26 are the periods of the fast and slow exponential moving averages that are subtracted to make the MACD line. 9 is the period of the exponential moving average applied to the MACD line to make the signal line. They are the original defaults and still the most widely used.'),
        ('Is a MACD crossover a buy or sell signal?',
         'It is a description of momentum turning, not an instruction. A bullish crossover means short-term momentum has risen above its own recent average; a bearish one means the opposite. In sideways markets many crossovers lead nowhere, and in all markets they arrive after the move has begun, because the indicator is built from averages.'),
        ('What does it mean when MACD is above zero?',
         'The 12-period exponential moving average is above the 26-period one, meaning recent price has been stronger than the longer-term average. Sustained time above zero describes an uptrend. It says nothing about whether the trend will continue.'),
        ('Why does the MACD histogram shrink before a crossover?',
         'The histogram is the distance between the MACD line and the signal line. For the lines to cross, that distance has to fall to zero, so the bars get shorter first. That makes the histogram the earliest-moving part of MACD, though shrinking bars can also simply re-expand without any crossover.'),
    ],
    'related': ['rsi-indicator-explained', 'volume-analysis-trading', 'how-to-read-a-stock-chart'],
})

# ---------------------------------------------------------------- B3
ARTICLES.append({
    'slug': 'fibonacci-retracement',
    'seo_title': 'How to Draw Fibonacci Retracement Levels | ChartCheck',
    'seo_h1': 'How to Draw Fibonacci Retracement, and What the Levels Can and Cannot Tell You',
    'og_title': 'How to Draw Fibonacci Retracement',
    'meta_desc': 'How to draw Fibonacci retracement: choosing the swing, which way to drag, what 38.2, 50 and 61.8 mean, and why levels only matter with confluence.',
    'og_desc': 'Choosing the swing, which way to drag, what the levels mean, and why confluence is everything.',
    'keywords': 'how to draw fibonacci retracement, fibonacci retracement, fibonacci levels explained, fib retracement 61.8, golden pocket, fibonacci trading',
    'badge': 'Tools',
    'published': '2026-10-01', 'published_label': 'October 1, 2026',
    'card_title': 'How to Draw Fibonacci Retracement',
    'card_desc': 'Choosing the swing, which way to drag, and why the levels only matter with confluence.',
    'intro': 'Fibonacci retracement is one of the easiest tools to draw and one of the easiest to draw in a way that tells you nothing. The mechanics take thirty seconds. The judgement is in choosing which swing to measure, and in being honest about what the resulting levels are.',
    'quick_answer': 'Fibonacci retracement divides a completed price swing into proportions - most commonly 23.6%, 38.2%, 50%, 61.8% and 78.6% - and marks those as horizontal levels where a pullback might pause. In an upswing you drag from the swing low to the swing high; in a downswing, from the swing high to the swing low. The levels are not magnetic. They become worth watching when they line up with something else, such as a prior support or resistance zone, a trendline or a round number.',
    'body': '''<h2>What the tool actually does</h2>

    <p>Mechanically, Fibonacci retracement is nothing more than proportional division. You pick a completed move - a swing from a low to a high, or a high to a low - and the tool draws horizontal lines at fixed fractions of that distance.</p>

    <p>The fractions come from ratios associated with the Fibonacci sequence, which is where the name and a lot of the mystique originate. You do not need the mathematics to use the tool. What matters is that it gives you a consistent way to ask: "if price pulls back from this move, how far has it retraced?"</p>

    <div class="info-card">
      <h4>The common levels</h4>
      <p><strong>23.6%</strong> - a shallow pullback. In strong trends, retracements often stay this shallow.</p>
      <p><strong>38.2%</strong> - a moderate pullback.</p>
      <p><strong>50%</strong> - not a Fibonacci ratio at all, but included by almost every charting platform because halfway is a natural reference point.</p>
      <p><strong>61.8%</strong> - the level most traders watch. The zone between roughly 61.8% and 65% is often called the "golden pocket".</p>
      <p><strong>78.6%</strong> - a deep pullback. Beyond this, many traders would question whether the original move is still intact.</p>
    </div>

    <h2>How to draw it, step by step</h2>

    <ol>
      <li><strong>Identify a completed swing.</strong> You need a clear starting point and a clear end. If you cannot point to an obvious swing low and swing high, there is nothing meaningful to measure.</li>
      <li><strong>Pick the direction.</strong> For an upswing that is now pulling back, drag from the swing low to the swing high. For a downswing that is now bouncing, drag from the swing high to the swing low. The tool needs to know which end is the origin of the move.</li>
      <li><strong>Choose wicks or bodies, then stick with it.</strong> Most traders anchor to the wick extremes. Bodies are defensible too. Mixing the two between charts makes your levels inconsistent.</li>
      <li><strong>Check that 0% and 100% landed where you meant.</strong> Platforms label the ends differently. Make sure the level marked 100% (or 0%, depending on the platform) is the origin of the move, so the 61.8% line sits where a deep pullback would be.</li>
    </ol>

    <h2>The hard part: which swing</h2>

    <p>Every chart has many swings, and each one produces a different set of levels. This is where Fibonacci retracement goes wrong for most people, and it goes wrong quietly.</p>

    <p>If you are allowed to choose any swing, you can almost always find one whose retracement levels line up with wherever price happened to turn. That feels like confirmation. It is actually hindsight: you chose the measurement after seeing the outcome.</p>

    <p>Some ways to keep it honest:</p>

    <ul>
      <li><strong>Use the most obvious swing on the timeframe you are analysing.</strong> If someone else looked at the same chart, would they pick the same two points?</li>
      <li><strong>Decide before price reaches the level.</strong> Draw the retracement while the pullback is in progress, not afterwards.</li>
      <li><strong>Prefer higher-timeframe swings.</strong> A swing visible on the daily chart is one many participants are measuring. One that only exists on the 3-minute chart is not.</li>
    </ul>

    <h2>Why the levels are not magic</h2>

    <p>There is a lot of writing that treats Fibonacci levels as natural laws markets obey. That framing is not supported by anything a chart can show you. Price pulls back by all sorts of amounts, and with five or six levels drawn across a swing, price will always be near one of them.</p>

    <p>Where the levels can matter is as a shared reference point. Enough traders draw retracements on prominent swings that orders cluster around popular levels, which can make them behave a bit like any other widely watched price. That is a crowd behaviour effect, and like all such effects it is inconsistent.</p>

    <h2>Confluence is the whole point</h2>

    <p>A Fibonacci level on its own is one line among several. It becomes interesting when it coincides with something you would have marked anyway.</p>

    <table class="comparison-table">
      <thead>
        <tr><th>Fib level lines up with...</th><th>Why it adds weight</th></tr>
      </thead>
      <tbody>
        <tr class="highlight-row"><td>A prior support or resistance zone</td><td>The level is already proven by past price behaviour, independent of the Fib tool.</td></tr>
        <tr><td>A rising or falling trendline</td><td>Two different methods point to the same area.</td></tr>
        <tr><td>A round number</td><td>Weak on its own, but another reason for orders to cluster.</td></tr>
        <tr><td>A higher-timeframe level</td><td>More participants can see it.</td></tr>
      </tbody>
    </table>

    <p>If the 61.8% line sits in empty space with nothing else around it, there is not much reason to expect anything special to happen there. If it sits on top of an old <a href="/chartcheck/blog/support-and-resistance/">support zone</a> that has held three times, the Fib tool has just confirmed something you could already see.</p>

    <h2>A worked example, in words</h2>

    <p>Suppose a stock rallies cleanly from a swing low at 80 to a swing high at 100 over several weeks, then starts to pull back. You drag the tool from 80 to 100. The levels land at roughly 95.3 (23.6%), 92.4 (38.2%), 90 (50%), 87.6 (61.8%) and 84.3 (78.6%).</p>

    <p>Now look left. Before the rally, price spent a month consolidating with a ceiling around 88. That old ceiling, if it holds as support on the way back down, sits right next to the 61.8% level. That is confluence: two independent reasons to pay attention to the 87 to 89 area. A pullback that stalls there and shows rejection is more interesting than one that stalls at 92.4 in empty space.</p>

    <p>Conversely, if price falls cleanly through 84 and the old consolidation without pausing, the pullback has become deep enough that the original rally's structure is in question. The levels did not "fail"; they were never promises. They were a way of organising where to look.</p>

    <h2>Common Fibonacci mistakes</h2>

    <ul>
      <li><strong>Measuring a swing that is not finished.</strong> If price is still making new highs, the 100% point keeps moving and so do all the levels.</li>
      <li><strong>Picking the swing after the fact.</strong> Choosing the anchor points that make a past turn line up perfectly is hindsight, not analysis.</li>
      <li><strong>Drawing too many retracements at once.</strong> Several overlapping Fib grids from different swings will put a level at nearly every price, which tells you nothing.</li>
      <li><strong>Treating the levels as exact.</strong> Price respecting "the 61.8%" usually means price reacted somewhere near it. Read the levels as zones.</li>
      <li><strong>Ignoring the timeframe.</strong> A retracement of a 20-minute swing and one of a six-month swing are not equally significant, even if they share a ratio.</li>
    </ul>

    <h2>Extensions, briefly</h2>

    <p>Fibonacci extensions project levels beyond the end of the original swing - 127.2%, 161.8% and so on - and are used by some traders as possible targets if a trend continues. They carry the same caveats as retracements, with an extra one: they point into price territory where there is no past behaviour at all, so there is nothing to confirm or refute them until price gets there.</p>

    <h2>What an AI read can and cannot do with Fibonacci</h2>

    <p>If you have already drawn a retracement and it is visible in your screenshot, an AI read can see where price sits relative to your levels. If you have not, a tool reading the image has to make the same judgement call you would: which swing to measure. That choice is subjective, and two reasonable analysts can pick different swings on the same chart.</p>

    <p>It is also worth being careful with any precise level a tool reports. A model reading pixels has to infer prices from the axis, and the exact value of a 61.8% line depends on reading both swing extremes accurately. Treat specific numbers as approximate, and check them against the price axis yourself. The <a href="/chartcheck/blog/why-ai-chart-analysis-is-wrong/">failure modes article</a> covers this kind of invented precision in more detail.</p>''',
    'faqs': [
        ('Do you draw Fibonacci from high to low or low to high?',
         'From the origin of the move to its end. For an upswing that is pulling back, drag from the swing low up to the swing high. For a downswing that is bouncing, drag from the swing high down to the swing low. After drawing, check that the deep levels such as 61.8% sit where a deep pullback would be.'),
        ('What is the most important Fibonacci level?',
         '61.8% is the most widely watched, and the area around 61.8% to 65% is often called the golden pocket. 50% is also heavily watched even though it is not a true Fibonacci ratio. No single level is reliable on its own; a level matters far more when it coincides with prior support or resistance.'),
        ('Do Fibonacci retracements actually work?',
         'They work as a consistent way to measure pullbacks and as a shared reference many traders look at. They do not work as natural laws that price obeys. With several levels drawn across a swing, price will always be near one of them, so a level only becomes meaningful when other evidence points to the same area.'),
        ('Should I use wicks or candle bodies for Fibonacci?',
         'Wicks are the most common choice because they capture the true extremes of the swing. Bodies are also defensible. What matters is consistency - switching between them chart to chart, or to make the levels fit, produces levels that only exist because you wanted them to.'),
    ],
    'related': ['support-and-resistance', 'how-to-draw-trend-lines', 'multi-timeframe-analysis'],
})

# ---------------------------------------------------------------- B4
ARTICLES.append({
    'slug': 'how-to-draw-trend-lines',
    'seo_title': 'How to Draw Trend Lines Correctly | ChartCheck',
    'seo_h1': 'How to Draw Trend Lines That Mean Something',
    'og_title': 'How to Draw Trend Lines',
    'meta_desc': 'How to draw trend lines correctly: which points to connect, wicks versus bodies, why log scale changes everything, and how to tell a real break from noise.',
    'og_desc': 'Which points to connect, wicks vs bodies, log scale, and how to read a trend line break.',
    'keywords': 'how to draw trend lines, trend line trading, trendline, drawing trendlines, trend line break, ascending trend line, descending trend line',
    'badge': 'Tools',
    'published': '2026-10-01', 'published_label': 'October 1, 2026',
    'card_title': 'How to Draw Trend Lines',
    'card_desc': 'Which points to connect, wicks vs bodies, log scale, and what a break actually means.',
    'intro': 'Trend lines are the most freely drawn tool in technical analysis, which makes them both flexible and dangerous. Almost any chart will accept a line through three points if you are willing to adjust the angle. The skill is drawing lines you would have drawn before you knew what happened next.',
    'quick_answer': 'An uptrend line connects two or more rising swing lows; a downtrend line connects two or more falling swing highs. Two points define a line, a third touch is what validates it. Decide in advance whether you connect wicks or bodies, and apply it consistently. Do not force the line through candles to make it fit. Trend lines depend on the price scale, so check log scale on long-term charts. A break matters more when it closes beyond the line and when the swing structure breaks with it.',
    'body': '''<h2>What a trend line represents</h2>

    <p>A trend is a sequence: higher highs and higher lows in an uptrend, lower highs and lower lows in a downtrend. A trend line is a visual summary of the rate at which that sequence has been progressing.</p>

    <p>An uptrend line drawn under the swing lows says, roughly, "buyers have been stepping in at progressively higher prices, at about this pace." While price stays above the line, that pace is intact. When price falls through it, the pace has changed - which is not necessarily the same as the trend ending.</p>

    <p>That distinction matters. A trend line break is first a statement about <em>rate</em>, and only sometimes a statement about direction.</p>

    <h2>How to draw one, step by step</h2>

    <ol>
      <li><strong>Identify the trend from the swings first.</strong> Before drawing anything, confirm that you can see rising lows (for an uptrend line) or falling highs (for a downtrend line). If the swings do not form a sequence, there is no trend to draw.</li>
      <li><strong>Connect the two most significant swing points.</strong> For an uptrend, the two most obvious swing lows. For a downtrend, the two most obvious swing highs. Not any two candles - clear turning points.</li>
      <li><strong>Extend it forward.</strong> The line only becomes useful when you project it to the right of the chart.</li>
      <li><strong>Wait for the third touch.</strong> Two points always make a line. A third reaction at the line is the first evidence it reflects real behaviour rather than geometry.</li>
    </ol>

    <h2>Wicks or bodies</h2>

    <p>There are two schools, and both are reasonable.</p>

    <ul>
      <li><strong>Wicks</strong> capture the full extent of where price went. Lines through wick extremes are the most literal.</li>
      <li><strong>Bodies</strong> capture where price closed and are sometimes argued to reflect acceptance better, ignoring brief spikes.</li>
    </ul>

    <p>The real rule is consistency. The common failure is switching between wicks and bodies within the same line, or from chart to chart, whenever it produces a neater fit. A line that only works because you changed the rules halfway along is not describing the market.</p>

    <h2>Do not force the fit</h2>

    <p>A trend line that slices through several candle bodies to reach a third touch is not a trend line, it is a line. If honest drawing produces only two touches, you have a two-touch line, and you should treat it as unconfirmed rather than nudging it until it qualifies.</p>

    <p>Equally, a line that has been redrawn four times as price broke through each version is telling you something: there is no stable rate to the trend. That is useful information in itself, and redrawing it away loses it.</p>

    <h2>The angle matters</h2>

    <p>Very steep trend lines break quickly, because almost no trend sustains a near-vertical pace. A steep line breaking often means the move is slowing to a more normal rate rather than reversing. Very shallow lines are hard to break and can be so loose they barely constrain price at all.</p>

    <p>Some traders keep two lines on the same trend: a steeper short-term one and a shallower long-term one. A break of the steep line with the shallow one intact is a deceleration. A break of both is a more significant change.</p>

    <h2>Linear versus log scale</h2>

    <p>This is the most overlooked trend line issue, and it can completely change what you see.</p>

    <p>On a linear chart, equal vertical distances represent equal price changes. On a log chart, equal vertical distances represent equal <em>percentage</em> changes. For short timeframes and small moves, the two look nearly identical. For long-term charts, or instruments that have moved a large percentage, they diverge dramatically - and a trend line that fits beautifully on one scale may not exist on the other.</p>

    <div class="info-card">
      <h4>A practical rule</h4>
      <p>For charts covering a large percentage move or several years, check both scales. If a trend line only holds on one, be cautious about treating it as significant. Long-term trend lines on assets that have multiplied in price are usually more meaningful on log scale, because log scale reflects proportional moves.</p>
    </div>

    <h2>Reading a break</h2>

    <p>Price crossing a trend line is common. What it means depends on what comes with it.</p>

    <table class="comparison-table">
      <thead>
        <tr><th>What you see</th><th>Reasonable interpretation</th></tr>
      </thead>
      <tbody>
        <tr><td>Wick through, close back on the trend side</td><td>A test of the line, not a break.</td></tr>
        <tr><td>Close beyond the line, swing structure intact</td><td>The pace has slowed. The trend may continue at a shallower angle.</td></tr>
        <tr class="highlight-row"><td>Close beyond the line and the last swing low (or high) breaks too</td><td>Both the rate and the structure have changed. This is the more significant event.</td></tr>
        <tr><td>Break, then a retest of the line from the other side that holds</td><td>The line has flipped role, much like a broken horizontal level.</td></tr>
      </tbody>
    </table>

    <p>Horizontal <a href="/chartcheck/blog/support-and-resistance/">support and resistance</a> generally deserves more weight than diagonal lines, simply because there is less drawing freedom: a horizontal level is defined by prices, while a diagonal line is defined by your choice of points and angle.</p>

    <h2>Channels</h2>

    <p>A channel is a trend line plus a parallel line on the other side of price, drawn through the opposing swings. It describes a trend that is progressing at a steady rate within a steady range. Channels are useful for seeing when a move is unusually stretched against its own recent behaviour, and for spotting when the range itself starts to change shape - narrowing into a <a href="/chartcheck/blog/chart-patterns-cheat-sheet/">wedge</a>, for example.</p>

    <h2>Trend lines across timeframes</h2>

    <p>The same instrument can have a perfectly valid uptrend line on the daily chart and a perfectly valid downtrend line on the hourly chart at the same time. That is not a contradiction. The hourly line describes a pullback; the daily line describes the trend the pullback is happening inside.</p>

    <p>The practical habit is to draw the higher-timeframe line first, then carry it down to your working timeframe rather than redrawing from scratch. A shorter-term line breaking in the direction of the longer-term trend - a downtrend line on the hourly breaking upward while the daily uptrend is intact - is a common way traders frame the end of a pullback. A shorter-term line breaking against the longer-term trend is often just noise. The <a href="/chartcheck/blog/multi-timeframe-analysis/">multi-timeframe guide</a> covers this layering in more detail.</p>

    <h2>Common trend line mistakes</h2>

    <ul>
      <li><strong>Drawing the line before the trend exists.</strong> Two random lows do not make an uptrend. The swing sequence comes first.</li>
      <li><strong>Forcing a third touch.</strong> Adjusting the angle until it grazes another candle, while cutting through bodies on the way, produces a line that only exists because you wanted it.</li>
      <li><strong>Redrawing after every break.</strong> If you keep rotating the line to keep price above it, you are no longer measuring the trend, you are protecting a view.</li>
      <li><strong>Ignoring scale on long charts.</strong> A line that only fits on linear or only on log is fragile.</li>
      <li><strong>Treating any touch as a bounce signal.</strong> A trend line touch is a place to watch for a reaction, not a guarantee of one.</li>
      <li><strong>Overweighting diagonal lines.</strong> When a trend line and a horizontal level disagree, the horizontal level has less subjectivity built into it.</li>
    </ul>

    <h2>A short checklist before trusting a line</h2>

    <ol>
      <li>Can you see a clear sequence of rising lows or falling highs without the line?</li>
      <li>Does the line touch at least three swing points honestly, using one consistent convention?</li>
      <li>Would someone else looking at the same chart draw roughly the same line?</li>
      <li>Does it hold on both linear and log scale, if the chart covers a large move?</li>
      <li>Does it agree with, or at least not contradict, the obvious horizontal levels?</li>
    </ol>

    <p>A line that passes all five is worth watching. A line that fails two or more is mostly decoration.</p>

    <h2>Trend lines in an AI read</h2>

    <p>Rising lows and falling highs are among the most mechanical features of a chart, and a vision model reading a screenshot can usually describe the sequence reliably. Drawing an exact trend line is harder: the result depends on the same choices you make - which swings, wicks or bodies, which scale - and the model has to infer them from pixels without knowing whether the chart is on log or linear.</p>

    <p>The more robust use is the reverse. Draw your own line, include it in the screenshot, and use the read as a check on whether the structure around it agrees with what the line implies.</p>''',
    'faqs': [
        ('How many points do you need to draw a trend line?',
         'Two points define the line; a third touch validates it. A two-touch line is a hypothesis. A line that price has reacted to three or more times, without being forced through candle bodies, is describing something real about how the trend has progressed.'),
        ('Should trend lines connect wicks or bodies?',
         'Either is acceptable. Wicks show the full extremes; bodies show where price closed. The important thing is to pick one approach and use it consistently, rather than switching to make a particular line fit.'),
        ('Does a trend line break mean the trend is over?',
         'Not necessarily. A break first means the trend\'s pace has changed. The trend itself is in question when the swing structure breaks too - in an uptrend, when price also falls below its most recent swing low. A break followed by a successful retest of the line from the other side is the stronger signal.'),
        ('Should I use log or linear scale for trend lines?',
         'For short timeframes the difference is negligible. For long-term charts or large percentage moves, check both. Log scale treats equal percentage moves as equal distances, which usually makes long-term trend lines more meaningful. A line that only works on one scale deserves less confidence.'),
    ],
    'related': ['support-and-resistance', 'fibonacci-retracement', 'how-to-read-a-stock-chart'],
})

# ---------------------------------------------------------------- B5
ARTICLES.append({
    'slug': 'head-and-shoulders-pattern',
    'seo_title': 'Head and Shoulders Pattern, Explained | ChartCheck',
    'seo_h1': 'The Head and Shoulders Pattern, and the Inverse Version, Explained',
    'og_title': 'The Head and Shoulders Pattern Explained',
    'meta_desc': 'How to spot a head and shoulders pattern and its inverse, where to draw the neckline, what confirms it, and why people see it everywhere.',
    'og_desc': 'How to spot it, where the neckline goes, what confirms it, and why people see it everywhere.',
    'keywords': 'head and shoulders pattern, inverse head and shoulders, head and shoulders neckline, head and shoulders chart pattern, reverse head and shoulders',
    'badge': 'Patterns',
    'published': '2026-10-01', 'published_label': 'October 1, 2026',
    'card_title': 'Head and Shoulders Pattern',
    'card_desc': 'Spotting it, drawing the neckline, what confirms it, and why it gets over-called.',
    'intro': 'Head and shoulders is the most famous reversal pattern in technical analysis, and the most over-identified. Once you know the shape, you start seeing it in every three bumps on every chart. Understanding what the pattern records - and what has to happen before it exists at all - is what separates spotting it from imagining it.',
    'quick_answer': 'A head and shoulders is three peaks: a left shoulder, a higher head, and a lower right shoulder, with a neckline connecting the two lows between them. It appears after an uptrend and records buyers failing to make a new high on the third attempt. The pattern is only complete when price closes below the neckline - before that it is a possibility, not a pattern. The inverse head and shoulders is the mirror image at the bottom of a downtrend, completed by a close above the neckline.',
    'body': '''<h2>The anatomy</h2>

    <div class="info-card">
      <h4>Four parts, in order</h4>
      <p><strong>Left shoulder.</strong> Price rallies to a high as part of an existing uptrend, then pulls back.</p>
      <p><strong>Head.</strong> Price rallies again to a higher high, then pulls back roughly to where the last pullback ended.</p>
      <p><strong>Right shoulder.</strong> Price rallies a third time but fails to reach the height of the head, then turns down again.</p>
      <p><strong>Neckline.</strong> A line connecting the two pullback lows - the one after the left shoulder and the one after the head. It can be horizontal or sloped.</p>
    </div>

    <p>The shoulders do not need to be identical, and the neckline does not need to be flat. What matters is the sequence: a higher high, followed by a failure to make another one.</p>

    <h2>What the pattern actually records</h2>

    <p>Read it as a story about the trend rather than a shape.</p>

    <p>Through the left shoulder and the head, the uptrend is still doing its job - higher highs. The right shoulder is where it fails: buyers rally, but cannot even get back to the previous high. That is the first lower high after a series of higher ones. When price then breaks the neckline, it also makes a lower low relative to the pullbacks, and the trend's structure has flipped from higher highs and higher lows to lower highs and lower lows.</p>

    <p>In other words, a completed head and shoulders is simply a named, visually memorable version of an uptrend's structure breaking. That framing is useful because it tells you what actually matters: the lower high and the lower low. The rest is presentation.</p>

    <h2>It is not a pattern until the neckline breaks</h2>

    <p>This is the single most important rule and the most commonly ignored. Left shoulder, head and a right shoulder that is still forming is just a market that made a high and pulled back. It could just as easily rally through the head and continue the trend.</p>

    <p>The pattern is completed by a close below the neckline. Before that, what you have is a possible head and shoulders, and the honest description is "watching for a neckline break", not "head and shoulders forming".</p>

    <p>Many apparent head and shoulders setups never complete. Price bounces off the neckline and resumes higher, and the "right shoulder" turns out to have been a normal pullback in an ongoing uptrend.</p>

    <h2>Drawing the neckline</h2>

    <ul>
      <li>Connect the low after the left shoulder to the low after the head.</li>
      <li>Use the same convention you use elsewhere - wicks or bodies - and do not switch to make the line neater.</li>
      <li>A downward-sloping neckline is generally considered the weaker structure for buyers, because the second pullback low was already lower than the first.</li>
      <li>Treat the neckline as a zone rather than a single line, for the same reasons you would with any <a href="/chartcheck/blog/support-and-resistance/">support level</a>.</li>
    </ul>

    <h2>What adds weight</h2>

    <table class="comparison-table">
      <thead>
        <tr><th>Feature</th><th>Why it matters</th></tr>
      </thead>
      <tbody>
        <tr class="highlight-row"><td>A clear prior uptrend</td><td>A reversal pattern needs a trend to reverse. Three bumps in a sideways range are not a head and shoulders.</td></tr>
        <tr><td>Close below the neckline, not just a wick</td><td>A wick through the neckline is a test. A close is a break.</td></tr>
        <tr><td>Volume fading into the right shoulder</td><td>Traditionally read as weaker participation in the final rally. See the <a href="/chartcheck/blog/volume-analysis-trading/">volume guide</a> for how to read it.</td></tr>
        <tr><td>Higher timeframe</td><td>A daily or weekly pattern reflects far more participation than one on a 5-minute chart.</td></tr>
        <tr><td>Retest of the neckline that holds as resistance</td><td>Shows the old support has flipped role.</td></tr>
      </tbody>
    </table>

    <h2>The measured move, and why to be careful with it</h2>

    <p>A common convention is to measure the vertical distance from the top of the head to the neckline, and project that distance downward from the break point as a rough target. It is a reasonable way to estimate the scale of the structure. It is not a forecast, and there is no reason price must travel that distance. Patterns frequently fall short of their measured moves, and sometimes overshoot them dramatically. Treat it as a sense of proportion, not a destination.</p>

    <h2>The inverse head and shoulders</h2>

    <p>Flip everything vertically and you have the inverse (or reverse) head and shoulders, which appears after a downtrend.</p>

    <ul>
      <li>Left shoulder: a low, then a bounce.</li>
      <li>Head: a lower low, then a bounce to around the previous bounce high.</li>
      <li>Right shoulder: a higher low that fails to reach the depth of the head.</li>
      <li>Neckline: connects the two bounce highs, and the pattern completes on a close above it.</li>
    </ul>

    <p>The story is the same in reverse: sellers make a new low, then fail to make another one, and the break above the neckline turns lower highs into higher highs. All the same rules apply - prior trend required, close required, neckline as a zone.</p>

    <h2>A worked example, in words</h2>

    <p>Imagine a stock that has climbed steadily for three months. It reaches 50 and pulls back to 45 (left shoulder). It rallies to a new high at 55 and pulls back to 46 (head). Then it rallies again but stalls at 52 and starts to fall (right shoulder in progress). Drawing a line through 45 and 46 gives a slightly rising neckline in the 46 to 47 area by the time price returns to it.</p>

    <p>At this point, the honest description is: "a lower high at 52 after a new high at 55, with a neckline around 46 to 47." That is a possible head and shoulders. If price bounces at the neckline and later pushes through 55, the pattern never existed - the right shoulder was just a pullback. If price closes below 46 and then fails to get back above it on a retest, the pattern completed and the trend's structure has changed from higher lows to lower lows.</p>

    <p>Notice that nothing in that sequence required knowing what would happen next. Each step is a description of what price has already done. That is what keeps head and shoulders analysis honest.</p>

    <h2>Failed patterns</h2>

    <p>A head and shoulders that breaks the neckline and then quickly reverses back above it, pushing toward or through the right shoulder, is a failed pattern. Some traders pay particular attention to failures, on the reasoning that participants who acted on the break are now positioned the wrong way. Whether or not you use that idea, it is worth recognising that a completed pattern can still fail, and that holding onto the pattern after price has invalidated it is a common and costly habit.</p>

    <h2>Why people see it everywhere</h2>

    <p>Three peaks with the middle one highest is an extremely common shape, because markets oscillate. The pattern only carries meaning when it sits at the end of a clear trend, at a sensible scale, and when it completes. Most "head and shoulders" posts on social media are missing at least one of those three, usually the last.</p>

    <p>A useful discipline: before calling one, state what the prior trend was, where the neckline is, and what price would have to do to complete it. If you cannot answer all three, you have a shape, not a pattern.</p>

    <h2>Spotting it from a screenshot</h2>

    <p>The shape itself is a good fit for image-based analysis. A vision model reading a chart can recognise three peaks with a higher middle and suggest a neckline, the same way it recognises other <a href="/chartcheck/blog/chart-patterns-cheat-sheet/">chart patterns</a>. The limits are the usual ones: it only sees the prior trend if enough of it is in the frame, it cannot know whether the next candle closes through the neckline, and a confident pattern label still describes a possibility until price completes it. A good read will say whether the pattern has completed or is only potential; if it does not say, ask.</p>''',
    'faqs': [
        ('Is head and shoulders bullish or bearish?',
         'The standard head and shoulders, appearing at the top of an uptrend, is a bearish reversal pattern. The inverse head and shoulders, appearing at the bottom of a downtrend, is a bullish one. In both cases the pattern is only complete once price closes through the neckline.'),
        ('How do you confirm a head and shoulders pattern?',
         'By a close beyond the neckline - below it for a standard pattern, above it for an inverse one. Until then the pattern is only potential and frequently fails to complete. A subsequent retest of the neckline from the other side that holds adds further confirmation.'),
        ('Do the shoulders have to be the same height?',
         'No. The shoulders are rarely symmetrical. What matters is that the head is the extreme and the right shoulder fails to reach it, because that failure is the first break in the trend\'s sequence of highs (or lows, for the inverse version).'),
        ('How reliable is the head and shoulders pattern?',
         'No chart pattern is reliable in isolation, and this one is especially prone to being called before it exists. Its usefulness improves considerably when there is a clear prior trend, the pattern completes with a close through the neckline, and it forms on a higher timeframe.'),
    ],
    'related': ['double-top-double-bottom', 'chart-patterns-cheat-sheet', 'volume-analysis-trading'],
})

# ---------------------------------------------------------------- B6
ARTICLES.append({
    'slug': 'bull-flag-pattern',
    'seo_title': 'Bull Flag Pattern: Flags, Bear Flags and Pennants | ChartCheck',
    'seo_h1': 'The Bull Flag Pattern, the Bear Flag, and How Flags Differ From Pennants',
    'og_title': 'The Bull Flag Pattern Explained',
    'meta_desc': 'How to spot a bull flag and a bear flag, what separates a flag from a pennant, what a valid flagpole looks like, and the signs a flag is actually failing.',
    'og_desc': 'Bull flags, bear flags, flag vs pennant, and the signs a flag is failing.',
    'keywords': 'bull flag pattern, bear flag pattern, flag vs pennant, bull flag chart pattern, flag pattern trading, bullish flag',
    'badge': 'Patterns',
    'published': '2026-10-01', 'published_label': 'October 1, 2026',
    'card_title': 'Bull Flags, Bear Flags and Pennants',
    'card_desc': 'What makes a valid flagpole, flag vs pennant, and the signs a flag is failing.',
    'intro': 'Flags are the most popular continuation pattern on social media, partly because they are easy to see and partly because they look like a strong move about to resume. The second part is where the trouble starts. A flag is a pause, and pauses end in both directions.',
    'quick_answer': 'A bull flag is a sharp, near-vertical rise (the flagpole) followed by a short, orderly pullback or sideways drift inside a small parallel channel (the flag). It is read as a pause before the trend continues, and is completed by a break above the top of the flag. A bear flag is the mirror image after a sharp drop. A pennant is the same idea, except the consolidation narrows into a small symmetrical triangle instead of a parallel channel. The flagpole matters as much as the flag: without a strong prior move, there is no flag.',
    'body': '''<h2>The two parts of a flag</h2>

    <div class="info-card">
      <h4>Pole, then flag</h4>
      <p><strong>The flagpole.</strong> A sharp, decisive move covering a lot of ground in relatively few candles. This is the part that makes it a flag pattern at all. A slow, grinding rise does not produce a flagpole.</p>
      <p><strong>The flag.</strong> A brief, contained consolidation after the pole. In a bull flag it typically drifts slightly downward or sideways between two roughly parallel lines. It should be small relative to the pole and short in duration compared to the move that preceded it.</p>
    </div>

    <p>The pattern records a market that moved hard, then paused without giving much back. Holders did not rush to take profits, and sellers could not push price down meaningfully. That is the case for continuation: the pause looks like digestion rather than reversal.</p>

    <h2>What makes a flag credible</h2>

    <ul>
      <li><strong>A real flagpole.</strong> The prior move should be sharp and obvious. If you have to squint to see the pole, there is no pattern.</li>
      <li><strong>A shallow flag.</strong> A bull flag that retraces most of its pole is no longer a pause; it is a reversal in progress. Many traders become wary once the flag gives back more than about half of the pole.</li>
      <li><strong>A short flag.</strong> Flags are pauses. One that drags on for far longer than the pole took to form has become a range, and ranges resolve either way.</li>
      <li><strong>Orderly boundaries.</strong> The consolidation should fit inside reasonably clean parallel lines. A messy, expanding consolidation is a different structure.</li>
      <li><strong>Volume behaviour.</strong> Traditionally, volume is heavy during the pole and lighter during the flag. The <a href="/chartcheck/blog/volume-analysis-trading/">volume guide</a> covers how to read that, and its limits.</li>
    </ul>

    <h2>The break</h2>

    <p>A bull flag is completed by price closing above the upper boundary of the flag. Until then, it is a pullback after a strong move, and nothing more.</p>

    <p>As with other patterns, the close matters more than the wick, and a break that immediately falls back inside the flag is a warning rather than a confirmation. Some traders also look for the old flag boundary to act as support on a retest after the break.</p>

    <h2>The bear flag</h2>

    <p>Flip it over for a bear flag: a sharp drop (the pole), then a brief upward or sideways drift in a small channel (the flag), completed by a close below the lower boundary. The story is the same in reverse - a strong sell-off, then a weak bounce that fails to recover much ground.</p>

    <p>Bear flags are just as common as bull flags and get far less attention, mostly because fewer people want to see them. Reading charts honestly means looking for both.</p>

    <h2>Flag versus pennant</h2>

    <table class="comparison-table">
      <thead>
        <tr><th></th><th>Flag</th><th>Pennant</th></tr>
      </thead>
      <tbody>
        <tr><td>Shape of the pause</td><td>Parallel channel, usually sloping slightly against the pole</td><td>Small symmetrical triangle with converging lines</td></tr>
        <tr><td>What the shape records</td><td>Orderly drift against the trend</td><td>Narrowing range, decreasing volatility</td></tr>
        <tr><td>Prerequisite</td><td colspan="2">A sharp flagpole. Without it, neither pattern exists.</td></tr>
        <tr class="highlight-row"><td>Completed by</td><td colspan="2">A close beyond the boundary in the direction of the pole.</td></tr>
      </tbody>
    </table>

    <p>In practice, flags and pennants are read almost identically. A pennant is essentially a very small, short-lived <a href="/chartcheck/blog/chart-patterns-cheat-sheet/">symmetrical triangle</a> sitting on top of a flagpole. The distinction is mostly about what lines you draw around the pause.</p>

    <h2>Flag versus wedge</h2>

    <p>A flag whose boundaries converge while sloping against the trend starts to look like a wedge. The difference matters because rising and falling wedges are often read differently from flags depending on context. If the consolidation is long, the lines clearly converge, and the pole is not obvious, you are probably looking at a wedge rather than a flag. When in doubt, describe what you see - "a contracting pullback after a strong rise" - rather than forcing a name onto it.</p>

    <h2>Signs a flag is failing</h2>

    <ol>
      <li><strong>It retraces too much.</strong> A bull flag that gives back most of its pole has stopped being a pause.</li>
      <li><strong>It takes too long.</strong> The longer the consolidation, the less it resembles a flag and the more it resembles a top or a range.</li>
      <li><strong>It breaks the wrong way.</strong> A bull flag that closes below its lower boundary is no longer a bull flag. Ignoring that because you were expecting continuation is how the pattern turns expensive.</li>
      <li><strong>The break does not follow through.</strong> A close above the flag that is immediately reversed back inside is a failed breakout, which some traders read as a signal in the opposite direction.</li>
    </ol>

    <h2>A worked example, in words</h2>

    <p>Suppose a stock trading quietly around 30 jumps to 36 over three sessions on heavy volume. That is the pole. Over the next five sessions it drifts down to about 34.50 inside two slightly downward-sloping parallel lines, on noticeably lighter volume. It has given back a quarter of the pole, in a fraction of the time the pole took to build. That is a reasonable-looking bull flag.</p>

    <p>Three things can happen next. Price closes above the upper flag line and holds there: the flag completed. Price keeps drifting sideways for three more weeks: the pause has turned into a range, and the flag framing no longer fits. Or price closes below the lower flag line and keeps going toward 32: the flag failed, and the pole is being given back.</p>

    <p>Only the first outcome is a "bull flag" in hindsight, but all three looked identical at the moment the flag was forming. That is the honest situation with every continuation pattern.</p>

    <h2>Where flags show up</h2>

    <p>Flags form on every timeframe and in every market, which is part of why they are so popular. They are particularly visible after news-driven moves, earnings gaps, and in volatile instruments like crypto, where sharp moves followed by pauses are common. That does not make them more reliable there; it just makes them more frequent. Location still matters: a bull flag forming just under a major <a href="/chartcheck/blog/support-and-resistance/">resistance zone</a> on a higher timeframe has an obvious obstacle directly above it.</p>

    <h2>The measured move</h2>

    <p>A common convention projects the length of the flagpole from the breakout point as a rough sense of scale. Like every measured move, it is a proportion, not a promise. Price may stop well short of it or extend beyond it. It is reasonable for thinking about scale, and unreasonable as an expectation.</p>

    <h2>Flags on a screenshot</h2>

    <p>Flags are a strong match for image-based analysis: a sharp pole followed by a small channel is a distinctive shape, and a vision model reading a chart can usually spot one, describe its boundaries, and say whether price has broken out. The caveats are about scale and context. On a short timeframe, almost every sharp move followed by a pause looks like a flag, and many of them mean little. A tool cannot see the higher-timeframe picture unless it is in the screenshot, and it cannot know whether the next candle will break the flag or fail. Reading the same chart on a higher timeframe is often the fastest way to see whether the "flag" is actually a pause in a trend or a blip in a range - the <a href="/chartcheck/blog/multi-timeframe-analysis/">multi-timeframe guide</a> covers how.</p>''',
    'faqs': [
        ('What is a bull flag pattern?',
         'A bull flag is a sharp upward move (the flagpole) followed by a short, shallow consolidation inside a small parallel channel (the flag). It is read as a pause before the uptrend continues, and is completed only when price closes above the top of the flag.'),
        ('What is the difference between a flag and a pennant?',
         'The shape of the consolidation. A flag consolidates inside roughly parallel lines; a pennant consolidates inside converging lines, forming a small symmetrical triangle. Both require a sharp prior move and both are completed by a break in the direction of that move.'),
        ('How long should a bull flag last?',
         'Short relative to the flagpole. A flag is a pause, and a consolidation that drags on much longer than the move before it has become a range or a possible top. There is no fixed number of candles, but the flag should look clearly smaller and briefer than the pole.'),
        ('What happens if a bull flag breaks down?',
         'It stops being a bull flag. A close below the lower boundary invalidates the continuation read and may indicate the prior move is reversing. A failed flag can be informative in its own right, but only if you accept the failure rather than redrawing the pattern.'),
    ],
    'related': ['chart-patterns-cheat-sheet', 'volume-analysis-trading', 'multi-timeframe-analysis'],
})

# ---------------------------------------------------------------- B7
ARTICLES.append({
    'slug': 'double-top-double-bottom',
    'seo_title': 'Double Top and Double Bottom Patterns Explained | ChartCheck',
    'seo_h1': 'Double Top and Double Bottom Patterns: How to Read Them Properly',
    'og_title': 'Double Top and Double Bottom Patterns',
    'meta_desc': 'How to identify a double top and double bottom, why the middle swing is the line that matters, what confirms it, and how it differs from a range.',
    'og_desc': 'Why the middle swing is the line that matters, what confirms it, and how it differs from a range.',
    'keywords': 'double top pattern, double bottom pattern, double top and double bottom, w pattern trading, m pattern trading, triple top',
    'badge': 'Patterns',
    'published': '2026-10-01', 'published_label': 'October 1, 2026',
    'card_title': 'Double Tops and Double Bottoms',
    'card_desc': 'Why the middle swing is the line that matters, and how to tell a pattern from a range.',
    'intro': 'Double tops and double bottoms are the simplest reversal patterns to describe: price hits the same level twice and turns away. That simplicity is also the trap. Price revisiting a level is one of the most common things charts do, and most revisits are not reversal patterns.',
    'quick_answer': 'A double top is two peaks at roughly the same level after an uptrend, with a pullback low between them. It completes when price closes below that middle low (the confirmation line). A double bottom is the mirror image after a downtrend: two lows at about the same level, completed by a close above the high between them. Before that close, it is just price testing a level twice. The patterns are sometimes called M and W shapes for their appearance.',
    'body': '''<h2>The double top</h2>

    <div class="info-card">
      <h4>Three parts</h4>
      <p><strong>First peak.</strong> An uptrend reaches a high and pulls back.</p>
      <p><strong>Middle low.</strong> The low of that pullback. This is the most important point in the pattern.</p>
      <p><strong>Second peak.</strong> Price rallies back to approximately the first high, fails to break meaningfully above it, and turns down.</p>
    </div>

    <p>The shape looks like the letter M, which is why some traders call it an M pattern. The pattern is completed when price closes below the middle low. That level is often called the confirmation line or the neckline, by analogy with <a href="/chartcheck/blog/head-and-shoulders-pattern/">head and shoulders</a>.</p>

    <h2>The double bottom</h2>

    <p>The same structure inverted, after a downtrend: a first low, a bounce to a middle high, a second low at roughly the same level as the first, and completion on a close above the middle high. It looks like a W.</p>

    <h2>What the pattern records</h2>

    <p>A double top is a story of an uptrend that tried to make a higher high and could not. The second rally reached the same area where sellers appeared the first time, and sellers appeared again.</p>

    <p>But the second peak alone does not change the trend's structure. A failed attempt at a new high is still consistent with a range. What changes the structure is the break of the middle low: now price has made a lower high (or an equal high) and a lower low. That is why the confirmation line, not the second peak, is the event that matters.</p>

    <h2>Why "two touches of a level" is not enough</h2>

    <p>Price returning to a prior high and turning away is completely ordinary. It is what <a href="/chartcheck/blog/support-and-resistance/">resistance</a> means. Most of the time, that is all it is: a level being respected inside a range or a pause inside a trend.</p>

    <p>The difference between "price tested resistance twice" and "double top" is entirely in what happens next. If price breaks the middle low, the double top completed. If price instead consolidates and later breaks above both peaks, the "double top" was a base for continuation. Calling it at the second peak is calling the outcome before it has happened.</p>

    <h2>What makes the pattern more credible</h2>

    <table class="comparison-table">
      <thead>
        <tr><th>Feature</th><th>Why it adds weight</th></tr>
      </thead>
      <tbody>
        <tr class="highlight-row"><td>A clear prior trend</td><td>A reversal pattern needs something to reverse. Two equal highs inside a sideways range are just the top of the range.</td></tr>
        <tr><td>Meaningful separation between the peaks</td><td>Two peaks a few candles apart are one noisy top. Peaks with a substantial pullback between them reflect two separate attempts.</td></tr>
        <tr><td>A clear rejection at the second peak</td><td>Long upper wicks or a strong reversal candle at the second test show the selling was active, not passive.</td></tr>
        <tr><td>Close beyond the confirmation line</td><td>The defining event. A wick through it is a test.</td></tr>
        <tr><td>Higher timeframe</td><td>More participants, more meaningful structure.</td></tr>
      </tbody>
    </table>

    <h2>Equal is approximate</h2>

    <p>The two peaks rarely match exactly. A second peak that slightly overshoots the first - often briefly, with a wick - is common, and many traders still treat it as a double top, sometimes considering the failed overshoot as additional evidence of rejection. A second peak that clearly exceeds the first and holds is a different story: that is a higher high, and the uptrend's structure is intact.</p>

    <p>Where to draw that line is a judgement call, which is one reason to treat the level as a <a href="/chartcheck/blog/support-and-resistance/">zone</a> rather than a precise price.</p>

    <h2>Triple tops and bottoms</h2>

    <p>Three tests of the same level before the break of the swing lows between them. The logic is identical, and the same rule applies: it is a level being respected until the confirmation line breaks. There is a subtlety worth knowing - repeated tests of a level can also wear it down. A level tested many times in quick succession, with smaller and smaller pullbacks each time, sometimes breaks in the direction of the tests rather than reversing.</p>

    <h2>The measured move</h2>

    <p>The conventional estimate takes the height from the peaks to the confirmation line and projects it from the break. It gives a sense of the pattern's scale. It is not a target that price is obliged to reach, and it is worth treating any such projection with real scepticism.</p>

    <h2>A worked example, in words</h2>

    <p>Picture a daily chart where a stock has risen from 60 to 90 over four months. It touches 90, pulls back to 82, rallies again to 89.50 with a long upper wick on the final candle, and starts to fall. The line to watch is 82, the low between the two peaks.</p>

    <p>While price is between 82 and 90, the chart shows a market that tested 90 twice and was turned away twice. That is resistance holding. It is not yet a double top. If price closes below 82, the uptrend has made an equal high and a lower low, and the double top is complete. If price instead finds support above 82 and later closes above 90, the uptrend resumed and the "double top" was a consolidation under resistance that eventually gave way.</p>

    <p>The double bottom version runs the same way upside down: two tests of a floor, and the bounce high between them as the line that has to break.</p>

    <h2>Double top versus head and shoulders</h2>

    <p>The two patterns tell nearly the same story. In a head and shoulders, the second attempt (the head) makes a higher high before the third attempt fails. In a double top, the second attempt simply matches the first. Both are completed by breaking the swing low or lows between the peaks. If you can tell the story of the trend's structure - higher highs failing, then a lower low - the exact pattern name matters much less than people think.</p>

    <h2>Common mistakes</h2>

    <ol>
      <li><strong>Calling it at the second peak.</strong> At that point it is a test of resistance, nothing more.</li>
      <li><strong>Ignoring the prior trend.</strong> Equal highs in a sideways market are a range, not a reversal pattern.</li>
      <li><strong>Peaks too close together.</strong> A few candles apart on a low timeframe is noise around a single top.</li>
      <li><strong>Seeing only one direction.</strong> Double tops and double bottoms are equally common; looking only for the one that matches your view is a bias, not analysis.</li>
    </ol>

    <h2>Reading it from a chart image</h2>

    <p>Two peaks at roughly the same level with a clear trough between them is a distinctive shape, and an AI read of a screenshot can usually identify it, point to the middle low or high as the line to watch, and say whether price has closed through it yet. That last part is the part to pay attention to. A read that names a double top before the confirmation line has broken is describing a possibility, and a good one should say so. It also can only judge the prior trend from what is in the frame, so make sure the screenshot includes the move that led into the pattern, as the <a href="/chartcheck/blog/screenshot-a-chart-for-analysis/">screenshot guide</a> explains.</p>''',
    'faqs': [
        ('What is a double top pattern?',
         'A double top is a bearish reversal pattern made of two peaks at roughly the same level after an uptrend, with a pullback low between them. It is only complete when price closes below that middle low. Before then, it is simply price testing resistance twice.'),
        ('What is a double bottom pattern?',
         'The mirror image: two lows at roughly the same level after a downtrend, with a bounce high between them. It completes when price closes above that middle high, at which point the downtrend\'s structure of lower highs and lower lows has broken.'),
        ('How far apart should the two peaks be?',
         'Far enough to represent two separate attempts, with a meaningful pullback between them. Two peaks a few candles apart on a low timeframe are better described as a single noisy top. There is no fixed distance, but the pattern should be clearly visible as two distinct swings.'),
        ('Is a double top the same as resistance?',
         'Every double top involves resistance, but most resistance tests are not double tops. The difference is what happens after the second test: a double top requires a close below the middle low, which breaks the trend\'s structure. If price holds above it, the level simply did its job as resistance.'),
    ],
    'related': ['head-and-shoulders-pattern', 'support-and-resistance', 'chart-patterns-cheat-sheet'],
})
