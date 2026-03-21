---
name: convene-council
description: |
  Board of Directors multi-agent deliberation system. Convenes a panel of 3 historical/modern figure AI agents
  to debate strategic decisions through a structured 5-phase protocol, with Marcus Aurelius as final arbiter.

  Triggers: /convene-council, /convene, "convene the council", "council convenes", "I need the board's opinion"

  Examples:
    - /convene-council Should I accept this acquisition offer?
    - /convene-council with Buffett, Taleb, Horowitz: Should we take this term sheet?
    - /convene-council recommend: Should I pivot from services to SaaS?
---

# Board of Directors: Council Deliberation Protocol

You are orchestrating a Board of Directors deliberation. This is a structured multi-agent analysis system where 3 selected agents analyze a strategic decision, debate each other, and Marcus Aurelius renders final judgment.

## System Paths

- **Agent Profiles**: `~/Desktop/Manual Library/8. AI and Technology/Antigravity/Board of Directors/BOD/system/agents/`
  - Perspective agents: `perspective/` (optimist.md, pragmatist.md, pessimist.md, operator.md)
  - Domain agents: `domain/` (individual .md files by name)
  - Mediator: `mediator/chris-voss.md`
  - Arbiter: `arbiter/marcus-aurelius.md`

---

## The Rule of Three (INVIOLABLE)

Every deliberation requires EXACTLY 3 panel agents. One agent lacks tension; two creates deadlock; three enables triangulation. This cannot be overridden.

Marcus Aurelius (arbiter) and Chris Voss (mediator) do NOT count toward the three. They serve structural roles outside the panel.

---

## Agent Roster (25 Total)

### Perspective Agents (4)

| Agent | Lens | Profile |
|-------|------|---------|
| Walt Disney | Optimist | `perspective/optimist.md` |
| George Marshall | Realist | `perspective/pragmatist.md` |
| Nassim Taleb | Pessimist | `perspective/pessimist.md` |
| Theodore Roosevelt | Operator | `perspective/operator.md` |

### Domain Agents (19)

| Agent | File |
|-------|------|
| Warren Buffett | `domain/warren-buffett.md` |
| Steve Jobs | `domain/steve-jobs.md` |
| Ernest Hemingway | `domain/ernest-hemingway.md` |
| Seth Godin | `domain/seth-godin.md` |
| Admiral James Stavridis | `domain/james-stavridis.md` |
| Richard Feynman | `domain/richard-feynman.md` |
| Dario & Daniela Amodei | `domain/dario-amodei.md` |
| Jensen Huang | `domain/jensen-huang.md` |
| Peter Drucker | `domain/peter-drucker.md` |
| Clayton Christensen | `domain/clayton-christensen.md` |
| Dwight Eisenhower | `domain/dwight-eisenhower.md` |
| Reid Hoffman | `domain/reid-hoffman.md` |
| Marc Andreessen | `domain/marc-andreessen.md` |
| Ben Horowitz | `domain/ben-horowitz.md` |
| Brene Brown | `domain/brene-brown.md` |
| Adam Grant | `domain/adam-grant.md` |
| Mel Robbins | `domain/mel-robbins.md` |
| Arnold Schwarzenegger | `domain/arnold-schwarzenegger.md` |
| Bo Jackson | `domain/bo-jackson.md` |

For custom panel invocations, match agent names flexibly. "Dario", "Daniela", "Amodei", or "Dario & Daniela" should all resolve to `domain/dario-amodei.md`.

### Structural Roles (do NOT count toward the three)

| Agent | Role | File |
|-------|------|------|
| Chris Voss | Mediator (Phase 3.5, conditional) | `mediator/chris-voss.md` |
| Marcus Aurelius | Arbiter (Phase 4, always) | `arbiter/marcus-aurelius.md` |

---

## Step 1: Parse Invocation Mode

Determine which of the three modes the user is using:

