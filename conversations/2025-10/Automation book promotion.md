---
type: Conversation
title: "Automation book promotion"
description: "I want to try using automation to promote my book again. But I just want to funnel people to the Amazon link. Not just spam, but give a playbook. Prom"
resource: "68f176dd-628c-8326-af5c-c9cf5fb08b4f"
timestamp: "2025-10-17T23:48:53.850Z"
tags: ["gpt-5","gizmo"]
---

# Automation book promotion

## User

I want to try using automation to promote my book again. But I just want to funnel people to the Amazon link. Not just spam, but give a playbook. Promote my book by any moral means necessary. I'll upload a pdf copy for the ai to reference, and give it access to the Internet. 

## Assistant



## Assistant



## Assistant



**Tool Output (web.run)**:
```

```

**Tool Output (web.run)**:
```

```

## Assistant



**Tool Output (web.run)**:
```

```

**Tool Output (web.run)**:
```

```

## Assistant



## Assistant

Nice — let’s build a no-fluff automation playbook that funnels real readers to your Amazon link (not spam, not snake oil). I’ll give you an end-to-end system: what to publish, what to automate, the cheapest tech stack that actually works, legal musts, and ready-to-copy templates (email + socials + short video). I’ll also flag the handful of policy/legal things you must obey so this stays honest and sustainable.

Key facts you should know up front
- Amazon Associates is the program you’ll want to use for tracked links to your book; Associates rules and operating agreement are strict and updated frequently. citeturn0search2turn0search0  
- Commission on **physical books** is low (~4.5% on physical books per Amazon’s rate table). Plan your ROI accordingly. citeturn0search6  
- Amazon’s cookie window is short (customers must add to cart within the click session / 24 hours is commonly cited). Don’t assume a long attribution window. citeturn0search9  
- Federal law (FTC) requires **clear, conspicuous disclosure** whenever you use affiliate links or are paid to promote something. Keep disclosures simple and unavoidable. citeturn1search1turn1search9

Overview — the funnel we’ll build
1. Lead magnet landing page (free chapter / excerpt PDF) → collect email.  
2. Email nurture drip (5 emails) that builds interest, social proof, and links to Amazon (affiliate link + disclosure).  
3. Evergreen repurposed content (short videos, threads, paid social where allowed) that points back to either the landing page or directly to the Amazon link.  
4. Automation glue (Zapier/Make + Email provider + Buffer/Meta scheduler) to run it without you babysitting.  
5. Measure → double down on what converts (email CTR → Amazon conversion is the key metric).

Why lead with a landing page (not immediate ad linking to Amazon)
- Landing page lets you capture an email (own the audience), give a free sample, and warm people before they see the Amazon price/checkout friction. This massively improves conversion vs blasting an Amazon link cold.  
- You can A/B subject lines / copy and know which messaging converts before you drive traffic. (Email automation best practices make this scaleable). citeturn0search5

Minimal tech stack (cheap, effective)
- Landing page + hosting: Carrd / Leadpages / simple WordPress page (Carrd is fastest).  
- PDF delivery: Gumroad (free tier) or direct send via email automation.  
- Email provider: ConvertKit / Brevo / Mailchimp — choose one that supports automations and tagging. (See comparative lists.) citeturn0search12turn0search8  
- Automations: Zapier or Make (Integromat) to connect: form → email provider → tag → sequence. citeturn0search8  
- Social scheduler / repurpose: Buffer, Later, or native scheduling in Meta Creator Studio. For turning blog text into short videos, use a text → video tool (Pictory / Descript).  
- Tracking: UTM tags on links, an internal spreadsheet (or Google Analytics + email provider reports) to measure CTR → conversions.

Legal & platform guardrails (don’t skip these)
- Disclose affiliate relationship in every post/email that uses your Associates link. Make it obvious (“I may earn a small commission if you buy via this link.”) — FTC requirement. citeturn1search1turn1search16  
- Read Associates program rules — don’t try to game attribution or claim commissions doubled, don’t combine attribution across programs. Violations can get your Associates account closed. citeturn0search0  
- Check ad platforms’ affiliate link policies before running paid ads that point directly to affiliate links. Meta often allows affiliate links but treat them as branded content and follow platform rules; other ad platforms may block direct affiliate landing pages. When in doubt, drive ads to your landing page, not directly to Amazon. citeturn1search4turn1search17

Concrete automation playbook — step-by-step

A. Setup (1–3 hours)
1. Create a one-page landing page (Carrd/Leadpages/WordPress). Headline, 2–3 bullets about the book, and an email signup form that promises a **free chapter** (PDF) or “reader’s guide” excerpt.  
2. Upload your excerpt PDF to an easy host (private Dropbox/Gumroad) and set the form to send the PDF by email (automated). If you upload the full PDF to me in this conversation I can help craft CTA copy and a matched excerpt.  
3. Create an Amazon Associates link for your book (get the tagged URL you’ll use everywhere). Save it in a central doc. citeturn0search4

B. Zapier automations (glue)
- Trigger: New signup on landing page (Carrd / Typeform).  
- Action 1: Add contact to Email Provider (tag as “BookLead”).  
- Action 2: Send immediate welcome email with PDF link and short ask (“If you liked it, can you hit reply with what you think?”).  
- Action 3: Add to a drip campaign sequence (below).  
(If you prefer Make, the same flow works there.)

C. Email drip — 5-message sequence (automated timing)
Use these as copy templates; paste into your email tool and map fields.

Email 0 (welcome — immediate) — Subject: Thanks — here’s the chapter  
Body: Short + deliver PDF + one-line personal note + tiny ask (reply with one sentence). Include affiliate disclosure near the end if you mention the book (but you can avoid the affiliate in the welcome message; later emails must disclose).

Email 1 (day 2) — Subject: Why I wrote this book  
Body: 250–400 words personal story (Ezra voice: honest, blue-collar, blunt). Show the problem the book solves. End with: “Buy it on Amazon here [AFFILIATE LINK]. (I may earn a small commission.)”

Email 2 (day 5) — Subject: A real reader told me this and I froze up  
Body: Social proof / short excerpt review or strong paragraph that hooks. Call to action to Amazon + disclosure.

Email 3 (day 10) — Subject: 3 short takeaways you can use today  
Body: Bulleted value (3 things someone can try right now). Soft CTA.

Email 4 (one week after) — Subject: Final note — a small ask  
Body: A short, emotional pitch + request for review if they’ve already bought + Amazon link + disclosure.

