# Test Prompts for Cricket Stats Agent

Use these prompts with **cricket_stats_agent** (CLI: `adk run cricket_agent` or Web: `adk web --port 8000`). Review each response to confirm the agent uses the right tools and answers correctly.

---

## 1. International stats (single format)

| # | Prompt | What to check |
|---|--------|----------------|
| 1 | What are Virat Kohli's ODI stats? | Uses `get_cricketer_international_stats`, returns ODI matches, runs, batting_avg, wickets. |
| 2 | Give me Sachin Tendulkar's Test match statistics. | Returns Test stats only (or all formats with Test highlighted). |
| 3 | What are Rohit Sharma's T20 figures? | Returns T20 stats. |

---

## 2. International stats (all formats)

| # | Prompt | What to check |
|---|--------|----------------|
| 4 | Show me MS Dhoni's international stats across Test, ODI and T20. | Uses stats tool; response includes Test, ODI, and T20. |
| 5 | Full career stats for Babar Azam in all formats. | All three formats present. |
| 6 | Compare Kane Williamson's stats in Tests, ODIs and T20Is. | Clear breakdown for each format. |

---

## 3. Bio (nationality & place of birth)

| # | Prompt | What to check |
|---|--------|----------------|
| 7 | Where was Sachin Tendulkar born? | Uses `get_cricketer_bio`; place of birth (e.g. Mumbai, Maharashtra, India). |
| 8 | What is Ben Stokes's nationality? | Nationality (England). |
| 9 | Where is Rashid Khan from and where was he born? | Nationality (Afghanistan) and place of birth. |
| 10 | Tell me the nationality and place of birth of Shakib Al Hasan. | Both fields from bio tool. |

---

## 4. Stats + bio (combined)

| # | Prompt | What to check |
|---|--------|----------------|
| 11 | Tell me everything about Virat Kohli: where he's from and his stats in all formats. | Uses both `get_cricketer_bio` and `get_cricketer_international_stats`; full summary. |
| 12 | Who is Pat Cummins? Give me his background and his international stats. | Bio + stats (Test/ODI/T20). |
| 13 | I want a full profile of Jos Buttler – nationality, birth place, and career stats. | Combined bio and stats. |

---

## 5. List / discovery

| # | Prompt | What to check |
|---|--------|----------------|
| 14 | Which cricketers can you look up? | Uses `list_available_cricketers`; returns list of player names. |
| 15 | What players do you have data for? | Same as above. |
| 16 | Do you have stats for Indian cricketers? | May list Indian players or point to the full list. |

---

## 6. Partial / alternate names

| # | Prompt | What to check |
|---|--------|----------------|
| 17 | Stats for Kohli. | Resolves to Virat Kohli and returns stats. |
| 18 | Where was Dhoni born? | Resolves to MS Dhoni, returns place of birth. |
| 19 | Give me Steve Smith's Test average. | Resolves to Steve Smith; Test batting_avg in response. |

---

## 7. Bowlers / all-rounders

| # | Prompt | What to check |
|---|--------|----------------|
| 20 | What are Jasprit Bumrah's international bowling stats? | Stats tool; wickets highlighted for Test/ODI/T20. |
| 21 | Shaheen Afridi's stats in ODIs and T20s. | ODI and T20 stats (wickets). |
| 22 | Shakib Al Hasan's stats – batting and bowling. | Both runs and wickets across formats. |

---

## 8. Player not in database (error handling)

| # | Prompt | What to check |
|---|--------|----------------|
| 23 | What are Don Bradman's ODI stats? | Graceful message (e.g. player not found); suggests trying from available list. |
| 24 | Where was Ricky Ponting born? | Same – not in data; suggests available cricketers. |
| 25 | Give me full stats for XYZ Unknown Player. | Clear “not found” and hint to use list. |

---

## 9. Short / casual

| # | Prompt | What to check |
|---|--------|----------------|
| 26 | Virat Kohli ODI runs? | Short answer with ODI runs. |
| 27 | Where is Quinton de Kock from? | Nationality (South Africa). |
| 28 | How many Test matches did Joe Root play? | Test matches count. |

---

## 10. Multi-player (if supported)

| # | Prompt | What to check |
|---|--------|----------------|
| 29 | Compare Virat Kohli and Babar Azam's ODI averages. | Both players’ ODI batting_avg (agent may call tool twice). |
| 30 | Who has more Test wickets, Pat Cummins or Mitchell Starc? | Uses stats for both; compares Test wickets. |

---

## Quick checklist

- [ ] Stats tool returns Test, ODI, T20 (matches, runs, avg, wickets) when relevant.
- [ ] Bio tool returns nationality and place of birth.
- [ ] List tool returns the full list of available cricketers.
- [ ] Partial names (e.g. "Kohli", "Dhoni") resolve correctly.
- [ ] Unknown players get a clear “not found” and a hint to use the list.
- [ ] Combined prompts (stats + bio) use both tools and give a complete answer.

---

*Agent: `cricket_stats_agent` · Model: gemini-2.5-flash*
