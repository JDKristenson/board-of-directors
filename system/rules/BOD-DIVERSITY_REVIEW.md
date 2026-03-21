# Diversity & Balance Review — Roster Health Audit

## Purpose

Ensure the Board of Directors maintains:
1. **Demographic diversity** — Gender, era, nationality, industry backgrounds
2. **Cognitive diversity** — Thinking styles, risk profiles, decision approaches
3. **Balance** — No single agent dominates due to profile construction or over-selection

This review runs quarterly (or on-demand) to identify imbalances and recommend corrections.

---

## Invocation

### Scheduled
```
Quarterly: First Monday of Jan, Apr, Jul, Oct at 9:00 AM
```

### Manual
```
/diversity-review
/roster-health
/balance-check
"Check the board for diversity"
"Are my agents balanced?"
```

---

## Review Dimensions

### Dimension 1: Demographic Diversity

Audit the roster across identity dimensions:

| Dimension | Categories | Target Distribution |
|-----------|------------|---------------------|
| **Gender** | Male, Female, Non-binary | No >70% single gender |
| **Era** | Ancient, Pre-modern, Modern, Contemporary | Representation across eras |
| **Nationality/Region** | Americas, Europe, Asia, Africa, Global | No >60% single region |
| **Industry Origin** | Tech, Finance, Military, Arts, Academia, Sports, Government | No >40% single industry |
| **Living Status** | Living, Historical | Mix of both |

#### Current Roster Audit (v1.3)

| Dimension | Distribution | Status |
|-----------|--------------|--------|
| **Gender** | Male: 23 (92%), Female: 2 (8%) | 🔴 Imbalanced |
| **Era** | Ancient: 1, Modern: 6, Contemporary: 18 | 🟡 Contemporary-heavy |
| **Region** | Americas: 18, Europe: 6, Global: 1 | 🟡 US-dominant |
| **Industry** | Tech: 7, Finance: 2, Military: 4, Arts: 2, Academia: 3, Sports: 2, Business: 5 | 🟡 Tech-heavy |
| **Living** | Living: 14, Historical: 11 | ✅ Balanced |

### Dimension 2: Cognitive Diversity

Audit thinking styles and decision approaches:

| Dimension | Spectrum | Agents |
|-----------|----------|--------|
| **Risk Orientation** | Risk-seeking ↔ Risk-averse | |
| | Risk-seeking | Disney, Roosevelt, Andreessen, Hoffman |
| | Balanced | Marshall, Drucker, Eisenhower |
| | Risk-averse | Taleb, Buffett |
| **Time Horizon** | Short-term ↔ Long-term | |
| | Short-term/Action | Roosevelt, Robbins, Horowitz |
| | Balanced | Marshall, Drucker, Voss |
| | Long-term | Buffett, Aurelius, Christensen |
| **Decision Style** | Intuitive ↔ Analytical | |
| | Intuitive | Disney, Jobs, Brown |
| | Balanced | Hoffman, Godin, Jackson |
| | Analytical | Feynman, Marshall, Taleb |
| **Optimism** | Optimistic ↔ Pessimistic | |
| | Optimistic | Disney, Robbins, Andreessen |
| | Balanced | Marshall, Drucker, Huang |
| | Pessimistic | Taleb, Horowitz (wartime) |
| **Communication** | Direct ↔ Diplomatic | |
| | Direct | Hemingway, Ramsay*, Taleb |
| | Balanced | Drucker, Marshall, Stavridis |
| | Diplomatic | Brown, Grant, Voss |

*If added

#### Cognitive Balance Assessment

| Spectrum | Distribution | Status |
|----------|--------------|--------|
| Risk Orientation | Balanced with slight risk-seeking tilt | ✅ Healthy |
| Time Horizon | Balanced | ✅ Healthy |
| Decision Style | Slight analytical bias | 🟡 Acceptable |
| Optimism | Balanced (by design) | ✅ Healthy |
| Communication | Direct-leaning | 🟡 Could add more diplomatic |

### Dimension 3: Agent Dominance Detection

Track whether any agent disproportionately influences outcomes:

#### Selection Frequency
```
Over last 20 deliberations:
- Warren Buffett: 14 (70%) ⚠️ High
- George Marshall: 12 (60%)
- Nassim Taleb: 11 (55%)
- Peter Drucker: 10 (50%)
- Theodore Roosevelt: 8 (40%)
...
- Bo Jackson: 1 (5%)
- Mel Robbins: 1 (5%)
```

**Warning Threshold**: >60% selection rate suggests over-reliance

#### Citation in Judgments
```
How often does Marcus cite each agent's reasoning as decisive:
- Warren Buffett: 9/14 (64%) ⚠️ High influence
- Nassim Taleb: 7/11 (64%) ⚠️ High influence
- Peter Drucker: 5/10 (50%)
...
```

**Warning Threshold**: >60% citation rate in judgments

#### Profile Length Analysis
```
Agent profile word counts:
- Dario Amodei: 2,847 words
- Warren Buffett: 2,654 words
- Peter Drucker: 2,612 words
- Average: 2,100 words
- Bo Jackson: 1,456 words
- Mel Robbins: 1,523 words
```

**Warning**: Profiles >25% above average may have unfair advantage

#### Framework Breadth Analysis
```
How broadly applicable are each agent's frameworks?

High Breadth (applies to most decisions):
- George Marshall (realist analysis) — Universal
- Warren Buffett (opportunity cost) — Universal
- Peter Drucker (effectiveness) — Universal

Medium Breadth:
- Steve Jobs (design thinking) — Product/UX focused
- Seth Godin (marketing) — Growth/positioning focused

Narrow Breadth:
- Bo Jackson (multi-sport) — Physical/performance focused
- Admiral Stavridis (defense) — Security/government focused
```

**Risk**: High-breadth agents get selected more, reinforcing dominance

---

## Diversity Scoring

### Overall Roster Health Score

Calculate a composite score (0-100):

```
DIVERSITY_SCORE = (
  (Gender_Score × 0.20) +
  (Era_Score × 0.10) +
  (Region_Score × 0.15) +
  (Industry_Score × 0.15) +
  (Cognitive_Score × 0.25) +
  (Dominance_Score × 0.15)
)

Where each sub-score:
- 100 = Ideal distribution
- 75 = Acceptable with minor gaps
- 50 = Significant imbalance
- 25 = Critical imbalance
```

### Current Score Estimate (v1.3 Roster)

| Dimension | Score | Notes |
|-----------|-------|-------|
| Gender | 35 | 92% male is significant gap |
| Era | 65 | Contemporary-heavy but acceptable |
| Region | 55 | US-dominant |
| Industry | 70 | Tech-heavy but diverse enough |
| Cognitive | 80 | Good spectrum coverage |
| Dominance | 60 | Some over-reliance on Buffett/Taleb |
| **Overall** | **61/100** | 🟡 Room for improvement |

---

## Rebalancing Recommendations

Based on current audit:

### Priority 1: Gender Diversity 🔴

**Current**: 2 female agents (Brown, [partial: Amodei duo])
**Target**: 5-7 female agents (20-28%)

**Recommended Additions**:
| Candidate | Domain | Why |
|-----------|--------|-----|
| Sara Blakely | Entrepreneurship | Bootstrap founder, complements Hoffman |
| Serena Williams | Elite Performance | Champion mindset, complements Jackson |
| Doris Kearns Goodwin | Leadership History | Historical decision patterns |
| Condoleezza Rice | Strategy/Diplomacy | National security, global perspective |
| Oprah Winfrey | Communication/Media | Influence, interviewing, platform building |

### Priority 2: Regional Diversity 🟡

**Current**: 72% US-based backgrounds
**Target**: <60% single region

**Recommended Additions**:
| Candidate | Region | Domain |
|-----------|--------|--------|
| Masayoshi Son | Japan/Asia | Tech investment, bold bets |
| Richard Branson | UK/Europe | Entrepreneurship, brand |
| Nelson Mandela | Africa | Leadership, reconciliation |
| Lee Kuan Yew | Singapore/Asia | Governance, nation-building |