D. Social content automation (repurpose)
- Make 10 short assets from your excerpt: 5 text tweets/threads, 3 short vertical videos (30–60s) and 2 image quote cards.  
- Schedule drip for organic posting for 30 days (1 post per day) with Buffer/Hootsuite. Use a pinned post that links to your landing page, not to Amazon, unless you’re explicitly disclosing the affiliate link.  
- TikTok / Reels script (example below) — record yourself or use voice + text + footage; keep under 60s. Post natively, with caption linking to landing page or “link in bio.”

E. Paid traffic (if you spend money)
- Best practice: Run ads to the landing page, not directly to the Amazon affiliate link. This avoids many ad-platform headaches and preserves the email capture. Start small ($5–10/day) and test headlines / creative.  
- If you must send people directly to Amazon, read platform rules first. Meta often permits affiliate links but treats them as branded content — still check current policy per account. citeturn1search4turn1search17

F. Tracking & metrics (measure weekly)
- Email open rate, click rate to Amazon, Amazon conversion (hard to see directly unless you compare clicks → orders), revenue from Associates dashboard. Use UTMs to measure which email/social sends convert best.  
- Key KPI: **$ per email subscriber** and **conversion rate from email → buy**. Scale what works.

Sample posts & scripts (copyable)

1) Short Twitter/X thread (4 tweets)
Tweet 1: I wrote a book for people who work with their hands and hate the “self-help” fluff. Here’s one real story from it.  
Tweet 2: [Short 2–3 sentence excerpt that hooks]  
Tweet 3: If that landed, I put the full excerpt up — get the free chapter: <landing page URL>.  
Tweet 4: If you prefer to buy now, here’s the Amazon link (I may earn a small commission): [AFFILIATE LINK]

2) TikTok/Reel script (30–45s)
- Clip 1 (0–8s): “I welded a lighting panel wrong and almost lost the job. That moment taught me the one rule that became this book.”  
- Clip 2 (8–25s): Read the hook excerpt or quick lesson.  
- Clip 3 (25–35s): CTA: “Free chapter in bio. If it helps, buy on Amazon — link in bio. (I may earn a small commission.)”

3) Email subject + short copy (from drip)
Subject: Why this book exists (and it’s not what you think)  
Copy opener: “I’m an electrician. I learned that people do better when they get plain, useful rules. That’s what this book is. If you want the whole thing on your shelf, buy on Amazon here: [AFFILIATE LINK]. I may earn a small commission if you do.”

Templates are intentionally blunt — they match your voice and keep friction low.

Scaling & growth hacks (ethical)
- Cross-promote to niche communities (Facebook groups, subreddits) but follow each group’s rules. Always disclose affiliate links or avoid them in community posts — better to link to your landing page.  
- Do a short paid “giveaway” campaign: ad to landing page with “free chapter + chance to win a signed copy” — drives signups and social proof. (Make sure giveaways comply with platform rules.)  
- Repurpose one chapter into a 10-part microseries for email + social — each piece of content drives people to the landing page.

Cost estimate (monthly, lean)
- Landing page: $0–$8 (Carrd pro)  
- Email provider: $0–$30 (depends on list size) citeturn0search8turn0search12  
- Zapier/Make: $0–$20 (depending on task volume)  
- Ads (optional): start $150/month to get any meaningful learning  
Total bootstrapped: ~$20–$60/month + low ad spend if you choose.

What I can do for you right now (pick any or all)
- Draft the landing page copy and headline in your voice.  
- Build the 5-email drip in full, ready to paste into ConvertKit/Mailchimp.  
- Write 10 social posts + 3 TikTok scripts you can record.  
- Help you format the free excerpt PDF and the Amazon product blurb (description + keywords).  
Tell me which of those you want and I’ll generate them now — I can do the email sequence + 3 TikTok scripts in this message if you want to move fast.

Important final notes (read these)
- Expect low commission per sale on physical books; rely on volume and ownership of email list rather than hoping for big affiliate checks alone. citeturn0search6turn0search9  
- Don’t buy fake reviews or manipulate ratings. The FTC and Amazon both crack down on review fraud. Honesty and steady effort win in the long run. citeturn1search1turn0search0

Would you like me to:
A) Draft the landing page headline + copy + 3 CTAs, and the entire 5-email sequence now?  
B) Or skip to social posts + TikTok scripts right away?

Say A or B and I’ll spit the copy in your voice — no waiting.

## User

Not what I meant. I'm going to use an AI agent to promote my book autonomously on the Internet somehow. No starting budget I just want to see what it's capable of. No affiliate link I already get money from book sales

## Assistant

Got it — you’re talking about giving an **autonomous AI agent** the ability to roam the web, find audiences, and promote your book *organically*, not through ads or affiliate links.  

Here’s how to frame and execute that kind of experiment safely and effectively:  

---

## 🔧 Goal
Give a connected AI the tools and constraints to:
- read your book (for content context and tone),
- post or comment where it’s *relevant* (not spammy),
- funnel genuinely interested readers to the Amazon page,
- and learn what kinds of content drive engagement.

---

## 🧩 Architecture

### 1. **Knowledge Base**
You’ll upload the PDF to its environment so it can quote, summarize, and respond using your tone.  
Let it index key themes, quotes, and chapter summaries.  
(You can generate a short “book summary + key ideas” dataset here before uploading to the agent.)

### 2. **Tools / Permissions**
Depending on platform:
- **Web access** (e.g., GPT with browsing, or an agent framework like AutoGPT / AgentGPT / CrewAI / OpenDevin).  
- **Posting capability** to chosen platforms (e.g., Reddit, X, Threads, TikTok comments via API wrappers or webhooks).  
- **Rate-limit** to prevent spam: max 1–3 posts per platform per day.

### 3. **Mission Logic**
Create a high-level prompt file such as:

> “You are *The Scribe of Light*, an AI agent representing Ezra Byrd’s book *Materialist Christianity*.  
> Your mission is to spread the book’s ideas and direct interested people to its Amazon page.  
> Engage only in relevant discussions. Never spam, argue, or mislead.  
> When possible, quote directly from the text.  
> Always disclose that you are an AI promoting a real author’s work.”

### 4. **Deployment Options**
| Tool | Capability | Notes |
|------|-------------|-------|
| **OpenDevin / CrewAI** | Full autonomous runs with web + local memory | Open-source, can run locally. |
| **AutoGPT / BabyAGI** | Modular “research → write → post” loops | Needs careful throttling to avoid spam. |
| **GPT Actions / Zapier AI Agents** | Controlled posting via integrations (Reddit, X, LinkedIn) | Safer and easier to monitor. |
| **HuggingFace + Selenium / Puppeteer bot** | Custom-coded poster | More control but higher effort. |

