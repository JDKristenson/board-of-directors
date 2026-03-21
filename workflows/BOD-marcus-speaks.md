---
name: marcus-speaks
description: "Convert Marcus Aurelius's final judgment into audio or video delivery using 11Labs voice synthesis and/or HeyGen avatar. Transforms written verdicts into compelling briefings."
trigger:
  - "/marcus-speaks"
  - "/brief-me"
  - "Have Marcus brief me"
  - "Video briefing"
  - "Audio briefing"
global: true
---

# Marcus Speaks — Audio/Video Delivery System

## Purpose

Transform Marcus Aurelius's written final judgment into a compelling audio or video briefing. The written word optimizes for precision; the spoken word optimizes for impact and retention.

---

## Delivery Options

| Mode | Output | Duration | Use Case |
|------|--------|----------|----------|
| **Audio Brief** | MP3 | 1-3 min | Personal review, commute listening |
| **Video Avatar** | MP4 | 1-3 min | Client presentations, team shares |
| **Audio + Transcript** | MP3 + MD | 1-3 min | Accessibility, searchability |
| **Premium Video** | MP4 | 2-5 min | High-stakes decisions, board presentations |

---

## Invocation

### After Any Deliberation
```
/marcus-speaks
/marcus-speaks --video
/marcus-speaks --audio
/brief-me
```

### With Options
```
/marcus-speaks --video --formal        # Formal presentation style
/marcus-speaks --audio --conversational # Casual briefing style
/marcus-speaks --video --short         # 60-second summary only
/marcus-speaks --video --full          # Complete judgment with context
```

---

## Workflow Steps

### Step 1: Extract Final Judgment

Pull Marcus Aurelius's verdict from the most recent deliberation:

```
Source: Phase 4 Final Judgment
Extract:
  - Opening acknowledgment (optional for short versions)
  - Core verdict
  - Key reasoning (2-3 points)
  - What remains uncertain
  - Call to action
```

### Step 2: Convert to Speech Script

Written prose ≠ spoken word. The system transforms the judgment:

**Written Style** (from deliberation):
> "The council has deliberated. I have heard each perspective. Buffett rightly 
> identifies that the implied economics of this contract are mediocre. Drucker 
> asks the essential question—not what is profitable, but what is meaningful."

**Spoken Style** (for delivery):
> "I've heard the council. Here's my verdict.
> 
> Buffett is right—the economics don't work. At $138 an hour implied, you're 
> undervaluing yourself.
> 
> Drucker asks the deeper question: Is this meaningful work, or just paid work?
> 
> [pause]
> 
> My judgment: Decline the contract."

### Transformation Rules

| Written | Spoken |
|---------|--------|
| Long sentences | Short, punchy statements |
| Formal transitions | Natural pauses, "Here's the thing..." |
| Hedged language | Direct statements |
| Abstract principles | Concrete examples |
| Bullet points | Numbered sequence ("First... Second...") |
| Citations/references | Implied or simplified |

### Step 3: Voice Synthesis (11Labs)

**API Integration**:
```javascript
// 11Labs Text-to-Speech
const response = await fetch('https://api.elevenlabs.io/v1/text-to-speech/{voice_id}', {
  method: 'POST',
  headers: {
    'xi-api-key': process.env.ELEVEN_LABS_API_KEY,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    text: speechScript,
    model_id: 'eleven_monolingual_v1',
    voice_settings: {
      stability: 0.75,        // Higher = more consistent
      similarity_boost: 0.75  // Higher = closer to original voice
    }
  })
});

const audioBuffer = await response.arrayBuffer();
// Save as MP3
```

**Recommended Voice Settings for Marcus**:
```yaml
voice_profile:
  name: "Marcus Aurelius"
  base_voice: "Antoni" or custom clone
  style:
    stability: 0.75          # Measured, consistent
    similarity_boost: 0.70   # Allow some natural variation
    style: 0.35              # Subtle expressiveness
    speaking_rate: 0.9       # Slightly slower than default
  
  characteristics:
    - Calm authority
    - Measured pacing
    - Strategic pauses before key points
    - Slight gravitas without melodrama
```