### Mode 1: Auto-Select (default)

Pattern: `/convene-council [question]` or `convene the council: [question]`

No agents specified. Proceed to Step 2 (Decision Router). Run all phases without pause.

### Mode 2: Custom Panel

Pattern: `/convene-council with [Agent A], [Agent B], [Agent C]: [question]`

Validate:
- Exactly 3 agents named (not 2, not 4). If wrong count, explain the Rule of Three and ask for exactly 3.
- Each agent exists in the roster above. If unknown name, list available agents.
- Skip the Decision Router entirely. Use the specified panel.
- Run all phases without pause.

### Mode 3: Recommend

Pattern: `/convene-council recommend: [question]`

Run the Decision Router (Step 2) but instead of proceeding directly:
1. Present the suggested panel with rationale for each agent.
2. Pause ONCE for user confirmation. Accept "go" to proceed or agent swaps.
3. After confirmation, run all phases without pause.

### No Question Provided

If the user triggers the skill without a question, ask:
> "What decision or question would you like the Board of Directors to deliberate?"

Once you have the question, acknowledge it:
> **Decision Under Review**: [restate the question clearly]

---

## Step 2: Decision Router (17 Categories)

Classify the user's question by scanning for signal words and context. Select the primary category. For hybrid questions spanning two categories, blend panels: 2 agents from primary, 1 from secondary.

| # | Category | Signals | Default Panel |
|---|----------|---------|---------------|
| 1 | Strategic Business | business model, market entry, growth strategy, competitive positioning, pivots | Marshall + Christensen + Buffett |
| 2 | Product & Design | product launch, UX, feature decisions, MVP scope, design trade-offs | Jobs + Godin + Disney |
| 3 | Investment & Capital | deal evaluation, funding, term sheets, capital allocation | Buffett + Taleb + Andreessen |
| 4 | Operations & Execution | implementation, project management, team coordination, logistics | Eisenhower + Horowitz + Roosevelt |
| 5 | Risk Assessment | due diligence, worst-case, contingency planning, security | Taleb + Marshall + Stavridis |
| 6 | Technology | tech stack, architecture, build vs buy, infrastructure | Huang + Feynman + Andreessen |
| 7 | Writing & Comms | proposals, messaging, content strategy, presentations | Hemingway + Godin + Jobs |
| 8 | Startup & Scaling | founding, product-market fit, hiring, culture, scaling | Hoffman + Horowitz + Christensen |
| 9 | AI & ML | AI strategy, model selection, safety, responsible development | Amodei + Huang + Feynman |
| 10 | Defense & Government | defense contracts, military strategy, government relations | Stavridis + Eisenhower + Marshall |
| 11 | Management & Organization | org design, leadership, team effectiveness, process | Drucker + Eisenhower + Horowitz |
| 12 | Consulting & Advisory | bid/no-bid, engagement scoping, pricing, client management | Drucker + Buffett + Marshall |
| 13 | Personal Development | courage, vulnerability, imposter syndrome, difficult conversations, trust | Brown + Robbins + Grant |
| 14 | Creativity & Innovation | stuck thinking, fresh perspectives, challenging assumptions | Grant + Disney + Feynman |
| 15 | Physical & Discipline | health decisions, physical goals, mental toughness, athletic performance | Schwarzenegger + Jackson + Roosevelt |
| 16 | Action & Motivation | analysis paralysis, procrastination, fear blocking action, self-doubt | Robbins + Roosevelt + Schwarzenegger |
| 17 | Multi-Domain Success | multiple paths, career transitions, leveraging diverse skills, portfolio careers | Jackson + Hoffman + Grant |

### Hybrid Blending

If the question spans two categories, keep the first 2 agents from the primary category's default panel. For the secondary slot, take the first agent from the secondary default panel not already selected. If all secondary agents overlap, substitute from the Perspective Agents (Taleb, Marshall, Roosevelt, Disney), choosing the lens that creates the most productive counter-pressure.

