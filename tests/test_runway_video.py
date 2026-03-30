"""Tests for runway_video.py script generation and verdict loading."""

from __future__ import annotations

import json
import os
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

sys_path_fix = str(Path(__file__).resolve().parent.parent / "scripts")
import sys  # noqa: E402

sys.path.insert(0, sys_path_fix)

from runway_video import (  # noqa: E402
    MAX_SCRIPT_CHARS,
    MAX_SCRIPT_WORDS,
    _cap_script,
    build_script,
    create_session,
    load_verdict,
)


@pytest.fixture
def sample_verdict() -> dict:
    """Minimal valid verdict for testing."""
    return {
        "agents": ["Warren Buffett", "Nassim Taleb", "Marc Andreessen"],
        "question": "Should a bootstrapped SaaS founder accept a $10M Series A",
        "tension": "capital as weapon vs liability",
        "recommendation": "Decline unless a credible competitive threat is imminent.",
        "action": "Map every funded competitor in your space",
        "watch_signal": "a competitor closing a $20M+ round",
        "closer": "Never let the future disturb you.",
    }


@pytest.fixture
def sample_verdict_with_script() -> dict:
    """Verdict with pre-written script."""
    return {
        "agents": ["Buffett", "Taleb", "Andreessen"],
        "question": "test question",
        "script": "This is a pre-written script for Marcus to deliver.",
    }


@pytest.fixture
def verdict_file(tmp_path: Path, sample_verdict: dict) -> Path:
    """Write verdict to a temp file."""
    p = tmp_path / "verdict.json"
    p.write_text(json.dumps(sample_verdict))
    return p


class TestBuildScript:
    """Tests for build_script()."""

    def test_generates_script_from_verdict(self, sample_verdict: dict) -> None:
        script = build_script(sample_verdict)
        assert isinstance(script, str)
        assert len(script) > 50
        assert "Buffett" in script
        assert "Taleb" in script
        assert "Andreessen" in script

    def test_includes_recommendation(self, sample_verdict: dict) -> None:
        script = build_script(sample_verdict)
        assert "Decline" in script

    def test_includes_closer_quote(self, sample_verdict: dict) -> None:
        script = build_script(sample_verdict)
        assert "Never let the future disturb you" in script

    def test_respects_word_limit(self, sample_verdict: dict) -> None:
        script = build_script(sample_verdict)
        word_count = len(script.split())
        assert word_count <= MAX_SCRIPT_WORDS

    def test_respects_char_limit(self, sample_verdict: dict) -> None:
        script = build_script(sample_verdict)
        assert len(script) <= MAX_SCRIPT_CHARS

    def test_uses_prewritten_script(self, sample_verdict_with_script: dict) -> None:
        script = build_script(sample_verdict_with_script)
        assert script == "This is a pre-written script for Marcus to deliver."

    def test_raises_on_insufficient_agents(self) -> None:
        with pytest.raises(ValueError, match="Expected 3 agents"):
            build_script({"agents": ["Buffett", "Taleb"]})

    def test_handles_empty_agents_list(self) -> None:
        with pytest.raises(ValueError, match="Expected 3 agents"):
            build_script({"agents": []})

    def test_includes_action_item(self, sample_verdict: dict) -> None:
        script = build_script(sample_verdict)
        assert "Map every funded competitor" in script

    def test_includes_watch_signal(self, sample_verdict: dict) -> None:
        script = build_script(sample_verdict)
        assert "competitor closing" in script


class TestCapScript:
    """Tests for _cap_script()."""

    def test_short_script_unchanged(self) -> None:
        short = "This is a short script."
        assert _cap_script(short) == short

    def test_caps_at_word_limit(self) -> None:
        long_script = " ".join(["word"] * 200)
        result = _cap_script(long_script)
        assert len(result.split()) <= MAX_SCRIPT_WORDS + 1  # +1 for period

    def test_caps_at_char_limit(self) -> None:
        long_script = "a" * 3000
        result = _cap_script(long_script)
        assert len(result) <= MAX_SCRIPT_CHARS

    def test_adds_period_when_capping(self) -> None:
        long_script = " ".join(["word"] * 200)
        result = _cap_script(long_script)
        assert result.endswith(".")


class TestLoadVerdict:
    """Tests for load_verdict()."""

    def test_loads_valid_json(self, verdict_file: Path) -> None:
        result = load_verdict(verdict_file)
        assert result["agents"] == ["Warren Buffett", "Nassim Taleb", "Marc Andreessen"]

    def test_raises_on_missing_file(self) -> None:
        with pytest.raises(FileNotFoundError):
            load_verdict("/nonexistent/path.json")

    def test_raises_on_invalid_json(self, tmp_path: Path) -> None:
        bad_file = tmp_path / "bad.json"
        bad_file.write_text("not json {{{")
        with pytest.raises(json.JSONDecodeError):
            load_verdict(bad_file)


class TestCreateSession:
    """Tests for create_session() with mocked SDK."""

    def test_creates_session_successfully(self) -> None:
        mock_runway_module = MagicMock()
        mock_client = MagicMock()
        mock_runway_module.RunwayML.return_value = mock_client
        mock_session = MagicMock()
        mock_session.id = "session_abc123"
        mock_client.realtime_sessions.create.return_value = mock_session

        with patch.dict("sys.modules", {"runwayml": mock_runway_module}):
            result = create_session(
                avatar_id="avatar_123",
                script="Test script for Marcus.",
                api_secret="key_test123",
            )

        assert result["session_id"] == "session_abc123"
        assert result["status"] == "created"
        mock_client.realtime_sessions.create.assert_called_once()

    def test_raises_without_api_secret(self) -> None:
        mock_runway_module = MagicMock()
        with patch.dict("sys.modules", {"runwayml": mock_runway_module}), patch.dict(
            os.environ, {}, clear=True
        ):
            os.environ.pop("RUNWAYML_API_SECRET", None)
            with pytest.raises(RuntimeError, match="RUNWAYML_API_SECRET not set"):
                create_session("avatar_123", "script", api_secret=None)

    def test_raises_on_missing_sdk(self) -> None:
        with patch.dict("sys.modules", {"runwayml": None}), pytest.raises(
            ImportError, match="runwayml SDK not installed"
        ):
            create_session("avatar_123", "script", api_secret="key_test")
