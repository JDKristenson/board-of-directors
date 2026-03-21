# n8n Workflow: Marcus Speaks Automation

## Overview

This n8n workflow automates the conversion of Marcus Aurelius's final judgment into audio/video briefings using 11Labs and HeyGen APIs.

---

## Workflow Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                        n8n Workflow                               │
│                                                                   │
│  ┌─────────┐    ┌──────────┐    ┌─────────┐    ┌─────────────┐  │
│  │ Webhook │───▶│ Transform│───▶│ 11Labs  │───▶│   HeyGen    │  │
│  │ Trigger │    │  Script  │    │  Voice  │    │   Avatar    │  │
│  └─────────┘    └──────────┘    └─────────┘    └─────────────┘  │
│                                       │              │           │
│                                       ▼              ▼           │
│                                 ┌─────────────────────────┐      │
│                                 │   Store & Respond       │      │
│                                 │  (Drive / Return URL)   │      │
│                                 └─────────────────────────┘      │
└──────────────────────────────────────────────────────────────────┘
```

---

## Workflow JSON (Import to n8n)

```json
{
  "name": "Marcus Speaks - Audio/Video Generator",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "marcus-speaks",
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "webhook-trigger",
      "name": "Webhook Trigger",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 300]
    },
    {
      "parameters": {
        "jsCode": "// Extract and transform final judgment to speech script\n\nconst input = $input.first().json;\nconst judgment = input.final_judgment;\nconst format = input.format || 'standard';\nconst deliveryType = input.delivery_type || 'audio';\n\n// Transform written judgment to spoken script\nfunction transformToSpeech(judgment, format) {\n  const { topic, verdict, reasoning, uncertainty, call_to_action, agents } = judgment;\n  \n  let script = '';\n  \n  if (format === 'short') {\n    // 60-second version\n    script = `The council has spoken on ${topic}.\n\nMy verdict: ${verdict}\n\n${reasoning[0]}\n\nYour next step: ${call_to_action[0]}\n\nNow act.`;\n  } else if (format === 'standard') {\n    // 2-3 minute version\n    script = `I've heard the council deliberate on ${topic}.\n\nThree perspectives. One question. Here's where I land.\n\n`;\n    \n    // Add agent summaries\n    agents.forEach(agent => {\n      script += `${agent.name} argued: ${agent.summary}\\n\\n`;\n    });\n    \n    script += `My judgment: ${verdict}\\n\\n`;\n    script += `Here's why:\\n`;\n    reasoning.forEach((reason, i) => {\n      script += `${i + 1}. ${reason}\\n`;\n    });\n    \n    script += `\\nWhat I don't know: ${uncertainty}\\n\\n`;\n    script += `Your next steps:\\n`;\n    call_to_action.forEach((action, i) => {\n      script += `${i + 1}. ${action}\\n`;\n    });\n    \n    script += `\\nThe decision is yours. But if you ask what wisdom counsels—this is it.`;\n  } else {\n    // Full 4-5 minute version\n    script = `The council convened to address this question: ${topic}\\n\\n`;\n    // ... expanded version\n  }\n  \n  return script;\n}\n\nconst speechScript = transformToSpeech(judgment, format);\n\nreturn {\n  speech_script: speechScript,\n  delivery_type: deliveryType,\n  format: format,\n  original_judgment: judgment,\n  character_count: speechScript.length\n};"
      },
      "id": "transform-script",
      "name": "Transform to Speech Script",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [450, 300]
    },
    {
      "parameters": {
        "method": "POST",
        "url": "https://api.elevenlabs.io/v1/text-to-speech/{{$env.ELEVEN_LABS_VOICE_ID}}",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {
              "name": "xi-api-key",
              "value": "={{$env.ELEVEN_LABS_API_KEY}}"
            },
            {
              "name": "Content-Type",
              "value": "application/json"
            }
          ]
        },
        "sendBody": true,
        "bodyParameters": {
          "parameters": [
            {
              "name": "text",
              "value": "={{$json.speech_script}}"
            },
            {
              "name": "model_id",
              "value": "eleven_monolingual_v1"
            },
            {
              "name": "voice_settings",
              "value": "={\"stability\": 0.75, \"similarity_boost\": 0.70}"
            }
          ]
        },
        "options": {
          "response": {
            "response": {
              "responseFormat": "file"
            }
          }
        }
      },
      "id": "eleven-labs-tts",
      "name": "11Labs Text-to-Speech",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4,
      "position": [650, 300]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$node['Transform to Speech Script'].json.delivery_type}}",
              "operation": "equals",
              "value2": "video"
            }
          ]
        }
      },
      "id": "check-video-needed",
      "name": "Video Needed?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [850, 300]
    },
    {
      "parameters": {
        "method": "POST",
        "url": "https://api.heygen.com/v2/video/generate",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {
              "name": "X-Api-Key",
              "value": "={{$env.HEYGEN_API_KEY}}"
            },
            {
              "name": "Content-Type",
              "value": "application/json"
            }
          ]
        },
        "sendBody": true,
        "specifyBody": "json",
        "jsonBody": "={\n  \"video_inputs\": [{\n    \"character\": {\n      \"type\": \"avatar\",\n      \"avatar_id\": \"{{$env.HEYGEN_AVATAR_ID}}\",\n      \"avatar_style\": \"normal\"\n    },\n    \"voice\": {\n      \"type\": \"audio\",\n      \"audio_url\": \"{{$node['Upload Audio Temp'].json.url}}\"\n    },\n    \"background\": {\n      \"type\": \"color\",\n      \"value\": \"#1a1a2e\"\n    }\n  }],\n  \"dimension\": {\n    \"width\": 1920,\n    \"height\": 1080\n  }\n}",
        "options": {}
      },
      "id": "heygen-generate",
      "name": "HeyGen Generate Video",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4,
      "position": [1050, 200]
    },
    {
      "parameters": {
        "method": "GET",
        "url": "=https://api.heygen.com/v1/video_status.get?video_id={{$json.data.video_id}}",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {
              "name": "X-Api-Key",
              "value": "={{$env.HEYGEN_API_KEY}}"
            }
          ]
        },
        "options": {}
      },
      "id": "heygen-poll-status",
      "name": "Poll HeyGen Status",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4,
      "position": [1250, 200]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$json.data.status}}",
              "operation": "equals",
              "value2": "completed"
            }
          ]
        }
      },
      "id": "check-video-ready",
      "name": "Video Ready?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [1450, 200]
    },
    {
      "parameters": {
        "amount": 10,
        "unit": "seconds"
      },
      "id": "wait-for-video",
      "name": "Wait 10s",
      "type": "n8n-nodes-base.wait",
      "typeVersion": 1,
      "position": [1450, 350]
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "={\n  \"success\": true,\n  \"delivery_type\": \"{{$node['Transform to Speech Script'].json.delivery_type}}\",\n  \"audio_url\": \"{{$node['Upload to Drive'].json.webViewLink}}\",\n  \"video_url\": \"{{$json.data.video_url}}\",\n  \"transcript\": \"{{$node['Transform to Speech Script'].json.speech_script}}\",\n  \"duration_estimate\": \"{{Math.round($node['Transform to Speech Script'].json.character_count / 15)}} seconds\"\n}",
        "options": {}
      },
      "id": "respond-success",
      "name": "Return Result",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1,
      "position": [1650, 200]
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "={\n  \"success\": true,\n  \"delivery_type\": \"audio\",\n  \"audio_url\": \"{{$node['Upload to Drive'].json.webViewLink}}\",\n  \"transcript\": \"{{$node['Transform to Speech Script'].json.speech_script}}\",\n  \"duration_estimate\": \"{{Math.round($node['Transform to Speech Script'].json.character_count / 15)}} seconds\"\n}",
        "options": {}
      },
      "id": "respond-audio-only",
      "name": "Return Audio Only",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1,
      "position": [1050, 400]
    }
  ],
  "connections": {
    "Webhook Trigger": {
      "main": [
        [
          {
            "node": "Transform to Speech Script",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Transform to Speech Script": {
      "main": [
        [
          {
            "node": "11Labs Text-to-Speech",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "11Labs Text-to-Speech": {
      "main": [
        [
          {
            "node": "Check Video Needed?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Check Video Needed?": {
      "main": [
        [
          {
            "node": "HeyGen Generate Video",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Return Audio Only",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HeyGen Generate Video": {
      "main": [
        [
          {
            "node": "Poll HeyGen Status",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Poll HeyGen Status": {
      "main": [
        [
          {
            "node": "Video Ready?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Video Ready?": {
      "main": [
        [
          {
            "node": "Return Result",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Wait 10s",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Wait 10s": {
      "main": [
        [
          {
            "node": "Poll HeyGen Status",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "settings": {
    "executionOrder": "v1"
  }
}
```

---

## Environment Variables Required

Set these in your n8n instance:

```bash
# 11Labs Configuration
ELEVEN_LABS_API_KEY=your_api_key_here
ELEVEN_LABS_VOICE_ID=your_marcus_voice_id

# HeyGen Configuration  
HEYGEN_API_KEY=your_api_key_here
HEYGEN_AVATAR_ID=your_marcus_avatar_id

# Optional: Google Drive for storage
GOOGLE_DRIVE_FOLDER_ID=your_briefings_folder_id
```

---

## Webhook Payload Format

Call the webhook with this structure:

```json
{
  "final_judgment": {
    "topic": "6-month consulting contract decision",
    "verdict": "Decline the contract",
    "reasoning": [
      "Opportunity cost exceeds the $180K value",
      "Board seat has unlimited upside; contract has ceiling",
      "6-month pause damages advisory momentum"
    ],
    "uncertainty": "Whether the board seat will actually materialize",
    "call_to_action": [
      "Decline the contract within the week",
      "Pursue the board seat actively",
      "Protect your advisory practice"
    ],
    "agents": [
      {"name": "Warren Buffett", "summary": "The implied rate is mediocre and opportunity cost is too high"},
      {"name": "Peter Drucker", "summary": "This work employs you but doesn't develop you"},
      {"name": "Nassim Taleb", "summary": "You're trading options for certainty—bad trade"}
    ]
  },
  "format": "standard",
  "delivery_type": "video"
}
```

---

## Calling from Antigravity

Add this to the convene-council workflow:

```javascript
// After Phase 4 completes, offer video/audio delivery
const deliveryPrompt = `
Deliberation complete. Would you like Marcus to brief you?

- "/marcus-speaks" — Audio briefing (1-3 min)
- "/marcus-speaks --video" — Video avatar briefing
- "/marcus-speaks --short" — 60-second summary

Or just say "brief me" for the default audio version.
`;

// When user triggers marcus-speaks:
const webhookUrl = "https://your-n8n-instance.app.n8n.cloud/webhook/marcus-speaks";

const response = await fetch(webhookUrl, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    final_judgment: extractedJudgment,
    format: userSelectedFormat,
    delivery_type: userSelectedType
  })
});

const result = await response.json();
// result.audio_url or result.video_url
```

---

## Testing the Workflow

### 1. Test 11Labs Connection
```bash
curl -X POST "https://api.elevenlabs.io/v1/text-to-speech/YOUR_VOICE_ID" \
  -H "xi-api-key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text": "The council has spoken. Here is my verdict.", "model_id": "eleven_monolingual_v1"}' \
  --output test.mp3
```

### 2. Test HeyGen Connection
```bash
curl -X POST "https://api.heygen.com/v2/video/generate" \
  -H "X-Api-Key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "video_inputs": [{
      "character": {"type": "avatar", "avatar_id": "YOUR_AVATAR_ID"},
      "voice": {"type": "text", "input_text": "Test message"},
      "background": {"type": "color", "value": "#1a1a2e"}
    }],
    "dimension": {"width": 1280, "height": 720}
  }'
```

### 3. Test Full Workflow
```bash
curl -X POST "https://your-n8n-instance/webhook/marcus-speaks" \
  -H "Content-Type: application/json" \
  -d @test-judgment.json
```

---

## Cost Management

### Per-Briefing Costs
| Component | Standard (2-3 min) | Short (60s) |
|-----------|-------------------|-------------|
| 11Labs | ~$0.50 | ~$0.15 |
| HeyGen | ~$0.30 | ~$0.10 |
| **Total** | **~$0.80** | **~$0.25** |

### Monthly Budget Planning
| Usage | Audio Only | With Video |
|-------|------------|------------|
| 10 briefings/month | ~$5 | ~$8 |
| 25 briefings/month | ~$12 | ~$20 |
| 50 briefings/month | ~$25 | ~$40 |

---

## Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| 11Labs 401 | Invalid API key | Check ELEVEN_LABS_API_KEY |
| HeyGen timeout | Video still processing | Increase poll wait time |
| Audio too fast | Character count high | Reduce script length or adjust rate |
| Avatar lip sync off | Audio quality issue | Use higher quality 11Labs output |

---

*n8n Workflow Template v1.0 | Marcus Speaks Automation*
