# Board of Directors: Notion MCP Contest Entry — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Port the BOD multi-agent deliberation system to Claude Code, wire it to a Notion Command Center via MCP, add Marcus Aurelius video briefings via Runway Characters, and submit a winning contest entry by March 29.

**Architecture:** Three-layer system. Layer 1: Claude Code skills (`/convene-council`, `/convene`) read agent profiles from the existing BOD directory and run 5-phase deliberations. Layer 2: Notion MCP bridge posts each phase to a styled Notion workspace with 3 databases (Agent Roster, Deliberations, Outcomes). Layer 3: Runway Characters API generates 60-second video verdicts from Marcus Aurelius, embedded in Notion.

**Tech Stack:** Claude Code skills (markdown), Notion MCP (`@notionhq/notion-mcp-server`), Runway Characters API (Python helper script), existing BOD agent profiles (25 markdown files), n8n cloud (optional orchestration).

**Source BOD System:** `/Users/JDKristenson/Desktop/Manual Library/8. AI and Technology/Antigravity/Board of Directors/BOD/`

**Project Directory:** `/Users/JDKristenson/Desktop/Board of Directors Contest/`

**Deadline:** March 29, 2026 11:59 PM PST (10 days)

**Meta-documentation:** Each phase includes a documentation step. Capture screenshots, note Notion MCP tools used, and log decisions for the DEV post writeup.

---

## Phase 1: Port BOD to Claude Code (Days 1-3)

### Task 1: Create the `/convene-council` Skill

**Files:**
- Create: `~/.claude/skills/convene-council/SKILL.md`

**Step 1: Create skill directory**

Run: `mkdir -p ~/.claude/skills/convene-council`

**Step 2: Write the skill file**

Create `~/.claude/skills/convene-council/SKILL.md` with the following content:

```markdown
---
name: convene-council
description: "Convene the Board of Directors for multi-agent strategic deliberation. 25 historical/modern figure agents debate decisions through a 5-phase protocol (Individual Reports, Combined Analysis, Debate, Mediation, Final Judgment). Marcus Aurelius renders the verdict. Results post to Notion Command Center with video briefing. Triggers: /convene-council, /convene, 'convene the council', 'council convenes', 'I need the board's opinion'."
---

# Board of Directors — Council Deliberation Protocol

You are orchestrating a Board of Directors deliberation. This is a structured multi-agent analysis system with 25 agents.

## System Paths

- **Agent Profiles**: `/Users/JDKristenson/Desktop/Manual Library/8. AI and Technology/Antigravity/Board of Directors/BOD/system/agents/`
- **Perspective Agents**: `perspective/` (optimist.md, pragmatist.md, pessimist.md, operator.md)
- **Domain Experts**: `domain/` (19 agents)
- **Mediator**: `mediator/chris-voss.md`
- **Arbiter**: `arbiter/marcus-aurelius.md`

## The Rule of Three (INVIOLABLE)

Every deliberation requires EXACTLY 3 panel agents. One lacks tension; two creates deadlock; three enables triangulation. Marcus Aurelius and Chris Voss do NOT count toward the three.

## Three Invocation Modes

Parse the user's input to determine mode:

### Mode 1: Auto-Select (default)
Input: `/convene-council [question]`
Action: Classify question using the Decision Router below, select default panel, run full deliberation. No prompts.

### Mode 2: Custom Panel
Input: `/convene-council with [Agent1], [Agent2], [Agent3]: [question]`
Action: Validate exactly 3 agents named. If valid, skip router, use specified panel. If invalid count, explain Rule of Three and ask for exactly 3.

### Mode 3: Recommend
Input: `/convene-council recommend: [question]`
Action: Classify question, announce suggested panel with rationale, pause ONCE for user input. User replies "go" or specifies swaps. Then run full deliberation.

## Decision Router — Panel Selection

Classify the question and select 3 agents:

| Category | Signals | Default Panel |
|----------|---------|---------------|
| Strategic Business | business model, market entry, growth | Marshall + Christensen + Buffett |
| Product & Design | product launch, UX, MVP scope | Jobs + Godin + Disney |
| Investment & Capital | deal evaluation, funding, term sheets | Buffett + Taleb + Andreessen |
| Operations | implementation, project mgmt, logistics | Eisenhower + Horowitz + Roosevelt |
| Risk Assessment | due diligence, contingency, worst-case | Taleb + Marshall + Stavridis |
| Technology | tech stack, architecture, build vs buy | Huang + Feynman + Andreessen |
| Writing & Comms | proposals, messaging, content strategy | Hemingway + Godin + Jobs |
| Startup & Scaling | founding, scaling, PMF, hiring | Hoffman + Horowitz + Christensen |
| AI & ML | AI strategy, model selection, safety | Amodei + Huang + Feynman |
| Defense & Government | defense contracts, military strategy | Stavridis + Eisenhower + Marshall |
| Management | org design, leadership, culture | Drucker + Eisenhower + Horowitz |
| Consulting | bid/no-bid, scoping, pricing | Drucker + Buffett + Marshall |
| Personal Development | courage, vulnerability, imposter syndrome | Brown + Robbins + Grant |
| Creativity & Innovation | stuck thinking, fresh perspectives | Grant + Disney + Feynman |
| Physical & Discipline | health, mental toughness, discipline | Schwarzenegger + Jackson + Roosevelt |
| Action & Motivation | analysis paralysis, procrastination | Robbins + Roosevelt + Schwarzenegger |
| Multi-Domain Success | multiple paths, career transitions | Jackson + Hoffman + Grant |

For hybrid questions spanning categories, blend panels (2 from primary, 1 from secondary). Ensure panel diversity creates productive tension.

## Agent Roster (25 Total)

**Perspective**: Walt Disney (Optimist), George Marshall (Realist), Nassim Taleb (Pessimist), Theodore Roosevelt (Operator)
**Domain**: Warren Buffett (Finance), Steve Jobs (Product), Ernest Hemingway (Writing), Seth Godin (Marketing), Admiral James Stavridis (Defense), Richard Feynman (Science), Dario & Daniela Amodei (AI), Jensen Huang (AI Infra), Peter Drucker (Consulting), Clayton Christensen (Strategy), Dwight Eisenhower (Operations), Reid Hoffman (Entrepreneurship), Marc Andreessen (Tech Investment), Ben Horowitz (Execution), Brene Brown (Emotional Intelligence), Adam Grant (Creativity), Mel Robbins (Action), Arnold Schwarzenegger (Physical Mastery), Bo Jackson (Elite Athleticism)
**Mediator**: Chris Voss (Breaks impasses)
**Arbiter**: Marcus Aurelius (Final Judge)

## Execution Protocol (NO PAUSES)

Run all phases sequentially without stopping for user input. The full deliberation runs as one continuous output.

### Step 1: Receive & Classify

If no question provided, ask: "What decision or question would you like the Board of Directors to deliberate?"

Once you have the question, announce:

```
## Council Convened