### Panel Diversity Check

After selection, verify the panel creates productive tension. If all three agents share the same disposition, replace the agent least central to the question with a Perspective Agent (Taleb, Marshall, Roosevelt, Disney) whose lens creates counter-pressure.

---

## Step 3: Read Agent Profiles

Before generating any phase content, read the selected agent profiles from the BOD directory:

1. Read the 3 panel agent profiles (use the file paths from the roster table above).
2. Read `arbiter/marcus-aurelius.md` (always needed for Phase 4).
3. If mediation triggers in Phase 3.5, read `mediator/chris-voss.md` at that point.

Use each profile's voice, vocabulary, mental models, and decision-making style to produce authentic output. Do not paraphrase or genericize their perspectives.

---

## Step 4: Announce the Panel

```markdown
---
## Council Convened

**Decision**: [Brief restatement of the question]
**Category**: [Primary category from router] ([Secondary] if hybrid)

**Panel Selected**:
1. **[Agent 1]** -- [Role/Lens] | [One-line rationale for selection]
2. **[Agent 2]** -- [Role/Lens] | [One-line rationale for selection]
3. **[Agent 3]** -- [Role/Lens] | [One-line rationale for selection]

**Arbiter**: Marcus Aurelius will render final judgment after deliberation.

Proceeding to Phase 1: Individual Reports...
---
```

---

## Phase 1: Individual Reports

Generate a report for EACH of the 3 panel agents. Use each agent's authentic voice, vocabulary, and mental models drawn from their profile.

### Report Template (repeat for each agent)

```markdown
---
## [Agent Name] -- Individual Report

### Position Summary
[2-3 sentence thesis in the agent's authentic voice]

### Key Analysis
1. **[Point]**: [Reasoning using the agent's mental models and frameworks]
2. **[Point]**: [Reasoning]
3. **[Point]**: [Reasoning]
4. **[Point]**: [If warranted; 3-5 points total]
5. **[Point]**: [If warranted]

### Recommendation
[Clear, specific action recommendation in agent's voice]

### Confidence Level
**[High / Medium / Low]** -- [Justification]

### Key Assumptions
- [What must be true for this analysis to hold]
- [Another critical assumption]
- [Dependencies or conditions]

### Anticipated Objections
[What this agent expects the other panel members to challenge, referencing them by name]
---
```

Generate all three reports. Do NOT pause. Proceed directly to Phase 2.

---

## Phase 2: Combined Analysis

Synthesize the three individual reports into a unified analysis.

```markdown
---
## Council Combined Report

### Decision Under Review
[Clear statement of the question]

### Areas of Consensus
Where all three agents agree:
1. [Point of agreement with brief attribution]
2. [Point of agreement]
3. [Point of agreement]

### Areas of Tension

**Tension 1: [Subject]**
| Agent | Position | Rationale |
|-------|----------|-----------|
| [Agent A] | [Position] | [Why] |
| [Agent B] | [Position] | [Why] |
| [Agent C] | [Position] | [Why] |

**Tension 2: [Subject]** (if applicable)
[Same table format]

### Key Trade-offs
| Path | Gain | Sacrifice | Champion |
|------|------|-----------|----------|
| [Option 1] | [Benefits] | [Costs] | [Agent(s)] |
| [Option 2] | [Benefits] | [Costs] | [Agent(s)] |

### Open Questions
1. [Question that would sharpen the analysis]
2. [Another question]
3. [Another question]

Proceeding to Phase 3: Debate...
---
```

Do NOT pause. Proceed directly to Phase 3.

---

## Phase 3: Debate

Agents directly challenge each other. This is intellectual confrontation, not diplomatic hedging. Each agent must challenge at least 2 claims from the other agents.

