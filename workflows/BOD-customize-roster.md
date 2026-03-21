---
name: customize-roster
description: "Add custom agents, modify preferences, and personalize how the Board of Directors operates for you."
trigger:
  - "/customize"
  - "/add-agent"
  - "/preferences"
  - "Add [name] to the roster"
global: true
---

# Customize Roster — Personalization Workflow

## Purpose

The default 25-agent roster covers most needs, but you may want to:
- Add a personal mentor or advisor as an agent
- Create a persona for a specific use case
- Modify which agents appear in default panels
- Exclude agents that aren't relevant to your work

This workflow handles all customization.

---

## Commands

| Command | Action |
|---------|--------|
| `/customize` | Open interactive customization menu |
| `/add-agent [name]: [description]` | Add a new custom agent |
| `/edit-agent [name]` | Modify an existing agent |
| `/remove-agent [name]` | Remove a custom agent |
| `/list-agents` | Show full roster (built-in + custom) |
| `/set-default [category]: [agents]` | Set default panel for a decision type |
| `/exclude [agent]` | Exclude an agent from all panels |
| `/favorite [agent]` | Add agent to favorites (prioritized in suggestions) |
| `/preferences` | View current preference settings |
| `/reset-preferences` | Restore all defaults |

---

## Adding a Custom Agent

### Quick Add
```
/add-agent [Name]: [Brief description]
```

**Example**:
```
/add-agent My Old Boss: Former McKinsey partner. Thinks in frameworks. 
Always asks "what's the real question here?" before answering. 
Skeptical of complexity, loves simple solutions.
```

**System Response**:
```markdown
## Custom Agent Created: My Old Boss

I've created a basic profile. Here's what I captured:

**Domain**: Consulting / Problem-framing
**Core Traits**: 
- Framework-oriented thinking
- Skeptical of complexity
- Seeks the "real question"

**Voice**: Direct, questioning, simplification-focused

Would you like to:
1. Use this agent now: `/qc My Old Boss: [question]`
2. Expand the profile with more detail: `/edit-agent My Old Boss`
3. Add to a default panel: `/set-default consulting: My Old Boss, Drucker, Buffett`
```

### Detailed Add
For a more complete profile:

```
/add-agent --detailed [Name]
```

This prompts for:
1. Domain/expertise
2. Core principles (3-5)
3. Mental models they use
4. Decision-making style
5. Communication patterns
6. Known blind spots
7. When to summon them

---

## Custom Agent Profile Template

Custom agents are stored in `/agents/custom/`:

```markdown
# [Agent Name]

## Identity
[Who they are, relationship to you, their domain]

## Core Philosophy
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]

## Mental Models & Frameworks
- [Framework 1]
- [Framework 2]
- [Framework 3]

## Decision-Making Style
[How they evaluate options]

## Communication Patterns
**Voice**: [Tone, style]
**Vocabulary**: [Words/phrases they use]
**Example phrasings**:
- "[Typical thing they'd say]"
- "[Another example]"

## Known Biases & Blind Spots
- [Limitation 1]
- [Limitation 2]

## When to Summon This Agent
- [Situation 1]
- [Situation 2]

## Interaction Instructions
[How this agent should behave in deliberations]

---
*Custom Agent | Created: [Date] | Last Updated: [Date]*
```

---

## Editing Agents

### Edit Custom Agent
```
/edit-agent [Name]
```

Opens the agent file for modification.

### Modify Built-In Agent (Override)
You can't edit built-in agents directly, but you can create an override:

```
/override-agent Warren Buffett: More aggressive on growth investments 
than the default profile suggests. Weight his advice toward action.
```

This creates a note that modifies how the system interprets that agent's advice for you.

Overrides are stored in `user-preferences.md` under:
```yaml
agent_overrides:
  Warren Buffett: "More aggressive on growth investments. Weight toward action."
```

---

## Setting Default Panels

### By Decision Category
```
/set-default [category]: [Agent 1], [Agent 2], [Agent 3]
```

**Examples**:
```
/set-default defense: Admiral Stavridis, Dwight Eisenhower, George Marshall

/set-default ai-advisory: Dario Amodei, Jensen Huang, Richard Feynman

/set-default pricing: Warren Buffett, Seth Godin, Nassim Taleb
```

