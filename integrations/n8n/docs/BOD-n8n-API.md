# Board of Directors API Documentation

## Overview

The Board of Directors API enables you to submit decision queries and receive structured deliberation results, including optional audio/video briefings from Marcus Aurelius.

**Base URL**: `https://jdkristensonn8n.app.n8n.cloud`

---

## Endpoints

### 1. Full Deliberation

**POST** `/webhook/board-of-directors`

Runs a complete 4-phase deliberation with 3 advisors plus Marcus Aurelius.

#### Request

```json
{
  "query": "Should I take the 6-month consulting contract or pursue the board seat?",
  "context": {
    "options": [
      "Take the contract ($180K guaranteed)",
      "Pursue the board seat (potential $500K+ equity)",
      "Try to do both",
      "Do neither, focus on advisory practice"
    ],
    "stakes": {
      "upside": "Board seat could be worth $500K+ in equity over 3-5 years",
      "downside": "Lose $180K guaranteed revenue, board seat may not materialize",
      "timeline": "Contract decision needed in 30 days"
    },
    "constraints": {
      "resources": "$50K runway, 3 months available time",
      "non_negotiables": ["Cannot work full-time for both simultaneously"]
    },
    "subtext": {
      "fear": "Afraid of making the safe choice and regretting it later",
      "hope": "Want validation that the board seat is worth the risk",
      "deeper_question": "Am I ready to move from consultant to operator?"
    }
  },
  "options": {
    "agents": null,
    "delivery": "audio",
    "format": "standard",
    "include_full_deliberation": true
  }
}
```

#### Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `query` | string | **Yes** | The decision question to deliberate |
| `context` | object | No | Structured context to inform the deliberation |
| `context.options` | array | No | Options being considered |
| `context.stakes` | object | No | Upside, downside, and timeline |
| `context.constraints` | object | No | Resources and non-negotiables |
| `context.subtext` | object | No | Fear, hope, and deeper question |
| `options.agents` | array | No | Specific 3 agents to use (null = auto-select) |
| `options.delivery` | string | No | `"text"`, `"audio"`, or `"video"` (default: `"audio"`) |
| `options.format` | string | No | `"short"` (60s), `"standard"` (2-3min), `"full"` (4-5min) |
| `options.include_full_deliberation` | boolean | No | Include all phases in response (default: true) |

#### Available Agents

```
Warren Buffett     - Finance & Investment
Peter Drucker      - Management & Consulting
Nassim Taleb       - Risk & Uncertainty
George Marshall    - Strategy & Operations
Theodore Roosevelt - Action & Leadership
Steve Jobs         - Product & Design
Reid Hoffman       - Entrepreneurship & Networks
Clayton Christensen - Innovation & Strategy
Ben Horowitz       - Startup Execution
Admiral Stavridis  - Defense & Geopolitics
```

#### Response