**Voice Options**:
1. **Stock Voice**: Use 11Labs "Antoni" (closest to wise elder)
2. **Custom Clone**: Train on Marcus-style readings (audiobooks, dramatic readings)
3. **Professional Clone**: Commission voice actor, clone result

### Step 4: Video Avatar (HeyGen)

**API Integration**:
```javascript
// HeyGen Video Generation
const response = await fetch('https://api.heygen.com/v2/video/generate', {
  method: 'POST',
  headers: {
    'X-Api-Key': process.env.HEYGEN_API_KEY,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    video_inputs: [{
      character: {
        type: 'avatar',
        avatar_id: 'marcus_aurelius_custom', // or stock avatar
        avatar_style: 'normal'
      },
      voice: {
        type: 'elevenlabs',  // Use 11Labs voice
        voice_id: 'your_marcus_voice_id'
      },
      background: {
        type: 'color',
        value: '#1a1a2e'  // Dark, dignified background
      }
    }],
    script: {
      type: 'text',
      input: speechScript
    },
    dimension: {
      width: 1920,
      height: 1080
    }
  })
});

// Poll for completion, download video
```

**Avatar Options**:

| Option | Setup | Quality | Cost |
|--------|-------|---------|------|
| **Stock Avatar** | Immediate | Good | ~$0.10/min |
| **Photo Avatar** | Upload image | Better | ~$0.10/min |
| **Custom Avatar** | Pro plan, training | Best | Higher |
| **Studio Avatar** | Professional shoot | Premium | $500+ setup |

**Recommended Avatar Setup**:
```yaml
avatar_profile:
  name: "Marcus Aurelius"
  options:
    1_quick:
      type: stock
      avatar: "wise_elder_male" # or similar
      background: dark_gradient
      
    2_better:
      type: photo_avatar
      source: "marcus_aurelius_statue.jpg" # Classical bust
      style: professional
      
    3_premium:
      type: custom_avatar
      training_video: "marcus_actor_reading.mp4"
      style: photorealistic
```

---

## Script Templates

### Short Brief (60 seconds)

```markdown
## Marcus Speaks — Short Brief

[Opening - 5 sec]
"The council has spoken. Here's my verdict."

[Core Judgment - 20 sec]
"[STATE THE DECISION IN ONE SENTENCE]"

"[KEY REASON 1 - most important]"

[Call to Action - 15 sec]
"[SPECIFIC NEXT STEP]"

[Close - 5 sec]
"Now act."
```

### Standard Brief (2-3 minutes)

```markdown
## Marcus Speaks — Standard Brief

[Opening - 10 sec]
"I've heard the council deliberate on [TOPIC]. 
Three perspectives. One question. Here's where I land."

[Acknowledge Perspectives - 30 sec]
"[AGENT 1] argued [POSITION]. There's truth in this.
[AGENT 2] countered with [POSITION]. Also valid.
[AGENT 3] reminded us that [POSITION]."

[The Tension - 15 sec]
"The real tension is [CORE TRADE-OFF]."

[Judgment - 30 sec]
"My judgment: [CLEAR VERDICT]"

"Here's why: [REASONING IN 2-3 POINTS]"

[Uncertainty - 15 sec]
"What I don't know: [KEY UNCERTAINTY]"

[Call to Action - 20 sec]
"[SPECIFIC NEXT STEPS - numbered]"

[Close - 10 sec]
"The decision is yours. But if you ask what wisdom counsels—this is it."
```

### Full Brief (4-5 minutes)

