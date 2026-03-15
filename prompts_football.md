# Test Prompts for Football Stats Agent

Use these with **football_stats_agent** (CLI: `adk run football_agent` or Web: `adk web --port 8000` → select football_stats_agent).

---

## 1. Stats (international / club)

| # | Prompt | What to check |
|---|--------|----------------|
| 1 | What are Messi's international stats? | Uses `get_football_player_stats`; returns caps, goals. |
| 2 | Give me Cristiano Ronaldo's club goals and appearances. | Club stats (appearances, goals, assists). |
| 3 | How many goals does Erling Haaland have for club and country? | International + club goals. |

---

## 2. Bio (nationality, position, club)

| # | Prompt | What to check |
|---|--------|----------------|
| 4 | Where was Kylian Mbappé born and what is his position? | Place of birth, position. |
| 5 | What is Mohamed Salah's current club and nationality? | current_club, nationality. |
| 6 | Tell me the position and club of Kevin De Bruyne. | position, current_club. |

---

## 3. Combined (stats + bio)

| # | Prompt | What to check |
|---|--------|----------------|
| 7 | Tell me everything about Lionel Messi: where he's from and his stats. | Both tools; full summary. |
| 8 | Full profile of Jude Bellingham – club, country, and stats. | Bio + stats. |

---

## 4. List / discovery

| # | Prompt | What to check |
|---|--------|----------------|
| 9 | Which footballers can you look up? | Uses `list_available_footballers`. |
| 10 | What players do you have data for? | Same. |

---

## 5. Partial names / not found

| # | Prompt | What to check |
|---|--------|----------------|
| 11 | Stats for Mbappé. | Resolves to Kylian Mbappé. |
| 12 | Give me stats for Unknown Player XYZ. | Clear "not found" and hint to use list. |

---

*Agent: `football_stats_agent` · Model: gemini-2.5-flash*
