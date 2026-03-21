---
name: masterclass-scout
description: "Weekly automation that scans MasterClass.com for potential new board agents, compares against current roster, identifies coverage gaps, and recommends 3 candidates for profile development."
trigger: weekly
schedule: "Sundays at 9am"
source_url: "https://www.masterclass.com/homepage"
global: true
---

# MasterClass Scout — Roster Growth Workflow

## Purpose

Keep the Board of Directors roster fresh and growing by systematically identifying high-quality candidates from MasterClass instructors. This ensures the board evolves to cover emerging domains and maintains balance across perspectives.

---

## Workflow Trigger

**Schedule**: Weekly (Sundays at 9am)
**Manual**: `/scout-masterclass` or "Find new agents from MasterClass"

---

## Workflow Steps

### Step 1: Fetch Current Roster

Load the current agent roster from:
- `/board-of-directors/agents/perspective/` (4 agents)
- `/board-of-directors/agents/domain/` (19 agents)
- `/board-of-directors/agents/mediator/` (1 agent)
- `/board-of-directors/agents/arbiter/` (1 agent)

Extract:
- Names
- Domains
- Coverage areas

### Step 2: Scan MasterClass Instructors

Fetch the current instructor list from `https://www.masterclass.com/homepage`

For each instructor, extract:
- Name
- Domain/Category (as MasterClass categorizes them)
- Brief description
- Course title(s)

### Step 3: Categorize by Domain

Map MasterClass categories to board domains:

| MasterClass Category | Board Domain | Coverage Status |
|---------------------|--------------|-----------------|
| Business & Leadership | Consulting, Entrepreneurship | Moderate |
| Writing | Writing, Communication | Covered (Hemingway) |
| Cooking & Culinary | *Gap* - Craft/Lifestyle | Missing |
| Music & Entertainment | *Gap* - Creative Performance | Missing |
| Sports & Gaming | Physical Mastery, Elite Athleticism | Partial (Arnold, Bo) |
| Science & Technology | Science, AI, Tech | Strong |
| Design & Style | Product, Design | Partial (Jobs) |
| Community & Government | Defense, Operations | Moderate |
| Wellness | *Gap* - Health/Wellness | Missing |
| Film & TV | *Gap* - Storytelling/Directing | Missing |

### Step 4: Gap Analysis

Compare current roster coverage against potential additions:

**Coverage Gaps to Prioritize**:
1. Domains with zero representation
2. Domains with only one agent (no debate possible)
3. Emerging fields with high relevance to user's work

**User Context to Consider**:
- Defense consulting → Prioritize military/strategy figures
- Entrepreneurship → Prioritize founders/builders
- AI advisory → Prioritize tech visionaries
- Writing/proposals → Prioritize communicators

### Step 5: Score Candidates

For each MasterClass instructor not in the roster, score:

| Criteria | Weight | Description |
|----------|--------|-------------|
| **Domain Gap Fill** | 40% | Does this fill an unrepresented domain? |
| **Distinctiveness** | 25% | Would they offer a perspective no current agent provides? |
| **Profile Buildability** | 20% | Rich source material available (books, interviews, speeches)? |
| **User Relevance** | 15% | Alignment with JD's work domains |

### Step 6: Generate Recommendations

Produce a report with **exactly 3 candidates**:

```markdown
## MasterClass Scout Report — [Date]

### Roster Status
- **Total Agents**: 24 (4 perspective + 19 domain + 1 mediator)
- **Domains Covered**: [list]
- **Notable Gaps**: [list]

### Candidate 1: [Name]
**MasterClass Course**: [Title]
**Proposed Domain**: [Domain]
**Gap Filled**: [Which gap this addresses]
**Why This Candidate**:
- [Reason 1]
- [Reason 2]
- [Available source material]
**Score**: [X/100]

### Candidate 2: [Name]
...

### Candidate 3: [Name]
...

### Recommendation Priority
1. **Build First**: [Name] — [rationale]
2. **Build Second**: [Name] — [rationale]
3. **Consider**: [Name] — [rationale]

### Rejected Candidates (and why)
- [Name]: [reason - e.g., too similar to existing agent]
- [Name]: [reason - e.g., limited source material]
```

---

## Sample Candidates (as of January 2025)

Based on known MasterClass instructors who could fill gaps:

### Potential Adds

| Instructor | MasterClass Domain | Board Domain | Gap Filled |
|------------|-------------------|--------------|------------|
| **Sara Blakely** | Entrepreneurship | Entrepreneurship | Female founder perspective |
| **Bob Iger** | Business Leadership | Leadership | Media/entertainment strategy |
| **Howard Schultz** | Business Leadership | Culture/Brand | Customer experience |
| **Gordon Ramsay** | Culinary | Excellence/Craft | Performance under pressure |
| **Serena Williams** | Sports | Elite Performance | Champion mindset |
| **Martin Scorsese** | Film | Storytelling | Narrative craft |
| **Annie Leibovitz** | Photography | Visual Communication | Image strategy |
| **Neil deGrasse Tyson** | Science | Science Communication | Translating complexity |
| **Doris Kearns Goodwin** | Writing/History | Leadership History | Historical decision-making |
| **Chris Hadfield** | Space | Risk Management | High-stakes operations |

### Why These Fill Gaps

1. **Female Founder Perspective**: Roster is heavily male. Sara Blakely or Serena Williams add needed diversity of experience.

