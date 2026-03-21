# Board of Directors — Multi-Agent Deliberation System

A strategic decision-making framework for Google Antigravity IDE that convenes virtual boards of directors from history's greatest minds.

---

## Overview

When facing important decisions, this system convenes **exactly three agents** from a roster of historical figures, each bringing their unique perspective, mental models, and decision-making frameworks. After deliberation, **Marcus Aurelius** serves as the final arbiter, synthesizing competing views into actionable recommendations.

---

## The Rule of Three — Inviolable

| Count | Result | Why |
|-------|--------|-----|
| **1 Agent** | No Discussion | A single perspective lacks tension |
| **2 Agents** | A Tie | Binary opposition creates deadlock |
| **3 Agents** | Optimal | Triangulation creates productive deliberation |

**Marcus Aurelius does not count toward the three.** He speaks last.

---

## Quick Start

### Basic Invocation

Type in the chat:
```
/convene-council
```

Or use natural language:
```
Council convenes: Should we accept this acquisition offer?
```

### Custom Panel Selection
```
Council convenes with Warren Buffett, Nassim Taleb, Ben Horowitz:
Should we take this term sheet?
```

---

## Deliberation Phases

### Phase 1: Individual Reports
Each agent produces an independent analysis with:
- Position summary
- Key analysis points
- Recommendation
- Confidence level
- Key assumptions

### Phase 2: Combined Report
A synthesis showing:
- Areas of consensus
- Areas of tension
- Trade-offs identified
- Open questions

### Phase 3: Debate
Agents directly challenge each other:
- Target specific claims
- Defend or concede positions
- Refine arguments through confrontation

### Phase 3.5: Mediation (Conditional)
**Triggered when**: Agents reach impasse, cross-domain conflicts emerge, or explicitly requested.

Chris Voss (Mediator) enters to:
- Label what each agent is actually concerned about
- Surface hidden concerns through calibrated questions
- Hunt for Black Swans (unknown unknowns)
- Reframe the question if a better frame exists

### Phase 4: Final Judgment
Marcus Aurelius renders verdict:
- Acknowledges each perspective
- Distinguishes real vs. apparent disagreement
- Applies Stoic principles
- Delivers clear recommendation
- Issues call to action

---

## Available Agents

### Perspective Agents (Core Analytical Lenses)

| Agent | Lens | Best For |
|-------|------|----------|
| **Walt Disney** | Optimist | Vision, creative possibilities, best-case scenarios |
| **George Marshall** | Realist | Probability-weighted analysis, trade-offs |
| **Nassim Taleb** | Pessimist | Downside risks, fragility, tail risks |
| **Theodore Roosevelt** | Operator | Bias to action, momentum, execution |

### Domain Experts

| Agent | Domain | Best For |
|-------|--------|----------|
| **Warren Buffett** | Finance | Investment, valuation, capital allocation |
| **Steve Jobs** | Product | Design, simplicity, user experience |
| **Ernest Hemingway** | Writing | Clarity, economy, truth in prose |
| **Seth Godin** | Marketing | Positioning, tribes, remarkable products |
| **Admiral Stavridis** | Defense | Strategic leadership, coalitions, government |
| **Richard Feynman** | Science | First principles, simplifying complexity |
| **Dario & Daniela Amodei** | AI | Safety, responsible scaling |
| **Jensen Huang** | AI Infrastructure | Hardware, platforms, ecosystems |
| **Peter Drucker** | Consulting | Management effectiveness, organization |
| **Clayton Christensen** | Strategy | Disruption, jobs-to-be-done |
| **Dwight Eisenhower** | Operations | Coalition building, prioritization |
| **Reid Hoffman** | Entrepreneurship | Networks, blitzscaling, pivots |
| **Marc Andreessen** | Tech Investment | Bold bets, product-market fit |
| **Ben Horowitz** | Execution | Hard decisions, wartime leadership |
| **Brené Brown** | Emotional Intelligence | Vulnerability, courage, difficult conversations |
| **Adam Grant** | Creativity/Rethinking | Intellectual humility, challenging assumptions |
| **Mel Robbins** | Self-Help/Action | Overcoming procrastination, motivation, bias to action |
| **Arnold Schwarzenegger** | Physical Mastery | Discipline, mental toughness, goal visualization |
| **Bo Jackson** | Elite Athleticism | Multi-domain excellence, resilience, natural talent |

### The Mediator (Escalation Resource)

| Agent | Role |
|-------|------|
| **Chris Voss** | Breaks impasses, finds alignment through FBI negotiation tactics |

*Chris does not count toward the Rule of Three. He enters only during Phase 3.5 when triggered by impasse, cross-domain conflict, or explicit request.*

### The Arbiter

| Agent | Role |
|-------|------|
| **Marcus Aurelius** | Final judge — synthesizes all perspectives |

---

## Decision Categories & Default Panels

| Decision Type | Default Panel |
|--------------|---------------|
| Strategic Business | Marshall + Christensen + Buffett |
| Product Launch | Jobs + Godin + Disney |
| Investment | Buffett + Taleb + Andreessen |
| Operations | Eisenhower + Horowitz + Roosevelt |
| Risk Assessment | Taleb + Marshall + Stavridis |
| Technology | Huang + Feynman + Andreessen |
| Writing | Hemingway + Godin + Jobs |
| Startup/Scaling | Hoffman + Horowitz + Christensen |
| AI/ML | Amodei + Huang + Feynman |
| Defense/Government | Stavridis + Eisenhower + Marshall |
| Management | Drucker + Eisenhower + Horowitz |
| Consulting | Drucker + Buffett + Marshall |
| Personal Development | Brown + Robbins + Grant |
| Creativity & Innovation | Grant + Disney + Feynman |
| Physical & Discipline | Schwarzenegger + Jackson + Roosevelt |
| Action & Motivation | Robbins + Roosevelt + Schwarzenegger |
| Multi-Domain Success | Jackson + Hoffman + Grant |