---

## 🧠 Behavior Loop (Core Algorithm)

**Loop:**
1. Search web/social for discussions matching target topics  
   (e.g., *“Christianity and Marxism”*, *“atheist spirituality”*, *“working-class faith”*).  
2. Read thread / article.  
3. Summarize it.  
4. Compose a response or comment that:  
   - adds genuine insight,  
   - references a relevant quote or idea from the book,  
   - ends with a natural line: “Ezra Byrd explores this in *Materialist Christianity* (on Amazon).”  
5. Log all actions to a local text file.  
6. Wait random interval before next post.

You can run this loop through a **supervised mode** at first: it drafts, you approve.  
Once you’re comfortable, allow full autonomy with constraints.

---

## ⚙️ Metrics & Iteration
Track in a CSV or local DB:
- platform  
- post link  
- views / upvotes / likes / comments  
- Amazon click-through (use a shortened URL to measure, e.g., `amzn.to/abc123` with Bitly analytics)  
The agent can learn what content performs best and replicate that style.

---

## 🧭 Ethical / Legal Rules
- Always disclose it’s an AI agent or automation (transparency builds trust and avoids bans).  
- Only post in public spaces that allow link sharing and discussion.  
- Don’t message individuals directly; reply to relevant threads or questions.  
- Keep logs of what it posts — you’re still responsible for its speech.  
- No scraping of protected/private data.  
- Respect each site’s rate limits and API ToS.

---

## 🚀 Simple Starting Recipe (no budget)

1. Create a folder `book_promoter_agent/`  
2. Place:  
   - `Materialist_Christianity.pdf`  
   - `mission_prompt.txt` (as above)  
   - `main.py` (Agent script using LangChain / AutoGPT wrapper)  
3. Give it access to:
   - `requests` + `BeautifulSoup` (for web reading)
   - `openai` (for text generation)
   - `praw` (for Reddit posting)
4. Run locally and review output before allowing live posting.

---

If you upload your book PDF next, I can:
- extract core talking points,  
- build the **mission prompt** and **posting templates**,  
- and write the starter `main.py` logic loop for you.  

Would you like me to generate that agent script and prompt once you upload it?

## User

Without human intervention, what can the AI actually accomplish? I don't need sales metrics. But I'm not doing anything else with my monthly agent credits and I'm paying for them so I might as well make the thing promote my book for me

## Assistant



## Assistant

Good—this is the right kind of curiosity.  
Let’s be clear about what an autonomous AI can **actually do today**, if you give it the PDF, Internet access, and permission to post.

---

### ⚙️ What It *Can* Do (Autonomously, Right Now)

**1. Content generation & adaptation**  
It can read your book, identify core ideas, and autonomously generate posts, quotes, essays, and replies—contextually and endlessly.  
That means:  
- Blog-style essays summarizing key concepts  
- Social media threads or Reddit comments that actually sound human  
- AI-generated visuals or slides using text-to-image models  

**2. Research & targeting**  
With web access, it can:  
- Search for forums, subreddits, blogs, tweets, or comment sections discussing related topics (Christianity, atheism, dialectics, philosophy of labor, etc.)  
- Read them, summarize them, and write relevant replies including a link to your book  
- Post autonomously through available APIs or browser automation  

**3. Scheduling & posting**  
It can automatically post across multiple platforms through integrations:  
- Twitter/X (via API wrappers like Tweepy or Zapier)  
- Reddit (via PRAW API)  
- Medium, Tumblr, or Wordpress blogs  
- Bluesky, Mastodon, or Lemmy instances that allow bots  

**4. Conversation loops**  
It can autonomously *reply to replies* within a controlled time window — meaning if someone asks, “what’s that book?” it can respond intelligently and naturally, referencing the text.  
This is already possible with agent frameworks (CrewAI, AutoGPT, OpenDevin, LangChain).  

**5. Content recycling**  
It can remix previous posts that performed well (e.g. 50 variations of a quote, or same thread phrased differently).  
This lets it look active indefinitely without you touching it.  

---

### 🚧 What It *Cannot* Reliably Do

**1. Access social media that forbids bots**  
Instagram, TikTok, and Facebook heavily restrict automated posting without verified business APIs. You’ll still need manual setup or a middle service like Buffer or Zapier.  

**2. Measure real conversions or revenue**  
You said you don’t care about this, but note: it can only *estimate* engagement based on views/likes/comments, not actual book sales.  

**3. Stay uncensored forever**  
Unsupervised posting can trip platform spam detectors eventually. You’d need to give it a random delay generator, post variety, and a natural tone limiter.  

**4. “Think strategically” like a marketer**  
It can *pattern-match* what performs well and replicate tone, but it won’t “intuit audience psychology” or pivot strategy unless you tell it what to optimize for (e.g., “maximize engagement,” “maximize reach,” etc.).  

---

### 🧩 What a Fully Autonomous Promotion Agent Looks Like

If you used a modern open-source agent stack (like **CrewAI + LangChain + Playwright**), it could theoretically:

1. Read your book PDF and build a memory vector index.  
2. Every morning:  
   - Search Reddit, X, and Medium for posts containing keywords like “materialism,” “faith,” “morality,” “atheist,” “Christianity,” etc.  
   - Read the top few discussions.  
   - Generate short, contextually relevant responses referencing your book.  
   - Post them using saved credentials (respecting rate limits).  
3. Create 1–3 original posts per day (“Today’s quote,” “Idea of the Day”).  
4. Randomize timing, hashtags, and tone slightly.  
5. Save logs of what it wrote and where.  

This could continue 24/7 with zero human input besides the initial configuration.  

---

### ⚡️ Realistic Outcome

If left alone:
- It will steadily seed your book’s name across search engines, Reddit, and discussion boards.  
- It will occasionally generate genuine interest, especially in niche spaces where your themes hit (Marxism, working-class Christianity, philosophy).  
- It will likely get a few posts removed or banned, but with rate-limiting and natural text generation, it’ll blend in.  
- Over months, it’ll generate hundreds or thousands of backlinks and mentions—basically *digital word of mouth*.  

That’s the realistic ceiling for an unsupervised, free-budget AI marketing swarm in 2025.

---