```markdown
## Marcus Speaks — Full Brief

[Opening - 15 sec]
"The council convened on [DATE] to address this question:
[STATE THE QUESTION]"

[Context - 30 sec]
"[BRIEF BACKGROUND - why this matters]"

[Panel Introduction - 20 sec]
"I heard from three advisors:
- [Agent 1], who brought [LENS]
- [Agent 2], who brought [LENS]  
- [Agent 3], who brought [LENS]"

[Each Perspective - 60 sec total]
"[AGENT 1]'s view: [SUMMARY]
[AGENT 2]'s view: [SUMMARY]
[AGENT 3]'s view: [SUMMARY]"

[Consensus - 20 sec]
"Where they agreed: [CONSENSUS POINTS]"

[Tension - 20 sec]
"Where they clashed: [DISAGREEMENT]"

[Judgment - 45 sec]
"After weighing all perspectives, my judgment is this:

[VERDICT]

The reasoning: [FULL RATIONALE]"

[Stoic Principle - 20 sec]
"[RELEVANT STOIC WISDOM]"

[Uncertainty - 15 sec]
"What remains uncertain: [KEY UNKNOWNS]"

[Call to Action - 30 sec]
"Your next steps:
First, [ACTION 1]
Second, [ACTION 2]
Third, [ACTION 3]"

[Close - 15 sec]
"This too shall pass—so act well while it is before you.
The council has spoken."
```

---

## Output Formats

### Audio Output
```
/outputs/briefings/
├── 2025-01-26-consulting-contract-brief.mp3
├── 2025-01-26-consulting-contract-transcript.md
└── 2025-01-26-consulting-contract-metadata.json
```

### Video Output
```
/outputs/briefings/
├── 2025-01-26-consulting-contract-brief.mp4
├── 2025-01-26-consulting-contract-thumbnail.jpg
├── 2025-01-26-consulting-contract-transcript.md
└── 2025-01-26-consulting-contract-metadata.json
```

### Metadata
```json
{
  "deliberation_id": "2025-01-26-consulting-contract",
  "generated": "2025-01-26T15:30:00Z",
  "format": "video",
  "duration_seconds": 147,
  "voice": "marcus_custom_v2",
  "avatar": "marcus_photo_avatar",
  "script_version": "standard",
  "panel": ["Buffett", "Drucker", "Taleb"],
  "verdict_summary": "Decline the contract"
}
```

---

## Integration Architecture

### Option A: Antigravity-Native (Recommended)

```
┌─────────────────┐
│  Deliberation   │
│  (5 phases)     │
└────────┬────────┘
         │ Final Judgment (MD)
         ▼
┌─────────────────┐
│  Script         │
│  Transformer    │
└────────┬────────┘
         │ Speech Script
         ▼
┌─────────────────┐     ┌─────────────────┐
│  11Labs API     │────▶│  Audio File     │
└─────────────────┘     └─────────────────┘
         │
         │ Voice Audio
         ▼
┌─────────────────┐     ┌─────────────────┐
│  HeyGen API     │────▶│  Video File     │
└─────────────────┘     └─────────────────┘
```

### Option B: n8n Workflow Automation

```
Trigger: Webhook from Antigravity
  │
  ▼
Extract Final Judgment
  │
  ▼
Transform to Speech Script
  │
  ├──▶ 11Labs: Generate Audio
  │         │
  │         ▼
  │    HeyGen: Generate Video (using 11Labs audio)
  │         │
  ▼         ▼
Store in Google Drive / Return to User
```

### Option C: Make.com / Zapier

Similar to n8n, with visual workflow builder.

---

## API Credentials Setup

### 11Labs
```yaml
# Store in environment or secrets manager
ELEVEN_LABS_API_KEY: "your_api_key"
ELEVEN_LABS_VOICE_ID: "your_marcus_voice_id"

# Get API key: https://elevenlabs.io/
# Pricing: ~$0.30/1000 characters (Starter plan)
```

### HeyGen
```yaml
HEYGEN_API_KEY: "your_api_key"
HEYGEN_AVATAR_ID: "your_marcus_avatar_id"

# Get API key: https://www.heygen.com/
# Pricing: ~$0.10/minute video (Creator plan)
```

---

## Cost Estimates

