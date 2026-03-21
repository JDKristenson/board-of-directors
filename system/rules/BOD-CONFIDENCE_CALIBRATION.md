# Confidence Calibration — Validating Agent Predictions

## Purpose

Agents report confidence levels (High/Medium/Low) with every recommendation. But are these meaningful? Does "High Confidence" actually predict success?

Confidence Calibration tracks the relationship between stated confidence and actual outcomes, enabling:
- Identification of over/underconfident agents
- Adjustment of how much weight to give confidence signals
- System-wide accuracy improvement over time

---

## How Calibration Works

### Data Collection
Every deliberation captures:
- Agent name
- Confidence level stated
- Recommendation made
- (Later) Outcome observed via `/log-outcome`

### Calibration Calculation
For each confidence level, we track:
- **Stated**: How often agents claim this confidence
- **Accuracy**: What % of those claims led to successful outcomes
- **Calibration**: Is accuracy proportional to confidence?

**Well-Calibrated**: High confidence = high accuracy, Low confidence = lower accuracy
**Overconfident**: High confidence stated, but accuracy doesn't match
**Underconfident**: Low confidence stated, but accuracy is actually high

---

## Calibration Report

Access via:
```
/calibration-report
```

### Sample Output

```markdown
## Confidence Calibration Report
**Based on**: 47 logged outcomes
**Period**: 2024-07-01 to 2025-01-26

---

### System-Wide Calibration

| Confidence | Times Stated | Success Rate | Expected | Calibration |
|------------|--------------|--------------|----------|-------------|
| High | 28 | 82% | 80%+ | ✅ Well-calibrated |
| Medium | 14 | 64% | 50-80% | ✅ Well-calibrated |
| Low | 5 | 60% | <50% | ⚠️ Underconfident |

**Interpretation**: 
- High confidence signals are reliable—trust them
- Medium confidence is appropriately uncertain
- Low confidence may be too cautious—outcomes often better than expected

---

### Agent-Level Calibration

| Agent | High Conf Accuracy | Medium Conf Accuracy | Low Conf Accuracy | Assessment |
|-------|-------------------|---------------------|-------------------|------------|
| Warren Buffett | 90% (10/11) | 67% (4/6) | N/A | ✅ Excellent |
| Nassim Taleb | 60% (3/5) | 75% (3/4) | 100% (2/2) | ⚠️ Overconfident on High |
| Peter Drucker | 100% (5/5) | 50% (1/2) | N/A | ✅ Good (small sample) |
| George Marshall | 75% (6/8) | 60% (3/5) | N/A | ✅ Slightly overconfident |
| Seth Godin | 67% (2/3) | N/A | N/A | ⚠️ Small sample |

---

### Recommendations

1. **Trust Buffett's High Confidence**: 90% accuracy rate on high-confidence calls
2. **Discount Taleb's High Confidence**: Only 60% accurate—weight his Medium/Low equally
3. **Seek more data on Godin**: Only 3 data points, insufficient for calibration
4. **Low confidence often wrong direction**: System-wide, low confidence = 60% success

---

### Sample Size Warnings

Agents with fewer than 5 outcomes are flagged as insufficient data:
- Steve Jobs (2 outcomes)
- Admiral Stavridis (1 outcome)
- Brené Brown (0 outcomes)

*Calibration improves with more logged outcomes. Use `/log-outcome` consistently.*
```

---

## Calibration Metrics

### Per-Agent Metrics

```yaml
agent_calibration:
  Warren Buffett:
    total_recommendations: 17
    outcomes_logged: 11
    high_confidence:
      stated: 11
      successful: 10
      accuracy: 90%
    medium_confidence:
      stated: 6
      successful: 4
      accuracy: 67%
    low_confidence:
      stated: 0
      successful: N/A
      accuracy: N/A
    overall_accuracy: 82%
    calibration_score: 0.92  # 1.0 = perfect calibration
    assessment: "Well-calibrated, slight overconfidence on medium"
```

### Calibration Score Formula

```
Calibration Score = 1 - Average(|Expected Accuracy - Actual Accuracy|)

Where Expected Accuracy:
  High = 0.85
  Medium = 0.65
  Low = 0.40
```

**Score Interpretation**:
- 0.90-1.00: Excellent calibration
- 0.75-0.89: Good calibration
- 0.60-0.74: Moderate calibration (some adjustment needed)
- Below 0.60: Poor calibration (significant adjustment needed)

