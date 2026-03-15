"""
Football player data: stats (club & international) and bio.
Loads from football_players.json (La Liga, Premier League, top 200 players).
"""

import json
import os
from typing import Optional

_DATA_DIR = os.path.dirname(os.path.abspath(__file__))
_JSON_PATH = os.path.join(_DATA_DIR, "football_players.json")


def _load_footballers() -> dict:
    """Load players from JSON and return dict keyed by normalized name."""
    out = {}
    if not os.path.isfile(_JSON_PATH):
        return out
    with open(_JSON_PATH, encoding="utf-8") as f:
        players = json.load(f)
    for p in players:
        name = p.get("name") or ""
        key = (name or "").strip().lower()
        if not key:
            continue
        # Ensure club has required keys; add clean_sheets for goalkeepers if missing
        club = p.get("club") or {}
        if p.get("position") == "Goalkeeper" and "clean_sheets" not in club:
            club["clean_sheets"] = club.get("clean_sheets", 0)
        out[key] = {
            "name": p.get("name", ""),
            "nationality": p.get("nationality", ""),
            "place_of_birth": p.get("place_of_birth", ""),
            "position": p.get("position", ""),
            "current_club": p.get("current_club", ""),
            "international": p.get("international") or {"caps": 0, "goals": 0},
            "club": club,
        }
    return out


FOOTBALLERS = _load_footballers()


def _normalize_name(name: str) -> str:
    return (name or "").strip().lower()


def find_footballer(player_name: str) -> Optional[dict]:
    """Return footballer record by name (fuzzy match on normalized name)."""
    key = _normalize_name(player_name)
    if key in FOOTBALLERS:
        return FOOTBALLERS[key].copy()
    for fkey, data in FOOTBALLERS.items():
        if key in fkey or fkey in key:
            return data.copy()
    return None


def list_footballer_names() -> list[str]:
    """Return list of known footballer names for hints."""
    seen = set()
    out = []
    for v in FOOTBALLERS.values():
        n = v["name"]
        if n not in seen:
            seen.add(n)
            out.append(n)
    return sorted(out)
