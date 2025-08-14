import json
import os
from textwrap import wrap

# Load ASCII arts from JSON file
def load_ascii_arts():
    json_path = os.path.join(os.path.dirname(__file__), 'ascii_arts.json')
    with open(json_path, 'r') as f:
        return json.load(f)

ASCII_ARTS = load_ascii_arts()

def speech_bubble(msg: str, width: int = 42) -> str:
    lines = wrap(msg, width=width) or [msg]
    maxw = max(len(l) for l in lines)
    top    = "  " + "_" * (maxw + 2)
    middle = "\n".join([f"< {l.ljust(maxw)} >" for l in lines])
    bottom = "  " + "-" * (maxw + 2)
    tail   = "         \\ \n          \\"
    return f"{top}\n{middle}\n{bottom}\n{tail}"

def render_art(message: str, art: str) -> str:
    return f"{speech_bubble(message)}\n{art}"