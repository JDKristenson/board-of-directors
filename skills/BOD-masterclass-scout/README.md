# MasterClass Scout Skill

A Google Antigravity skill that scouts MasterClass instructors to identify candidates for expanding the Board of Directors agent roster.

## Installation

### Option 1: Copy to Skills Directory
```bash
cp -r masterclass-scout ~/.gemini/antigravity/skills/
```

### Option 2: Symlink (for development)
```bash
ln -s /path/to/masterclass-scout ~/.gemini/antigravity/skills/masterclass-scout
```

## Dependencies

This skill requires the **Board of Directors** system (v1.3+) to be installed:
```
~/.gemini/antigravity/board-of-directors/
```

## Usage

### Manual Scout
```
/scout-masterclass
```
or
```
"Find new agents from MasterClass"
"Scout for new board members"
```

### With Options
```
/scout-masterclass --gaps        # Show coverage gaps only
/scout-masterclass --category Writing   # Focus on specific category
/scout-masterclass --compare "Gordon Ramsay"  # Evaluate specific instructor
```

### Scheduled (if automation enabled)
The skill runs automatically every Sunday at 9:00 AM.

## Output

Scout reports are saved to:
```
~/.gemini/antigravity/board-of-directors/scout-reports/
```

Format: `YYYY-MM-DD-scout-report.md`

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Main skill instructions and workflow |
| `instructor-reference.md` | Database of known MasterClass instructors |
| `report-template.md` | Template for generating scout reports |
| `manifest.json` | Skill metadata and configuration |
| `examples/` | Sample completed reports |

## How Scoring Works

Each candidate is scored on four criteria:

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Domain Gap Fill | 40% | Does this fill an unrepresented domain? |
| Distinctiveness | 25% | Unique perspective vs. existing agents? |
| Profile Buildability | 20% | Quality source material available? |
| User Relevance | 15% | Alignment with user's work domains? |

## After Scouting

To build a profile for a recommended candidate:
```
/add-agent [Name]: [Domain] expert known for [specialty]
```

Or request full research:
```
"Build a complete agent profile for [Name]"
```

## Customization

### Adjust Scoring Weights
Edit the weights in `SKILL.md` under "Step 4: Score Candidates"

### Add Instructors to Reference
Edit `instructor-reference.md` to add new MasterClass instructors

### Change Schedule
Edit `manifest.json` to adjust the cron schedule

## Version History

- **1.0.0** (2025-01-26): Initial release

## License

Part of the Board of Directors system for Google Antigravity IDE.