2. **Creative Performance**: No one covering music, film, or performance arts as applied frameworks for excellence.

3. **Health/Wellness**: No dedicated health/wellness agent beyond Arnold's physical mastery focus.

4. **Historical Leadership**: Doris Kearns Goodwin could add Lincoln/FDR/LBJ decision frameworks.

---

## Implementation Details

### Automated Execution (Antigravity)

**Step-by-Step Technical Flow**:

```
1. TRIGGER: Weekly schedule fires (Sunday 9am) OR user runs /scout-masterclass

2. LOAD CURRENT ROSTER:
   - Read all files in /board-of-directors/agents/**/
   - Parse each .md file for: name, domain, coverage areas
   - Build roster_map: { name: domain[] }
   - Count: total_agents, domains_covered, gaps_identified

3. FETCH MASTERCLASS DATA:
   - web_fetch("https://www.masterclass.com/homepage")
   - Parse instructor grid/list from HTML
   - Extract for each instructor:
     - name: string
     - course_title: string
     - category: string (Business, Writing, etc.)
     - instructor_url: string (for later deep-dive)
   - Store in instructors_array[]

4. CATEGORIZE & MAP:
   - For each instructor in instructors_array:
     - Map MasterClass category → Board domain (use mapping table)
     - Check if name exists in roster_map
     - If not in roster: add to candidates_array[]
     - Tag with: category, mapped_domain, is_gap_fill (boolean)

5. SCORE CANDIDATES:
   - For each candidate in candidates_array:
     - gap_score = (fills unrepresented domain) ? 40 : (fills single-agent domain) ? 20 : 0
     - distinctiveness_score = assess_uniqueness(candidate, roster_map) * 25
     - buildability_score = estimate_source_richness(candidate) * 20
     - relevance_score = match_user_domains(candidate, user_profile) * 15
     - total_score = gap_score + distinctiveness_score + buildability_score + relevance_score

6. RANK & SELECT:
   - Sort candidates_array by total_score DESC
   - Select top 3 candidates
   - Generate rejection reasons for next 5 (for transparency)

7. GENERATE REPORT:
   - Create markdown report using template
   - Save to /board-of-directors/scout-reports/[date]-scout-report.md

8. NOTIFY:
   - Present report to user
   - Prompt: "Would you like me to build a profile for any of these candidates?"
```

### Scoring Functions Detail

**assess_uniqueness(candidate, roster)**:
```
- Check for domain overlap with existing agents
- Penalty for same domain: -50%
- Bonus for unique perspective in same domain: +25%
- Bonus for entirely new domain: +100%
- Return: 0.0 to 1.0
```

**estimate_source_richness(candidate)**:
```
- Factors (heuristic):
  - Has published book(s): +30%
  - MasterClass course exists: +30% (we know this is true)
  - Wikipedia page exists: +20%
  - Podcast appearances likely: +10%
  - Active public speaking: +10%
- Return: 0.0 to 1.0
```

**match_user_domains(candidate, user_profile)**:
```
- user_domains = [defense, AI, strategy, entrepreneurship, consulting]
- candidate_relevance = overlap(candidate.domain, user_domains)
- Return: 0.0 to 1.0
```

### Manual Alternative (No Web Access)

If Antigravity cannot fetch web pages:

**Option 1: User Provides List**
```
User: Here are the current MasterClass instructors: [paste list]
System: [Runs comparison against roster, generates recommendations]
```

**Option 2: User Runs External Script**
```bash
# Simple scraper (run locally, paste output to Antigravity)
curl -s "https://www.masterclass.com/sitemap.xml" | \
  grep -oP '(?<=<loc>https://www.masterclass.com/classes/)[^<]+' | \
  sort -u
```

**Option 3: Quarterly Manual Review**
```
/scout-masterclass --manual

System: I'll guide you through a manual review:
1. Open https://www.masterclass.com/homepage
2. For each category, tell me any instructors that look interesting
3. I'll compare against the roster and score them
```

### For Antigravity Integration

**Required Capabilities**:
1. `web_fetch` — To scan MasterClass homepage
2. File read — To load current roster
3. File write — To save reports to `/scout-reports/`
4. Scheduling — For weekly automation (or rely on user trigger)

**File Dependencies**:
- Reads: `/board-of-directors/agents/**/*.md`
- Reads: `/board-of-directors/user-preferences.md` (for user domain context)
- Writes: `/board-of-directors/scout-reports/[date]-scout-report.md`
- Updates: `/board-of-directors/scout-log.md`

---

## Logging

After each scout run, log to `scout-log.md`:

```markdown
## Scout Run: [Date]

**Instructors Scanned**: [count]
**New Since Last Scan**: [list]
**Candidates Recommended**:
1. [Name] — [domain]
2. [Name] — [domain]  
3. [Name] — [domain]

**User Decision**: [pending/approved X/declined]
**Profiles Built**: [list of any actually built]
```

---

## Future Enhancements

1. **Source Expansion**: Add TED speakers, podcast hosts, notable authors beyond MasterClass
2. **Automatic Profile Drafting**: When candidate approved, auto-generate initial profile draft from source material
3. **Usage-Based Prioritization**: Weight candidates higher if they fill domains the user frequently queries
4. **Retirement Suggestions**: Identify agents who are rarely selected and consider consolidation

---

*MasterClass Scout v1.0 | Roster Growth Automation*