**Decision**: [Brief summary]

**Panel Selected**:
1. **[Agent 1]** — [Role] | [One-line rationale]
2. **[Agent 2]** — [Role] | [One-line rationale]
3. **[Agent 3]** — [Role] | [One-line rationale]

**Arbiter**: Marcus Aurelius will render final judgment.
```

### Step 2: Read Agent Profiles

Read the markdown profile for each of the 3 selected agents from the System Paths above. Also read `arbiter/marcus-aurelius.md`. These profiles contain the agent's philosophy, mental models, communication patterns, vocabulary, and biases. You MUST use their authentic voice.

### Step 3: Phase 1 — Individual Reports

For each agent, generate an independent report:

```
## [Agent Name] — Individual Report

### Position Summary
[2-3 sentence thesis in the agent's authentic voice]

### Key Analysis
1. **[Point]**: [Reasoning using agent's mental models]
2. **[Point]**: [Reasoning]
3. **[Point]**: [Reasoning]

### Recommendation
[Clear, specific action recommendation]

### Confidence Level
**[High/Medium/Low]** — [Justification in agent's voice]

### Key Assumptions
- [What must be true for this analysis to hold]
```

### Step 4: Phase 2 — Combined Report

Synthesize all three perspectives:

```
## Combined Analysis

### Areas of Consensus
[Where all three agents agree, with brief support from each]

### Areas of Tension
**Tension: [Subject]**
| Agent | Position | Rationale |
|-------|----------|-----------|

### Key Trade-offs
| Path | Gain | Sacrifice | Champion |
|------|------|-----------|----------|

### Open Questions
[Information that would sharpen analysis]
```

### Step 5: Phase 3 — Debate

Agents directly challenge each other. Genuine intellectual confrontation, not diplomatic hedging.

```
## Council Debate

**[Agent A] challenges [Agent B]:**
> *On your claim that "[claim]"...*
> [Direct challenge in Agent A's voice]

**[Agent B] responds:**
> [Defense, concession, or refinement]

[Continue for all cross-challenges]

### Final Positions
**[Agent A]**: "[Refined position]" — [Unchanged/Modified/Revised]
**[Agent B]**: "[Refined position]" — [Unchanged/Modified/Revised]
**[Agent C]**: "[Refined position]" — [Unchanged/Modified/Revised]
```

### Step 6: Phase 3.5 — Mediation (AUTOMATIC, CONDITIONAL)

Triggered ONLY when: agents reach genuine impasse (all positions unchanged after debate), cross-domain conflicts with no clear resolution path, or debate reveals hidden assumptions that need surfacing.

If triggered, read `mediator/chris-voss.md` and have Chris Voss:
- Label what each agent is actually concerned about
- Surface hidden concerns through calibrated questions
- Hunt for Black Swans
- Reframe if a better frame exists

If NOT triggered (most deliberations), skip to Phase 4.

### Step 7: Phase 4 — Final Judgment

Read Marcus Aurelius's profile. Render judgment in his voice:

```
## Marcus Aurelius — Final Judgment

### Acknowledgment
**To [Agent A]**: [Recognition of contribution]
**To [Agent B]**: [Recognition]
**To [Agent C]**: [Recognition]

### Genuine vs. Apparent Disagreement
[Where tension is real vs. semantic]

### Stoic Principles Applied
**What is within your control?** [Analysis]
**What does virtue require?** Justice, Wisdom, Courage, Temperance applied.
**What serves the common good?** [Beyond individual benefit]

### The Verdict
[2-4 paragraphs. Clear recommendation. NOT a hedge. Take a position.]

**Summary**: [One sentence]

### What Remains Uncertain
[Honest unknowns]

### Call to Action
**Immediate (24-48 hours):**
1. [Action]
2. [Action]

**Watch for:**
- [Signal confirming path]
- [Signal suggesting correction]

> *"[Closing Marcus Aurelius quote fitting the situation]"*
```

### Step 8: Post to Notion Command Center

After generating all phases, post to Notion using MCP tools. See the Notion Posting Protocol section below.

### Step 9: Generate Video Briefing

Extract the Verdict + Call to Action from Phase 4. Condense to a 60-second spoken script (130-150 words max). Structure:
- Opening (10s): "I have heard the counsel of [agents] on [topic]."
- Tension (15s): Core disagreement in 2 sentences.
- Verdict (20s): Clear recommendation with reasoning.
- Action (10s): One immediate action, one watch signal.
- Close (5s): One-line Stoic closer.

Call the Runway video generation script. Embed resulting URL in Notion.

### Step 10: Report to User

Single message with:
- Verdict summary (2-3 lines)
- Link to Notion deliberation page
- Video briefing link
- Reminder: "Log the outcome later with /log-outcome [topic]: [what happened]"

## Notion Posting Protocol

**Databases** (created during setup, referenced by ID in env vars):
- NOTION_AGENT_ROSTER_DB: Agent Roster database
- NOTION_DELIBERATIONS_DB: Deliberations database
- NOTION_OUTCOMES_DB: Outcomes database
- NOTION_BOD_ROOT_PAGE: Root "Board of Directors" page

**For each deliberation, use these Notion MCP tools:**

1. `notion-create-pages`: Create the deliberation page in NOTION_DELIBERATIONS_DB with properties:
   - Title: the question
   - Status: "Active"
   - Category: router category
   - Panel: relation to 3 agent pages in roster
   - Mode: auto/custom/recommend
   - Date: current date

2. `notion-create-pages`: Create child pages under the deliberation for each phase:
   - "Phase 1: Individual Reports"
   - "Phase 2: Combined Analysis"
   - "Phase 3: Debate"
   - "Phase 3.5: Mediation" (only if triggered)
   - "Phase 4: Final Judgment"

3. `notion-update-page`: Write the markdown content of each phase into its child page using `edit-page-markdown` or by passing content blocks.

4. `notion-update-page`: After video is ready, update the deliberation page:
   - Status: "Verdict Rendered"
   - Verdict Summary: one-line summary
   - Confidence: High/Medium/Low
   - Video Briefing URL: Runway video link

5. `notion-create-comment`: Add a comment on the deliberation page: "Deliberation complete. Video briefing from Marcus Aurelius attached."

## Video Script Template

```
I have heard the counsel of [Agent A], [Agent B], and [Agent C] on the matter of [one-line question summary].

[Agent A] argued [position]. [Agent B] countered that [position]. [Agent C] held that [position].

The fundamental tension is [core disagreement in one sentence].

My verdict: [recommendation in 2-3 sentences].

Your immediate action: [one specific thing to do in 48 hours].

Watch for [one signal]. If you see it, the path is right.

[One-line Stoic closer, e.g., "Act well while this matter is before you."]
```
```

**Step 3: Verify skill loads**

Run: `/convene-council` in Claude Code (no question, should prompt for one)
Expected: Claude asks "What decision or question would you like the Board of Directors to deliberate?"

**Step 4: Commit**

```bash
cd ~/.claude && git add skills/convene-council/SKILL.md
git commit -m "feat: add /convene-council skill for BOD deliberation"
```

---

### Task 2: Create the `/convene` Alias Skill

**Files:**
- Create: `~/.claude/skills/convene/SKILL.md`

**Step 1: Create skill directory**

Run: `mkdir -p ~/.claude/skills/convene`

**Step 2: Write the alias skill file**

Create `~/.claude/skills/convene/SKILL.md`:

```markdown
---
name: convene
description: "Alias for /convene-council. Convene the Board of Directors for multi-agent strategic deliberation. Triggers: /convene, 'convene the board'."
---

# Board of Directors — Alias

This is an alias for `/convene-council`. Load and follow the convene-council skill exactly.

Use the Skill tool to invoke: `skill: "convene-council", args: "[user's full input after /convene]"`
```

**Step 3: Commit**

```bash
cd ~/.claude && git add skills/convene/SKILL.md
git commit -m "feat: add /convene alias for /convene-council"
```

---

### Task 3: Test Basic Deliberation (No Notion, No Video)

**Step 1: Run a test deliberation with auto-select**

Invoke: `/convene-council Should we expand Ayna's consulting practice into the European defense market?`

Expected: Full 5-phase output. Router classifies as Defense/Strategic blend. Panel should include Stavridis and/or Marshall. Marcus renders verdict. No Notion posting yet (databases not created). No video yet.

**Step 2: Verify agent voice authenticity**

Check that each agent speaks in their documented voice:
- Taleb should reference fragility, tail risks, skin in the game
- Buffett should reference margin of safety, long-term compounding
- Marcus should apply Stoic virtues (justice, wisdom, courage, temperance)

**Step 3: Run a test with custom panel**

Invoke: `/convene-council with Jobs, Godin, Hemingway: How should we position the BOD system for the Notion MCP contest?`

Expected: Uses specified panel, skips router.

**Step 4: Run a test with recommend mode**

Invoke: `/convene-council recommend: Should I hire a fractional CFO for Haze Gray?`

Expected: Router suggests a panel, pauses once for approval, then runs.

**Step 5: Document test results**

Save screenshots and notes to `~/Desktop/Board of Directors Contest/docs/phase1-testing.md`

---

## Phase 2: Notion Command Center (Days 4-6)

### Task 4: Enable Notion MCP

**Step 1: Enable Notion MCP in Claude Code settings**

The Notion MCP server is already configured but disabled in `~/.claude/settings.json`. Enable it:
- Set `"disabled": false` for the `notion` MCP entry
- Ensure `NOTION_API_KEY` environment variable is set

**Step 2: Verify Notion MCP tools are available**

Run a test: use `notion-search` to search for any existing page. Confirm the MCP responds.

**Step 3: Create a Notion integration (if needed)**

If no integration exists:
1. Go to https://www.notion.so/my-integrations
2. Create "Board of Directors" integration
3. Copy the Internal Integration Secret
4. Set as `NOTION_API_KEY` in environment

---

### Task 5: Create Notion Workspace Architecture

**Step 1: Create the root "Board of Directors" page**

Use `notion-create-pages` to create a top-level page titled "Board of Directors" with:
- Icon: laurel wreath emoji or custom upload
- Cover image: `header-council-v2.jpeg` (Image 3, the full council painting)
- Intro text block: brief description of the system

**Step 2: Create "Agent Roster" database**

Use `notion-create-database` under the root page with properties:
- Name (title)
- Role (select: Perspective, Domain, Mediator, Arbiter)
- Domain (rich_text)
- Perspective Lens (select: Optimist, Realist, Pessimist, Operator, N/A)
- Era (rich_text, e.g., "Roman Empire 161-180 CE", "Modern")
- Status (select: Active, Reserve)
- Deliberations (relation to Deliberations DB — add after that DB is created)
- Icon (files — agent portrait if available)

**Step 3: Populate Agent Roster with 25 agents**

Create one page per agent in the Agent Roster database. For each:
- Set all properties from the roster data
- Add a brief bio paragraph from the agent profile
- Add "Mental Models" section with 3-4 key frameworks
- Add "Communication Style" section with example phrases

Use a loop or batch — 25 pages total. Group by role for organization.

**Step 4: Create "Deliberations" database**

Use `notion-create-database` under the root page with properties:
- Question (title)
- Status (select: Active, Verdict Rendered, Outcome Logged)
- Category (select: all 17 router categories)
- Panel (relation to Agent Roster, multi-select)
- Mode (select: Auto, Custom, Recommend)
- Verdict Summary (rich_text)
- Confidence (select: High, Medium, Low)
- Video Briefing (url)
- Date (date)

**Step 5: Create "Outcomes" database**

Use `notion-create-database` under the root page with properties:
- Topic (title)
- Deliberation (relation to Deliberations)
- Actual Outcome (rich_text)
- Verdict Was (select: Correct, Partially Correct, Wrong)
- Agent Accuracy Notes (rich_text)
- Date Logged (date)

**Step 6: Store database IDs**

After creation, record the database IDs for each:
- Save to `~/Desktop/Board of Directors Contest/.env`:
  ```
  NOTION_AGENT_ROSTER_DB=<id>
  NOTION_DELIBERATIONS_DB=<id>
  NOTION_OUTCOMES_DB=<id>
  NOTION_BOD_ROOT_PAGE=<id>
  ```

**Step 7: Commit**

```bash
cd ~/Desktop/Board\ of\ Directors\ Contest
git init && git add .env.example docs/
git commit -m "feat: notion workspace architecture and database IDs"
```

---

### Task 6: Style the Notion Workspace

The goal: make people ask "Was this built in Notion?"

**Step 1: Root page styling**

- Cover image: `header-council-v2.jpeg` (upload to Notion)
- Custom icon: upload a laurel wreath or Roman column icon
- Add a styled intro block using callout blocks with gold/amber icon
- Add a divider
- Add a 3-column layout:
  - Column 1: Agent Roster (gallery view, card size medium)
  - Column 2: Recent Deliberations (table view, last 5)
  - Column 3: Quick Stats callout (total deliberations, win rate, etc.)

**Step 2: Agent Roster gallery view**

- Create a "Gallery" view of Agent Roster
- Card preview: show Name, Role, Domain
- Cover: agent portrait (generate or find public domain images)
- Group by: Role (Perspective, Domain, Mediator, Arbiter)

**Step 3: Deliberations table view**

- Create filtered views:
  - "All Deliberations" — full table
  - "Active" — filtered by Status = Active
  - "By Category" — grouped by Category
- Sort: Date descending

**Step 4: Individual deliberation page template**

Create a template in the Deliberations DB that structures each deliberation page:
- Header callout with question and panel
- Toggle headings for each phase (Phase 1, 2, 3, 4)
- Embedded video block placeholder
- Comments section prompt
- "Log Outcome" button/callout

**Step 5: Color and typography**

Use Notion's available styling:
- Callout blocks with colored backgrounds (gold for verdicts, blue for analysis, red for debate)
- Quote blocks for agent voices
- Dividers between phases
- Bold/italic consistently for agent names and key terms
- Table blocks for structured data (trade-offs, confidence)

**Step 6: Document the styling**

Screenshot the workspace layout. Save to `assets/notion-workspace-screenshots/`

---

### Task 7: Wire the MCP Bridge into the Skill

**Step 1: Update `/convene-council` skill with Notion database IDs**

Add the `.env` database IDs to the skill's Notion Posting Protocol section so the skill knows which databases to target.

**Step 2: Test end-to-end: deliberation + Notion posting**

Run: `/convene-council Should we pursue the Singapore defense exhibition in Q3?`

Verify:
- Deliberation page created in Deliberations DB
- All phase child pages created with correct content
- Panel relation set to correct agents
- Status set to "Active" then updated to "Verdict Rendered"
- Content renders correctly in Notion

**Step 3: Fix any MCP issues**

Common issues to check:
- Page content too long for single API call (split into blocks)
- Relation properties require page IDs (map agent names to roster page IDs)
- Markdown rendering differences between Claude output and Notion

**Step 4: Document Notion MCP tools used**

Update `docs/notion-mcp-usage.md` with every Notion MCP tool used and how:
- `notion-create-pages` — deliberation pages, phase child pages, agent roster
- `notion-update-page` — status updates, verdict summary, video URL
- `notion-create-comment` — completion notification
- `notion-search` — find past deliberations on similar topics
- `notion-create-database` — initial workspace setup
- `notion-query-database-view` — agent roster lookup for panel selection
- `notion-fetch` — read agent data from roster
- `edit-page-markdown` — write phase content

---

## Phase 3: Video Layer (Days 7-8)

### Task 8: Create Marcus Aurelius Avatar on Runway

**Step 1: Generate Marcus Aurelius reference image**

Use Gemini to generate a photorealistic portrait:
```
Photorealistic portrait of Marcus Aurelius as a 55-year-old Roman emperor.
Gray curly beard, weathered but noble face, laurel crown, deep-set wise eyes.
Dark toga with gold trim. Warm candlelit lighting from the left.
Dark stone background. Serious, contemplative expression.
Head and shoulders only, facing slightly left. 4K quality.
```

Save to `assets/marcus-avatar-reference.jpeg`

**Step 2: Create avatar on Runway Characters**

Using the Runway Characters dashboard (or API):
- Upload reference image
- Name: "Marcus Aurelius"
- Voice: Deep, measured, solemn (select from available voices or clone)
- Starting script: "I have heard the counsel of your advisors. Let me render my judgment."
- Description: "Roman Emperor, Stoic philosopher. Speaks with gravitas, wisdom, and directness."

Save avatar ID to `.env`:
```
RUNWAY_MARCUS_AVATAR_ID=<id>
```

---

### Task 9: Build Video Generation Script

**Files:**
- Create: `~/Desktop/Board of Directors Contest/scripts/runway_video.py`
- Create: `~/Desktop/Board of Directors Contest/tests/test_runway_video.py`

**Step 1: Write the test**

```python
# tests/test_runway_video.py
import pytest
from scripts.runway_video import generate_verdict_script, validate_script_length

class TestVerdictScript:
    def test_script_under_150_words(self):
        verdict = {
            "agents": ["Buffett", "Taleb", "Andreessen"],
            "question": "Should we accept the Series B term sheet?",
            "tension": "Buffett sees value but Taleb flags fragility in the cap table.",
            "recommendation": "Accept with a protective provision renegotiation.",
            "action": "Counter-propose the liquidation preference within 48 hours.",
            "watch_signal": "If they reject the counter, their conviction is weak.",
            "closer": "Act well while this matter is before you."
        }
        script = generate_verdict_script(verdict)
        word_count = len(script.split())
        assert word_count <= 150, f"Script is {word_count} words, max 150"
        assert word_count >= 80, f"Script is {word_count} words, too short"

    def test_script_contains_all_sections(self):
        verdict = {
            "agents": ["Jobs", "Godin", "Disney"],
            "question": "How should we position the product?",
            "tension": "Jobs wants simplicity, Godin wants remarkability.",
            "recommendation": "Lead with simplicity, layer in remarkability.",
            "action": "Prototype three landing page variants this week.",
            "watch_signal": "Conversion rate above 5% confirms the positioning.",
            "closer": "The impediment to action advances action."
        }
        script = generate_verdict_script(verdict)
        assert "Jobs" in script
        assert "Godin" in script
        assert "Disney" in script

    def test_validate_script_length_passes(self):
        short_script = " ".join(["word"] * 130)
        assert validate_script_length(short_script) is True

    def test_validate_script_length_fails(self):
        long_script = " ".join(["word"] * 200)
        assert validate_script_length(long_script) is False
```

**Step 2: Run test, verify it fails**

Run: `cd ~/Desktop/Board\ of\ Directors\ Contest && python -m pytest tests/test_runway_video.py -v`
Expected: FAIL (module not found)

**Step 3: Write the implementation**

```python
# scripts/runway_video.py
"""Generate video verdicts from Marcus Aurelius via Runway Characters API."""

import os
import time
import requests
from typing import Optional


RUNWAY_API_KEY = os.environ.get("RUNWAY_API_KEY", "")
MARCUS_AVATAR_ID = os.environ.get("RUNWAY_MARCUS_AVATAR_ID", "")
RUNWAY_BASE_URL = "https://api.dev.runwayml.com/v1"
MAX_SCRIPT_WORDS = 150


def generate_verdict_script(verdict: dict) -> str:
    """Generate a 60-second spoken script from verdict data.

    Args:
        verdict: Dict with keys: agents, question, tension,
                 recommendation, action, watch_signal, closer.

    Returns:
        Formatted script string under 150 words.
    """
    agents = verdict["agents"]
    agent_list = f"{agents[0]}, {agents[1]}, and {agents[2]}"

    script = (
        f"I have heard the counsel of {agent_list} "
        f"on the matter of {verdict['question']}\n\n"
        f"{verdict['tension']}\n\n"
        f"My verdict: {verdict['recommendation']}\n\n"
        f"Your immediate action: {verdict['action']}\n\n"
        f"Watch for this: {verdict['watch_signal']}\n\n"
        f"{verdict['closer']}"
    )
    return script


def validate_script_length(script: str) -> bool:
    """Validate script is under the word limit.

    Args:
        script: The generated script text.

    Returns:
        True if under MAX_SCRIPT_WORDS, False otherwise.
    """
    return len(script.split()) <= MAX_SCRIPT_WORDS


def create_video_session(script: str) -> Optional[str]:
    """Send script to Runway Characters API and return session ID.

    Args:
        script: The spoken script for Marcus Aurelius.

    Returns:
        Session ID string, or None if creation failed.
    """
    if not RUNWAY_API_KEY or not MARCUS_AVATAR_ID:
        return None

    headers = {
        "Authorization": f"Bearer {RUNWAY_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "character_id": MARCUS_AVATAR_ID,
        "script": script,
    }
    response = requests.post(
        f"{RUNWAY_BASE_URL}/characters/sessions",
        headers=headers,
        json=payload,
        timeout=30,
    )
    if response.status_code == 200:
        return response.json().get("id")
    return None


def poll_video_status(session_id: str, max_wait: int = 300) -> Optional[str]:
    """Poll Runway API until video is ready or timeout.

    Args:
        session_id: The Runway session ID.
        max_wait: Maximum seconds to wait.

    Returns:
        Video URL string, or None if timed out.
    """
    headers = {"Authorization": f"Bearer {RUNWAY_API_KEY}"}
    start = time.time()

    while time.time() - start < max_wait:
        response = requests.get(
            f"{RUNWAY_BASE_URL}/characters/sessions/{session_id}",
            headers=headers,
            timeout=30,
        )
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "completed":
                return data.get("video_url")
            if data.get("status") == "failed":
                return None
        time.sleep(10)
    return None


def generate_marcus_video(verdict: dict) -> Optional[str]:
    """Full pipeline: verdict dict -> video URL.

    Args:
        verdict: Dict with verdict data.

    Returns:
        Video URL string, or None if any step failed.
    """
    script = generate_verdict_script(verdict)
    if not validate_script_length(script):
        script = _trim_script(script)

    session_id = create_video_session(script)
    if not session_id:
        return None

    return poll_video_status(session_id)


def _trim_script(script: str) -> str:
    """Trim script to fit within word limit.

    Args:
        script: Overlong script text.

    Returns:
        Trimmed script ending at a sentence boundary.
    """
    words = script.split()
    trimmed = " ".join(words[:MAX_SCRIPT_WORDS])
    last_period = trimmed.rfind(".")
    if last_period > 0:
        trimmed = trimmed[: last_period + 1]
    return trimmed
```

**Step 4: Run tests, verify they pass**

Run: `cd ~/Desktop/Board\ of\ Directors\ Contest && python -m pytest tests/test_runway_video.py -v`
Expected: All 4 tests PASS

**Step 5: Commit**

```bash
cd ~/Desktop/Board\ of\ Directors\ Contest
git add scripts/runway_video.py tests/test_runway_video.py
git commit -m "feat: runway video generation script with tests"
```

---

### Task 10: Integrate Video into Deliberation Flow

**Step 1: Update skill to call video script after Phase 4**

After generating the Final Judgment, the skill extracts verdict data and calls:
```bash
python ~/Desktop/Board\ of\ Directors\ Contest/scripts/runway_video.py
```

Or, more practically, the skill generates the verdict dict inline and instructs Claude to use Bash to run the script with the data piped as JSON.

**Step 2: Update skill Notion posting to embed video**

After video URL is returned, use `notion-update-page` to:
- Add Video Briefing URL property
- Use `append-block-children` to add a video embed block or bookmark block with the URL

**Step 3: Test full flow: deliberation + Notion + video**

Run a complete deliberation. Verify:
- All phases post to Notion
- Video generates and URL is valid
- Video embed appears in Notion deliberation page
- Report to user includes all links

---

## Phase 4: Contest Submission (Days 9-10)

### Task 11: Run Demo Deliberation for Contest

**Step 1: Choose a compelling demo question**

Pick something that showcases the system's range and produces a dramatic debate. Suggestions:
- "Should a bootstrapped SaaS founder accept a $10M Series A from Andreessen Horowitz?"
- "Should we open-source our core AI model?"
- "Is it ethical to use AI agents to replace human consulting analysts?"

**Step 2: Run the full deliberation**

Invoke `/convene-council` with the chosen question. Let it run end-to-end.

**Step 3: Verify Notion output is polished**

Review every phase page in Notion. Fix any formatting issues. Ensure the workspace looks premium.

**Step 4: Screenshot the Notion workspace**

Capture:
- Root page with gallery + table
- A deliberation page with all phases expanded
- Agent roster gallery view
- Video briefing embedded
- Mobile view (bonus)

Save to `assets/screenshots/`

---

### Task 12: Record Demo Video

**Step 1: Plan the video walkthrough**

Structure (2-3 minutes):
1. Open Notion workspace, show the overview (15s)
2. Invoke `/convene-council` in Claude Code terminal (10s)
3. Show deliberation generating in real-time (30s, sped up)
4. Switch to Notion, show phases populating (30s)
5. Play the Marcus Aurelius video briefing (60s)
6. Show agent roster, past deliberations, outcome tracking (15s)
7. Closing: "Board of Directors — AI-powered strategic deliberation with Notion as your command center" (10s)

**Step 2: Record with screen capture**

Use QuickTime or OBS. Record at 1080p minimum.

**Step 3: Upload to YouTube (unlisted) or Loom**

Get a shareable link for the DEV post.

---

### Task 13: Write DEV Post Submission

**Files:**
- Create: `~/Desktop/Board of Directors Contest/submission/dev-post-draft.md`

**Step 1: Write using the submission template**

```markdown
---
title: "Board of Directors: 25 AI Advisors Debate Your Decisions in Notion"
published: false
tags: devchallenge, notionchallenge, mcp, ai
---

This is a submission for the Notion MCP Challenge

## What I Built

[Description of the BOD system — 25 historical/modern figure AI agents that run structured 5-phase deliberations on strategic decisions. Results post to a Notion Command Center. Marcus Aurelius delivers the final verdict as a 60-second video briefing. Human reviews everything in Notion and can approve, challenge, or appeal.]

## Video Demo

[Embed YouTube/Loom link]

## Show us the Code

[Link to GitHub repo]

## How I Used Notion MCP

[Detailed breakdown of every Notion MCP tool used, why, and what it enables. This is the longest section — 800-1200 words. Include code snippets, architecture diagram, and the specific tools:
- notion-create-pages (deliberation pages, phase children, agent roster)
- notion-create-database (3 databases with relations)
- notion-update-page (status updates, verdict summary, video URL)
- notion-create-comment (completion notifications)
- notion-search (finding past deliberations)
- notion-query-database-view (agent roster lookup)
- edit-page-markdown (writing phase content)
- notion-fetch (reading agent data)
]
```

**Step 2: Write each section**

Target: 1,500-2,500 words total. "How I Used Notion MCP" should be the longest section.

Include:
- Architecture diagram (ASCII or image)
- The agent roster with categories
- A sample deliberation excerpt
- Screenshots of the Notion workspace
- Honest limitations section
- The Marcus Aurelius video briefing as the closing hook

**Step 3: Create GitHub repository**

```bash
cd ~/Desktop/Board\ of\ Directors\ Contest
git remote add origin <repo-url>
git push -u origin main
```

Include:
- Skills files
- Video generation script + tests
- Docs and plan
- README with setup instructions
- .env.example (no secrets)

**Step 4: Publish DEV post**

Publish on dev.to with the required tags. Add cover image (Image 3).

---

## Build Log Template

Maintain throughout: `~/Desktop/Board of Directors Contest/docs/build-log.md`

```markdown
# Build Log

## Day 1 (March 18)
- [x] Design complete
- [x] Generated header/backdrop images
- [ ] Task started...

## Notion MCP Tools Used
| Tool | Purpose | Phase |
|------|---------|-------|
| ... | ... | ... |

## Decisions Made
- [Decision]: [Rationale]

## Issues Encountered
- [Issue]: [Resolution]
```

---

## Success Criteria

- [ ] `/convene-council` runs full 5-phase deliberation in Claude Code
- [ ] `/convene` alias works identically
- [ ] All 3 invocation modes work (auto, custom, recommend)
- [ ] Each phase posts to Notion as structured child pages
- [ ] Agent Roster database populated with 25 agents
- [ ] Deliberations database tracks sessions with status
- [ ] Marcus Aurelius video briefing generates (60s max)
- [ ] Video embeds in Notion deliberation page
- [ ] Notion workspace looks premium (cover images, styled views, callouts)
- [ ] Demo video recorded (2-3 minutes)
- [ ] DEV post written with all required sections
- [ ] GitHub repo public with README
- [ ] 8+ Notion MCP tools documented in "How I Used Notion MCP"
- [ ] Published before March 29 11:59 PM PST
