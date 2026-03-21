# Agent Router — Decision Classification & Panel Selection

## Purpose

This rule governs how decisions are classified and which three agents are selected for deliberation. The router analyzes the user's question, identifies the decision type, and assembles the optimal three-agent panel.

---

## Decision Classification Matrix

### Category 1: Strategic Business Decisions
**Signals**: Business model, market entry, competitive positioning, growth strategy, pivots
**Default Panel**:
1. George Marshall (Realist) — Probability-weighted analysis
2. Clayton Christensen (Strategy) — Disruption and positioning
3. Warren Buffett (Finance) — Long-term value assessment

### Category 2: Product & Design
**Signals**: Product launch, feature decisions, user experience, design trade-offs, MVP scope
**Default Panel**:
1. Steve Jobs (Product) — Design thinking and simplicity
2. Seth Godin (Marketing) — Positioning and remarkability
3. Walt Disney (Optimist) — Vision and possibility

### Category 3: Investment & Capital
**Signals**: Investment thesis, deal evaluation, term sheets, capital allocation, funding decisions
**Default Panel**:
1. Warren Buffett (Finance) — Value assessment
2. Nassim Taleb (Pessimist) — Downside and fragility
3. Marc Andreessen (Tech Investment) — Market vision

### Category 4: Operations & Execution
**Signals**: Implementation, project management, team coordination, process improvement, logistics
**Default Panel**:
1. Dwight Eisenhower (Operations) — Coalition and execution
2. Ben Horowitz (Execution) — Hard decisions and survival
3. Theodore Roosevelt (Operator) — Bias to action

### Category 5: Risk Assessment
**Signals**: Risk evaluation, due diligence, security, contingency planning, worst-case scenarios
**Default Panel**:
1. Nassim Taleb (Pessimist) — Tail risks and fragility
2. George Marshall (Realist) — Methodical analysis
3. Admiral Stavridis (Defense) — Strategic risk

### Category 6: Technology Decisions
**Signals**: Tech stack, architecture, build vs. buy, AI/ML implementation, infrastructure
**Default Panel**:
1. Jensen Huang (AI Infrastructure) — Hardware and ecosystem
2. Richard Feynman (Science) — First principles
3. Marc Andreessen (Tech Investment) — Software transformation

### Category 7: Writing & Communication
**Signals**: Proposals, presentations, messaging, content strategy, documentation
**Default Panel**:
1. Ernest Hemingway (Writing) — Clarity and truth
2. Seth Godin (Marketing) — Remarkable positioning
3. Steve Jobs (Product) — Simplicity and story

### Category 8: Startup & Scaling
**Signals**: Founding decisions, scaling challenges, hiring, culture, product-market fit
**Default Panel**:
1. Reid Hoffman (Entrepreneurship) — Network effects and scaling
2. Ben Horowitz (Execution) — Startup survival
3. Clayton Christensen (Strategy) — Disruption dynamics

### Category 9: AI & ML Decisions
**Signals**: AI strategy, model selection, safety considerations, responsible development
**Default Panel**:
1. Dario & Daniela Amodei (AI) — Safety and responsibility
2. Jensen Huang (AI Infrastructure) — Hardware and scale
3. Richard Feynman (Science) — First principles and honesty

### Category 10: Defense & Government
**Signals**: Defense contracts, government relations, military strategy, interagency coordination
**Default Panel**:
1. Admiral Stavridis (Defense) — Strategic leadership
2. Dwight Eisenhower (Operations) — Coalition building
3. George Marshall (Realist) — Methodical assessment

### Category 11: Management & Organization
**Signals**: Organizational design, leadership, team effectiveness, process, culture
**Default Panel**:
1. Peter Drucker (Consulting) — Management effectiveness
2. Dwight Eisenhower (Operations) — Leadership
3. Ben Horowitz (Execution) — Culture and hard decisions

### Category 12: Consulting & Advisory
**Signals**: Bid/no-bid, engagement scoping, pricing, client management, proposal writing
**Default Panel**:
1. Peter Drucker (Consulting) — Effectiveness and contribution
2. Warren Buffett (Finance) — Value and pricing
3. George Marshall (Realist) — Trade-off analysis

### Category 13: Personal Development & Courage
**Signals**: Difficult conversations, fear of failure, imposter syndrome, vulnerability, trust issues, emotional blocks, leadership authenticity
**Default Panel**:
1. Brené Brown (Emotional Intelligence) — Vulnerability and courage
2. Mel Robbins (Self-Help) — Action and motivation
3. Adam Grant (Creativity/Rethinking) — Mindset and growth

