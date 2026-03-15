# Football Stats Agent (Google ADK + Gemini)

A **multi-tool agent** (mirror of the cricket agent) built with **Google Agent Development Kit (ADK)** and **Gemini** that describes international footballers' **stats** (club & international) and **bio** (nationality, place of birth, position, current club).

## Features

- **Stats**: International (caps, goals) and club (appearances, goals, assists, yellow/red cards; clean sheets for goalkeepers).
- **Bio**: Nationality, place of birth, position, current club.
- **Multi-tool**: The agent uses `get_football_player_stats`, `get_football_player_bio`, and `list_available_footballers`.

## Prerequisites

- Python 3.10+
- [Gemini API key](https://aistudio.google.com/app/apikey)

## Setup

1. **Use the same venv as the cricket agent (project root):**

   ```bash
   source .venv/bin/activate   # macOS/Linux
   ```

2. **Dependencies** are already in `requirements.txt` (same as cricket).

3. **API key**: Either copy from cricket or create `football_agent/.env`:

   ```bash
   cp football_agent/.env.example football_agent/.env
   # Edit football_agent/.env and set GOOGLE_API_KEY="your_key"
   ```
   Or re-use `cricket_agent/.env` by copying it to `football_agent/.env`.

## Run the agent

From the **project root**:

**CLI:**

```bash
adk run football_agent
```

**Web UI (both Cricket and Football agents):**

If `adk` is not found, the venv’s `adk` script may have a broken shebang. Use either:

```bash
# Option A: Run via module (works from project root with venv activated)
python3 -m google.adk.cli web --port 8000
```

```bash
# Option B: Use the run script (no need to activate venv)
./run_web.sh
# Or on a different port:  ./run_web.sh 8080
```

Then open **http://localhost:8000**, select **football_stats_agent** (or **cricket_stats_agent**), and chat.

## Example prompts

- "What are Messi's international and club stats?"
- "Where was Cristiano Ronaldo born and what is his current club?"
- "Give me full stats and bio for Erling Haaland."
- "Which footballers can you look up?"
- "How many goals does Mohamed Salah have for Liverpool and Egypt?"

## Project layout

```
Multi-tool-AiAgent/
  football_agent/
    __init__.py
    agent.py           # ADK agent + tools
    football_data.py   # Player data (stats + bio, dummy/representative)
    .env.example
    .env               # GOOGLE_API_KEY (create from .env.example or copy from cricket_agent)
  cricket_agent/
    ...
  requirements.txt
  README.md
  README_FOOTBALL.md   # This file
```

Data is in `football_data.py` (dummy/representative); you can extend it or plug in an external API later.
