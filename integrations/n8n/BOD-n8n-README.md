# Board of Directors — n8n Backend

A complete n8n workflow system that powers the Board of Directors deliberation engine with audio/video output capabilities.

## What This Does

```
┌─────────────────────────────────────────────────────────────────────┐
│                         YOUR WEBSITE                                 │
│    "Should I take this job offer or start my own company?"          │
└───────────────────────────────┬─────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         n8n WORKFLOW                                 │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ PHASE 1: Three Advisors Analyze                               │  │
│  │   • Warren Buffett → Financial angle                          │  │
│  │   • Peter Drucker → Management perspective                    │  │
│  │   • Reid Hoffman → Entrepreneurship lens                      │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                │                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ PHASE 2: Synthesis & Debate                                   │  │
│  │   • Find consensus                                            │  │
│  │   • Identify tensions                                         │  │
│  │   • Simulate debate exchanges                                 │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                │                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ PHASE 3: Marcus Aurelius Judgment                             │  │
│  │   • Stoic principles applied                                  │  │
│  │   • Clear verdict                                             │  │
│  │   • Actionable next steps                                     │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                │                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ PHASE 4: Audio/Video Generation                               │  │
│  │   • 11Labs voice synthesis                                    │  │
│  │   • (Optional) HeyGen avatar video                            │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                      │
└───────────────────────────────┬─────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         RESPONSE                                     │
│                                                                      │
│  {                                                                   │
│    "verdict": "Start the company",                                   │
│    "audio_url": "https://...",                                      │
│    "transcript": "I've heard the council..."                        │
│  }                                                                   │
└─────────────────────────────────────────────────────────────────────┘
```

## Package Contents

```
bod-n8n-backend/
├── workflows/
│   ├── board-of-directors-main.json    # Full deliberation workflow
│   └── board-quick-consult.json        # Single-agent quick consult
├── docs/
│   ├── API.md                          # Full API documentation
│   └── SETUP.md                        # Deployment guide
└── README.md                           # This file
```

## Quick Start

### 1. Import Workflows

1. Open n8n
2. Go to **Workflows** → **Import from File**
3. Import both JSON files

### 2. Configure Credentials

- **Anthropic API** (required) — For Claude AI
- **11Labs API** (optional) — For voice synthesis
- **HeyGen API** (optional) — For avatar videos
- **Google Drive** (optional) — For audio storage

### 3. Activate & Test

```bash
curl -X POST https://your-n8n.app.n8n.cloud/webhook/board-of-directors \
  -H "Content-Type: application/json" \
  -d '{"query": "Should I quit my job?", "options": {"delivery": "text"}}'
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/webhook/board-of-directors` | POST | Full 3-advisor deliberation |
| `/webhook/board-quick-consult` | POST | Single-agent consultation |

## Request Example

```json
{
  "query": "Should I take the consulting contract or pursue the board seat?",
  "context": {
    "stakes": {
      "upside": "Board seat worth $500K+ equity",
      "downside": "Lose $180K guaranteed"
    },
    "subtext": {
      "fear": "Making the safe choice and regretting it",
      "deeper_question": "Am I ready to be an operator?"
    }
  },
  "options": {
    "delivery": "audio",
    "format": "standard"
  }
}
```

## Response Example

```json
{
  "success": true,
  "deliberation_id": "bod-2025-01-26-x7k9m2",
  "panel": {
    "agents": ["Warren Buffett", "Peter Drucker", "Nassim Taleb"]
  },
  "phases": {
    "judgment": {
      "verdict": "Decline the contract. Pursue the board seat.",
      "rationale": "The $180K is real, but what you'd give up is worth more.",
      "call_to_action": [
        "Decline the contract within the week",
        "Pursue the board seat actively",
        "Protect your advisory practice"
      ]
    }
  },
  "delivery": {
    "type": "audio",
    "audio_url": "https://drive.google.com/...",
    "transcript": "I've heard the council deliberate...",
    "duration_seconds": 147
  }
}
```

## Available Agents

| Agent | Domain | Best For |
|-------|--------|----------|
| Warren Buffett | Finance | Investment, capital allocation |
| Peter Drucker | Management | Effectiveness, organizational |
| Nassim Taleb | Risk | Uncertainty, tail risks |
| George Marshall | Strategy | Operations, planning |
| Theodore Roosevelt | Action | Execution, momentum |
| Steve Jobs | Product | Design, user experience |
| Reid Hoffman | Entrepreneurship | Startups, networks |
| Clayton Christensen | Innovation | Disruption, strategy |
| Ben Horowitz | Execution | Hard decisions, startups |
| Admiral Stavridis | Defense | Security, government |

## Delivery Options

| Option | Time | Output |
|--------|------|--------|
| `text` | ~30s | JSON with transcript only |
| `audio` | ~60s | JSON + MP3 audio URL |
| `video` | ~3min | JSON + MP3 + MP4 video URL |

## Cost Estimates

| Component | Per Request |
|-----------|-------------|
| Claude API | ~$0.30-0.50 |
| 11Labs | ~$0.10-0.30 |
| HeyGen | ~$0.10-0.30/min |
| **Total** | **~$0.50-1.00** |

## Next Steps

After deploying the backend:

1. **Build frontend** — Website to submit queries and display results
2. **Custom voice** — Train Marcus Aurelius voice in 11Labs
3. **Custom avatar** — Create Marcus avatar in HeyGen
4. **Add agents** — Expand the roster with more advisors

## Documentation

- [API Reference](docs/API.md) — Full endpoint documentation
- [Setup Guide](docs/SETUP.md) — Detailed deployment instructions

---

## Architecture Note

This backend is designed to work with **any frontend** — React, Vue, vanilla JS, mobile app, etc. The API is stateless and returns JSON with all deliberation data.

For the frontend, you'll need:
1. Form to submit queries with optional context
2. Loading state while processing (~30s-3min)
3. Results display (verdict, reasoning, next steps)
4. Audio player for briefings
5. (Optional) Video player for avatar briefings

---

*Board of Directors n8n Backend v1.0*
*Powering AI-driven strategic deliberation*
