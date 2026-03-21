# Board of Directors — Implementation Guide

A step-by-step guide to installing the Board of Directors multi-agent deliberation system **globally** in Google Antigravity, so you can summon the council from any workspace.

---

## Table of Contents

1. [Overview](#overview)
2. [File Structure](#file-structure)
3. [Manual Installation](#manual-installation)
4. [Automated Installation (Antigravity Agent Prompts)](#automated-installation)
5. [Verification](#verification)
6. [First Use](#first-use)
7. [Troubleshooting](#troubleshooting)

---

## Overview

### What You're Installing

- **23 agent profiles** (4 perspective + 19 domain experts)
- **1 arbiter** (Marcus Aurelius)
- **Global rules** for council orchestration
- **Global workflows** for invocation and logging
- **Deliberation log** for historical tracking
- **Agent statistics** for pattern analysis

### Why Global Installation?

By installing to `~/.gemini/antigravity/`, the Board of Directors is available in **every workspace** without needing to copy files. You can summon the council whether you're working on a consulting proposal, evaluating an investment, or making any strategic decision.

---

## File Structure

After installation, your global Antigravity configuration will include:

```
~/.gemini/
├── GEMINI.md                              # Updated with BOD rules
└── antigravity/
    ├── global_workflows/
    │   ├── convene-council.md             # Main invocation
    │   └── log-deliberation.md            # Session logging
    └── board-of-directors/
        ├── README.md                       # Documentation
        ├── deliberation-log.md             # Historical record
        ├── agent-statistics.md             # Performance tracking
        ├── rules/
        │   ├── COUNCIL.md                  # Core orchestration rules
        │   └── AGENT_ROUTER.md             # Decision classification
        ├── agents/
        │   ├── perspective/
        │   │   ├── walt-disney.md
        │   │   ├── george-marshall.md
        │   │   ├── nassim-taleb.md
        │   │   └── theodore-roosevelt.md
        │   ├── domain/
        │   │   ├── warren-buffett.md
        │   │   ├── steve-jobs.md
        │   │   ├── ernest-hemingway.md
        │   │   ├── seth-godin.md
        │   │   ├── james-stavridis.md
        │   │   ├── richard-feynman.md
        │   │   ├── dario-amodei.md
        │   │   ├── jensen-huang.md
        │   │   ├── peter-drucker.md
        │   │   ├── clayton-christensen.md
        │   │   ├── dwight-eisenhower.md
        │   │   ├── reid-hoffman.md
        │   │   ├── marc-andreessen.md
        │   │   └── ben-horowitz.md
        │   └── arbiter/
        │       └── marcus-aurelius.md
        └── templates/
            ├── individual-report.md
            ├── combined-report.md
            ├── debate-transcript.md
            └── final-judgment.md
```

---

## Manual Installation

### Step 1: Create Directory Structure

Open Terminal and run:

```bash
mkdir -p ~/.gemini/antigravity/global_workflows
mkdir -p ~/.gemini/antigravity/board-of-directors/{rules,templates}
mkdir -p ~/.gemini/antigravity/board-of-directors/agents/{perspective,domain,arbiter}
```

### Step 2: Extract the ZIP File

1. Download `antigravity-bod-system.zip`
2. Extract to a temporary location
3. Copy contents to the global directory:

```bash
# Assuming you extracted to ~/Downloads/antigravity-bod/
cp -r ~/Downloads/antigravity-bod/.agent/rules/* ~/.gemini/antigravity/board-of-directors/rules/
cp -r ~/Downloads/antigravity-bod/.agent/agents/* ~/.gemini/antigravity/board-of-directors/agents/
cp -r ~/Downloads/antigravity-bod/.agent/templates/* ~/.gemini/antigravity/board-of-directors/templates/
cp ~/Downloads/antigravity-bod/.agent/workflows/* ~/.gemini/antigravity/global_workflows/
cp ~/Downloads/antigravity-bod/README.md ~/.gemini/antigravity/board-of-directors/
```

### Step 3: Add the Log and Statistics Files

Copy the deliberation log and statistics files:

```bash
# These are provided separately
cp deliberation-log.md ~/.gemini/antigravity/board-of-directors/
cp agent-statistics.md ~/.gemini/antigravity/board-of-directors/
```

### Step 4: Update Global Rules (GEMINI.md)

Create or edit `~/.gemini/GEMINI.md` to include the Board of Directors system:

```markdown
# Global Antigravity Rules

## Board of Directors — Multi-Agent Deliberation System

When the user invokes the council with `/convene-council` or says "Council convenes:", 
activate the Board of Directors deliberation system.

### System Location
All Board of Directors files are located at:
`~/.gemini/antigravity/board-of-directors/`

### Key Rules
1. **Rule of Three**: Always select exactly 3 agents (not 1, not 2, not 4)
2. **Marcus Aurelius is the Arbiter**: He speaks last, after deliberation
3. **Four Phases**: Individual Reports → Combined Report → Debate → Final Judgment
4. **Log Everything**: After each deliberation, update the log and statistics

### Agent Reference
Read agent profiles from:
- `~/.gemini/antigravity/board-of-directors/agents/perspective/` (4 agents)
- `~/.gemini/antigravity/board-of-directors/agents/domain/` (14 agents)
- `~/.gemini/antigravity/board-of-directors/agents/arbiter/` (Marcus Aurelius)

### Decision Router
Use `~/.gemini/antigravity/board-of-directors/rules/AGENT_ROUTER.md` to select 
the appropriate panel based on decision type.

### Logging
After each deliberation, update:
- `~/.gemini/antigravity/board-of-directors/deliberation-log.md`
- `~/.gemini/antigravity/board-of-directors/agent-statistics.md`
```

### Step 5: Restart Antigravity

Close and reopen Antigravity for the global rules to take effect.

---

## Automated Installation

Use these prompts to have the Antigravity agent do the work for you.

### Prompt 1: Initial Setup

Copy and paste this into Antigravity:

```
I need you to help me set up a global multi-agent deliberation system called "Board of Directors."

First, create the directory structure:

mkdir -p ~/.gemini/antigravity/global_workflows
mkdir -p ~/.gemini/antigravity/board-of-directors/{rules,templates}
mkdir -p ~/.gemini/antigravity/board-of-directors/agents/{perspective,domain,arbiter}

Then confirm the directories were created successfully.
```

### Prompt 2: Install Agent Profiles

```
Now I need you to create the agent profile files. I'll provide the content for each.

Create the following files in ~/.gemini/antigravity/board-of-directors/agents/perspective/:

1. walt-disney.md - Optimist perspective agent
2. george-marshall.md - Realist perspective agent  
3. nassim-taleb.md - Pessimist perspective agent
4. theodore-roosevelt.md - Operator perspective agent

For each file, use YAML frontmatter with:
- name: [agent-name]
- description: [when to use this agent]
- model: sonnet
- color: [appropriate color]
- role: perspective

Then include the agent's:
- Core philosophy (5 principles)
- Mental models
- How they analyze decisions
- Voice and characteristic phrases
- Known biases
- Output structure

Start with Walt Disney. Here's his core philosophy:
1. "If you can dream it, you can do it."
2. "All our dreams can come true, if we have the courage to pursue them."
3. "It's kind of fun to do the impossible."
4. "The way to get started is to quit talking and begin doing."
5. "I only hope that we don't lose sight of one thing — that it was all started by a mouse."
```

### Prompt 3: Install Domain Expert Profiles

```
Now create the domain expert profiles in ~/.gemini/antigravity/board-of-directors/agents/domain/

Create these 14 files:
1. warren-buffett.md - Finance domain
2. steve-jobs.md - Product domain
3. ernest-hemingway.md - Writing domain
4. seth-godin.md - Marketing domain
5. james-stavridis.md - Defense domain
6. richard-feynman.md - Science domain
7. dario-amodei.md - AI domain
8. jensen-huang.md - AI Infrastructure domain
9. peter-drucker.md - Consulting domain
10. clayton-christensen.md - Strategy domain
11. dwight-eisenhower.md - Operations domain
12. reid-hoffman.md - Entrepreneurship domain
13. marc-andreessen.md - Tech Investment domain
14. ben-horowitz.md - Execution domain

Use the same YAML frontmatter format. Each should have their authentic voice, mental models, and decision-making frameworks based on their actual philosophies and documented quotes.

Start with Warren Buffett. His core philosophy includes:
- "Buy wonderful businesses at fair prices"
- "Stay within your circle of competence"
- "Seek economic moats"
- "Be fearful when others are greedy and greedy when others are fearful"
```

### Prompt 4: Install the Arbiter

```
Now create the arbiter profile at:
~/.gemini/antigravity/board-of-directors/agents/arbiter/marcus-aurelius.md

Marcus Aurelius serves as the FINAL JUDGE after the three selected agents have deliberated. He does NOT count toward the Rule of Three.

His role:
1. Speaks LAST, after individual reports, combined report, and debate
2. Acknowledges each agent's perspective
3. Distinguishes genuine vs. apparent disagreement
4. Applies Stoic principles (Dichotomy of Control, Four Virtues)
5. Renders clear verdict
6. Issues call to action

Core philosophy:
1. "You have power over your mind—not outside events."
2. "Waste no more time arguing about what a good man should be. Be one."
3. "Everything is temporary."
4. "Virtue is the only good."
5. "We were born to work together."
```

### Prompt 5: Install Rules

```
Create the orchestration rules at:
~/.gemini/antigravity/board-of-directors/rules/COUNCIL.md

This file should define:
1. The Rule of Three (exactly 3 agents, no more, no less)
2. The four phases of deliberation
3. The council composition (perspective agents, domain experts, arbiter)
4. Rules of engagement
5. Invocation methods

Also create:
~/.gemini/antigravity/board-of-directors/rules/AGENT_ROUTER.md

This should contain the decision classification matrix:
- 12 decision categories
- Default panel for each category
- Selection algorithm
- Panel announcement format
```

### Prompt 6: Install Workflows

```
Create the main workflow at:
~/.gemini/antigravity/global_workflows/convene-council.md

This workflow should:
1. Analyze the user's decision/question
2. Select exactly 3 agents using the router
3. Generate individual reports from each agent
4. Create a combined synthesis report
5. Conduct a debate where agents challenge each other
6. Have Marcus Aurelius render final judgment
7. Offer follow-up options

Also create:
~/.gemini/antigravity/global_workflows/log-deliberation.md

This logs each session to deliberation-log.md and updates agent-statistics.md
```

### Prompt 7: Install Logging System

```
Create the historical tracking files:

1. ~/.gemini/antigravity/board-of-directors/deliberation-log.md
   - Template for each deliberation entry
   - Statistics summary table
   - Agent participation table
   - Outcome tracking table

2. ~/.gemini/antigravity/board-of-directors/agent-statistics.md
   - Detailed stats for each of the 18 agents
   - Selection rate, influence rate, debate win rate
   - Dominance analysis section
   - Metric definitions
```

### Prompt 8: Update Global Rules

```
Create or update ~/.gemini/GEMINI.md to include the Board of Directors system.

Add these rules:
1. When user says "/convene-council" or "Council convenes:", activate the BOD system
2. Always enforce the Rule of Three
3. Marcus Aurelius speaks last as arbiter
4. Follow the four-phase deliberation protocol
5. Log all deliberations after completion

Reference the files at ~/.gemini/antigravity/board-of-directors/
```

### Prompt 9: Verification

```
Verify the Board of Directors installation by:

1. List all files in ~/.gemini/antigravity/board-of-directors/
2. Confirm there are 4 perspective agents
3. Confirm there are 14 domain experts
4. Confirm Marcus Aurelius arbiter exists
5. Confirm both workflows exist in global_workflows
6. Confirm GEMINI.md includes BOD rules

Then show me a summary of what's installed.
```

---

## Verification

After installation, verify everything is in place:

### Check 1: Directory Structure
```bash
ls -la ~/.gemini/antigravity/board-of-directors/
```
Expected: rules/, agents/, templates/, deliberation-log.md, agent-statistics.md

### Check 2: Agent Count
```bash
ls ~/.gemini/antigravity/board-of-directors/agents/perspective/ | wc -l
# Expected: 4

ls ~/.gemini/antigravity/board-of-directors/agents/domain/ | wc -l
# Expected: 19

ls ~/.gemini/antigravity/board-of-directors/agents/arbiter/ | wc -l
# Expected: 1
```

### Check 3: Workflows
```bash
ls ~/.gemini/antigravity/global_workflows/
# Expected: convene-council.md, log-deliberation.md
```

### Check 4: Global Rules
```bash
cat ~/.gemini/GEMINI.md | grep -i "board of directors"
# Expected: Should find BOD references
```

---

## First Use

### Test the Installation

Open Antigravity in any workspace and type:

```
/convene-council
```

Or use natural language:

```
Council convenes: Should I accept a consulting engagement that's outside my core expertise but pays well?
```

### Expected Behavior

1. **Panel Selection**: System announces three agents based on decision type
2. **Phase 1**: Three individual reports generated
3. **Phase 2**: Combined synthesis report
4. **Phase 3**: Debate between agents
5. **Phase 4**: Marcus Aurelius renders final judgment
6. **Logging Prompt**: System offers to log the deliberation

### After Deliberation

Type `/log-deliberation` to record the session to the historical log.

---

## Troubleshooting

### Problem: "/convene-council" not recognized

**Cause**: Global workflows not loading

**Fix**: 
1. Verify file exists: `ls ~/.gemini/antigravity/global_workflows/convene-council.md`
2. Restart Antigravity
3. Check GEMINI.md includes BOD references

### Problem: Agents not found

**Cause**: Agent files not in correct location

**Fix**:
1. Verify: `ls ~/.gemini/antigravity/board-of-directors/agents/`
2. Should see: perspective/, domain/, arbiter/
3. Re-copy files if missing

### Problem: Only 1 or 2 agents selected

**Cause**: Rule of Three not enforced

**Fix**: Check that COUNCIL.md includes explicit Rule of Three enforcement

### Problem: Statistics not updating

**Cause**: Log workflow not running

**Fix**: 
1. Manually run `/log-deliberation` after each session
2. Verify log files exist and are writable

---

## Quick Reference After Installation

| Action | Command |
|--------|---------|
| Summon council | `/convene-council` |
| Natural language | "Council convenes: [question]" |
| Custom panel | "Council convenes with X, Y, Z: [question]" |
| Log session | `/log-deliberation` |
| View history | Open deliberation-log.md |
| View stats | Open agent-statistics.md |

---

## Maintenance

### Periodic Review
Every 10-20 deliberations, review:
- Agent statistics for dominance patterns
- Outcome tracking for accuracy
- Underutilized agents

### Updating Agent Profiles
If you want to modify an agent's voice or frameworks:
1. Edit the relevant .md file in agents/
2. Changes take effect immediately

### Adding New Agents
1. Create new .md file with YAML frontmatter
2. Add to appropriate subfolder (perspective/domain)
3. Update AGENT_ROUTER.md with new selection rules

---

*Implementation Guide v1.0 | Board of Directors for Google Antigravity*