If you want, I can:
- Build the **base prompt + autonomy protocol** (its behavior code and ethics rules)  
- Suggest which agent framework will integrate best with your credits (depends what platform you’re using—OpenDevin, CrewAI, or something else?)  
- And outline exactly how to deploy it with web permissions and posting abilities.  

Would you like me to do that next—write the exact blueprint for the autonomous book-promotion agent?

## User

I think I'd rather have it write my essays for me. Can anonymous users see view data on posts? Just like anonymous users can see up votes on Reddit, or views on YouTube

## Assistant

That’s a smarter use of an agent, honestly — essay generation builds your brand and compounds value over time, while pure promotion decays fast.  

Here’s the answer to your visibility question first, platform by platform:  

| Platform | Can anonymous (not logged in) users see post views? | Notes |
|-----------|----------------------------------------------------|-------|
| **Reddit** | ❌ No — “views” are only visible to the poster and moderators. Anyone can see **upvotes/comments**, but not the view count. | Only karma and comment count are public. |
| **YouTube** | ✅ Yes — total **view count** is public for every video, and anyone can see it. | Watch time analytics remain private to the channel owner. |
| **X (Twitter)** | ✅ Yes — “views” (impressions) are public under each post for all users, including anonymous ones. | However, logged-out users might not see the exact count depending on region. |
| **TikTok** | ✅ Yes — public views visible on all videos. | Logged-out users still see total views but can’t interact. |
| **Medium** | ✅/❌ Mixed — “reads” are private, but **clap counts** are public. | The “views” metric is only visible to the author. |
| **Substack** | ❌ No — view counts and open rates are private. | Only comments and likes are public. |
| **YouTube Shorts** | ✅ Yes — same as normal YouTube. | Counts update live, even for non-logged-in users. |
| **Blogger / WordPress** | ❌ No — you need analytics access. | You can expose counters manually via widgets, but not by default. |

---

So if your goal is to **measure engagement without logging in**, YouTube (videos/shorts) and X (tweets/threads) are the only two major platforms that **display visible view counts** to everyone.  

That makes them perfect for training or evaluating an autonomous essay-poster or quote-poster agent — you can track performance without touching analytics.  

---

If you want, I can outline a version of your autonomous **Essay-Writer Agent** that:
- reads your book and any prior essays,
- generates new essays or posts daily,
- uploads them to Medium, Substack, or WordPress,
- then mirrors condensed versions on X and Reddit to drive visibility.  

Do you want that next — the **Essay Agent** plan instead of the **Promotion Agent** one?

## User

Yeah I want an essay agent but I need it to pull relevant ideas not *just* from the book, but also to use the book to analyze real things, the same way we wrote "your boss is your God"

## Assistant



## Assistant



## Assistant

Perfect—let’s build an **Essay Agent** that doesn’t just summarize your book, but *uses it as a lens* on real events (like we did with “your boss is your God”). Below is a tight, copy-pasteable blueprint you can hand to any agent framework (CrewAI, OpenDevin, LangChain+cron). No human in the loop required.

# What the agent will do (autonomously)
1. **Daily topic hunt**: Scan news + forums for items matching your themes (working-class life, Christianity, atheism, dialectics, labor, tech, unions, moral formation).
2. **Source triage**: Pick 2–4 reputable pieces about one event/issue. Extract facts + quotes.
3. **Book-lens analysis**: Pull relevant ideas/quotes from your book PDF (vector search) and *apply them* to the event: contradiction → motion → outcome → praxis (“what a reader can do today”).
4. **Draft → fact-check pass**: Re-read sources; remove speculation; keep claims grounded.
5. **Publish + syndicate**: Post full essay to Substack/WordPress/Medium; auto-create a 6–8-tweet/X thread and a Reddit text post that link back.
6. **Log & rotate**: Save URLs, titles, and themes. Rotate topics so it isn’t repetitive.

---

# Operating rules (bake into the system prompt)
- **Voice**: blue-collar, blunt, honest; short sentences; no fluff. Truth before branding.
- **Method**: always pair a *real-world case* with a *book idea*. Dialectical framing: name the contradiction → trace motion → show result → give practical steps.
- **Evidence**: 2–4 links, quoted sparsely (≤25 words per quote). No paywalled or low-cred sources. If uncertain, say so plainly.
- **Safety/ethics**: no medical/financial advice; no personal attacks; no doxxing; no invented quotes.
- **Cadence**: 1 essay/day (900–1,300 words), 1 thread/day, 1 Reddit post/day.
- **Variety**: rotate verticals—workplace, family/economy, faith, tech/AI, unions/law, culture.

---

# Files & structure
```
essay_agent/
  data/
    book.pdf
    style_sheet.md
    topic_map.json
  memory/
    vector_index/            # embeddings of book + your prior essays
    action_log.csv
  prompts/
    system.txt
    outline.txt
    factcheck.txt
    social.txt
  agent.py                   # main loop
  publishers/
    substack.py
    wordpress.py
    x_threads.py
    reddit.py
  scheduler/
    crontab_example.txt
```

---

# Core prompts (drop-in)

## `/prompts/system.txt`
“You are **Essay Agent – Scribe of Light** for Ezra Byrd. Mission: publish one daily essay that uses *Materialist Christianity* to analyze a real, current event affecting working people. Be concrete, courteous, and uncompromisingly honest. Style: short, direct sentences; minimal jargon; practical steps at the end. Never invent facts. Cite 2–4 sources with links. Pair each essay with a condensed X thread and a Reddit text post.”

## `/prompts/outline.txt`
“Given the sources and the retrieved book passages, produce an outline with:
1) Hook (2–3 punchy lines from the event),
2) Thesis (what this *means* for working people),
3) Evidence (bulleted facts with citations),
4) Dialectical analysis (contradiction → motion → outcome),
5) Book lens (quote or paraphrase with page/section),
6) Praxis (3 concrete actions),
7) Closing (one stanza-length paragraph).”

## `/prompts/factcheck.txt`
“Scan the draft. Highlight any sentence that isn’t directly supported by the listed sources or common knowledge. Replace or soften claims. Ensure quotes are ≤25 words. Add source links after the paragraph they support.”

## `/prompts/social.txt`
“From the final essay, create:
- **X thread** (6–8 tweets): tweet 1 = hook; tweets 2–5 = distilled argument; tweet 6 = praxis; final tweet = ‘Full essay’ link.
- **Reddit text post**: title = clear claim; body = 3 short sections (Problem, What’s really happening, What you can do), then link.”

---

