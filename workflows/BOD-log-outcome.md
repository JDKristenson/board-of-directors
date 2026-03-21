---
name: log-outcome
description: "Track what happened after a council deliberation. Records actions taken, outcomes observed, and lessons learned. Feeds into agent accuracy tracking over time."
trigger: 
  - "/log-outcome"
  - "/outcome"
  - "Here's what happened with..."
global: true
---

# Execution Tracking — Log Outcomes & Learn

## Purpose

Marcus Aurelius renders judgment. Then what? Without tracking outcomes, the system cannot:
- Learn which agents give reliable advice
- Calibrate confidence levels against reality
- Identify systematic blind spots
- Help you make better decisions over time

Execution Tracking closes the loop.

---

## Invocation

### Command Format
```
/log-outcome [deliberation-id or topic]: [what happened]
```

### Examples
```
/log-outcome consulting-contract: Declined as recommended. Board seat came through 6 weeks later. Right call.

/log-outcome partnership-deal: Took the deal against council advice. It's going well so far—6 months in, 20% ahead of projections.

/log-outcome pricing-decision: Raised prices as recommended. Lost 2 clients but revenue up 15% net. Partial win.
```

### Natural Language
```
"Here's what happened with the consulting contract decision"
"Update on the partnership—we closed it"
"The pricing experiment results are in"
```

---

## Outcome Entry Format

When logging an outcome, the system captures:

```markdown
## Outcome Log: [Topic]

**Original Deliberation**: [Date] | [Link to deliberation]
**Panel**: [Agents involved]
**Recommendation**: [What Marcus advised]

---

### Action Taken
- [ ] Followed recommendation fully
- [ ] Followed recommendation partially
- [ ] Did not follow recommendation
- [ ] Modified recommendation based on new info

**Description**: [What you actually did]

---

### Outcome Observed

**Timeframe**: [How long since decision]

**Result**: 
- [ ] Clear success
- [ ] Partial success
- [ ] Neutral / Too early to tell
- [ ] Partial failure
- [ ] Clear failure

**Evidence**: [Concrete outcomes — numbers, events, feedback]

---

### Retrospective

**Was the recommendation right?**
- [ ] Yes — good advice, good outcome
- [ ] Yes — good advice, bad outcome (execution or luck issue)
- [ ] No — bad advice, good outcome (got lucky)
- [ ] No — bad advice, bad outcome
- [ ] Unclear

**What did we learn?**
[Key insight for future decisions]

**Which agent was most/least accurate?**
- Most accurate: [Agent] — [Why]
- Least accurate: [Agent] — [Why]

---

**Logged**: [Timestamp]
```

---

## Outcome Categories

### Success Spectrum

| Rating | Definition | Example |
|--------|------------|---------|
| **Clear Success** | Achieved desired outcome, exceeded expectations | "Revenue up 40%, client renewed for 2 years" |
| **Partial Success** | Achieved main goal with some downsides | "Won the contract but margin was tight" |
| **Neutral** | No clear win or loss, or too early to judge | "Partnership is proceeding, no red flags yet" |
| **Partial Failure** | Missed main goal but salvaged something | "Lost the bid but got invited to next RFP" |
| **Clear Failure** | Did not achieve goal, negative consequences | "Deal fell through, damaged relationship" |

### Recommendation Alignment

| Alignment | Meaning |
|-----------|---------|
| **Followed Fully** | Did exactly what Marcus recommended |
| **Followed Partially** | Adopted core recommendation with modifications |
| **Did Not Follow** | Went a different direction than recommended |
| **Modified with New Info** | Changed approach based on information that emerged after deliberation |

---

## Aggregation & Learning

Outcomes feed into three learning mechanisms:

### 1. Agent Accuracy Tracking

Updated in `agent-statistics.md`:

```markdown
## Agent Accuracy (Based on Logged Outcomes)

| Agent | Deliberations | Followed | Success Rate | Notes |
|-------|---------------|----------|--------------|-------|
| Warren Buffett | 12 | 10 | 80% | Strong on capital allocation |
| Nassim Taleb | 8 | 6 | 67% | Overcautious on 2 deals that worked |
| Peter Drucker | 5 | 5 | 100% | Small sample but perfect so far |
```