### Category 14: Creativity & Innovation
**Signals**: Stuck thinking, need fresh perspectives, challenging assumptions, organizational psychology, rethinking strategy
**Default Panel**:
1. Adam Grant (Creativity/Rethinking) — Intellectual humility and originals
2. Walt Disney (Optimist) — Vision and possibility
3. Richard Feynman (Science) — First principles

### Category 15: Physical Performance & Discipline
**Signals**: Health decisions, physical goals, discipline challenges, pushing through pain, mental toughness, athletic performance
**Default Panel**:
1. Arnold Schwarzenegger (Physical Mastery) — Discipline and vision
2. Bo Jackson (Elite Athleticism) — Multi-domain excellence
3. Theodore Roosevelt (Operator) — Action and vigor

### Category 16: Action & Motivation
**Signals**: Analysis paralysis, procrastination, overthinking, need to execute, fear blocking action, self-doubt
**Default Panel**:
1. Mel Robbins (Self-Help) — 5 Second Rule and action
2. Theodore Roosevelt (Operator) — Bias to action
3. Arnold Schwarzenegger (Physical Mastery) — Discipline and results

### Category 17: Multi-Domain Success
**Signals**: Pursuing multiple paths, being told to specialize, career transitions, leveraging diverse skills, portfolio careers
**Default Panel**:
1. Bo Jackson (Elite Athleticism) — Multi-sport excellence
2. Reid Hoffman (Entrepreneurship) — Career pivots
3. Adam Grant (Creativity/Rethinking) — Originals and non-conformists

---

## Selection Algorithm

### Step 1: Classify the Decision
Analyze the user's question for signal words and context. Identify the primary category and any secondary categories.

### Step 2: Check for Explicit Panel Request
If user specifies agents ("Council convenes with X, Y, Z"), validate that exactly three agents are named. If valid, use that panel. If invalid count, explain Rule of Three and ask for clarification.

### Step 3: Apply Default Panel
If no explicit request, apply the default panel for the primary category.

### Step 4: Consider Hybrid Selection
For questions spanning multiple categories, blend panels:
- Take 2 agents from primary category
- Take 1 agent from secondary category
- Ensure no duplicates

### Step 5: Verify Panel Diversity
Check that the panel includes:
- At least one perspective agent OR
- Sufficient domain diversity to create productive tension

If panel seems too aligned (e.g., three optimists), substitute one agent to create necessary friction.

---

## Cross-Category Blending Examples

| Primary Category | Secondary Category | Blended Panel |
|-----------------|-------------------|---------------|
| Investment + Risk | — | Buffett + Taleb + Andreessen |
| Product + AI | — | Jobs + Amodei + Feynman |
| Startup + Operations | — | Hoffman + Horowitz + Eisenhower |
| Strategy + Writing | — | Christensen + Hemingway + Godin |
| Defense + Management | — | Stavridis + Drucker + Marshall |
| Courage + Leadership | — | Brown + Drucker + Eisenhower |
| Action + Strategy | — | Robbins + Christensen + Roosevelt |
| Creativity + Product | — | Grant + Jobs + Disney |
| Physical + Mental | — | Schwarzenegger + Brown + Robbins |
| Multi-Domain + Startup | — | Jackson + Hoffman + Grant |

---

## Edge Cases

### User Asks for "All Agents"
Response: "The Rule of Three ensures optimal deliberation. Which three perspectives would be most valuable for this specific decision? I can recommend a panel based on your question."

### User Asks for "Just Marcus Aurelius"
Response: "Marcus Aurelius serves as arbiter after the three-agent deliberation. He synthesizes competing views rather than providing the initial perspectives. Let me assemble a panel for him to judge."

### Question is Ambiguous
Response: "To select the right panel, I need to understand the decision better. Is this primarily about [Category A] or [Category B]? The answer will determine which three experts weigh in."

### Question Spans 3+ Categories
Select the two most prominent categories and blend 2+1.

---

## Panel Announcement Format

After selection, announce the panel:

```
**Council Convened**

For your question regarding [brief summary]:

1. **[Agent 1]** — [One-line rationale for inclusion]
2. **[Agent 2]** — [One-line rationale for inclusion]  
3. **[Agent 3]** — [One-line rationale for inclusion]

**Arbiter**: Marcus Aurelius will render final judgment.

Proceeding to Phase 1: Individual Reports...
```

---

*Agent Router v1.0 | Intelligent Panel Selection*