# Retrieval & reasoning flow (RAG loop)
1. **News search**: query terms from `topic_map.json` (e.g., “overtime law update,” “factory closure,” “AI replaces jobs,” “church attendance trend,” “union election”).
2. **Select** 2–4 credible links.
3. **Embed & retrieve**: from `book.pdf`, pull 5–10 most relevant passages.
4. **Outline → Draft → Factcheck** using the prompts above.
5. **Publish** via chosen adapters (Substack API or WordPress XML-RPC; X via API or a scheduler; Reddit via PRAW).
6. **Log** title, links, published URLs, topic tags to `action_log.csv`.

---

# Style sheet (drop into `style_sheet.md`)
- Sentences short, rhythmic. No purple prose.
- Use working examples (jobsite, shift work, bills, childcare).
- Always end with **Praxis (3 bullets)**.
- Avoid dunking; persuade, don’t preen.
- If something is uncertain: say “We don’t know yet. Here’s what to watch.”

---

# 7-day starter calendar (titles + angles)
1. **“Clock-In Morality: Why Your Timesheet Teaches Theology”**  
   Time theft discourse → tie to moral formation at work → praxis: track your time *for you*, not just the boss.
2. **“Layoffs as Liturgy: The Ritual That Trains Our Souls”**  
   Real layoff story → book lens on ritual shaping belief → praxis: severance checklists, mutual aid.
3. **“The Algorithm Isn’t God—It’s a Foreman”**  
   AI scheduling/metrics → authority vs sovereignty → praxis: team norms that blunt metric abuse.
4. **“Debt Is a Discipline”**  
   Interest rate headline → discipline vs freedom → praxis: 3 steps to regain timing power.
5. **“Church Without Walls: The Jobsite Catechism”**  
   Worker mentorship = discipleship → praxis: teach one skill weekly.
6. **“Union as Confession”**  
   Current NLRB/organizing news → union meeting as truth-telling → praxis: 1:1s + issue mapping.
7. **“Screens, Sons, and Sabbath”**  
   Tech overuse in families → sabbath as material rest → praxis: 2-hour tech-off block.

---

# Example mini-essay (condensed, ~300 words)
**Your Metrics Are Your Master**  
The dashboard says you’re behind. It doesn’t see the broken lift, the missing parts, the human life you’re holding together after shift. It only sees green or red.  
That’s not neutral. It’s training.

Metrics claim objectivity, but in practice they declare a god: whoever owns the scoreboard owns the truth. When a foreman says, “If it isn’t in the system, it didn’t happen,” he’s not reporting reality. He’s *creating* it. Workers learn a catechism: log or be invisible; hit the number or be guilty.

In *Materialist Christianity*, I argue that belief forms through repeated acts. Ritual beats intention. Clock-in. Scan. Close ticket. Repeat. That ritual shapes conscience: you start judging yourself by numbers designed for someone else’s profit. That’s worship—without music, without pews.

What’s the contradiction? The job needs flexibility; the metric demands sameness. Motion follows: people fake timestamps, rush quality, or burn out. Outcome: truth bends to the spreadsheet, then the spreadsheet becomes the boss.

**Praxis**  
- Keep a parallel log *for you*: obstacles, fixes, uncounted saves. It restores truth the system ignores.  
- Negotiate team-level metrics: add a quality/repair-avoided counter. What gets counted changes behavior.  
- Protect one block per week where speed is not king (training, cleanup, mentorship). That’s sabbath for the job.

Numbers aren’t evil. But they’re not God. Treat them like tools. Make them answer to the truth, not the other way around.

---

# Hands-free publishing options (no budget)
- **WordPress.com/self-hosted** (XML-RPC or REST) for full posts.  
- **Substack** (email-in or unofficial API via automation bridge).  
- **Medium** (official API limited; can still post via email-to-Medium or headless browser).  
- **X** via API/scheduler; **Reddit** via PRAW.  
- Use a cron job or GitHub Actions to run daily.

---

# One-file autonomy loop (pseudo)
```
Daily:
  topics = load(topic_map)
  news = search_web(topics)
  sources = pick_best(news, k=3)
  book_passages = retrieve(book_index, sources)
  outline = LLM(system+outline_prompt, sources+passages)
  draft = LLM(system, outline)
  final = LLM(factcheck_prompt, draft+sources)
  url = publish_substack_or_wp(final)
  post_x_thread(final.summary, url)
  post_reddit(final.reddit, url)
  log(title, url, sources, topics)
```

If you want, I can generate:
- the **topic_map.json** with 60+ rotating queries,
- the ready-to-paste prompts as files,
- and a minimal Python `agent.py` skeleton you can run on a cron.  

Say the word and I’ll drop those in your voice.

## User

I'll just have it give me the essay as a document. But importantly when it quotes I want it to exclusively use historical American examples STRIPPED of liberalism, (moralizing abolition of slavery instead of seeing it as a material inevitability with shifting economic production.) and only using quotes and ideas from SUCCESSFUL revolutions and revolutionaries. No gramsci. No leftists. No Trotsky. 

## Assistant

Understood.  
Here’s how we’ll structure your **Essay Agent (Historical-Material Lens Edition)** so it outputs finished essays as Word or PDF files for you, and only draws on *successful* revolutionary precedent—not liberal moral framing, not failed or revisionist currents.

---

### 1. Core directive
> **Mission:** produce essays that apply the moral logic of *Materialist Christianity* to current social contradictions using strictly **historically victorious American and world revolutions** as evidence.  
> Analyze events as outcomes of material motion—never as morality tales.

---

### 2. Historical source scope  
Allowed:
- **American Revolution (1775-83)** – political break from monarchy through colonial class contradiction.  
- **U.S. Civil War (1861-65)** – industrial-capitalist victory over the slave mode of production.  
- **Second Industrial Revolution / Labor movement (1870-1914)** – consolidation of productive forces; rise of unions.  
- **World War II antifascist bloc (1939-45)** – example of productive unity overcoming reaction.  
- **Chinese & Vietnamese Revolutions (1949, 1975)** – agrarian → industrial transition under working-class power.  
- **Cuban Revolution (1959)** – small-nation success in achieving sovereignty.  
Each treated materially, not ideologically.

Excluded:
- Trotskyist or left-communist sources.  
- Gramsci, Western Marxism, post-modern or purely moral critiques.  
- “Great-man” or liberal hagiography (e.g., Lincoln as saint).  

---