```json
{
  "success": true,
  "deliberation_id": "bod-2025-01-26-x7k9m2",
  "query": "Should I take the 6-month consulting contract or pursue the board seat?",
  
  "panel": {
    "agents": ["Warren Buffett", "Peter Drucker", "Nassim Taleb"],
    "category": "auto_routed",
    "rationale": "Selected based on query relevance: Finance & Investment, Management & Consulting, Risk & Uncertainty"
  },
  
  "phases": {
    "individual_reports": [
      {
        "agent": "Warren Buffett",
        "position": "Decline the contract - the opportunity cost is too high",
        "analysis": "At $180K for 6 months, you're looking at roughly $30K/month. But what's the opportunity cost? If that board seat has even a 40% chance of materializing with $500K upside, the expected value calculation favors pursuing it. More importantly, you'd be trading away optionality - something I've learned to value highly.",
        "recommendation": "Pursue the board seat. The contract is a bird in hand, but sometimes the two in the bush are worth more.",
        "confidence": "High",
        "key_assumption": "The board seat is a genuine opportunity, not just a possibility"
      },
      {
        "agent": "Peter Drucker",
        "position": "The question isn't about money - it's about contribution",
        "analysis": "You're asking the wrong question. The real question is: Where can you make the greatest contribution? A consulting contract uses your existing skills. A board seat develops new ones. At this stage of your career, which matters more?",
        "recommendation": "Choose based on development, not income. If the board seat stretches you in ways that matter, take it.",
        "confidence": "Medium",
        "key_assumption": "Career development is more valuable than short-term income"
      },
      {
        "agent": "Nassim Taleb",
        "position": "You're trading options for certainty - almost always a bad trade",
        "analysis": "The contract is a negative option - it caps your upside while you do the work. The board seat is a positive option - limited downside (time), unlimited upside (equity, learning, network). Never trade optionality for certainty unless the certainty is dramatically better.",
        "recommendation": "Decline the contract. Pursue the board seat. If it doesn't work out, you'll find other opportunities. Optionality.",
        "confidence": "High",
        "key_assumption": "You can survive 6 months without the contract income"
      }
    ],
    
    "synthesis": {
      "consensus": [
        "The opportunity cost of the contract is significant",
        "The board seat offers asymmetric upside",
        "This decision is about more than money"
      ],
      "tensions": [
        "Certainty vs. optionality",
        "Income vs. development",
        "Safe choice vs. bold choice"
      ],
      "trade_offs": [
        "$180K guaranteed vs. potential $500K+ (with uncertainty)",
        "Using existing skills vs. developing new ones",
        "6 months committed vs. 6 months of optionality"
      ],
      "open_questions": [
        "How real is the board seat opportunity?",
        "Can you afford 6 months without guaranteed income?",
        "What does your gut tell you?"
      ]
    },
    
    "debate": {
      "exchanges": [
        {
          "from": "Nassim Taleb",
          "to": "Warren Buffett",
          "challenge": "You're assuming the board seat is a 'genuine opportunity.' But opportunities are never certain. The question is whether the asymmetry is worth the uncertainty.",
          "response": "Fair point. But I'm not saying wait for certainty - I'm saying do the expected value calculation. Even with uncertainty, the math favors the board seat."
        },
        {
          "from": "Peter Drucker",
          "to": "Nassim Taleb",
          "challenge": "You focus too much on optionality as an abstract concept. The question isn't just about options - it's about what contribution this person wants to make.",
          "response": "Contribution requires being in a position to contribute. Optionality preserves that position. A bad contract closes doors."
        }
      ]
    },
    
    "judgment": {
      "acknowledgments": "Buffett rightly calculates the opportunity cost. Drucker asks the essential question about contribution. Taleb reminds us that optionality has value.",
      "core_tension": "This is a tension between the certainty of income and the optionality of growth.",
      "stoic_principle": "We have power over our choices, not outcomes. Choose based on what you can control: the quality of your decision, not the certainty of the result.",
      "verdict": "Decline the contract. Pursue the board seat.",
      "rationale": "The council is unanimous in direction. The $180K is real, but what you would give up - the board seat possibility, the momentum, the optionality - is worth more. This is also about who you want to become, not just what you want to earn.",
      "uncertainty": "Whether the board seat will actually materialize. But that uncertainty doesn't change the quality of the decision.",
      "call_to_action": [
        "Decline the contract within the week - clarity is kindness",
        "Pursue the board seat actively - if it's worth giving up $180K, it's worth fighting for",
        "Protect your advisory practice - use the freed time to deepen those relationships"
      ]
    }
  },
  
  "delivery": {
    "type": "audio",
    "audio_url": "https://drive.google.com/file/d/xxx/view",
    "video_url": null,
    "transcript": "I've heard the council deliberate on your question...",
    "duration_seconds": 147
  },
  
  "metadata": {
    "generated_at": "2025-01-26T15:30:00Z",
    "processing_time_ms": 45000,
    "format": "standard"
  }
}
```

---

### 2. Quick Consult

**POST** `/webhook/board-quick-consult`

Get a quick response from a single advisor.

#### Request

```json
{
  "query": "Should I raise my consulting rates by 20%?",
  "agent": "Warren Buffett"
}
```

#### Response

```json
{
  "success": true,
  "consult_id": "qc-1706284200000",
  "agent": "Warren Buffett",
  "domain": "Finance",
  "query": "Should I raise my consulting rates by 20%?",
  "response": "Here's how I think about pricing: if your best clients would still hire you at 20% more, you're probably underpriced now. The question isn't whether you 'should' raise rates - it's whether the market will bear it.\n\nTest it. Quote the higher rate to your next three prospects. If two out of three say yes, your pricing power is confirmed. If all three balk, you have data.\n\nRemember: it's easier to discount from a high anchor than to raise from a low one. Start high, be willing to negotiate for the right client.\n\nMy recommendation: Raise the rates. But be prepared to articulate the value clearly. What does that 20% buy them that competitors don't offer?",
  "generated_at": "2025-01-26T15:35:00Z"
}
```

