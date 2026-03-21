---
name: brief-council
description: "Socratic intake process to gather full context before council deliberation. Ensures agents have the information they need to give good advice."
trigger:
  - "/brief-council"
  - "/context-briefing"
  - "/prepare-deliberation"
  - "Brief the council"
  - "Let me give context first"
global: true
---

# Brief Council — Context Gathering Workflow

## Purpose

Extract the full context needed for quality deliberation through structured Socratic questioning.

---

## Workflow Trigger

**Automatic Offer**: When `/convene-council` is invoked for complex questions
**Manual**: `/brief-council` or "Brief the council first"
**Skip**: `/convene-council --skip-briefing`

---

## Question Sets by Intake Mode

### Quick Mode (4 questions)
```yaml
questions:
  - id: q1_decision
    text: "What decision are you facing? (One sentence)"
    required: true
    
  - id: q2_options
    text: "What are your options?"
    required: true
    
  - id: q3_stakes
    text: "What happens if you choose wrong?"
    required: true
    
  - id: q4_timeline
    text: "When must this be decided?"
    required: true
```

### Standard Mode (8 questions)
```yaml
questions:
  # Surface the Decision
  - id: q1_decision
    text: "What decision are you facing?"
    required: true
    follow_up: "Is this the actual decision, or a symptom of a deeper one?"
    
  - id: q2_options
    text: "What are your options as you see them?"
    required: true
    
  # Understand Stakes
  - id: q3_downside
    text: "What happens if you choose wrong?"
    required: true
    
  - id: q4_inaction
    text: "What happens if you do nothing?"
    required: true
    
  - id: q5_timeline
    text: "What's your timeline for deciding and seeing results?"
    required: true
    
  # Map Constraints
  - id: q6_resources
    text: "What resources do you have available?"
    required: false
    
  - id: q7_nonneg
    text: "What's absolutely non-negotiable?"
    required: false
    
  # Surface Subtext
  - id: q8_fear
    text: "What are you really afraid of?"
    required: false
```

### Full Mode (15 questions)
```yaml
questions:
  # Phase 1: Surface the Decision
  - id: q1_decision
    text: "What decision are you facing? State it as simply as possible."
    required: true
    
  - id: q2_options
    text: "What are your options as you see them?"
    required: true
    
  - id: q3_deeper
    text: "Is this the actual decision, or a symptom of a deeper one?"
    required: true
    
  # Phase 2: Understand Stakes
  - id: q4_downside
    text: "What happens if you choose wrong? Worst realistic outcome."
    required: true
    
  - id: q5_inaction
    text: "What happens if you do nothing? What does delay cost?"
    required: true
    
  - id: q6_stakeholders
    text: "Who else is affected by this decision?"
    required: true
    
  - id: q7_timeline
    text: "What's the timeline? When must it be decided? When would results show?"
    required: true
    
  # Phase 3: Map Constraints
  - id: q8_resources
    text: "What resources are available? Money, time, relationships, skills."
    required: true
    
  - id: q9_nonneg
    text: "What's non-negotiable? What constraints cannot change?"
    required: true
    
  - id: q10_tried
    text: "What have you already tried? What worked, what didn't?"
    required: false
    
  - id: q11_missing
    text: "What information are you missing that would help?"
    required: false
    
  # Phase 4: Surface Subtext
  - id: q12_fear
    text: "What are you afraid of? The real fear, not the polished version."
    required: true
    
  - id: q13_hope
    text: "What do you secretly want the answer to be?"
    required: true
    
  - id: q14_friend
    text: "What would you advise a friend in this situation?"
    required: false
    
  - id: q15_beneath
    text: "What's the question beneath the question?"
    required: true
```

---

## Briefing Document Template

```markdown
# Council Briefing — {{TOPIC}}

**Prepared**: {{TIMESTAMP}}
**Intake Mode**: {{MODE}}
**Quality Score**: {{SCORE}}/100

---

## The Decision

{{Q1_DECISION}}

### Deeper Framing
{{Q3_DEEPER}}

---

## Options Under Consideration

{{#each OPTIONS}}
{{INDEX}}. {{OPTION}}
{{/each}}

---

## Stakes & Timeline

| Dimension | Assessment |
|-----------|------------|
| **Upside if right** | {{UPSIDE}} |
| **Downside if wrong** | {{Q4_DOWNSIDE}} |
| **Cost of inaction** | {{Q5_INACTION}} |
| **Decision deadline** | {{TIMELINE_DECIDE}} |
| **Results visible** | {{TIMELINE_RESULTS}} |

---

## Stakeholders

{{Q6_STAKEHOLDERS}}

---

## Constraints

### Resources Available
{{Q8_RESOURCES}}

### Non-Negotiables
{{Q9_NONNEG}}

### Flexible Constraints
{{FLEXIBLE_CONSTRAINTS}}

---

## Prior Attempts

{{Q10_TRIED}}

---

## Information Gaps

{{Q11_MISSING}}

---

## Subtext

### The Real Fear
> {{Q12_FEAR}}

### Desired Outcome
> {{Q13_HOPE}}

### The Deeper Question
> {{Q15_BENEATH}}

### Outside Perspective
> "What would I advise a friend?" — {{Q14_FRIEND}}

---

## Attached Context

{{#if ATTACHMENTS}}
{{#each ATTACHMENTS}}
- [{{NAME}}]({{PATH}})
{{/each}}
{{else}}
*No documents attached*
{{/if}}

---

## Memory Context

{{#if MEMORY_CONTEXT}}
### Relevant Past Discussions
{{#each MEMORY_CONTEXT}}
- {{DATE}}: {{SUMMARY}}
{{/each}}
{{else}}
*No relevant past conversations found*
{{/if}}

---

*Briefing ready for council deliberation*
```