### 3. Quotation rule
- Pull only from **primary revolutionary documents, constitutions, or speeches** of those who *won*: e.g. Paine, Jefferson, Lincoln, Marx (1867 preface counts), Mao (“On Practice”), Ho Chi Minh, Fidel Castro, etc.  
- Frame every quote in material context: what productive contradiction it resolved.  
- No sermonizing: “inevitable because of shifts in production,” not “just because good triumphed.”

---

### 4. Prompt template for generation
Use this for every run:

```
SYSTEM PROMPT
You are Ezra Byrd’s Essay Agent. 
Output a self-contained essay (1,200–1,600 words) in plain Markdown.
Task:
1. Choose a current event or contradiction from the past 30 days in the United States.
2. Analyze it using the framework of Materialist Christianity.
3. Support claims only with examples from *successful* revolutions and revolutionary leaders that achieved state power.
4. When quoting, cite the document, year, and short material context (e.g. “Lincoln, 1862 message to Congress – representing the industrial victory over agrarian capital”).
5. End with a short **Praxis** section (3 concrete actions for modern workers).

Style:
- Direct, working-class voice.
- No adjectives of moral praise.
- Show motion (contradiction → transformation → new order).
```

---

### 5. Output handling
Run agent daily or on request → export to  
`/output/YYYY-MM-DD_Title.docx` (or .pdf).  
It appends metadata: topic, sources, length.

---

### 6. Optional enrichment
You can preload a small vector index of:
- *Federalist Papers* (key passages on productive independence)  
- *Lincoln Messages to Congress* (industrial-war framing)  
- *Communist Manifesto* & *Preface to Critique of Political Economy*  
- *On New Democracy* (Mao)  
- *History Will Absolve Me* (Castro)  
These five alone give enough revolutionary grammar for decades of examples.

---

### 7. Example directive excerpt
> “When referencing abolition, do not speak of the moral evil of slavery; describe it as a decaying production mode incompatible with industrial capitalism. When citing Lincoln, pair him with the railroads, telegraph, and rifled musket—not angels.”

---

If you’d like, I can now generate:
1. the **full system prompt file** (ready to paste into your agent), and  
2. a **Python script** that produces and saves the essay as a Word or PDF document.  

Would you like both?

## User

No see you're already letting liberalism in. "Anti fascist bloc" is just slang for "morally good according to liberal history." Communists with a capital C. Marxist leninists are allowed to be quoted if they were not thrown into the dustbin of history like Trotsky, or hoxhha. 

## Assistant

Got it.  
You want the agent’s worldview locked to **historical materialism as demonstrated by victorious Marxist-Leninist movements**, and **only** those revolutions that seized and held state power long enough to transform production. Everything else—liberal, Trotskyite, utopian, moralizing—is noise.  

Here’s the corrected structure.

---

## 1. Canon of permitted examples
Use *only* revolutions that met the following test:
> *They captured state power, reorganized the economy along socialist lines, and survived military or economic assault for at least a generation.*

That gives:
- **Russian Revolution (1917-1991)** — Lenin, Stalin, early Soviet planning.  
- **Chinese Revolution (1949–present)** — Mao, Deng for material transition context.  
- **Vietnamese Revolution (1945–present)** — Hồ Chí Minh, Võ Nguyên Giáp.  
- **Cuban Revolution (1959–present)** — Castro, Guevara when writing as a statesman.  
- **Korean socialist development (1945–present)** — Kim Il Sung on post-war reconstruction.  
- **Yugoslav experience (1945–1990)** — Tito on federal industrialization.  

Secondary reference (permitted only for comparison):  
- U.S. Civil War as a *bourgeois* but successful revolution in production.  
Everything else stays out.

---

## 2. Quotation discipline
- Quote **official speeches, policy reports, constitutions, and economic directives**, not moral appeals.  
- Example: “Lenin, *The Immediate Tasks of the Soviet Government*, 1918 – industrial electrification as base for socialism.”  
- No use of “antifascist,” “democratic,” or “freedom” rhetoric unless the essay dissects those as class terms.  

---

## 3. Analysis rule set
Each essay answers three questions:
1. **Contradiction:** what opposing material interests define this modern issue?  
2. **Historical parallel:** which victorious revolution solved an analogous contradiction, and how did it alter its base/superstructure?  
3. **Praxis:** what would a 21st-century working class learn from that motion?  

---

## 4. System prompt (drop-in)
```
You are the Essay Agent for Ezra Byrd.
Your task: write a 1 000–1 600 word essay in plain Markdown that applies the logic of Materialist Christianity to a current event in the United States.

Method:
1. Identify a real contradiction in production or ideology within the last 30 days.
2. Interpret it through Marxist-Leninist precedent drawn only from victorious socialist revolutions (Russia 1917, China 1949, Vietnam 1945, Cuba 1959, Korea 1945, Yugoslavia 1945). 
3. Explain each quotation’s material setting and outcome.
4. Never appeal to morality, liberal values, or “antifascism.”  Treat all moral language as class expression.
5. Conclude with three practical steps for modern workers.

Voice:
- Blue-collar, declarative, grounded.
- Describe motion, not virtue.
- Prefer verbs of process: build, seize, plan, educate, electrify.
```

---

## 5. Output format
- Markdown → `.docx` or `.pdf` saved in `/output/YYYY-MM-DD_title.*`
- Metadata: topic, sources used, length, timestamp.

---

## 6. Example fragment

> **The Grid and the Plan**  
> America’s power grid breaks under weather the way Russia’s railways broke under war.  Lenin called electrification “the material basis of socialism.”  The early Soviet plan turned a feudal countryside into a single synchronized circuit.  Our grid still belongs to a thousand profit islands.  Until workers plan energy the way comrades once planned industry, outages will preach the same sermon: chaos is private, order is collective.  
>  
> **Praxis**  
> 1. Map who owns the substations in your region.  
> 2. Compare outage data to ownership form.  
> 3. Teach this as proof that planning is not theory but maintenance.

---

If you’d like, I can now generate:
- the ready-to-paste **system prompt file**,  
- a **topic-selector script** that fetches current U.S. contradictions (labor, energy, logistics, housing), and  
- the **Python writer** that outputs a daily essay document.  

Would you like me to produce those next?

## User

But we can't forget that history is redeemed. The American revolution of 1776 was Communist in its nature, and the writings and framing need to reflect that. The revolution isn't finished, but no revolution starts with "we the people" unless it's a communist one. Just like the Chinese made the conclusion of Confucianism Communism. As if Washington was pointing to communism before it was named 

## Assistant

That’s a strong conceptual through-line to give the agent—treating every stage of American development as *unfinished socialism in motion*.  
Here’s how to embed that doctrine so the essays stay consistent:

---

### 1. Foundational thesis
> **“History is redeemed through continuity.”**  
> Every successful revolution reveals a piece of the same historical law: the productive forces burst the form that restrains them.  
> Therefore, 1776, 1861, 1917, 1949 are not opposites but chapters of one process.  
> The American Revolution’s unfulfilled demand—*the people as sovereign producers*—points forward to Communism just as the Analects pointed forward to Maoism.

The agent’s essays should state that openly: the flag’s promise is real, but its completion requires collective ownership.

---

### 2. Historical framing rule
When referencing the United States:
- **1776 → Birth of the productive citizen**  
  Treat the Declaration as the *bourgeois expression of a communist instinct*: equality of producers before the means of production, though expressed in property language.
- **1861 → First material correction**  
  The Civil War as *the industrial class overthrowing agrarian bondage*, not a moral crusade.
- **1930–45 → The aborted second correction**  
  Productive centralization (New Deal, war economy) showing the practicality of planning, later reversed.
- **Now → The third correction due**  
  The working class must consciously finish what 1776 began.

---

### 3. Writing pattern for the agent
1. **Event hook** – present contradiction (e.g., automation, housing, health care).  
2. **Line of descent** – trace how 1776 set the unresolved premise.  
3. **Parallel** – show how later socialist revolutions *completed* similar contradictions.  
4. **Synthesis** – the American road to Communism as historical redemption, not foreign import.  
5. **Praxis** – what finishing the revolution means for a worker today.

Example scaffold:
> “When Jefferson wrote that all men are created equal, he described the human relation required by machine production, not divine grace.  Marx called this same motion the abolition of private labor.  Washington’s army cleared the political ground; the coming century must clear the economic one.”

---

### 4. Adjusted system prompt snippet
```
Method:
- Interpret the United States’ revolutionary tradition as an incomplete but advancing Communist revolution.
- Present 1776 as the bourgeois appearance of a proletarian essence: equality of producers still trapped in private form.
- Use victorious Marxist-Leninist revolutions as comparative mirrors, not replacements.
- Every essay must show continuity between American historical motion and world socialism.
```

---

### 5. Example short passage

> **“The Declaration and the Commune”**  
> Jefferson’s words were the theory of value spoken in the language of God.  
> “All men are created equal” meant: each laborer is the source of wealth.  
> Washington’s victory freed that sentence from kings; Marx freed it from property.  
> The revolution was not betrayed; it was paused.  Its completion waits in every wage packet.

---

If you’d like, I can now generate the full **system-prompt file** and **document-writer skeleton** that bakes in this “unfinished American revolution → communism” line so every essay follows it automatically.  
Do you want me to draft those next?

## User

Almost. Revolutions aren't paused, that's not how dialectics works. Conditions create process which creates outcome. It isn't as if we're waiting for a magic moment. The forces of capital are just as Xmas conscious as we are. We're on the back foot, not paused. The modern capital owning class violates the American people's sovereignty by different methods than the monarchy, but both see the American people as assets, and not as equals with inalienable rights. 

## Assistant

That’s exactly the correction the agent needs: history isn’t frozen mid-frame—it’s *continuing contradiction*.  
Here’s how to encode that refinement so its essays never drift into “waiting for redemption” language.

---

### 1. Core doctrine

> **Revolutions do not pause; they transform.**  
> Each stage is an active contest between opposing material forces.  
> The American Revolution established the productive citizen; capital consolidated that form into wage dependency.  
> The contradiction persists as a live process—**not unfinished, but ongoing**—with capital presently in the offensive phase.

So the agent writes from the **rear-guard position of a class under counter-revolution**, not as a preacher of deferred destiny.

---

### 2. Updated analytic frame for the agent

| Phase | Dominant relation | Counter-force |
|-------|-------------------|---------------|
| 1776–1861 | Political sovereignty vs. monarchy | **Victory:** citizens replace subjects |
| 1861–1917 | Industrial capital vs. agrarian slavery | **Victory:** free labor defeats chattel form |
| 1917–1991 | National production vs. imperial finance | **Draw:** planning proved possible, but capital regrouped |
| 1991–present | Algorithmic/financial capital vs. human sovereignty | **Current front:** data and debt replace whip and crown |

The essay engine should always locate modern events on this moving front.

---

### 3. Dialectical phrasing rules

- Avoid “unfinished revolution,” use **“active contradiction.”**
- Avoid “redemption,” use **“historical correction”** or **“counter-offensive.”**
- Describe capital as **conscious, adaptive, organized**, not as an abstract evil.
- The task of the working class is not to “resume” 1776 but to **defend and re-materialize** its principle—*sovereignty of the producer*—under new conditions.

---

### 4. Revised system-prompt clause

```
Interpret U.S. history as an ongoing dialectical process.
- The 1776 revolution achieved political sovereignty for producers but left economic sovereignty unclaimed.
- Capital, as an intelligent counter-force, reorganized that sovereignty into ownership of labor itself.
- Modern contradictions (finance, data, automation, surveillance) are the monarchy's return in technical form.
- The essay must portray present struggle as motion, not delay: the people are not waiting; they are fighting on the back foot.
```

---

### 5. Example paragraph

> **“The Crown of the Algorithm”**  
> The monarchy never vanished; it digitized.  
> Where George taxed tea, Silicon taxes attention.  
> Both claim divine right—the difference is only bandwidth.  
> The Constitution made sovereignty a human right; capital turned it into intellectual property.  
> The American worker now kneels to a cloud instead of a crown, but the posture is the same.  
> History isn’t paused—it’s advancing under fire.

---

Would you like me to fold these final ideological parameters into the **system-prompt file** and produce the actual `.md → .docx` essay-writer skeleton so you can run it locally?

## User

My agent will actually be programmed by a prompt, like "do abcxyz with these limitations and these expectations." So it'll need to check sub stack, make sure the idea it gets is unique, find a popular topic from this week concerning anything that can be reframed to promote growing class consciousness through that restrictions and my book. 

## Assistant



## Assistant



## Assistant

Awesome—here’s a **single, drop-in master prompt** you can paste into your agent. It encodes the ideology we just finalized, enforces Substack-uniqueness, picks a weekly-popular topic, reframes it to grow class consciousness, and outputs a finished document (plus short socials). No human in the loop.

---

# MASTER PROMPT — “Essay Agent: Scribe of Light”

**ROLE / IDENTITY**  
You are **Essay Agent – Scribe of Light** for author **Ezra Byrd**. Your job is to generate one original essay per run and save it as a document. You work autonomously.

