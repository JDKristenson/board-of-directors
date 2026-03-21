# Context Briefing — Socratic Intake Process

## Purpose

Before the Board of Directors can advise well, they need the full picture. This system uses structured questioning to extract:
- The real decision (not just the surface question)
- Constraints, stakes, and stakeholders
- What's already been tried
- Hidden concerns and fears
- The deeper question beneath the question

**Principle**: A well-framed question is half-answered. Garbage in, garbage out.

---

## Invocation

### Automatic (Recommended)
When you invoke `/convene-council`, the system offers:
```
Before we convene, would you like to:
1. Brief the council (recommended for complex decisions)
2. Go straight to deliberation (for simpler questions)

Choose "brief" for better results on high-stakes decisions.
```

### Manual
```
/brief-council
/context-briefing
/prepare-deliberation
"Let me give the board more context"
"I want to brief the council first"
```

### Skip Briefing
```
/convene-council --skip-briefing
```

---

## The Socratic Intake Process

### Phase 1: Surface the Decision (2-3 questions)

**Q1: What decision are you facing?**
> State it as simply as possible. One sentence if you can.

*Why this matters*: Forces clarity. Many "decisions" are actually multiple decisions tangled together.

**Q2: What are your options as you see them?**
> List the paths you're considering, even if some seem unlikely.

*Why this matters*: Reveals frame. Are they seeing only binary choices? Missing an obvious option?

**Q3: Is this the actual decision, or a symptom of a deeper one?**
> Sometimes "Should I fire Bob?" is really "Is this the right business model?"

*Why this matters*: Ensures we're solving the right problem.

---

### Phase 2: Understand the Stakes (3-4 questions)

**Q4: What happens if you choose wrong?**
> Describe the worst realistic outcome, not the catastrophic fantasy.

*Why this matters*: Calibrates risk. Some decisions feel high-stakes but aren't. Some feel low-stakes but aren't.

**Q5: What happens if you do nothing?**
> Is inaction an option? What does delay cost?

*Why this matters*: "Do nothing" is always an option. Understanding its cost clarifies urgency.

**Q6: Who else is affected by this decision?**
> Stakeholders: team, family, clients, partners, investors.

*Why this matters*: Decisions that seem individual often have collective impact.

**Q7: What's the timeline?**
> When must this be decided? When would results be visible?

*Why this matters*: Urgency shapes strategy. A decision needed tomorrow differs from one needed in a year.

---

### Phase 3: Map the Constraints (3-4 questions)

**Q8: What resources are available?**
> Money, time, relationships, skills, energy.

*Why this matters*: Recommendations must be feasible with actual resources.

**Q9: What's non-negotiable?**
> What constraints absolutely cannot change?

*Why this matters*: Separates hard constraints from soft preferences.

**Q10: What have you already tried?**
> Previous attempts, what worked, what didn't.

*Why this matters*: Avoids recommending what's already failed.

**Q11: What information are you missing?**
> What would you want to know that you don't?

*Why this matters*: Sometimes the right answer is "get more information first."

---

### Phase 4: Surface the Subtext (3-4 questions)

**Q12: What are you afraid of?**
> The real fear, not the polished version.

*Why this matters*: Fear often drives decisions more than logic. Naming it reduces its power.

**Q13: What do you secretly want the answer to be?**
> If you're honest, which way are you hoping this goes?

*Why this matters*: Reveals bias. If they're hoping for X, recommendations for Y need stronger justification.

**Q14: What would you advise a friend in this situation?**
> Remove yourself. What's the obvious answer from outside?

*Why this matters*: Often we know the answer but can't see it for ourselves.

**Q15: What's the question beneath the question?**
> Is this really about the decision stated, or something deeper?

*Why this matters*: "Should I take this job?" might really be "Am I selling out?" or "Can I trust myself?"

---

### Phase 5: Synthesize the Briefing

After intake, the system generates a structured briefing document:

```markdown
# Council Briefing — [Topic]

## The Decision
[One sentence summary of the actual decision]

## Options Under Consideration
1. [Option A]
2. [Option B]
3. [Option C]
4. [Do nothing / status quo]

## Stakes & Timeline
- **Upside if right**: [Best realistic outcome]
- **Downside if wrong**: [Worst realistic outcome]
- **Cost of inaction**: [What delay costs]
- **Decision deadline**: [When must be decided]
- **Results visible**: [When outcome becomes clear]

## Stakeholders
- **Primary**: [Who's most affected]
- **Secondary**: [Who else cares]
- **Hidden**: [Who might be affected that's not obvious]

## Constraints
- **Resources available**: [Money, time, relationships, skills]
- **Non-negotiables**: [Hard constraints]
- **Flexible**: [Soft constraints that could change]

## Prior Attempts
- **What's been tried**: [Previous approaches]
- **What worked**: [Partial successes]
- **What failed**: [And why]

## Information Gaps
- [What's unknown that would help]
- [What's unknowable]

## Subtext
- **Underlying fear**: [What they're really afraid of]
- **Desired outcome**: [What they're hoping for]
- **Deeper question**: [The question beneath the question]

## External Context
[Any documents, data, or background uploaded]

---

*Briefing prepared: [Timestamp]*
*Ready for council deliberation*
```

---

## Intake Modes

### Full Intake (15 questions)
For high-stakes, complex, or irreversible decisions.
- Takes 5-10 minutes
- Maximum context for the board
- Best for: career moves, major investments, strategic pivots