---

## Using Calibration Data

### In Deliberations
When an agent states confidence, the system can annotate:

```markdown
### Warren Buffett — Individual Report

...

**Confidence**: High
*[Calibration note: Buffett's high-confidence calls have 90% accuracy (10/11). 
This signal is reliable.]*
```

Or for a poorly calibrated agent:

```markdown
### Nassim Taleb — Individual Report

...

**Confidence**: High
*[Calibration note: Taleb's high-confidence calls have only 60% accuracy (3/5). 
Consider weighting this as medium confidence.]*
```

### In Marcus's Judgment
The arbiter can reference calibration:

> "Buffett expresses high confidence, which his track record supports. 
> Taleb also claims high confidence, but his calibration data suggests 
> his high-confidence calls are no more reliable than his medium-confidence ones. 
> I weight Buffett's view more heavily on this basis."

---

## Calibration Improvement Actions

Based on calibration data, the system may suggest:

### For Overconfident Agents
```markdown
**Calibration Alert: Nassim Taleb**

Taleb's high-confidence recommendations have succeeded only 60% of the time,
below the expected 85%+ for high confidence.

**Suggested Actions**:
1. Internally discount his "High" to "Medium" 
2. Require corroboration from another agent when Taleb is high confidence
3. Update his profile to note tendency toward overconfidence

Apply adjustment? [Yes / No / Review data]
```

### For Underconfident Agents
```markdown
**Calibration Alert: George Marshall**

Marshall's low-confidence recommendations have succeeded 80% of the time,
well above the expected 40% for low confidence.

**Suggested Actions**:
1. Trust his hedged recommendations more than stated
2. Note in his profile that he tends to undersell certainty
3. Weight his "Low" as effectively "Medium"

Apply adjustment? [Yes / No / Review data]
```

---

## Data Requirements

Calibration requires minimum data to be meaningful:

| Level | Minimum Outcomes | Why |
|-------|------------------|-----|
| System-wide | 20 | Basic patterns visible |
| Per-agent | 5 | Agent-specific patterns |
| Per-confidence level | 3 | Level-specific accuracy |

Below these thresholds, calibration data is marked as **preliminary**.

---

## Calibration Over Time

Track how calibration evolves:

```
/calibration-trend [Agent]
```

```markdown
## Calibration Trend: Nassim Taleb

| Period | High Conf Accuracy | Calibration Score |
|--------|-------------------|-------------------|
| Q3 2024 | 50% (1/2) | 0.65 |
| Q4 2024 | 67% (2/3) | 0.72 |
| Q1 2025 | 60% (3/5) | 0.70 |

**Trend**: Stable, consistently overconfident on high-confidence calls
**Recommendation**: Maintain discount on high-confidence signals
```

---

## Integration Points

### With Outcome Logging
When outcome is logged, calibration data updates automatically:

```
/log-outcome partnership-deal: Success — 30% above projections

[System]: Outcome logged. Updating calibration data...
- Buffett (High confidence): Now 10/11 (91%)
- Taleb (Medium confidence): Now 4/5 (80%)
- Calibration report updated.
```

### With Agent Statistics
Calibration feeds into `agent-statistics.md`:

```markdown
## Nassim Taleb — Statistics

**Participation**: 15 deliberations
**Influence Rating**: Medium
**Calibration Score**: 0.70 (Overconfident on High)
**Recommendation**: Discount high-confidence by one level
```

### With Agent Profiles
Persistent calibration issues can be added to Known Biases:

```markdown
## Known Biases & Blind Spots

- Tends toward excessive caution (existing)
- **Calibration note**: High-confidence claims are only 60% accurate; 
  treat as medium confidence (added via calibration system)
```

---

## Commands Reference

| Command | Action |
|---------|--------|
| `/calibration-report` | Full calibration analysis |
| `/calibration [Agent]` | Single agent calibration |
| `/calibration-trend [Agent]` | Calibration over time |
| `/apply-calibration-adjustment` | Apply suggested adjustments |
| `/reset-calibration` | Clear calibration data (not recommended) |

---

## Privacy Note

Calibration data is derived from your logged outcomes. It reflects your experience with these agents in your context. It does not draw on any external data about how others have experienced the system.

---

*Confidence Calibration v1.0 | Trust but Verify*
