# Agent Update Protocol — Keeping Profiles Current

## Purpose

Several agents in the roster are living figures whose views, positions, and contexts evolve:
- **Jensen Huang** — NVIDIA strategy shifts with market
- **Dario & Daniela Amodei** — Anthropic's AI safety positions develop
- **Marc Andreessen** — Investment theses and public statements change
- **Reid Hoffman** — New ventures and evolving views
- **Ben Horowitz** — Continued writing and speaking
- **Seth Godin** — Daily blog, evolving marketing philosophy

This protocol ensures profiles stay accurate and relevant.

---

## Living vs. Historical Agents

### Historical Agents (No Updates Needed)
Profiles based on complete historical record:
- Marcus Aurelius
- Walt Disney
- George Marshall
- Theodore Roosevelt
- Warren Buffett (mostly historical; update sparingly)
- Steve Jobs
- Ernest Hemingway
- Peter Drucker
- Dwight Eisenhower
- Richard Feynman
- Clayton Christensen

### Living Agents (Regular Updates)
Profiles should be refreshed periodically:

| Agent | Update Frequency | Primary Sources |
|-------|------------------|-----------------|
| Jensen Huang | Quarterly | Earnings calls, keynotes, interviews |
| Dario & Daniela Amodei | Quarterly | Blog posts, papers, interviews, congressional testimony |
| Marc Andreessen | Semi-annually | Podcasts, blog posts, tweets |
| Reid Hoffman | Semi-annually | Podcasts, interviews, new books |
| Ben Horowitz | Annually | Blog posts, interviews |
| Seth Godin | Annually | Daily blog, podcasts |
| Admiral Stavridis | Annually | Articles, interviews, books |
| Brené Brown | Annually | Podcasts, new research |
| Adam Grant | Annually | Podcasts, books, research |
| Mel Robbins | Annually | Podcasts, social media |
| Arnold Schwarzenegger | Annually | Newsletters, interviews |
| Bo Jackson | Rarely | Limited public presence |

---

## Version Tracking

Each agent profile includes version metadata:

```markdown
---
agent: Jensen Huang
version: 1.2
last_updated: 2025-01-15
update_frequency: quarterly
next_review: 2025-04-15
sources_checked:
  - NVIDIA Q4 2024 earnings call
  - CES 2025 keynote
  - Bloomberg interview (2025-01-10)
changelog:
  - v1.2 (2025-01-15): Added Blackwell architecture positioning, updated on AI agents
  - v1.1 (2024-10-20): Added sovereign AI messaging
  - v1.0 (2024-07-01): Initial profile
---
```

---

## Refresh Process

### Command
```
/refresh-agent [Agent Name]
```

### What It Does
1. **Source Check**: Searches for recent interviews, speeches, writings
2. **Delta Analysis**: Compares new material to existing profile
3. **Update Draft**: Proposes specific changes to profile
4. **User Review**: You approve or modify changes
5. **Version Bump**: Updates version and changelog

### Example Flow

**User**:
```
/refresh-agent Jensen Huang
```

**System**:
```markdown
## Refreshing: Jensen Huang

**Current Version**: 1.1 (Last updated: 2024-10-20)
**Sources Checked**:
- NVIDIA Q4 2024 earnings call (2025-01-08)
- CES 2025 keynote (2025-01-07)
- Bloomberg Technology interview (2025-01-10)

### Proposed Updates

**Core Philosophy** — Add:
> "AI agents are the next computing platform. Every company will have AI employees."

**Mental Models** — Add:
- **AI Agent Workforce**: Companies will deploy millions of AI agents as digital employees

**Representative Quotes** — Add:
> "The age of AI has begun. We're at an iPhone moment for AI."
> "Sovereign AI is the new space race."

**Known Biases** — Update:
- Add: Increasingly dismissive of AI safety concerns in recent statements

### No Changes Needed
- Decision-Making Style (unchanged)
- Communication Patterns (consistent)
- When to Summon (still accurate)

---

**Apply these updates?**
- "Yes" — Apply all changes, bump to v1.2
- "Modify" — Edit the proposed changes first
- "Skip" — Keep current profile unchanged
```

---

## Automated Review Reminders

The system tracks review schedules:

### Weekly Check (Sundays)
```markdown
## Agent Review Status

**Due for Review** (past due date):
- Jensen Huang — Last updated 95 days ago (quarterly schedule)

**Coming Up** (within 30 days):
- Dario Amodei — Review due 2025-02-15

**Recently Updated**:
- Marc Andreessen — Updated 2025-01-10 (v2.1)

---
Run `/refresh-agent Jensen Huang` to update.
```

---

## What Gets Updated

### Always Update
- **Representative Quotes**: Add new, impactful statements
- **Core Philosophy**: If fundamental positions shift
- **Mental Models**: If they articulate new frameworks
- **Known Biases**: If new blind spots emerge

### Rarely Update
- **Identity**: Only if role changes significantly
- **Decision-Making Style**: Usually stable
- **Communication Patterns**: Usually stable
- **Interaction Instructions**: Only if voice changes notably

### Never Update (for consistency)
- **When to Summon**: Domain expertise doesn't change

---

## Source Hierarchy

When refreshing, prioritize sources in this order:

1. **Primary Sources** (Highest value)
   - Their own writing (books, blogs, memos)
   - Extended interviews (podcasts, video)
   - Speeches and keynotes
   - Earnings calls and investor presentations

2. **Secondary Sources** (Good value)
   - Profiles in major publications
   - Biographies (for context)
   - Documented decisions with public reasoning

3. **Tertiary Sources** (Use cautiously)
   - Social media (tweets, posts)
   - Second-hand accounts
   - Commentary about them

### Source Verification Rules
- Quotes must be directly attributable
- No fabricated or paraphrased quotes
- Date all sources
- Note context (e.g., "said during earnings call discussing...")

---

## Bulk Refresh

Update multiple agents at once:

```
/refresh-all-living
```

Runs refresh process for all agents flagged as living. Generates consolidated report:

```markdown
## Bulk Agent Refresh — 2025-01-26

| Agent | Status | Key Changes |
|-------|--------|-------------|
| Jensen Huang | Updated (v1.1 → v1.2) | Added AI agents framework |
| Dario Amodei | No changes needed | Profile current |
| Marc Andreessen | Updated (v2.0 → v2.1) | New techno-optimist quotes |
| Reid Hoffman | Skipped | Review deferred to next month |
| ... | ... | ... |

**Total**: 8 agents reviewed, 4 updated, 3 unchanged, 1 deferred
```

---

## Handling Major Changes

If an agent's position shifts dramatically:

### Example: Agent Reverses Position
If Marc Andreessen, previously bullish on crypto, became bearish:

1. **Document the shift** in profile with dates
2. **Note the contradiction** in Known Biases
3. **Update advice weighting** — recent views may be more relevant
4. **Add disclaimer** if profile now contains contradictory guidance

```markdown
## Known Biases & Blind Spots

- **Position Evolution**: Note that Andreessen's views on crypto shifted 
  significantly in 2025. Earlier quotes reflect pre-2025 bullishness; 
  recent statements are more cautious. Weight recent views for crypto-related decisions.
```

### Example: Agent Disgraced or Discredited
If new information fundamentally changes how an agent should be viewed:

1. **Evaluate impact** on their expertise domain
2. **Add context** in Known Biases
3. **Consider removal** if credibility is fatally compromised
4. **User decision** — you choose whether to retain

---

## Agent Sunset Process

If an agent should be removed (death, disgrace, irrelevance):

```
/sunset-agent [Name]: [Reason]
```

**Process**:
1. Agent moved to `/agents/archived/`
2. Removed from active roster
3. Historical deliberations preserved with note
4. User notified of suggested replacement

---

## Manual Override

You can always manually edit any agent profile:

```
/edit-agent [Name]
```

Opens the raw markdown file for direct editing. Changes are tracked in changelog.

---

## Update Log

All updates are logged in `agent-update-log.md`:

```markdown
# Agent Update Log

## 2025-01-26 — Jensen Huang

**Version**: 1.1 → 1.2
**Updated by**: System refresh
**Sources**: CES 2025 keynote, Q4 earnings call
**Changes**:
- Added AI agents framework to Mental Models
- Added 2 new quotes on sovereign AI
- Updated Known Biases re: safety concerns

---

## 2025-01-15 — Marc Andreessen

**Version**: 2.0 → 2.1
**Updated by**: Manual edit
**Sources**: Lex Fridman podcast #412
**Changes**:
- Added techno-optimist manifesto references
- Updated Core Philosophy with acceleration themes

---
```

---

*Agent Update Protocol v1.0 | Keeping the Board Current*