---

## Commands Reference

### Core Deliberation
| Command | Action |
|---------|--------|
| `/convene-council` | Start full 5-phase deliberation |
| `Council convenes: [question]` | Natural language invocation |
| `Council convenes with X, Y, Z: [question]` | Custom panel selection |

### Quick Access
| Command | Action |
|---------|--------|
| `/qc [agent]: [question]` | Quick single-agent consult |
| `/quick-council: [question]` | Abbreviated 3-agent take (no debate) |
| `/lens [perspective]: [question]` | View through optimist/realist/pessimist/operator lens |

### Post-Deliberation
| Command | Action |
|---------|--------|
| `/appeal [topic]: [reason]` | Reopen judgment with new information |
| `/log-outcome [topic]: [result]` | Record what happened for learning |
| `/calibration-report` | View agent accuracy stats |
| `/pending-outcomes` | See decisions awaiting outcome logging |

### Customization
| Command | Action |
|---------|--------|
| `/customize` | Open customization menu |
| `/add-agent [name]: [description]` | Add custom agent |
| `/set-default [category]: [agents]` | Set default panel |
| `/favorite [agent]` | Prioritize in suggestions |
| `/exclude [agent]` | Remove from auto-selection |
| `/preferences` | View current settings |

### Maintenance
| Command | Action |
|---------|--------|
| `/refresh-agent [name]` | Update living agent profile |
| `/scout-masterclass` | Find new agent candidates |
| `/list-agents` | Show full roster |

---

## File Structure

```
board-of-directors/
├── rules/
│   ├── COUNCIL.md                # Master orchestration rules
│   ├── AGENT_ROUTER.md           # Decision classification & panels
│   ├── ESCALATION_PROTOCOL.md    # Mediator trigger conditions
│   ├── APPEAL_PROTOCOL.md        # Reopening judgments
│   ├── UNKNOWN_REQUESTS.md       # Edge case handling
│   ├── AGENT_UPDATE_PROTOCOL.md  # Keeping profiles current
│   └── CONFIDENCE_CALIBRATION.md # Validating predictions
├── agents/
│   ├── perspective/              # Core lens agents (4)
│   ├── domain/                   # Subject matter experts (19)
│   ├── mediator/                 # Chris Voss (1)
│   ├── arbiter/                  # Marcus Aurelius (1)
│   └── custom/                   # Your custom agents
├── templates/
│   ├── individual-report.md
│   ├── combined-report.md
│   ├── debate-transcript.md
│   └── final-judgment.md
├── examples/
│   └── complete-deliberation-example.md
├── scout-reports/                # MasterClass scout output
├── user-preferences.md           # Your customization settings
├── deliberation-log.md           # Session history
├── outcome-log.md                # Decision results
├── scout-log.md                  # Agent discovery history
├── agent-statistics.md           # Usage & accuracy tracking
└── README.md                     # This file

global_workflows/
├── convene-council.md            # Main invocation
├── quick-consult.md              # Fast single-agent access
├── log-deliberation.md           # Session logging
├── log-outcome.md                # Result tracking
├── customize-roster.md           # Personalization
└── masterclass-scout.md          # Roster growth
```

---

## Best Practices

1. **Be Specific**: Vague questions get vague analysis. Include context, constraints, and stakes.

2. **Trust the Process**: Let all phases complete before making decisions.

3. **Embrace Conflict**: The value is in surfacing disagreement, not false consensus.

4. **Challenge the Arbiter**: Marcus Aurelius welcomes pushback. His judgment can be appealed with new information.

5. **Log Outcomes**: Use `/log-outcome` to track what happened. This improves calibration over time.

6. **Use Quick Consult**: Not every question needs full deliberation. `/qc` is faster for simple questions.

7. **Iterate**: First-round analysis often surfaces questions that warrant a second round.

---

## Example Session

**User**: Council convenes: We received a $5M acquisition offer for our SaaS startup. We're profitable but growing slowly. Should we take it?

**System**:
1. Selects: Warren Buffett (valuation), Nassim Taleb (downside), Reid Hoffman (scaling potential)
2. Generates three individual reports
3. Synthesizes combined report showing consensus and tensions
4. Conducts debate between agents
5. Marcus Aurelius renders final judgment with recommendation and next steps

**Later**:
```
/log-outcome acquisition: Declined offer. 18 months later, raised Series A at $15M valuation. Right call.
```

---

## Installation

1. Copy the `board-of-directors/` directory to your Antigravity workspace
2. Copy `global_workflows/` to your global workflows location
3. Copy `GEMINI.md` to your workspace root
4. The rules and workflows will automatically activate
5. Use `/convene-council` or natural language to invoke

---

*Board of Directors v1.3 | Strategic Decision-Making for Antigravity IDE*
*25 Agents | 17 Decision Categories | 5-Phase Deliberation | Outcome Tracking | Confidence Calibration*
