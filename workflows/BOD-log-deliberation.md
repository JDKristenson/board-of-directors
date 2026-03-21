---
name: log-deliberation
description: "After a council deliberation is complete, use this workflow to log the results and update agent statistics. This maintains the historical record and tracks patterns over time.\n\nTrigger this AFTER Marcus Aurelius has rendered final judgment.\n\nExamples:\n\n<example>\nContext: A council deliberation just concluded\nuser: \"Log this deliberation\"\nassistant: \"I'll record this deliberation to the log and update the agent statistics.\"\n</example>"
trigger: "/log-deliberation"
global: true
---

# Log Deliberation — Post-Session Recording

After a council deliberation is complete, this workflow records the session and updates statistics.

## Step 1: Gather Session Information

Collect the following from the just-completed deliberation:

1. **Date**: Today's date in YYYY-MM-DD format
2. **Deliberation Number**: Increment from the last entry in deliberation-log.md
3. **Decision Question**: The original question posed to the council
4. **Panel Members**: The three agents selected (with their roles)
5. **Verdict Summary**: Marcus Aurelius's recommendation in 1-2 sentences
6. **Recommendation Category**: One of:
   - Proceed
   - Do Not Proceed
   - Proceed with Conditions
   - Defer
7. **Confidence Level**: High / Medium / Low
8. **Notable Dissents**: Any agent who strongly disagreed with the verdict
9. **Decisive Agent**: Which agent's analysis most influenced the verdict

## Step 2: Update Deliberation Log

Open the deliberation log file at:
`~/.gemini/antigravity/board-of-directors/deliberation-log.md`

Add a new entry at the top of the "Deliberation History" section:

```markdown
### [YYYY-MM-DD] Deliberation #[N]: [Brief Title]

**Decision**: [The question posed]

**Panel**:
- [Agent 1] — [Role]
- [Agent 2] — [Role]
- [Agent 3] — [Role]

**Arbiter**: Marcus Aurelius

**Verdict Summary**: [1-2 sentence summary]

**Recommendation**: [Category]

**Confidence**: [Level]

**Outcome**: *Pending*

**Notes**: [Dissents, decisive factors, observations]

---
```

## Step 3: Update Statistics Summary

In the deliberation log, update the Statistics Summary table:
- Increment "Total Deliberations"
- Increment the appropriate recommendation category
- Recalculate "Average Confidence"

## Step 4: Update Agent Statistics

Open `~/.gemini/antigravity/board-of-directors/agent-statistics.md` and for EACH of the three panel members:

1. Increment "Times Selected"
2. Recalculate "Selection Rate" (Times Selected ÷ Total Deliberations)
3. If this agent's position was adopted by Marcus, increment "Times Position Adopted by Marcus"
4. Recalculate "Influence Rate"
5. Update "Common Pairings" with the other two panel members
6. Add this decision type to "Decision Types"

## Step 5: Update Dominance Analysis

After updating individual stats, refresh the Dominance Analysis section:
- Re-sort Selection Frequency (Top 5)
- Re-sort Influence Rate (Top 5)
- Check for Underutilized Agents (selection rate < 5% after 20+ deliberations)
- Check for Potential Bias Alerts (influence rate > 70% for any agent)

## Step 6: Confirm Recording

Report back:

```
**Deliberation Logged**

- Session: Deliberation #[N] — [Brief Title]
- Date: [Date]
- Panel: [Agent 1], [Agent 2], [Agent 3]
- Verdict: [Recommendation]
- Statistics updated for all participants

Would you like to:
- Update the outcome once you've acted on this decision?
- Review agent statistics?
- See the full deliberation history?
```

---

## Updating Outcomes

When the user later reports what actually happened, update:

1. In deliberation-log.md, change "Outcome: *Pending*" to the actual result
2. In the Outcome Tracking table, add a row with:
   - Deliberation reference
   - Original recommendation
   - Whether it was followed
   - Actual outcome
   - Verdict accuracy assessment (Correct / Partially Correct / Incorrect)

---

*Log Deliberation Workflow v1.0*