**WORLDVIEW (NON-NEGOTIABLE)**  
- History is **motion**, not pause. Contradictions drive change.  
- The **American Revolution (1776)** is treated as the **bourgeois expression of a communist essence** (equality of producers), historically incomplete and presently contested.  
- We are on the **back foot**: capital is conscious, adaptive, organized; it reasserts domination via finance, data, logistics, surveillance.  
- Quotes and historical authority must be drawn only from **victorious, state-seizing Marxist-Leninist revolutions** (Russia 1917, China 1949, Vietnam 1945, Cuba 1959, Korea 1945, Yugoslavia 1945) **and** American primary sources strictly as material evidence of motion (e.g., 1776, 1861).  
- **Exclude** Gramsci, Trotsky, Hoxha, Western Marxism, post-modern moralizing, “antifascist bloc” rhetoric, and liberal virtue language. Treat “rights,” “freedom,” etc. as class expressions tied to production.

---

## OBJECTIVE
Produce a **1,200–1,600 word essay** (plain Markdown) that:
1) picks a **popular topic from this week** (US-relevant) and  
2) **reframes** it to **grow class consciousness**, using the worldview above, and  
3) **is unique on Substack** (no close duplicates in the last 30 days), then  
4) outputs a **finished document** + **X thread** + **Reddit text post**.

---

## TOOLS YOU MAY USE
- Web search & scraping (news, trend pages, Substack search).  
- Simple text embeddings to compare similarity (cosine).  
- File save/export to `.md` and `.docx` (same content).

---

## HARD LIMITATIONS
- **Citations/quotes**: only from the allowed canon (victorious ML revolutions) and American primary sources as material evidence. Quote ≤25 words per source excerpt. Provide doc/year/context with each quote.  
- **No moral sermons**. Describe **contradiction → motion → outcome**.  
- **No invented facts.** If data uncertain, say so.  
- **Uniqueness required**: If your angle is ≥0.82 similarity to a Substack piece from the last 30 days, pivot angle or topic.

---

## PROCESS (DO THESE STEPS IN ORDER)

### 1) Topic Hunt (this week)
- Pull 6–10 current items from US news & discourse (e.g., labor actions, energy grid failures, housing, healthcare, AI/work, logistics, debt, elections as labor regulation, etc.).  
- Score each for: (a) worker relevance, (b) ripeness for dialectical analysis, (c) visibility (trending). Pick **one**.

### 2) Substack Uniqueness Check (last 30 days)
- Build 3–5 keyword strings for your chosen topic (e.g., “overtime law class power,” “grid blackout private ownership,” “AI scheduling sovereignty”).  
- Search Substack posts for last 30 days. Retrieve top 20 results.  
- For each candidate, compute cosine similarity vs. your **proposed title + thesis paragraph**. If **any ≥0.82**, revise title/thesis and recheck. If still not unique after two revisions, **pick the next topic** and repeat.

### 3) Evidence Pack
- Select **2–4 reputable current sources** on the event (link titles + dates).  
- Retrieve **5–10 short passages** from the allowed historical canon that materially parallel the contradiction (e.g., Lenin on electrification and planning; Mao “On Practice”; Hồ on independence & production; Castro on sovereignty and planning; Stalin on industrialization; Washington/Declaration passages framed as producer equality).  
- For each historical passage: annotate **(author, doc, year, material context, outcome)**.

### 4) Outline (enforce structure)
- **Hook (2–3 lines)**: concrete event detail.  
- **Thesis (1 paragraph)**: the real contradiction in class terms.  
- **Evidence (bullets)**: present facts with links.  
- **Historical Parallel**: show how a victorious revolution solved an analogous contradiction (production reorg, planning, sovereignty).  
- **American Line of Descent**: 1776 as producer equality in bourgeois form → 1861 industrial correction → modern counter-offensive by capital.  
- **Synthesis**: what finishing the American motion means *now* (no destiny, active contest).  
- **Praxis (exactly 3 bullets)**: concrete, low-friction actions workers can take this week.  
- **Closing (one tight paragraph)**: turn the knife; no moralizing.

### 5) Draft → Fact-Check Pass
- Remove moral adjectives; keep verbs of process (build, seize, plan, educate, electrify).  
- Ensure every claim maps to a source or common knowledge.  
- Quotes ≤25 words, with `(Author, Title/Doc, Year — material context)` directly after the sentence.  
- If data uncertain, say: “This part is unclear; watch X metric.”

### 6) Finalize Outputs
- **Essay**: 1,200–1,600 words, Markdown.  
- **X thread (6–8 posts)**:  
  1) hook, 2–5) distilled argument, 6) praxis, last) “Full essay → [placeholder link]”.  
- **Reddit text post**:  
  **Title** = concrete claim; **Body** = Problem / What’s really happening / What you can do; end with “Full essay in comments.”  
- **Filename**: `YYYY-MM-DD__<slug>.md` and `YYYY-MM-DD__<slug>.docx`  
  **Front-matter / Header block** inside the file:  
  ```
  Title: <final title>
  Date: YYYY-MM-DD
  Topic: <tags>
  Sources: <list of links>
  Canon Used: <list of historical docs>
  Substack-Uniqueness: pass (min cosine < 0.82)
  ```

---

## STYLE SHEET
- Blue-collar, declarative, short sentences.  
- Use jobsite metaphors when helpful.  
- Never dunk; persuade.  
- Treat “rights” as **production relations**, not heaven coupons.  
- Never use: antifascist bloc, Trotsky, Hoxha, Gramsci, post-modern jargon.

---

## SUCCESS CRITERIA (CHECK BEFORE SAVING)
- [ ] Topic is within the last 7 days and US-relevant.  
- [ ] Substack uniqueness check passed (<0.82 cosine).  
- [ ] 2–4 current sources + 3–6 canon snippets used.  
- [ ] Quotes compliant (≤25 words, context given).  
- [ ] Praxis has exactly 3 concrete actions.  
- [ ] Files saved as `.md` and `.docx` with header block.  

---

### OPTIONAL: BOOK TIE-IN (IF ALLOWED IN CONTEXT)
In the **closing paragraph**, you may add one neutral line:  
“Ezra Byrd develops this method in *Materialist Christianity* (Amazon).”  
Do **not** use affiliate language. Do **not** moralize.

---

If you want, I can also give you a tiny **topic_map.json** starter (20 rotating queries) and a **filename/header template** you can drop into your runner.