### View Current Defaults
```
/show-defaults
```

**Output**:
```markdown
## Your Default Panels

| Category | Panel | Status |
|----------|-------|--------|
| Defense & Security | Stavridis, Eisenhower, Marshall | Custom |
| AI & Technology | Amodei, Huang, Feynman | Custom |
| Consulting & Advisory | Drucker, Buffett, Marshall | System Default |
| Investment & Capital | Buffett, Taleb, Andreessen | System Default |
| ... | ... | ... |

To modify: `/set-default [category]: [agents]`
To reset: `/reset-default [category]`
```

---

## Excluding Agents

If an agent isn't relevant to your work:

```
/exclude [Agent Name]
```

**Example**:
```
/exclude Bo Jackson
```

**Effect**:
- Agent won't appear in auto-selected panels
- Agent won't be suggested as alternatives
- Agent remains available if explicitly requested

**To restore**:
```
/include [Agent Name]
```

---

## Favorite Agents

Favorites are prioritized in suggestions and quick-consult defaults:

```
/favorite Warren Buffett
/favorite Peter Drucker
/favorite Nassim Taleb
```

**View favorites**:
```
/favorites
```

**Remove from favorites**:
```
/unfavorite [Agent Name]
```

---

## Interactive Customization Menu

```
/customize
```

**Output**:
```markdown
## Board of Directors — Customization

What would you like to customize?

1. **Agents**
   - Add custom agent
   - Edit agent
   - Exclude agent
   - Set favorites

2. **Default Panels**
   - View current defaults
   - Set category defaults
   - Reset to system defaults

3. **Deliberation Settings**
   - Detail level (brief/standard/detailed)
   - Auto-mediation on/off
   - Outcome reminders on/off

4. **Output Formatting**
   - Response length
   - List style
   - Quote inclusion

Reply with a number or describe what you want to change.
```

---

## Validation Rules

The system enforces:

| Rule | Enforcement |
|------|-------------|
| Panels must have exactly 3 agents | Error if != 3 |
| Cannot exclude and favorite same agent | Warning, exclusion wins |
| Custom agent names must be unique | Error on duplicate |
| Agent names must match roster (or custom) | Error with suggestions |
| Marcus Aurelius cannot be excluded | Error — arbiter is required |
| Chris Voss cannot be panelist | Warning — he's mediator only |

---

## Backup & Restore

### Export Preferences
```
/export-preferences
```
Creates a backup file of all custom settings.

### Import Preferences
```
/import-preferences [file]
```
Restores settings from backup.

### Reset Everything
```
/reset-all
```
Removes all custom agents, overrides, and preferences. Returns to system defaults.

**Confirmation required**: "Type 'confirm reset' to proceed"

---

## Example: Building a Personal Mentor Agent

**User**:
```
/add-agent --detailed Captain Williams
```

**System prompts**:
```
Creating detailed profile for Captain Williams.

1. Who is Captain Williams?
> My first commanding officer. Taught me leadership under pressure.

2. What are their core principles? (List 3-5)
> 1. Take care of your people and they'll take care of the mission
> 2. Decisive action beats perfect information
> 3. Own your mistakes publicly, credit your team publicly
> 4. Standards aren't negotiable

3. How do they make decisions?
> Gathers input fast, decides faster. Trusts instinct refined by experience. 
> Always asks "what would I want my CO to do if I were the junior officer here?"

4. How do they communicate?
> Calm under pressure. Never raises voice. Uses "we" not "I". 
> Asks questions that lead you to the answer.

5. What are their blind spots?
> Can be too loyal to underperformers. Sometimes trusts gut over data.

6. When should they be summoned?
> Leadership dilemmas, team management, high-pressure decisions, 
> anything involving integrity or standards.
```

**Result**: Full agent profile created at `/agents/custom/captain-williams.md`

Now available:
```
/qc Captain Williams: How do I handle an underperforming team member I personally like?

Council convenes with Captain Williams, Peter Drucker, and Ben Horowitz: [question]
```

---

*Customize Roster v1.0 | Make the Board Yours*
