# User Preferences — System Customization

## Overview

This file configures how the Board of Directors operates for you. Modify these settings to personalize agent selection, default behaviors, and system responses.

---

## User Profile

```yaml
name: "JD"
domains:
  - Defense consulting
  - AI advisory
  - Strategy
  - Entrepreneurship
  - Business development

background:
  - Navy ship captain
  - VP at McKinsey & Company
  - Independent consultant

communication_style:
  tone: "Direct, friendly, professional"
  email_greeting: "Hi {First name},"
  email_closing: "All the Best,\n\nJD"
```

---

## Default Panels by Decision Type

Override the system defaults with your preferred panels:

```yaml
default_panels:
  # Uncomment and modify to set custom defaults
  
  # consulting_advisory:
  #   - Peter Drucker
  #   - Warren Buffett
  #   - George Marshall
  
  # defense_strategy:
  #   - Admiral Stavridis
  #   - Dwight Eisenhower
  #   - Nassim Taleb
  
  # startup_investment:
  #   - Marc Andreessen
  #   - Reid Hoffman
  #   - Warren Buffett
  
  # Use "auto" to let the system choose (default behavior)
  default: auto
```

---

## Agent Preferences

### Frequently Used Agents
Agents you call on most often (prioritized in suggestions):

```yaml
favorite_agents:
  - Warren Buffett
  - Peter Drucker
  - Nassim Taleb
  - George Marshall
```

### Excluded Agents
Agents you never want on a panel:

```yaml
excluded_agents: []
  # Example: 
  # - Bo Jackson  # Not relevant to my work
```

### Agent Nicknames
Shortcuts for quick-consult:

```yaml
agent_aliases:
  buffett: Warren Buffett
  taleb: Nassim Taleb
  drucker: Peter Drucker
  arnold: Arnold Schwarzenegger
  brene: Brené Brown
  voss: Chris Voss
  marcus: Marcus Aurelius
```

---

## Custom Agents

Add your own agents (mentors, advisors, personas):

```yaml
custom_agents:
  # Example custom agent:
  # - name: "My Mentor"
  #   domain: "Career guidance"
  #   core_principles:
  #     - "Always ask what you're optimizing for"
  #     - "Relationships compound faster than revenue"
  #   voice: "Warm but direct, asks more questions than gives answers"
  #   summon_when: "Career crossroads, relationship decisions"
```

To build a full custom agent profile, use:
```
/add-agent [name]: [description of who they are and how they think]
```

---

## Deliberation Preferences

```yaml
deliberation:
  # How verbose should reports be?
  detail_level: standard  # Options: brief, standard, detailed
  
  # Include debate phase?
  include_debate: true
  
  # Auto-trigger mediation on impasse?
  auto_mediation: true
  
  # Prompt for outcome logging?
  outcome_reminders: true
  reminder_intervals: [30, 90]  # Days after deliberation
  
  # Default confidence threshold for "High"
  high_confidence_threshold: 0.8
```

---

## Quick Consult Preferences

```yaml
quick_consult:
  # Default agent for ambiguous quick questions
  default_agent: George Marshall
  
  # Auto-suggest upgrade to full council for high-stakes?
  suggest_upgrade: true
  
  # Include confidence level in responses?
  show_confidence: true
```

---

## Output Formatting

```yaml
formatting:
  # Use headers in reports?
  use_headers: true
  
  # Include agent quotes?
  include_quotes: true
  
  # Bullet points or prose?
  list_style: bullets  # Options: bullets, prose, mixed
  
  # Maximum response length (approximate)
  max_length: standard  # Options: brief, standard, comprehensive
```

---

## Notification Preferences

```yaml
notifications:
  # Remind about pending outcomes?
  outcome_reminders: true
  
  # Weekly digest of system usage?
  weekly_digest: false
  
  # Alert when new agents are available?
  new_agent_alerts: true
```

---

## How to Modify

### Option 1: Direct Edit
Edit this file directly in your Antigravity project.

### Option 2: Commands
Use natural language commands:

```
"Add Buffett to my favorites"
"Exclude Bo Jackson from panels"
"Set my default panel for defense decisions to Stavridis, Eisenhower, and Marshall"
"Make deliberations more brief"
"Turn off outcome reminders"
```

### Option 3: `/customize` Command
```
/customize
```
Opens interactive customization menu.

---

## Reset to Defaults

```
/reset-preferences
```
Restores all settings to system defaults.

---

## Preference Validation

The system validates preferences on load:
- Excluded agents cannot be in favorite_agents
- Custom panels must have exactly 3 agents
- Agent names must match roster (or custom_agents)
- Invalid settings are ignored with a warning

---

*User Preferences v1.0 | Personalize Your Board*
