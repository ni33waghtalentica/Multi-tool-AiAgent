#!/usr/bin/env python3
"""
Standalone test for football_agent data and tools (no ADK/LLM).
Run from project root: python test_football_agent.py
"""
import sys
import importlib.util
sys.path.insert(0, ".")

def test_football_data():
    spec = importlib.util.spec_from_file_location("football_data", "football_agent/football_data.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    find_footballer = m.find_footballer
    list_footballer_names = m.list_footballer_names
    FOOTBALLERS = m.FOOTBALLERS
    assert len(FOOTBALLERS) >= 15
    p = find_footballer("Messi")
    assert p is not None and p["name"] == "Lionel Messi"
    assert p["international"]["goals"] == 108
    p2 = find_footballer("Haaland")
    assert p2 is not None and p2["current_club"] == "Manchester City"
    names = list_footballer_names()
    assert "Lionel Messi" in names and "Cristiano Ronaldo" in names
    print("  football_data: OK")

def test_agent_tools():
    try:
        from football_agent.agent import (
            get_football_player_stats,
            get_football_player_bio,
            list_available_footballers,
        )
    except ImportError as e:
        print("  agent tools: SKIP (ADK not installed:", e, ")")
        return
    r = get_football_player_stats("Messi")
    assert r["status"] == "success" and r["player_name"] == "Lionel Messi"
    assert "international" in r and "club" in r
    r2 = get_football_player_bio("Ronaldo")
    assert r2["status"] == "success" and "Portugal" in r2["nationality"]
    r3 = list_available_footballers()
    assert r3["status"] == "success" and len(r3["footballers"]) >= 15
    r4 = get_football_player_stats("Unknown Player XYZ")
    assert r4["status"] == "error"
    print("  agent tools: OK")

if __name__ == "__main__":
    print("Testing football_agent...")
    test_football_data()
    test_agent_tools()
    print("All tests passed.")
