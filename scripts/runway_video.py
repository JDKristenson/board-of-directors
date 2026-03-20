"""Generate a Marcus Aurelius video briefing from a BOD verdict.

Creates a Runway Characters real-time session where Marcus Aurelius
delivers the verdict as a 60-second spoken briefing.

Usage:
    python scripts/runway_video.py --verdict-file /tmp/bod_verdict.json

Environment variables:
    RUNWAYML_API_SECRET: Runway API key (required)
    RUNWAY_MARCUS_AVATAR_ID: UUID of Marcus Aurelius avatar (required)
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Optional


SCRIPT_TEMPLATE = """\
Three of history's greatest minds just debated: {question_short}.

{agent_a} argued {position_a}. {agent_b} pushed back, warning {concern_b}. \
{agent_c} cut through with {insight_c}.

After weighing all perspectives, here is the judgment: \
{recommendation}

The first move: {action}. \
Watch for {watch_signal}; that tells you if you're on the right track.

As Marcus Aurelius wrote: "{closer}"

Follow for more from the Board of Directors.\
"""

MAX_SCRIPT_WORDS = 150
MAX_SCRIPT_CHARS = 2000  # Runway personality/startScript limit


def build_script(verdict: dict[str, Any]) -> str:
    """Build a 60-second video script from verdict JSON.

    Args:
        verdict: Dict with keys: agents, question, tension,
                 recommendation, action, watch_signal, closer.
                 Optionally includes a pre-written 'script' key.

    Returns:
        Script text capped at ~150 words.
    """
    if verdict.get("script"):
        return _cap_script(verdict["script"])

    agents = verdict.get("agents", [])
    if len(agents) < 3:
        raise ValueError(f"Expected 3 agents, got {len(agents)}")

    script = SCRIPT_TEMPLATE.format(
        question_short=verdict.get("question", "a strategic decision"),
        agent_a=agents[0],
        position_a=_extract_position(verdict, 0),
        agent_b=agents[1],
        concern_b=_extract_concern(verdict, 1),
        agent_c=agents[2],
        insight_c=_extract_insight(verdict, 2),
        recommendation=verdict.get("recommendation", "proceed with caution"),
        action=verdict.get("action", "gather more information"),
        watch_signal=verdict.get("watch_signal", "early signals of success"),
        closer=verdict.get("closer", "The happiness of your life depends upon the quality of your thoughts."),
    )
    return _cap_script(script)


def _extract_position(verdict: dict[str, Any], idx: int) -> str:
    """Extract position summary for agent at index."""
    positions = verdict.get("positions", [])
    if idx < len(positions):
        return positions[idx]
    return verdict.get("tension", "their perspective")


def _extract_concern(verdict: dict[str, Any], idx: int) -> str:
    """Extract concern for agent at index."""
    concerns = verdict.get("concerns", [])
    if idx < len(concerns):
        return concerns[idx]
    return "of significant risks"


def _extract_insight(verdict: dict[str, Any], idx: int) -> str:
    """Extract insight for agent at index."""
    insights = verdict.get("insights", [])
    if idx < len(insights):
        return insights[idx]
    return "a different perspective entirely"


def _cap_script(script: str) -> str:
    """Cap script to MAX_SCRIPT_WORDS words and MAX_SCRIPT_CHARS characters."""
    words = script.split()
    if len(words) > MAX_SCRIPT_WORDS:
        script = " ".join(words[:MAX_SCRIPT_WORDS])
        if not script.endswith((".", "!", "?", '"')):
            script += "."
    if len(script) > MAX_SCRIPT_CHARS:
        script = script[:MAX_SCRIPT_CHARS - 1] + "."
    return script


def create_session(
    avatar_id: str,
    script: str,
    api_secret: Optional[str] = None,
) -> dict[str, Any]:
    """Create a Runway Characters real-time session.

    Args:
        avatar_id: UUID of the Marcus Aurelius avatar.
        script: Text for Marcus to speak as startScript.
        api_secret: Runway API key. Falls back to env var.

    Returns:
        Dict with session_id, status, and connection info.

    Raises:
        RuntimeError: If API call fails.
        ImportError: If runwayml SDK not installed.
    """
    try:
        from runwayml import RunwayML
    except ImportError as e:
        raise ImportError(
            "runwayml SDK not installed. Run: pip install runwayml"
        ) from e

    secret = api_secret or os.environ.get("RUNWAYML_API_SECRET")
    if not secret:
        raise RuntimeError("RUNWAYML_API_SECRET not set")

    client = RunwayML(api_key=secret)

    personality = (
        "You are Marcus Aurelius, Roman Emperor and Stoic philosopher. "
        "You have just presided over a Board of Directors deliberation. "
        "Deliver the verdict with gravitas, wisdom, and directness. "
        "Speak in measured tones. Do not break character."
    )

    session = client.realtime_sessions.create(
        model="gwm1_avatars",
        avatar={
            "type": "custom",
            "avatarId": avatar_id,
        },
        personality=personality,
        start_script=script,
    )

    session_id = session.id if hasattr(session, "id") else session.get("id")

    return {
        "session_id": session_id,
        "status": "created",
        "message": (
            f"Session created. Poll status at /v1/realtime_sessions/{session_id} "
            "until READY, then consume credentials to connect via WebRTC."
        ),
    }


def load_verdict(path: str | Path) -> dict[str, Any]:
    """Load verdict JSON from file.

    Args:
        path: Path to JSON file.

    Returns:
        Parsed verdict dict.

    Raises:
        FileNotFoundError: If file doesn't exist.
        json.JSONDecodeError: If invalid JSON.
    """
    filepath = Path(path)
    if not filepath.exists():
        raise FileNotFoundError(f"Verdict file not found: {filepath}")
    return json.loads(filepath.read_text())


def main() -> None:
    """CLI entrypoint."""
    parser = argparse.ArgumentParser(
        description="Generate Marcus Aurelius video briefing from BOD verdict"
    )
    parser.add_argument(
        "--verdict-file",
        required=True,
        help="Path to verdict JSON file",
    )
    parser.add_argument(
        "--script-only",
        action="store_true",
        help="Generate script text only, don't create Runway session",
    )
    args = parser.parse_args()

    verdict = load_verdict(args.verdict_file)
    script = build_script(verdict)

    if args.script_only:
        sys.stdout.write(script + "\n")
        word_count = len(script.split())
        sys.stderr.write(f"[{word_count} words, {len(script)} chars]\n")
        return

    avatar_id = os.environ.get("RUNWAY_MARCUS_AVATAR_ID")
    if not avatar_id:
        sys.stderr.write(
            "RUNWAY_MARCUS_AVATAR_ID not set. "
            "Outputting script only.\n"
        )
        sys.stdout.write(script + "\n")
        return

    result = create_session(avatar_id, script)
    sys.stdout.write(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