---

## Error Handling

### Error Response Format

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Missing required field: query",
    "details": null
  }
}
```

### Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `VALIDATION_ERROR` | 400 | Invalid or missing request fields |
| `UNKNOWN_AGENT` | 400 | Requested agent not in roster |
| `AGENT_GENERATION_FAILED` | 500 | AI failed to generate report |
| `AUDIO_GENERATION_FAILED` | 500 | 11Labs API error |
| `VIDEO_GENERATION_FAILED` | 500 | HeyGen API error |
| `TIMEOUT` | 504 | Request exceeded time limit |

---

## Rate Limits

| Endpoint | Limit | Window |
|----------|-------|--------|
| `/board-of-directors` | 10 requests | per minute |
| `/board-quick-consult` | 30 requests | per minute |

---

## Webhook Headers

Requests should include:

```
Content-Type: application/json
```

Responses include:

```
Content-Type: application/json
X-Deliberation-ID: bod-2025-01-26-x7k9m2
```

---

## Frontend Integration Examples

### JavaScript/Fetch

```javascript
async function runDeliberation(query, context = {}, options = {}) {
  const response = await fetch('https://jdkristensonn8n.app.n8n.cloud/webhook/board-of-directors', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      query,
      context,
      options: {
        delivery: 'audio',
        format: 'standard',
        ...options
      }
    })
  });
  
  if (!response.ok) {
    throw new Error(`API error: ${response.status}`);
  }
  
  return response.json();
}

// Usage
const result = await runDeliberation(
  "Should I hire a junior developer or outsource to an agency?",
  {
    stakes: {
      upside: "Build internal capability",
      downside: "Slower delivery, training overhead"
    }
  }
);

console.log(result.phases.judgment.verdict);
// Play audio
if (result.delivery.audio_url) {
  const audio = new Audio(result.delivery.audio_url);
  audio.play();
}
```

### React Hook

```typescript
import { useState, useCallback } from 'react';

interface DeliberationResult {
  success: boolean;
  deliberation_id: string;
  phases: {
    judgment: {
      verdict: string;
      rationale: string;
      call_to_action: string[];
    };
  };
  delivery: {
    audio_url: string | null;
    transcript: string;
  };
}

export function useDeliberation() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);
  const [result, setResult] = useState<DeliberationResult | null>(null);

  const deliberate = useCallback(async (query: string, context?: object) => {
    setLoading(true);
    setError(null);
    
    try {
      const response = await fetch('/api/board-of-directors', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query, context })
      });
      
      const data = await response.json();
      
      if (!data.success) {
        throw new Error(data.error?.message || 'Deliberation failed');
      }
      
      setResult(data);
      return data;
    } catch (err) {
      setError(err as Error);
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  return { deliberate, loading, error, result };
}
```

---

## Testing

### cURL Examples

**Full Deliberation:**
```bash
curl -X POST https://jdkristensonn8n.app.n8n.cloud/webhook/board-of-directors \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Should I quit my job to start a company?",
    "options": {
      "delivery": "text",
      "format": "short"
    }
  }'
```

**Quick Consult:**
```bash
curl -X POST https://jdkristensonn8n.app.n8n.cloud/webhook/board-quick-consult \
  -H "Content-Type: application/json" \
  -d '{
    "query": "How should I price my new SaaS product?",
    "agent": "Steve Jobs"
  }'
```

---

## Delivery Options

### Text Only (`delivery: "text"`)
- Fastest response (~30-45 seconds)
- Returns transcript in `delivery.transcript`
- No audio/video URLs

### Audio (`delivery: "audio"`)
- Medium response time (~60-90 seconds)
- Returns audio URL in `delivery.audio_url`
- Uses 11Labs for voice synthesis
- Voice: Marcus Aurelius (custom or stock)

### Video (`delivery: "video"`)
- Longest response time (~2-3 minutes)
- Returns video URL in `delivery.video_url`
- Uses HeyGen for avatar generation
- Also includes audio URL

---

## Format Options

| Format | Duration | Best For |
|--------|----------|----------|
| `short` | ~60 seconds | Quick decisions, daily briefings |
| `standard` | 2-3 minutes | Most decisions |
| `full` | 4-5 minutes | High-stakes, complex decisions |

---

*API Documentation v1.0*
