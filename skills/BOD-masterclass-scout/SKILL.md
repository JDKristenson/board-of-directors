# MasterClass Scout Skill

## Purpose

Systematically identify high-quality candidates from MasterClass instructors to expand the Board of Directors agent roster. This skill scans MasterClass.com, compares instructors against the current roster, identifies coverage gaps, and recommends candidates for profile development.

---

## Invocation

### Triggers
- `/scout-masterclass`
- `/scout`
- "Find new agents from MasterClass"
- "Scout for new board members"
- "Who should we add to the roster?"
- "Check MasterClass for candidates"

### With Options
```
/scout-masterclass                    # Full scan with top 3 recommendations
/scout-masterclass --gaps             # Show coverage gaps only
/scout-masterclass --category [name]  # Focus on specific category
/scout-masterclass --compare [name]   # Evaluate specific instructor
```

---

## Skill Workflow

### Step 1: Load Current Roster

Read agent profiles from the Board of Directors system:

```
Location: ~/.gemini/antigravity/board-of-directors/agents/
Structure:
  - perspective/   (4 agents: Disney, Marshall, Taleb, Roosevelt)
  - domain/        (19 agents: Buffett, Jobs, Hemingway, etc.)
  - mediator/      (1 agent: Voss)
  - arbiter/       (1 agent: Marcus Aurelius)
  - custom/        (user-added agents)
```

Extract for each agent:
- Name
- Primary domain
- Secondary domains/tags
- Known biases (to identify perspective gaps)

### Step 2: Fetch MasterClass Instructors

**Primary Method** (if web access available):
```
URL: https://www.masterclass.com/sitemap.xml
Alternative: https://www.masterclass.com/classes

Extract:
- Instructor name
- Course title
- Category
- Brief bio/description
```

**Fallback Method** (no web access):
```
Prompt user: "I can't access MasterClass directly. Please either:
1. Paste the instructor list from masterclass.com/classes
2. Tell me specific instructors you're curious about
3. Ask me to analyze known MasterClass instructors from my training data"
```

### Step 3: Map Categories

| MasterClass Category | Board Domain | Current Coverage |
|---------------------|--------------|------------------|
| Business & Leadership | Consulting, Entrepreneurship, Execution | Strong (Drucker, Hoffman, Horowitz) |
| Writing | Writing, Communication | Single (Hemingway) |
| Cooking & Culinary Arts | Craft, Excellence | **Gap** |
| Music & Entertainment | Creative Performance | **Gap** |
| Sports & Gaming | Physical Mastery, Elite Performance | Partial (Schwarzenegger, Jackson) |
| Science & Technology | Science, AI, Tech | Strong (Feynman, Amodei, Huang) |
| Design, Arts & Style | Product, Design, Visual | Single (Jobs) |
| Community & Government | Defense, Operations, Leadership | Strong (Stavridis, Eisenhower) |
| Wellness | Health, Wellbeing | **Gap** |
| Film & Television | Storytelling, Directing | **Gap** |

### Step 4: Score Candidates

For each instructor not in the roster, calculate:

```
TOTAL_SCORE = (Gap_Fill × 0.40) + (Distinctiveness × 0.25) + 
              (Buildability × 0.20) + (User_Relevance × 0.15)

Where:
- Gap_Fill (0-100): Does this fill an unrepresented domain?
  - 100 = Fills complete gap (no agents in domain)
  - 60 = Fills partial gap (only 1 agent in domain)
  - 20 = Adds depth to covered domain
  
- Distinctiveness (0-100): Unique perspective vs. existing agents?
  - 100 = Completely novel viewpoint
  - 50 = Different angle in similar domain
  - 20 = Similar to existing agent
  
- Buildability (0-100): Quality source material available?
  - 100 = Books + speeches + interviews + documented decisions
  - 70 = Some books/interviews
  - 40 = Limited public material
  
- User_Relevance (0-100): Alignment with user's work domains?
  - Defense, AI, Strategy, Entrepreneurship, Consulting = high relevance
```

### Step 5: Generate Report

Output a structured report to: `~/.gemini/antigravity/board-of-directors/scout-reports/`

---

## Output Format

### Full Scout Report

```markdown
# MasterClass Scout Report — [DATE]

## Roster Status

| Category | Agents | Coverage |
|----------|--------|----------|
| Perspective | 4 | Complete |
| Domain | 19 | Gaps in Craft, Creative, Wellness |
| Mediator | 1 | Complete |
| Arbiter | 1 | Complete |
| Custom | [N] | User-defined |
| **Total** | **25+** | |

## Coverage Gaps Identified

### Critical Gaps (Zero Coverage)
1. **Culinary/Craft Excellence** — No agent for mastery through repetition, service excellence
2. **Creative Performance** — No agent for music, film direction, artistic vision
3. **Health/Wellness** — No agent for holistic wellbeing, longevity, mental health

### Partial Gaps (Single Agent)
1. **Writing** — Only Hemingway (fiction-focused). Gap in business/technical writing.
2. **Design** — Only Jobs (product). Gap in visual/graphic design.

---

## Top 3 Candidates

### Candidate 1: [NAME]

| Attribute | Value |
|-----------|-------|
| **MasterClass Course** | [Course Title] |
| **Proposed Domain** | [Domain] |
| **Gap Filled** | [Which gap] |
| **Score** | [XX/100] |

**Why This Candidate**:
- [Key strength 1]
- [Key strength 2]
- [Unique perspective they bring]

**Source Material Available**:
- [ ] Published books
- [ ] Extended interviews/podcasts
- [ ] Speeches/keynotes
- [ ] Documented decisions
- [ ] MasterClass content

**Sample Principles** (preview):
1. "[Quote or principle 1]"
2. "[Quote or principle 2]"

---

### Candidate 2: [NAME]
[Same structure]

---

### Candidate 3: [NAME]
[Same structure]

---

## Recommendation Priority

| Priority | Candidate | Rationale |
|----------|-----------|-----------|
| 🥇 Build First | [Name] | [Why highest priority] |
| 🥈 Build Second | [Name] | [Why second] |
| 🥉 Consider | [Name] | [Why third] |

---

## Rejected Candidates

| Instructor | Reason for Rejection |
|------------|---------------------|
| [Name] | Too similar to [existing agent] |
| [Name] | Limited source material |
| [Name] | Domain already well-covered |

---

## Next Steps

To build a profile for any candidate:
```
/add-agent [Name]: [Brief description]
```

Or request full profile generation:
```
"Build a full agent profile for [Name]"
```

---

*Scout Report Generated: [TIMESTAMP]*
*Next Scheduled Scan: [DATE]*
```

