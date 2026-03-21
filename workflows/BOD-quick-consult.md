---
name: quick-consult
description: "Bypass full council deliberation for quick single-agent perspectives or abbreviated takes. Use when you need speed over depth."
trigger: 
  - "/quick-consult"
  - "/qc"
  - "Quick take from..."
  - "What would [agent] say about..."
global: true
---

# Quick Consult — Single-Agent & Abbreviated Mode

## Purpose

Not every question needs a full 5-phase deliberation. Quick Consult provides fast access to individual agent perspectives or abbreviated multi-agent takes when speed matters more than exhaustive analysis.

---

## Invocation Options

### Single Agent Consult
```
/quick-consult [agent]: [question]
/qc buffett: Is this acquisition overpriced?
What would Taleb say about this risk?
Quick take from Roosevelt on whether to act now
```

### Abbreviated Council (3 agents, no debate)
```
/quick-council: [question]
Quick council: Should I take this meeting?
```

### Perspective Lens Only
```
/lens [perspective]: [question]
/lens pessimist: What could go wrong with this partnership?
/lens optimist: What's the upside potential here?
/lens realist: What are the actual probabilities?
/lens operator: What's the fastest path to execution?
```

---

## Response Formats

### Single Agent Response

When a single agent is consulted, they provide:

```markdown
## [Agent Name] — Quick Take

**On**: [Brief restatement of question]

**My View**: [2-3 sentence position]

**Key Consideration**: [The one thing you must not ignore]

**Confidence**: [High/Medium/Low]

**If you want more depth**: "Convene full council with [suggested panel]"
```

**Constraints**:
- No debate (only one voice)
- No Marcus Aurelius judgment (not enough perspectives to synthesize)
- Response should be under 150 words
- Agent speaks in their authentic voice

---

### Abbreviated Council Response

When quick-council is invoked:

```markdown
## Quick Council — [Topic]

**Panel**: [Agent 1], [Agent 2], [Agent 3]

### [Agent 1]:
[2-3 sentence take]

### [Agent 2]:
[2-3 sentence take]

### [Agent 3]:
[2-3 sentence take]

**Consensus**: [One sentence on where they agree, if anywhere]

**Tension**: [One sentence on where they disagree]

**For full deliberation**: `/convene-council` to proceed with debate and judgment
```

**Constraints**:
- No debate phase
- No mediation
- No Marcus Aurelius judgment
- Total response under 300 words
- Panel selected automatically based on question type

---

### Perspective Lens Response

When a perspective lens is requested:

```markdown
## [Perspective] Lens — [Topic]

**Through the eyes of the [Optimist/Realist/Pessimist/Operator]**:

[3-4 sentence analysis from that perspective only]

**The question this lens asks**: [Key question this perspective would prioritize]

**Blind spot warning**: [What this lens might miss]
```

**Perspective Mappings**:
- Optimist → Walt Disney
- Realist → George Marshall
- Pessimist → Nassim Taleb
- Operator → Theodore Roosevelt

---

## When to Use Quick Consult

| Situation | Use Quick Consult? | Why |
|-----------|-------------------|-----|
| Time-sensitive decision (minutes matter) | ✅ Yes | Speed over depth |
| Low-stakes choice | ✅ Yes | Full council is overkill |
| Need domain expertise only | ✅ Yes | Single expert may suffice |
| Want to test one perspective | ✅ Yes | Before committing to full deliberation |
| Complex, high-stakes decision | ❌ No | Use full council |
| Trade-offs across life domains | ❌ No | Needs debate + mediation |
| Emotional/values-laden choice | ❌ No | Needs multiple perspectives |

---

## Escalation Path

Quick Consult can escalate to full council:

```
User: /qc buffett: Should I invest in this startup?

Buffett: [Quick take]... 

"This decision has significant complexity. I'd recommend convening full council 
with Buffett, Taleb, and Hoffman for proper deliberation. Say 'convene council' 
to proceed."

User: convene council

[System proceeds to full 5-phase deliberation]
```

---

## Agent Availability for Quick Consult

All 25 agents are available for quick consult:

**Perspective Agents**:
- Disney, Marshall, Taleb, Roosevelt

**Domain Experts**:
- Buffett, Jobs, Hemingway, Godin, Stavridis, Feynman
- Amodei, Huang, Drucker, Christensen, Eisenhower
- Hoffman, Andreessen, Horowitz, Brown, Grant
- Robbins, Schwarzenegger, Jackson

**Mediator** (special case):
- Voss — Available for "How do I navigate this conversation?" questions

**Arbiter** (special case):
- Marcus Aurelius — Available for "I need to make peace with this decision" reflections

---

## Examples

### Example 1: Single Agent
```
User: /qc hemingway: Is this proposal too long?

## Ernest Hemingway — Quick Take

**On**: Whether your proposal is too long

**My View**: If you're asking, it probably is. Cut it by a third. Then cut it again.
The client doesn't want to read your proposal—they want to know you can solve 
their problem. One page that proves you understand beats ten pages that prove 
you can write.

**Key Consideration**: What's the one thing they must believe to say yes? 
Say that. Delete the rest.

**Confidence**: High

**If you want more depth**: "Convene full council with Hemingway, Godin, Jobs"
```

### Example 2: Perspective Lens
```
User: /lens pessimist: What could go wrong with this partnership?

## Pessimist Lens — Partnership Risk

**Through the eyes of the Pessimist (Nassim Taleb)**:

This partnership has hidden fragilities you haven't stress-tested. What happens 
when their incentives diverge from yours? When their key person leaves? When 
market conditions flip and the partnership becomes a liability rather than an 
asset? You're seeing the upside. I see the tail risks. The question isn't 
whether the partnership can succeed—it's whether it can fail catastrophically, 
and whether you've limited your exposure to that scenario.

**The question this lens asks**: What's the worst realistic outcome, and can 
you survive it?

**Blind spot warning**: This lens may underweight genuine upside and the cost 
of inaction.
```

### Example 3: Abbreviated Council
```
User: /quick-council: Should I take this speaking engagement for half my usual fee?

## Quick Council — Speaking Fee Decision

**Panel**: Warren Buffett, Seth Godin, Theodore Roosevelt

### Warren Buffett:
Price signals value. Discounting trains them to expect discounts. Unless this 
opens a door worth more than the fee difference, hold your price or decline.

### Seth Godin:
Who's in that room? If it's your smallest viable audience—the people who will 
spread your ideas—it might be worth it. If it's a generic crowd, your time is 
better spent elsewhere.

### Theodore Roosevelt:
What's the opportunity cost? If you're sitting idle, take it and deliver a 
speech so good they'll never forget you. Action beats waiting for the perfect 
engagement.

**Consensus**: Don't discount just to fill the calendar.

**Tension**: Whether the audience composition changes the calculus.

**For full deliberation**: `/convene-council` to proceed with debate and judgment
```

---

## Logging

Quick consults are logged in `deliberation-log.md` with tag `[QUICK]`:

```markdown
## [QUICK] 2025-01-26 — Speaking Fee

**Mode**: Abbreviated Council
**Agents**: Buffett, Godin, Roosevelt
**Question**: Should I take this speaking engagement for half my usual fee?
**Outcome**: [User decision, if recorded]
```

---

*Quick Consult v1.0 | Fast Access to Agent Perspectives*
