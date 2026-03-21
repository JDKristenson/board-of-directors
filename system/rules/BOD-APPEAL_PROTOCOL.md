# Appeal Protocol — Reopening Judgments

## Purpose

Marcus Aurelius's judgments are final but not infallible. This protocol governs when and how deliberations can be reopened, ensuring the system learns from new information without enabling endless second-guessing.

---

## Grounds for Appeal

An appeal may be filed when:

### 1. New Material Information
Information emerges that was unavailable during original deliberation and would likely change the analysis.

**Examples**:
- "I just learned the client has a competing bid at 2x our price"
- "The timeline changed—we now have 6 months instead of 3"
- "A key assumption was wrong—they don't actually need the feature we prioritized"

**Not valid**:
- Information that was available but not mentioned
- Feelings that have changed without new facts
- Buyer's remorse

### 2. Changed Circumstances
External conditions have shifted materially since the judgment.

**Examples**:
- Market conditions changed
- Key personnel changed
- Regulatory environment shifted
- New competitor entered

**Not valid**:
- Circumstances you should have anticipated
- Minor fluctuations within expected variance

### 3. Flawed Process
The original deliberation had a procedural flaw that may have affected the outcome.

**Examples**:
- Wrong panel for the decision type
- Agent spoke outside their expertise
- Key perspective was missing
- Mediation should have been triggered but wasn't

**Not valid**:
- Disagreement with the process design itself
- Preference for a different panel after the fact

### 4. Implementation Barrier
The recommended action proves impossible or far more difficult than anticipated.

**Examples**:
- "I tried to execute the recommendation but hit an unexpected blocker"
- "The approach requires resources I don't actually have"
- "The stakeholder I needed won't participate"

**Not valid**:
- Difficulty you should have anticipated
- Unwillingness rather than inability

---

## Appeal Process

### Step 1: File the Appeal

State clearly:
```
I'm appealing the judgment on [topic] because:
- Ground: [New information / Changed circumstances / Flawed process / Implementation barrier]
- Specific reason: [What changed or what was missed]
- What I'm asking for: [Re-deliberation / Panel change / Scope adjustment]
```

**Or use shorthand**:
```
/appeal [topic]: [reason]
Appeal: The partnership decision—I just learned they have a competing offer
Reopen: The pricing judgment—market rates have shifted 20%
```

### Step 2: Appeal Screening

Before reopening, the system evaluates:

| Question | If Yes | If No |
|----------|--------|-------|
| Is this new information material? | Proceed | Deny appeal |
| Would this likely change the analysis? | Proceed | Deny appeal |
| Is this genuinely new or just repackaged? | Proceed | Deny appeal |
| Has enough time passed for meaningful change? | Proceed | Deny appeal |

**Cooling Off Period**: Appeals filed within 1 hour of judgment require explicit override. This prevents impulsive reopening.

### Step 3: Determine Appeal Type

| Appeal Type | Process | When to Use |
|-------------|---------|-------------|
| **Minor Adjustment** | Marcus Aurelius revisits with new info, issues amended judgment | Small new facts, same panel would reach same conclusion |
| **Partial Re-Deliberation** | One agent re-analyzes, Marcus re-weighs | New info affects one domain only |
| **Full Re-Deliberation** | Complete new 5-phase process | Fundamentally different situation |
| **Panel Swap** | New panel assigned, full deliberation | Original panel was wrong for the question |

### Step 4: Execute Appeal

**For Minor Adjustment**:
```markdown
## Amended Judgment — [Topic]

**Original Judgment**: [Date, summary]

**New Information**: [What changed]

**Revised Analysis**: [How this changes things]

**Amended Recommendation**: [Updated guidance]

**What Remains Unchanged**: [Parts of original judgment that still hold]
```

**For Full Re-Deliberation**:
- Original deliberation is archived (not deleted)
- New deliberation proceeds through all phases
- Final judgment explicitly addresses what changed from original

---

## Appeal Limits

To prevent analysis paralysis:

| Limit | Rule |
|-------|------|
| **Appeals per decision** | Maximum 2 appeals on same decision |
| **Time window** | Appeals must be filed within 30 days of original judgment |
| **Cooling off** | Minimum 1 hour between judgment and appeal (unless emergency) |
| **Scope creep** | Appeal must address the original question, not expand scope |

After 2 appeals, the decision is **final**. Further reconsideration requires:
- 90+ days elapsed, AND
- Genuinely material new circumstances, AND
- Explicit acknowledgment that this is exceptional

---

## Appeal Outcomes

### Appeal Granted
```markdown
## Appeal Granted — [Topic]

**Original Judgment**: [Date]
**Appeal Ground**: [Which ground]
**New Information**: [Summary]
**Appeal Type**: [Minor/Partial/Full/Panel Swap]

[Proceed with appropriate re-deliberation]
```

### Appeal Denied
```markdown
## Appeal Denied — [Topic]

**Original Judgment**: [Date]
**Appeal Ground Claimed**: [What user claimed]
**Reason for Denial**: [Why this doesn't meet appeal criteria]

**Original judgment stands.**

**If you still have concerns**: [Guidance on what would constitute valid grounds]
```

---

## Special Cases

### Emergency Override
If circumstances require immediate action that contradicts the judgment:

```
/emergency-override: [situation]
```

This logs that you acted against the judgment with reasoning, for later review. No re-deliberation—just documentation.

### "What If" Exploration
If you want to explore how different assumptions would change the outcome *without* formally appealing:

```
/what-if [assumption]: How would this change the judgment?
```

This generates speculative analysis without reopening the formal judgment.

### Request for Clarification
If you don't understand the judgment but don't disagree:

```
/clarify: [specific question about the judgment]
```

Marcus Aurelius explains reasoning without re-deliberating.

---

## Logging Appeals

All appeals are logged in `deliberation-log.md`:

```markdown
## [APPEAL] 2025-01-26 — Partnership Decision

**Original Judgment**: 2025-01-24
**Appeal Ground**: New Information
**Reason**: Competing offer discovered at 2x price
**Appeal Type**: Partial Re-Deliberation
**Outcome**: Appeal granted, Buffett re-analyzed, judgment amended
**Amended Recommendation**: [Summary]
```

---

## Example Appeal Flow

**Original Deliberation** (Jan 20):
> Council recommends taking the $50K consulting contract despite tight timeline.

**New Information** (Jan 25):
> User learns client has history of scope creep and payment delays.

**Appeal Filed**:
```
/appeal consulting contract: New info—client has reputation for scope creep and late payment. Source is a trusted colleague who worked with them last year.
```

**Screening**:
- Is this material? Yes—changes risk profile significantly
- Would it change analysis? Likely—Taleb would have flagged this
- Is it new? Yes—not available during original deliberation

**Appeal Granted** → Partial Re-Deliberation (Taleb re-analyzes)

**Amended Judgment**:
> Given the new information about client reputation, the risk profile has shifted. Recommend either declining or restructuring with 50% upfront payment and tightly scoped deliverables. Original recommendation is withdrawn.

---

## Marcus Aurelius on Appeals

> "If someone is able to show me that what I think or do is not right, I will happily change, for I seek the truth, by which no one was ever truly harmed. The injury is to persist in one's own self-deception and ignorance."

The appeal process embodies this principle. New information is welcomed. But endless reconsideration without new substance is not wisdom—it is paralysis disguised as thoroughness.

---

*Appeal Protocol v1.0 | Reopening Judgments with Integrity*