### 2. Confidence Calibration

Compares agent confidence levels to actual outcomes:

```markdown
## Confidence Calibration

| Confidence Level | Times Used | Accuracy | Calibration |
|------------------|------------|----------|-------------|
| High | 24 | 83% | Well-calibrated |
| Medium | 18 | 61% | Slightly overconfident |
| Low | 7 | 71% | Underconfident — low confidence often right |
```

### 3. Decision Category Performance

Tracks which types of decisions the system handles well:

```markdown
## Category Performance

| Category | Deliberations | Success Rate | Notes |
|----------|---------------|--------------|-------|
| Consulting & Advisory | 8 | 87% | Strong domain |
| Investment & Capital | 5 | 60% | Taleb too conservative? |
| Product & Design | 3 | 100% | Small sample |
```

---

## Outcome Review Prompts

The system will prompt for outcome logging:

### 30-Day Check-In
```
You had a council deliberation on [topic] 30 days ago. 
Recommendation: [summary]

Do you have an outcome to log? 
- "/log-outcome [topic]: [what happened]"
- "Not yet — check back in 30 days"
- "Decision is still pending"
```

### 90-Day Review
```
Three deliberations from 90 days ago have no logged outcomes:
1. [Topic A] — Recommended: [X]
2. [Topic B] — Recommended: [Y]
3. [Topic C] — Recommended: [Z]

Would you like to log outcomes for any of these?
```

---

## Outcome Log Storage

Outcomes are stored in `outcome-log.md`:

```markdown
# Outcome Log

## 2025-01-26 — Consulting Contract Decision

**Original Deliberation**: 2025-01-20
**Panel**: Buffett, Drucker, Taleb
**Recommendation**: Decline contract, pursue board seat

**Action**: Followed fully — declined contract
**Outcome**: Clear Success
**Evidence**: Board seat confirmed 6 weeks later. Equity stake worth ~$50K on paper. AI advisory landed 2 new clients during the period.

**Retrospective**: 
- Recommendation was right
- Buffett's opportunity cost framing was key insight
- Taleb's optionality argument proved correct
- No agent was wrong on this one

---

## 2025-02-15 — Pricing Increase Decision

**Original Deliberation**: 2025-01-28
**Panel**: Godin, Buffett, Marshall
**Recommendation**: Raise prices 20%, accept some client loss

**Action**: Followed partially — raised 15%
**Outcome**: Partial Success
**Evidence**: Lost 2 of 12 clients (17%), but revenue up 12% net. Remaining clients did not push back.

**Retrospective**:
- Recommendation was directionally right
- Should have followed fully — the 15% was hedging unnecessarily
- Godin was most accurate: "The clients who leave weren't your clients"
- Marshall was too conservative on expected churn

---
```

---

## Commands Reference

| Command | Action |
|---------|--------|
| `/log-outcome [topic]: [result]` | Log an outcome for a past deliberation |
| `/outcomes` | View recent outcome logs |
| `/outcome-stats` | View agent accuracy and calibration stats |
| `/pending-outcomes` | See deliberations awaiting outcome logging |

---

## Integration with Deliberation Log

When an outcome is logged, the original entry in `deliberation-log.md` is updated:

**Before**:
```markdown
## 2025-01-20 — Consulting Contract

**Panel**: Buffett, Drucker, Taleb
**Question**: Should I take $180K 6-month defense contract?
**Recommendation**: Decline
**Outcome**: [Pending]
```

**After**:
```markdown
## 2025-01-20 — Consulting Contract

**Panel**: Buffett, Drucker, Taleb
**Question**: Should I take $180K 6-month defense contract?
**Recommendation**: Decline
**Outcome**: ✓ Success — Board seat came through, right call
**Outcome Logged**: 2025-03-15
```

---

## Why This Matters

> "We do not learn from experience. We learn from reflecting on experience." — John Dewey

The Board of Directors is only as good as its track record. Without outcome tracking:
- You're trusting agents without verification
- Confidence levels are arbitrary
- The system can't improve

With outcome tracking:
- Agents earn credibility through results
- You can weight advice from proven performers
- The system gets smarter over time

---

*Execution Tracking v1.0 | Closing the Loop on Decisions*