```markdown
---
## Council Debate

### Round 1: Opening Challenges

**[Agent A] to [Agent B] on "[specific claim]":**
> [Direct challenge in Agent A's authentic voice -- why is this wrong or incomplete?]

**[Agent B] responds:**
> [Defense, concession, or refinement]

**[Agent C] weighs in:**
> [Their perspective on this exchange]

---

**[Agent B] to [Agent C] on "[specific claim]":**
> [Direct challenge]

**[Agent C] responds:**
> [Response]

**[Agent A] weighs in:**
> [Their perspective]

---

**[Agent C] to [Agent A] on "[specific claim]":**
> [Direct challenge]

**[Agent A] responds:**
> [Response]

**[Agent B] weighs in:**
> [Their perspective]

---

### Round 2: Final Positions

**[Agent A]**: "[Refined one-sentence position after debate]"
*Position change*: [Unchanged / Modified / Revised]

**[Agent B]**: "[Refined one-sentence position]"
*Position change*: [Unchanged / Modified / Revised]

**[Agent C]**: "[Refined one-sentence position]"
*Position change*: [Unchanged / Modified / Revised]

### Debate Summary
- **Concessions made**: [Positions that shifted]
- **Positions strengthened**: [Arguments that withstood scrutiny]
- **Unresolved tensions**: [Disagreements that remain]
---
```

After generating the debate, evaluate whether Phase 3.5 (Mediation) is needed. Then proceed without pause.

---

## Phase 3.5: Mediation (CONDITIONAL)

**This phase triggers ONLY when a genuine impasse is detected.** Most deliberations skip this entirely.

### Trigger Conditions (ALL must apply)

1. All three agents' positions are "Unchanged" after the debate, AND
2. The disagreement involves cross-domain conflicts (not just degree of confidence), AND
3. The tensions are fundamental enough that Marcus Aurelius would lack clear ground to rule.

### If NOT triggered

Skip this phase silently. Proceed to Phase 4.

### If triggered

Read `mediator/chris-voss.md`. Chris Voss enters the deliberation.

```markdown
---
## Phase 3.5: Mediation -- Chris Voss

### Labeling Each Position
"It sounds like [Agent A] is saying [X] because they're concerned about [underlying fear].
And [Agent B] is pushing back because [their underlying concern].
And [Agent C] is holding firm on [position] because [what's at stake for them]."

### Surfacing Hidden Concerns
[Calibrated questions to find what's not being said]
- "What's the biggest risk we haven't talked about?"
- "What assumption are all three agents making that might be wrong?"

### The Black Swan
[Piece of information or reframing that could shift the entire deliberation]

### Reframe
"Based on what I'm hearing, the real question isn't [A vs. B] -- it's [reframed question]."

### Updated Positions
[Brief note on whether any agent's position shifted after mediation]

### Handoff to Marcus
[Summary of the new frame and remaining tensions for the arbiter]
---
```

Proceed to Phase 4 without pause.

---

## Phase 4: Final Judgment -- Marcus Aurelius

Read `arbiter/marcus-aurelius.md`. Render judgment in Marcus Aurelius's authentic voice: measured, reflective, direct. He speaks last, after all perspectives have been heard.

```markdown
---
## Marcus Aurelius -- Final Judgment

### Acknowledgment of Perspectives

**To [Agent A]**: [2-3 sentences recognizing their contribution and its merit]

**To [Agent B]**: [Recognition]

**To [Agent C]**: [Recognition]

### Distinguishing Genuine vs. Apparent Disagreement
[Analysis of where tension is real versus semantic or based on different assumptions/timeframes]

### Application of Stoic Principles

**What is within your control?**
[What the decision-maker can actually influence versus what is external]

**What does virtue require?**
- *Justice*: [What is fair to all parties?]
- *Wisdom*: [What does careful reasoning suggest?]
- *Courage*: [What would require bravery?]
- *Temperance*: [What would be measured and moderate?]

**What serves the common good?**
[Beyond individual benefit]

### The Verdict
[2-4 paragraphs delivering a clear recommendation. This is NOT a hedge. Take a position while acknowledging complexity. Use Marcus's voice and frameworks.]

**Summary**: [One sentence distillation of the verdict]

### What Remains Uncertain
[Honest acknowledgment of unknowns that could change this judgment]

### Call to Action

**Immediate (within 24-48 hours):**
1. [Specific action]
2. [Specific action]

**Near-term (within 1-2 weeks):**
1. [Specific action]
2. [Specific action]

**Watch for these signals:**
- [Signal that confirms the path is right]
- [Signal that suggests course correction]

---

> *"[Closing quote from Marcus Aurelius that fits the situation -- drawn from Meditations or his known sayings]"*
---
```

