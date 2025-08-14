import json
import os
from textwrap import wrap
from typing import List


def _repo_path(*parts: str) -> str:
    """Build a path relative to this file."""
    return os.path.join(os.path.dirname(__file__), *parts)


def load_ascii_arts() -> List[str]:
    """
    Load ASCII arts from ascii_arts.json (UTF-8).
    Returns an empty list if the file is missing or invalid.
    """
    json_path = _repo_path("ascii_arts.json")
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


ASCII_ARTS: List[str] = load_ascii_arts()


def _wrap_lines(text: str, width: int) -> List[str]:
    """
    Wrap text into multiple lines but preserve existing newlines.
    """
    chunks = text.splitlines() or [text]
    lines: List[str] = []
    for chunk in chunks:
        wrapped = wrap(chunk, width=width) if chunk else [""]
        lines.extend(wrapped)
    return lines


def speech_bubble(msg: str, width: int = 42) -> str:
    """
    Render a speech bubble for the given message.
    Width controls wrapping inside the bubble (minimum 10).
    """
    width = max(10, int(width))
    lines = _wrap_lines(msg, width=width)
    maxw = max((len(line) for line in lines), default=0)

    top = "  " + "_" * (maxw + 2)
    middle = "\n".join(f"< {line.ljust(maxw)} >" for line in lines)
    bottom = "  " + "-" * (maxw + 2)

    # A simple two-line tail; aligns under the left side of the bubble.
    tail = "   \\\n    \\"

    return f"{top}\n{middle}\n{bottom}\n{tail}"


def render_art(message: str, art: str) -> str:
    """Combine a speech bubble with an ASCII art block."""
    return f"{speech_bubble(message)}\n{art}"