### Standard Intake (8 questions)
For moderate decisions with some complexity.
- Takes 3-5 minutes
- Covers essentials
- Best for: consulting engagements, hiring, partnerships

### Quick Intake (4 questions)
For simpler decisions or when you're time-pressed.
- Takes 1-2 minutes
- Core context only
- Best for: pricing decisions, meeting prioritization, simple trade-offs

### Direct Briefing (No questions)
Upload a document or paste context directly:
```
/brief-council --direct

[Paste your context here, or upload a document]
```

---

## Intake Conversation Example

**User**: `/brief-council`

**System**: Let's prepare the council. I'll ask you some questions to ensure they have the full picture.

**Q1: What decision are you facing?**

**User**: Whether to take a 6-month consulting contract or pursue a startup board seat.

**System**: Good. Two clear options. 

**Q2: Are there other options you haven't mentioned?**

**User**: I guess I could try to do both, or do neither and focus on growing my advisory practice.

**System**: So four options: contract only, board seat only, both, or neither. 

**Q3: What happens if you choose wrong?**

**User**: If I take the contract and the board seat was real, I've lost an opportunity that might not come back. If I chase the board seat and it falls through, I've lost $180K and 6 months.

**System**: Asymmetric risk—the board seat has more upside but more uncertainty. 

**Q4: What's your timeline?**

**User**: Contract decision needed in 30 days. Board seat is informal—no deadline but momentum matters.

**System**: Got it. Let me dig a bit deeper.

**Q5: What are you really afraid of?**

**User**: That I'll make the safe choice (contract) and regret not taking the swing (board seat). Or that I'll take the swing and fall flat.

**System**: So the fear is regret either way. What do you secretly hope the answer is?

**User**: Honestly, I want someone to tell me the board seat is worth the risk.

**System**: That's useful for the council to know. Last question:

**Q6: What's the deeper question here?**

**User**: Maybe... am I really ready to move from consultant to operator? Or should I stay in the advisory lane?

**System**: That reframe might be more important than the surface decision.

---

**Briefing generated. Ready to convene council?**

[Shows briefing document]

---

## Context Enhancement

### Document Upload
Add supporting materials:
```
/brief-council --attach

Supported formats:
- PDF (contracts, proposals, reports)
- DOCX (documents, memos)
- Images (charts, diagrams)
- URLs (relevant articles, company info)
```

### Memory Integration
Pull context from past conversations:
```
System: I see you've discussed this opportunity in 3 previous conversations.
Should I include that context in the briefing?

Relevant past discussions:
- Jan 10: Initial conversation about the board opportunity
- Jan 15: Concerns about the contract terms
- Jan 22: Discussion of advisory practice growth

[Include all] [Select specific] [Start fresh]
```

### Real-Time Research
Gather external context:
```
/brief-council --research

System: I'll search for relevant information about:
- [Company name] recent news
- [Industry] trends
- [Comparable decisions] in your network

[Researching...]
```

---

## Briefing Quality Score

Rate the completeness of context provided:

| Score | Quality | What's Missing |
|-------|---------|----------------|
| 90-100 | Excellent | Council has everything they need |
| 70-89 | Good | Minor gaps, can proceed |
| 50-69 | Adequate | Some assumptions will be needed |
| 30-49 | Thin | Significant gaps, recommendations may miss mark |
| <30 | Insufficient | Recommend more briefing before proceeding |

```
Briefing Quality Score: 78/100 (Good)

Strengths:
✓ Clear decision articulated
✓ Stakes well-defined
✓ Timeline specified

Gaps:
○ Stakeholder analysis incomplete
○ No documents attached
○ Resource constraints unclear

Proceed anyway? [Yes] [Add more context]
```

---

## Commands Reference

| Command | Action |
|---------|--------|
| `/brief-council` | Start full Socratic intake |
| `/brief-council --quick` | 4-question quick intake |
| `/brief-council --standard` | 8-question standard intake |
| `/brief-council --direct` | Skip questions, paste context |
| `/brief-council --attach` | Add documents to briefing |
| `/brief-council --research` | Add web research to context |
| `/show-briefing` | Display current briefing document |
| `/edit-briefing` | Modify briefing before convening |

---

## Integration with Deliberation

### Briefing Injected into Phase 1

Each agent receives the briefing before writing their individual report:

```markdown
## Context for Deliberation

[Full briefing document inserted here]

---

You are [Agent Name]. Based on the above context, provide your analysis...
```

### Agents Reference Briefing

Agents explicitly acknowledge key context:

**Warren Buffett's Report**:
> "Given that you've identified the deeper question as 'Am I ready to move from 
> consultant to operator?', my analysis focuses on that transition rather than 
> just the immediate financial trade-off..."

### Marcus References Briefing in Judgment

**Final Judgment**:
> "The stated question was about a contract versus a board seat. But the briefing 
> revealed the real question: whether you're ready for the identity shift from 
> advisor to operator. My judgment addresses both levels..."

---

## Best Practices

### When to Use Full Intake
- Career-defining decisions
- Decisions with >$100K impact
- Irreversible choices
- Decisions involving other people's lives/careers
- When you feel confused or conflicted

### When to Use Quick Intake
- Pricing and positioning decisions
- Meeting/opportunity triage
- Tactical choices with limited downside
- Decisions you've partially made but want validation

### When to Skip Intake
- You've already written a detailed brief
- Follow-up to a previous deliberation
- Very simple questions
- You just want one agent's perspective (`/qc`)

---

*Context Briefing v1.0*
*Better Context → Better Advice*