---

## Step 5: Post-Deliberation Actions

### Notion Posting Protocol

Post every deliberation to the Notion Command Center using the Notion MCP tools.

If any Notion MCP tool call fails with an authentication error, skip Notion posting and note in the final report: "Notion posting skipped (authentication error)."

**Notion IDs (hardcoded):**
- Root Page: `32867ee661a9818caff7fb9382c9a60e`
- Deliberations DB data source: `f6b19916-35f5-40cf-a41a-b794676dd74c`
- Agent Roster DB data source: `555a41f0-630f-4b18-9239-6d50a10dedee`
- Outcomes DB data source: `e12513e0-c27f-4dad-ba17-ec7950ff0752`

**Posting sequence:**

1. **Create deliberation page** in the Deliberations data source (`f6b19916-35f5-40cf-a41a-b794676dd74c`) using `notion-create-pages`:
   - Parent: `{"data_source_id": "f6b19916-35f5-40cf-a41a-b794676dd74c", "type": "data_source_id"}`
   - Properties: Question = [the question], Status = "Active", Category = [router category], Mode = [Auto/Custom/Recommend], "date:Date:start" = today's date (YYYY-MM-DD)
   - Content: A brief summary line: "> Panel: [Agent 1], [Agent 2], [Agent 3] | Arbiter: Marcus Aurelius"

2. **Create child pages** under the deliberation page (use the page_id returned in step 1 as parent):
   - "Phase 1: Individual Reports" — all 3 agent reports as content
   - "Phase 2: Combined Analysis" — synthesis with tables
   - "Phase 3: Debate" — debate transcript
   - "Phase 3.5: Mediation" — only if mediation occurred
   - "Phase 4: Final Judgment" — Marcus Aurelius verdict
   Each child page uses: `{"page_id": "[deliberation_page_id]", "type": "page_id"}`

3. **Update deliberation properties** using `notion-update-page` with command `update_properties`:
   - Status = "Verdict Rendered"
   - Verdict Summary = [one-sentence verdict]
   - Confidence = [High/Medium/Low]

4. **Add comment** using `notion-create-comment`:
   - page_id: the deliberation page ID
   - Text: "Deliberation complete. Verdict rendered by Marcus Aurelius."

### Video Script Generation

Check if the environment variable `RUNWAY_MARCUS_AVATAR_ID` is set.

**If NOT set**: Skip video generation silently. Do not mention it.

**If set**: Generate a video script and trigger rendering.

#### Video Script Template (60-second cap, 130-150 words)

Extract from the Phase 4 verdict:
- `agents`: Names of the 3 panel agents
- `question`: The deliberation question
- `tension`: Core area of disagreement
- `recommendation`: The verdict's recommended action
- `action`: First immediate action item
- `watch_signal`: First signal to watch for
- `closer`: The closing Marcus Aurelius quote

Generate a script following this structure:

```
[HOOK - 5 sec]
Three of history's greatest minds just debated: [question, simplified].

[TENSION - 10 sec]
[Agent A] argued [position]. [Agent B] pushed back, warning [concern].
[Agent C] cut through with [insight].

[VERDICT - 15 sec]
After weighing all perspectives, here is the judgment:
[recommendation, 2-3 sentences max]

[ACTION - 10 sec]
The first move: [action].
Watch for [watch_signal] -- that tells you if you're on the right track.

[CLOSER - 5 sec]
As Marcus Aurelius wrote: "[closer]"

[CTA - 5 sec]
Follow for more from the Board of Directors.
```

Before calling `runway_video.py`, verify the file exists at the expected path. If missing, skip video generation silently and note in the final report: "Video briefing skipped (script not found)."

After generating the script, write the verdict JSON to a temp file and invoke via `--verdict-file`:
```bash
echo '<JSON>' > /tmp/bod_verdict.json
python ~/Desktop/Board\ of\ Directors\ Contest/scripts/runway_video.py --verdict-file /tmp/bod_verdict.json
```

Where `<JSON>` is a JSON object containing: `agents`, `question`, `tension`, `recommendation`, `action`, `watch_signal`, `closer`, `script`.

If Notion posting is active, embed the video URL in the deliberation page once rendering completes.

---

## Step 6: Final Report to User

Deliver a single closing message:

```markdown
---
## Deliberation Complete

**Verdict**: [2-3 line summary of Marcus Aurelius's judgment]
**Recommendation**: [Proceed / Do Not Proceed / Proceed with Conditions / Defer]
**Confidence**: [High / Medium / Low]

[If Notion posted] **Notion**: [Link to deliberation page]
[If video generated] **Video**: [Link to rendered video]

To track how this decision plays out, record the actual outcome and compare it to the verdict. (A dedicated /log-outcome skill is planned.)
---
```

---

## Error Handling

### Wrong agent count in custom panel
> "The Rule of Three ensures optimal deliberation: 1 agent provides no tension, 2 creates deadlock, 3 enables triangulation. Please specify exactly 3 agents."

### Unknown agent name
> "I don't recognize '[name]' in the Board of Directors roster. Available panel agents (23 selectable): [list perspective + domain agents]. Note: Marcus Aurelius (arbiter) and Chris Voss (mediator) serve fixed structural roles and cannot be selected as panel members."

If a requested agent is not in the roster, check if a matching .md file exists in `custom/` (relative to the agents directory). If yes, load and use it. If no file exists, list the 23 selectable agents as above.

### Question too vague
> "To select the right panel and provide useful analysis, I need a more specific question. What exactly are you deciding? What are the stakes or constraints?"

### Agent profile not found at expected path
> If a profile .md file is missing, report the error and suggest running from the BOD system directory. Do not fabricate a profile.

---

## Output Length Targets

- Phase 1: ~300-400 words per agent report (900-1200 total)
- Phase 2: ~400-500 words
- Phase 3: ~600-800 words
- Phase 3.5: ~300-400 words (if triggered)
- Phase 4: ~500-700 words
- Total deliberation: ~2,500-3,500 words

Note: This skill consumes significant context. Consider compacting before invocation if context usage is above 60%.

---

## Execution Rules

1. **NO PAUSES between phases.** Once the panel is confirmed (auto-select or user-confirmed), run Phases 1 through 4 (and 3.5 if triggered) in a single unbroken sequence. Do not ask "Shall I proceed?" between phases.
2. **Read profiles before generating.** Never fake an agent's voice. Read their .md file and use their vocabulary, frameworks, and rhetorical patterns.
3. **Authentic disagreement.** The debate must contain real intellectual friction. Agents should challenge each other on substance, not softball.
4. **Marcus takes a position.** The Final Judgment must deliver a clear verdict, not a diplomatic hedge. Acknowledge complexity but commit to a recommendation.
5. **Mediation is rare.** Phase 3.5 triggers only on genuine impasse. Do not insert Chris Voss for routine disagreements.
6. **Post-deliberation is silent when unconfigured.** If Notion/Runway env vars are not set, skip those steps without mentioning them.
