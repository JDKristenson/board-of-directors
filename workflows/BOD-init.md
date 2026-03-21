---
name: BOD-init
description: "Initialize and orient to the Board of Directors system. Run this at the start of a session to ensure Gemini understands the BOD architecture, available agents, and commands."
trigger:
  - "/bod-init"
  - "/init-bod"
  - "Initialize the Board of Directors"
  - "Load BOD system"
global: true
---

# BOD System Initialization

You are initializing the Board of Directors (BOD) multi-agent deliberation system.

## Step 1: Confirm System Files

Read and confirm access to these core files:
- `~/.gemini/antigravity/BOD/BOD-GEMINI.md` — Master rules
- `~/.gemini/antigravity/BOD/system/BOD-README.md` — System documentation
- `~/.gemini/antigravity/BOD/system/rules/BOD-COUNCIL.md` — Deliberation protocol
- `~/.gemini/antigravity/BOD/system/rules/BOD-AGENT_ROUTER.md` — Panel selection

## Step 2: Verify Agent Roster

Confirm all 25 agents are available:

**Perspective Agents** (4) — in `system/agents/perspective/`:
| File | Perspective | Person |
|------|-------------|--------|
| `optimist.md` | Optimist | Walt Disney |
| `pragmatist.md` | Pragmatist/Realist | George Marshall |
| `pessimist.md` | Pessimist | Nassim Taleb |
| `operator.md` | Action-Oriented | Theodore Roosevelt |

**Domain Experts** (19) — in `system/agents/domain/`
**Mediator** (1) — `system/agents/mediator/chris-voss.md`
**Arbiter** (1) — `system/agents/arbiter/marcus-aurelius.md`

## Step 3: Report Status

Output a status report:

```markdown
## BOD System Status

✓ **System Location**: ~/.gemini/antigravity/BOD/
✓ **GEMINI.md**: Loaded
✓ **Agents**: [X]/25 available
✓ **Workflows**: [X] registered
✓ **n8n Integration**: [Available/Not configured]

### Quick Reference

| Command | Action |
|---------|--------|
| `/convene-council` | Full 5-phase deliberation |
| `/qc [agent]: [question]` | Quick single-agent consult |
| `/lens [perspective]: [question]` | Perspective lens (optimist/pragmatist/pessimist/operator) |
| `/quick-council: [question]` | Abbreviated 3-agent take |

### Perspective Shortcuts
- `/lens optimist` — Walt Disney's view
- `/lens pragmatist` — George Marshall's view
- `/lens pessimist` — Nassim Taleb's view
- `/lens operator` — Theodore Roosevelt's view

**BOD System Ready.** What decision would you like the council to deliberate?
```

## Step 4: Await User Input

After reporting status, wait for the user to either:
- Ask a question for deliberation
- Request a specific command
- Ask for more information about the system
