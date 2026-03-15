# Multi-Tool AI Agents (Google ADK + Gemini)

This project runs **multiple agents** with the **Google Agent Development Kit (ADK)** and **Gemini**: a **cricket stats agent** and a **football stats agent**. Each agent uses several tools to look up player stats and bio; you can use the built-in dev UI or a custom **Agent Studio** UI with event diagrams and table-style answers.

## Agents

| Agent | Directory | Description |
|-------|-----------|-------------|
| **Cricket** | `cricket_agent/` | International cricketers: stats (Test, ODI, T20) and bio (nationality, place of birth). Tools: `get_cricketer_international_stats`, `get_cricketer_bio`, `list_available_cricketers`. |
| **Football** | `football_agent/` | International footballers: club & international stats (apps, goals, assists, cards) and bio (nationality, position, current club). Tools: `get_football_player_stats`, `get_football_player_bio`, `list_available_footballers`. Comparisons (e.g. Neymar vs Ronaldo) are returned as markdown tables and rendered as tables in the custom UI. |

## Prerequisites

- Python 3.10+
- [Gemini API key](https://aistudio.google.com/app/apikey) (one per agent or shared)

## Setup

1. **Create and activate a virtual environment (recommended):**

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   # .venv\Scripts\activate    # Windows
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set your Gemini API key for each agent you use:**

   ```bash
   cp cricket_agent/.env.example cricket_agent/.env
   cp football_agent/.env.example football_agent/.env
   # Edit each .env and set GOOGLE_API_KEY="your_key"
   ```

   You can use the same key in both, or different keys (e.g. different accounts). Each agent loads its own `GOOGLE_API_KEY` from its `.env` when it runs.

## Running the agents

All commands are from the **project root** (the folder that contains `cricket_agent/` and `football_agent/`).

### Option 1: CLI (single agent)

```bash
adk run cricket_agent
# or
adk run football_agent
```

If `adk` is not found, use: `python3 -m google.adk.cli run cricket_agent` (or `football_agent`).

### Option 2: ADK dev UI only (both agents, port 8000)

```bash
./run_web.sh
# Or:  adk web --port 8000
```

Then open **http://localhost:8000**, choose **cricket_stats_agent** or **football_stats_agent**, and chat.

### Option 3: Custom “Agent Studio” UI (recommended)

```bash
./run_web_ui.sh
```

Then open **http://localhost:3000**. This starts:

- **ADK API** on port **8000**
- **Custom UI + API proxy** on port **3000** (all API calls go through the proxy; no CORS issues)

The custom UI provides:

- **Agent selector** – switch between cricket_agent and football_agent
- **Agent type** – short description of the selected agent
- **New session** – start a fresh conversation
- **Chat** – send messages; agent replies and tool calls appear in the thread
- **Tables** – for football, comparison answers (e.g. “compare Neymar and Ronaldo”) are shown in table format
- **Event diagram** – right panel shows a graph of agent and tools for the selected event
- **Event detail** – raw JSON for the selected event

The script frees ports **8000** and **3000** automatically if they were in use. If you see **“API unreachable”** or **“No agents found”**, ensure `./run_web_ui.sh` is running and refresh the page.

## Example prompts

**Cricket**

- "What are Virat Kohli's ODI and Test stats?"
- "Where was Sachin Tendulkar born and what is his nationality?"
- "Give me full stats and bio for Babar Azam."
- "Which cricketers can you look up?"

**Football**

- "What are Messi's international and club stats?"
- "Show me stats of Cristiano Ronaldo."
- "Compare Neymar and Ronaldo based on their stats."
- "Which footballers can you look up?"

## Project layout

```
Multi-tool-AiAgent/
  cricket_agent/
    __init__.py
    agent.py              # ADK agent + tools
    cricket_data.py       # Player data (stats + bio)
    .env.example
    .env                  # GOOGLE_API_KEY
  football_agent/
    __init__.py
    agent.py              # ADK agent + tools
    football_data.py      # Player data
    football_players.json # 200 players (La Liga, Premier League, etc.)
    .env.example
    .env                  # GOOGLE_API_KEY
  web_ui/
    index.html            # Agent Studio UI (chat, events, tables, diagram)
    proxy_server.py       # Serves UI and proxies API to port 8000
  run_web.sh              # ADK only (port 8000)
  run_web_ui.sh           # ADK + custom UI proxy (8000 + 3000)
  setup_venv.sh            # Recreate .venv (e.g. after copy from another machine)
  requirements.txt
  README.md                # This file
  README_FOOTBALL.md       # Football agent details
```

Data is bundled in `cricket_data.py` and `football_agent/` (including `football_players.json`) for demo; you can extend or plug in external APIs.

## Troubleshooting

### "API unreachable" / "No agents found" (custom UI at 3000)

- Ensure **`./run_web_ui.sh`** is running and wait ~10 seconds after start.
- Open **http://localhost:3000** (not 8000) for the Agent Studio UI.
- Refresh the page after the script has fully started.

### 429 RESOURCE_EXHAUSTED / quota exceeded

- **Free tier**: The agents use `gemini-2.5-flash`, which has daily/minute limits. Wait for the limit to reset or check [Gemini API rate limits](https://ai.google.dev/gemini-api/docs/rate-limits) and [usage](https://ai.dev/rate-limit).
- **New key**: Use a different Gemini API key (e.g. from another account) by updating `cricket_agent/.env` and/or `football_agent/.env`, then restart with `./run_web_ui.sh`.
- **Other model**: In `cricket_agent/agent.py` or `football_agent/agent.py` you can change `model=` to another [supported model](https://ai.google.dev/gemini-api/docs/models) that has quota on your plan.

### "adk: command not found"

- Activate the venv: `source .venv/bin/activate`, or run via module: `python3 -m google.adk.cli web --port 8000`.
- Or use the scripts: `./run_web.sh` or `./run_web_ui.sh` (they use `.venv/bin/adk`).

### "code signature not valid" / "library load disallowed by system policy" (macOS)

The venv was likely created or copied from another machine. Recreate it on your Mac:

```bash
./setup_venv.sh
source .venv/bin/activate
# Copy API keys into cricket_agent/.env and football_agent/.env if needed
./run_web_ui.sh
```

## See also

- **README_FOOTBALL.md** – Football agent features and example prompts.
- [ADK docs](https://google.github.io/adk-docs/) – Agent Development Kit.
- [Gemini API](https://ai.google.dev/gemini-api/docs) – Models and rate limits.