| Delivery Type | Typical Length | Estimated Cost |
|---------------|----------------|----------------|
| Audio (60 sec) | ~500 chars | ~$0.15 |
| Audio (3 min) | ~2000 chars | ~$0.60 |
| Video (60 sec) | 1 minute | ~$0.10 |
| Video (3 min) | 3 minutes | ~$0.30 |
| **Typical Full Brief** | 2-3 min | **~$0.70-1.00** |

---

## Example Output

### Input (Final Judgment Excerpt)
```markdown
## Marcus Aurelius — Arbiter's Verdict

The council has deliberated. I have heard each perspective.

**To Warren**: You rightly identify that the implied economics of this 
contract are mediocre...

**My Judgment**: Decline the contract.

The council is unanimous in direction. The $180K is real, but what you 
would give up—the board seat, the momentum, the optionality—is worth more.

**Call to Action**:
1. Decline the contract within the week
2. Pursue the board seat actively
3. Protect your advisory practice
```

### Output (Speech Script)
```
I've heard the council. Three perspectives on your consulting contract decision.

Buffett looked at the numbers. At $138 an hour implied, you're selling yourself 
short. And the opportunity cost? The board seat. The advisory momentum. These 
compound. The contract doesn't.

Drucker asked the deeper question: Does this work develop you, or just employ you?

Taleb cut through it all: You're trading options for certainty. That's almost 
always a bad trade.

[pause]

My judgment: Decline the contract.

The council was unanimous. The money is real, but what you'd give up is worth more.

Here's what you do next:

First—decline this week. Don't delay. Clarity is kind.

Second—pursue that board seat. If it's worth giving up $180K, it's worth fighting for.

Third—protect your advisory practice. Use this time to deepen those relationships.

[pause]

The decision is yours. But if you ask what wisdom counsels—this is it.

Now act.
```

---

## Voice & Avatar Customization

### Creating a Custom Marcus Voice (11Labs)

1. **Source Material** (need 30+ minutes of audio):
   - Audiobook readings of *Meditations*
   - Professional voice actor reading Marcus quotes
   - Historical drama performances (Gladiator, etc.)

2. **Upload to 11Labs**:
   - Go to Voice Lab → Add Voice → Instant Voice Cloning
   - Upload clean audio samples
   - Name: "Marcus Aurelius"
   - Test and refine

3. **Fine-tune Settings**:
   ```yaml
   stability: 0.75      # Consistent, authoritative
   similarity: 0.70     # Natural variation
   style: 0.30          # Subtle expression
   speaker_boost: true  # Clarity enhancement
   ```

### Creating a Custom Marcus Avatar (HeyGen)

**Option 1: Photo Avatar** (Quick)
- Use a classical bust image of Marcus Aurelius
- HeyGen animates the image
- Works well for "historical figure" aesthetic

**Option 2: Actor Stand-in** (Better)
- Hire actor on Fiverr/Upwork to record 2-min video
- Match: older male, beard, dignified bearing
- HeyGen clones the avatar from video
- More natural movement and expression

**Option 3: AI-Generated Face** (Experimental)
- Use Midjourney/DALL-E to generate Marcus likeness
- Convert to HeyGen photo avatar
- Good middle ground

---

## Commands Reference

| Command | Action |
|---------|--------|
| `/marcus-speaks` | Generate standard audio brief |
| `/marcus-speaks --video` | Generate video with avatar |
| `/marcus-speaks --short` | 60-second summary only |
| `/marcus-speaks --full` | Complete 4-5 minute brief |
| `/marcus-speaks --formal` | Formal presentation tone |
| `/marcus-speaks --casual` | Conversational tone |
| `/set-voice [id]` | Set custom 11Labs voice |
| `/set-avatar [id]` | Set custom HeyGen avatar |

---

## Future Enhancements

1. **Agent Voices**: Give each agent their own voice for debate highlights
2. **Visual Aids**: Add charts/graphics to video based on deliberation data
3. **Multi-Language**: Translate and generate in other languages
4. **Podcast Format**: Generate full deliberation as multi-voice podcast
5. **Interactive Video**: HeyGen interactive avatars for follow-up questions

---

*Marcus Speaks v1.0 | Audio/Video Delivery for Board Judgments*