---

## Quality Scoring

Calculate briefing completeness:

```javascript
function calculateQualityScore(briefing) {
  let score = 0;
  
  // Core elements (60 points)
  if (briefing.decision) score += 15;
  if (briefing.options?.length >= 2) score += 10;
  if (briefing.downside) score += 10;
  if (briefing.timeline) score += 10;
  if (briefing.stakeholders) score += 10;
  if (briefing.constraints) score += 5;
  
  // Subtext elements (25 points)
  if (briefing.fear) score += 10;
  if (briefing.desired_outcome) score += 5;
  if (briefing.deeper_question) score += 10;
  
  // Enhancement elements (15 points)
  if (briefing.prior_attempts) score += 5;
  if (briefing.attachments?.length > 0) score += 5;
  if (briefing.memory_context?.length > 0) score += 5;
  
  return score;
}
```

### Score Interpretation

| Score | Rating | Guidance |
|-------|--------|----------|
| 90-100 | Excellent | Proceed with confidence |
| 75-89 | Good | Council has what they need |
| 60-74 | Adequate | Some assumptions required |
| 45-59 | Thin | Consider adding context |
| <45 | Insufficient | Recommend more briefing |

---

## Conversation Flow

### Starting the Briefing

```
User: /brief-council

System: Let's prepare a thorough briefing for the council.

I'll ask you a series of questions to make sure they have the full picture. 
This typically takes 3-5 minutes and significantly improves the quality of 
their advice.

**Intake mode**: [Quick (4 questions)] [Standard (8 questions)] [Full (15 questions)]

Or: [Skip to direct briefing] — paste your own context
```

### During Intake

```
System: [Question 5 of 8]

What happens if you do nothing? What does delay cost?

User: If I do nothing, the contract offer expires in 30 days and the board 
opportunity might go to someone else while I'm deliberating.

System: So inaction has real costs on both fronts. Two more questions about 
constraints, then we'll get to the deeper stuff.

[Question 6 of 8]
What resources do you have available? Think money, time, relationships, skills.
```

### Completing the Briefing

```
System: Briefing complete. Here's what I'll share with the council:

[Displays briefing document]

**Quality Score**: 82/100 (Good)

✓ Clear decision and options
✓ Stakes well-defined
✓ Subtext surfaced
○ No documents attached (optional)

Ready to convene? [Yes, convene council] [Add more context] [Edit briefing]
```

---

## Integration with Council

### Briefing Injection

The briefing is prepended to each agent's prompt:

```markdown
## Council Briefing

[Full briefing document]

---

## Your Task

You are {{AGENT_NAME}}. Based on the briefing above, provide your analysis 
following your documented frameworks and decision-making approach.

Pay particular attention to:
- The stated decision AND the deeper question identified
- The real fear surfaced during intake
- What the person secretly hopes the answer is (potential bias to address)
```

### Agent Acknowledgment

Agents explicitly reference briefing elements:

```markdown
### Warren Buffett — Individual Report

**Context Acknowledgment**: I note that you've identified fear of regret 
as central to this decision, and that you're hoping someone validates the 
riskier path. I'll address both.

**Analysis**: ...
```

---

## Commands Reference

| Command | Action |
|---------|--------|
| `/brief-council` | Start standard 8-question intake |
| `/brief-council --quick` | Quick 4-question intake |
| `/brief-council --full` | Full 15-question intake |
| `/brief-council --direct` | Paste context without questions |
| `/brief-council --attach` | Add documents to briefing |
| `/show-briefing` | View current briefing |
| `/edit-briefing` | Modify before convening |
| `/convene-council` | Auto-offers briefing for complex questions |
| `/convene-council --skip-briefing` | Skip directly to deliberation |

---

## Best Practices

### When to Use Full Intake
- Career moves, major pivots
- Decisions with >$100K impact
- Irreversible or hard-to-reverse choices
- When you feel genuinely conflicted

### When to Use Standard Intake
- Consulting engagement decisions
- Partnership evaluations
- Hiring/team decisions
- Investment opportunities

### When to Use Quick Intake
- Pricing decisions
- Meeting prioritization
- Simple trade-offs
- Validation of decisions mostly made

### When to Skip
- Follow-up to previous deliberation (context already exists)
- Very simple questions
- Quick consults (`/qc`)
- When you've pre-written a detailed brief

---

*Brief Council Workflow v1.0*
*Better Briefing → Better Deliberation*
