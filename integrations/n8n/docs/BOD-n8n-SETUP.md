# Board of Directors n8n Backend — Setup Guide

## Overview

This guide walks you through deploying the Board of Directors deliberation system on n8n, with audio/video output capabilities.

---

## Prerequisites

1. **n8n Instance** (cloud or self-hosted)
2. **Anthropic API Key** (for Claude)
3. **11Labs API Key** (for voice synthesis) — Optional
4. **HeyGen API Key** (for video avatar) — Optional
5. **Google Drive** (for audio storage) — Or alternative storage

---

## Step 1: Import Workflows

### Main Deliberation Workflow

1. Open n8n
2. Go to **Workflows** → **Import from File**
3. Select `board-of-directors-main.json`
4. Click **Import**

### Quick Consult Workflow

1. Import `board-quick-consult.json` the same way

---

## Step 2: Configure Credentials

### Anthropic (Required)

1. Go to **Settings** → **Credentials**
2. Click **Add Credential**
3. Select **Anthropic API**
4. Enter your API key
5. Save as "Anthropic - BOD"

### 11Labs (For Audio)

1. Get API key from [elevenlabs.io](https://elevenlabs.io)
2. In n8n, go to **Settings** → **Variables**
3. Add:
   - `ELEVEN_LABS_API_KEY`: Your API key
   - `ELEVEN_LABS_VOICE_ID`: Your Marcus voice ID (or use default)

**Recommended Voice IDs:**
- `pNInz6obpgDQGcFmaJgB` - "Adam" (mature male)
- `ErXwobaYiN019PkySvjV` - "Antoni" (wise elder)
- Custom: Create your own at 11Labs Voice Lab

### HeyGen (For Video)

1. Get API key from [heygen.com](https://heygen.com)
2. Add environment variables:
   - `HEYGEN_API_KEY`: Your API key
   - `HEYGEN_AVATAR_ID`: Your avatar ID
   - `HEYGEN_VOICE_ID`: Voice to use (optional)

**Recommended Avatar IDs:**
- `josh_lite3_20230714` - Professional male
- Create custom from photo at HeyGen

### Google Drive (For Audio Storage)

1. In n8n, add Google OAuth2 credential
2. Enable Drive API in Google Cloud Console
3. Create a folder for briefings
4. Update the "Upload to Drive" node with your folder ID

---

## Step 3: Configure the Workflows

### Main Workflow Adjustments

1. **Open** the imported workflow
2. **Anthropic Model nodes**: 
   - Click each "Anthropic Model" node
   - Select your Anthropic credential
   
3. **11Labs node**:
   - Verify the voice ID in the URL
   - Or replace with your custom voice
   
4. **Upload to Drive node**:
   - Select your Google credential
   - Set the destination folder

5. **HeyGen nodes** (if using video):
   - Verify API key variable
   - Set avatar ID

### Quick Consult Adjustments

1. Same Anthropic credential setup
2. No audio/video configuration needed

---

## Step 4: Test the Endpoints

### Test Main Deliberation

```bash
# Test with text-only (fastest)
curl -X POST https://YOUR_N8N_URL/webhook/board-of-directors \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Should I take this job offer?",
    "options": {
      "delivery": "text",
      "format": "short"
    }
  }'
```

### Test Quick Consult

```bash
curl -X POST https://YOUR_N8N_URL/webhook/board-quick-consult \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Is now a good time to raise prices?",
    "agent": "Warren Buffett"
  }'
```

### Test with Audio

```bash
curl -X POST https://YOUR_N8N_URL/webhook/board-of-directors \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Should I pivot my startup?",
    "options": {
      "delivery": "audio",
      "format": "standard"
    }
  }'
```

---

## Step 5: Activate Workflows

1. Open each workflow
2. Toggle the **Active** switch to ON
3. Webhooks are now live

---

## Environment Variables Reference

| Variable | Required | Description |
|----------|----------|-------------|
| `ELEVEN_LABS_API_KEY` | For audio | 11Labs API key |
| `ELEVEN_LABS_VOICE_ID` | For audio | Voice ID to use |
| `HEYGEN_API_KEY` | For video | HeyGen API key |
| `HEYGEN_AVATAR_ID` | For video | Avatar ID |
| `HEYGEN_VOICE_ID` | For video | Voice ID (optional) |

---

## Customization

### Add or Modify Agents

Edit the `Route to Agents` code node to add new agents:

```javascript
const AGENTS = {
  // Add your agent
  'New Agent': {
    domain: 'Your Domain',
    voice: 'Description of their voice and style',
    frameworks: ['Framework 1', 'Framework 2'],
    tendencies: 'Their natural tendencies',
    keywords: ['keyword1', 'keyword2']
  },
  // ... existing agents
};
```

### Adjust Marcus Voice Style

In the speech script generator, modify the script templates:

```javascript
// Short script
script = `The council has spoken...`;

// Standard script  
script = `I've heard the council...`;

// Full script
script = `The council convened to address...`;
```

### Change Default Agents

Modify the routing logic in `Route to Agents` node to change which agents are selected by default.

---

## Monitoring & Debugging

### View Execution Logs

1. Go to **Executions** in n8n
2. Filter by workflow name
3. Click any execution to see node-by-node output

### Common Issues

| Issue | Solution |
|-------|----------|
| "Missing query field" | Ensure request body has `query` string |
| Anthropic 401 | Check API key credential |
| 11Labs timeout | Check API key, try shorter text |
| HeyGen pending forever | Video may still be processing, check HeyGen dashboard |
| Drive upload fails | Verify OAuth permissions include Drive |

### Timeout Configuration

For long deliberations, increase timeout:

1. **Workflow Settings** → **Timeout**
2. Set to 300 seconds (5 minutes) for video generation

---

## Production Considerations

### Security

1. Consider adding authentication to webhooks
2. Use HTTPS (n8n cloud does this automatically)
3. Rate limit API calls

### Performance

1. Text-only responses: ~30-45 seconds
2. Audio responses: ~60-90 seconds
3. Video responses: ~2-3 minutes

### Costs

| Service | Estimated Cost |
|---------|---------------|
| Anthropic Claude | ~$0.30-0.50 per deliberation |
| 11Labs | ~$0.10-0.30 per audio |
| HeyGen | ~$0.10-0.30 per minute of video |
| **Total per deliberation** | ~$0.50-1.00 |

---

## Webhook URLs

After activation, your endpoints will be:

| Endpoint | URL |
|----------|-----|
| Full Deliberation | `https://YOUR_N8N/webhook/board-of-directors` |
| Quick Consult | `https://YOUR_N8N/webhook/board-quick-consult` |

---

## Next Steps

1. ✅ Import workflows
2. ✅ Configure credentials
3. ✅ Test endpoints
4. ✅ Activate workflows
5. 🔲 Build frontend to consume API
6. 🔲 Set up custom Marcus voice (11Labs)
7. 🔲 Set up custom Marcus avatar (HeyGen)

---

*Setup Guide v1.0*