---

## Known MasterClass Instructors (Reference)

When web access is unavailable, use this reference list:

### Business & Leadership
- Sara Blakely (Spanx founder)
- Bob Iger (Disney CEO)
- Howard Schultz (Starbucks)
- Anna Wintour (Vogue)
- Chris Voss (FBI Negotiation) ✓ Already in roster

### Writing
- Malcolm Gladwell
- Neil Gaiman
- Margaret Atwood
- James Patterson
- David Sedaris
- R.L. Stine

### Film & Television
- Martin Scorsese
- Ron Howard
- Spike Lee
- Werner Herzog
- Jodie Foster
- Aaron Sorkin

### Music
- Herbie Hancock
- Usher
- Alicia Keys
- deadmau5
- Hans Zimmer
- Yo-Yo Ma

### Sports & Gaming
- Serena Williams
- Tony Hawk
- Stephen Curry
- Simone Biles
- Wayne Gretzky
- Lewis Hamilton

### Culinary
- Gordon Ramsay
- Thomas Keller
- Wolfgang Puck
- Massimo Bottura
- Alice Waters

### Science & Wellness
- Neil deGrasse Tyson
- Jane Goodall
- Chris Hadfield
- Matthew Walker (sleep)

### Design & Photography
- Annie Leibovitz
- Frank Gehry
- Kelly Wearstler

### History & Politics
- Doris Kearns Goodwin
- Condoleezza Rice
- David Axelrod
- Karl Rove

---

## Integration with Board of Directors

### After Scout Approval

When user approves a candidate:

1. **Generate Profile Draft**
   ```
   /add-agent [Name]: [MasterClass domain] expert
   ```

2. **Research Deep Dive**
   - Fetch additional sources (books, interviews)
   - Extract core principles
   - Identify mental models
   - Document decision patterns

3. **Create Full Profile**
   - Follow standard agent profile template
   - Save to `agents/domain/[name].md`
   - Update `agent-statistics.md`
   - Update AGENT_ROUTER.md with new category mappings

4. **Log Addition**
   ```markdown
   ## Scout Addition: [Date]
   
   **Candidate**: [Name]
   **Source**: MasterClass Scout Report [Date]
   **Domain**: [Domain]
   **Profile Created**: [Date]
   **First Deliberation**: [Pending]
   ```

---

## Maintenance

### Weekly Automation (if enabled)
- Schedule: Sundays at 9:00 AM
- Auto-generates report to scout-reports/
- Notifies user of new candidates

### Manual Trigger
- User runs `/scout-masterclass`
- Interactive session with real-time analysis

### Logging
All scout runs logged to `scout-log.md`:
```markdown
| Date | Instructors Scanned | Candidates Found | Profiles Built |
|------|---------------------|------------------|----------------|
| [Date] | [N] | [Names] | [Names or "Pending"] |
```

---

## Example Session

**User**: `/scout-masterclass`

**Gemini**:
```
Scanning MasterClass roster against your Board of Directors...

📊 Current Roster: 25 agents across 17 domains

🔍 Coverage Gaps Identified:
- Culinary/Craft Excellence (0 agents)
- Creative Performance/Film (0 agents)  
- Health/Wellness (0 agents)
- Business Writing (partial - Hemingway is fiction-focused)

🎯 Top 3 Candidates:

1. **Gordon Ramsay** (Score: 87/100)
   - Fills: Craft Excellence gap
   - Brings: Performance under pressure, standards, feedback delivery
   - Rich source material: Books, shows, documented kitchen philosophy

2. **Martin Scorsese** (Score: 82/100)
   - Fills: Storytelling/Directing gap
   - Brings: Narrative craft, visual thinking, artistic vision
   - Rich source material: Interviews, documentaries, MasterClass

3. **Sara Blakely** (Score: 79/100)
   - Fills: Female founder perspective
   - Brings: Bootstrapping, consumer products, resilience
   - Rich source material: Interviews, MasterClass, documented Spanx journey

Would you like me to build a full profile for any of these candidates?
```

**User**: "Build Gordon Ramsay"

**Gemini**: [Generates full agent profile following template]

---

*MasterClass Scout Skill v1.0*
*For Google Antigravity IDE*