### Priority 3: Dominance Mitigation 🟡

**Issue**: Buffett selected in 70% of deliberations

**Solutions**:
1. **Soft cap**: If agent selected >50% of last 10 deliberations, suggest alternatives
2. **Rotation encouragement**: "Buffett was on your last 3 panels. Consider Christensen or Drucker for fresh perspective?"
3. **Profile balancing**: Review high-word-count profiles for trimming
4. **Framework tagging**: Tag frameworks by specificity to avoid over-broad agents

---

## Review Report Format

### Quarterly Review Output

```markdown
# Diversity & Balance Review — Q1 2025

## Executive Summary

**Overall Health Score**: 61/100 (🟡 Room for improvement)

**Critical Issues**:
- Gender diversity at 8% female (target: 20%+)

**Watch Items**:
- Buffett selection rate at 70% (potential over-reliance)
- US-origin agents at 72%

**Healthy Areas**:
- Cognitive diversity well-balanced
- Living/historical mix appropriate
- Risk orientation spectrum covered

---

## Detailed Audit

### Demographic Diversity
[Full breakdown by dimension]

### Cognitive Diversity
[Spectrum analysis]

### Agent Dominance
[Selection and citation patterns]

---

## Recommendations

### Immediate Actions
1. Add 2-3 female agents to roster

### Medium-term Actions
1. Add 1-2 non-US/Europe agents
2. Implement soft selection caps

### Monitoring
1. Track Buffett selection rate
2. Review after next 10 deliberations

---

## Next Review

**Scheduled**: April 7, 2025
**Focus Areas**: Gender progress, dominance patterns

---

*Review Generated: January 6, 2025*
*Reviewer: Diversity & Balance System v1.0*
```

---

## Integration Points

### With Agent Router
When selecting panels, consider:
```
IF agent.selection_rate > 0.50 in last 10:
  SHOW warning: "[Agent] has been on 50%+ of recent panels. 
  Consider [alternative] for fresh perspective?"
```

### With Scout System
Weight diversity gaps in candidate scoring:
```
diversity_bonus = 0
IF candidate.gender == underrepresented: diversity_bonus += 15
IF candidate.region == underrepresented: diversity_bonus += 10
IF candidate.industry == underrepresented: diversity_bonus += 5

TOTAL_SCORE += diversity_bonus
```

### With Statistics Tracking
Add diversity fields to `agent-statistics.md`:
```markdown
## Diversity Metrics

| Agent | Gender | Era | Region | Industry | Last Selected |
|-------|--------|-----|--------|----------|---------------|
| Buffett | M | Modern | US | Finance | 2025-01-25 |
| Brown | F | Contemporary | US | Academia | 2025-01-20 |
...
```

---

## Automated Alerts

### Selection Imbalance Alert
```
⚠️ Diversity Alert: Warren Buffett has been selected for 7 of your 
last 10 deliberations. Consider rotating to ensure diverse perspectives.

Suggested alternatives for finance/investment questions:
- Clayton Christensen (strategy/disruption angle)
- Marc Andreessen (growth/tech angle)
- Nassim Taleb (risk/downside angle)
```

### Roster Imbalance Alert
```
📊 Quarterly Diversity Check: Your roster is 92% male.

Top candidates to improve gender diversity:
1. Sara Blakely (Entrepreneurship) — Score: 79
2. Serena Williams (Elite Performance) — Score: 75
3. Doris Kearns Goodwin (Leadership History) — Score: 72

Run `/scout-masterclass --diversity` for full analysis.
```

---

## Commands Reference

| Command | Action |
|---------|--------|
| `/diversity-review` | Full quarterly-style audit |
| `/balance-check` | Quick dominance check |
| `/roster-demographics` | Demographic breakdown only |
| `/roster-cognitive` | Cognitive diversity breakdown only |
| `/dominance-report` | Agent selection/citation patterns |
| `/rebalance-suggestions` | Recommendations for improving diversity |

---

*Diversity & Balance Review v1.0*
*Ensuring the Board Represents Multiple Perspectives*
