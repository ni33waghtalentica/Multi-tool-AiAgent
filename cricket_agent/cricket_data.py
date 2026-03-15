"""
Sample international cricketer data: stats (ODI, Test, T20) and bio (nationality, place of birth).
Used by cricket_agent tools. Data is representative for demo; extend or connect to an API for production.
"""

from typing import Optional

# Format: "normalized_name": { "name", "nationality", "place_of_birth", "test", "odi", "t20" }
CRICKETERS = {
    "virat kohli": {
        "name": "Virat Kohli",
        "nationality": "India",
        "place_of_birth": "Delhi, India",
        "test": {"matches": 113, "runs": 8848, "batting_avg": 49.15, "wickets": 0},
        "odi": {"matches": 292, "runs": 13848, "batting_avg": 58.67, "wickets": 0},
        "t20": {"matches": 117, "runs": 4188, "batting_avg": 52.35, "wickets": 0},
    },
    "sachin tendulkar": {
        "name": "Sachin Tendulkar",
        "nationality": "India",
        "place_of_birth": "Mumbai, Maharashtra, India",
        "test": {"matches": 200, "runs": 15921, "batting_avg": 53.78, "wickets": 46},
        "odi": {"matches": 463, "runs": 18426, "batting_avg": 44.83, "wickets": 154},
        "t20": {"matches": 1, "runs": 10, "batting_avg": 10.00, "wickets": 0},
    },
    "rohit sharma": {
        "name": "Rohit Sharma",
        "nationality": "India",
        "place_of_birth": "Nagpur, Maharashtra, India",
        "test": {"matches": 59, "runs": 4137, "batting_avg": 43.54, "wickets": 2},
        "odi": {"matches": 262, "runs": 10709, "batting_avg": 49.12, "wickets": 8},
        "t20": {"matches": 151, "runs": 3974, "batting_avg": 31.79, "wickets": 1},
    },
    "ms dhoni": {
        "name": "MS Dhoni",
        "nationality": "India",
        "place_of_birth": "Ranchi, Jharkhand, India",
        "test": {"matches": 90, "runs": 4876, "batting_avg": 38.09, "wickets": 0},
        "odi": {"matches": 350, "runs": 10773, "batting_avg": 50.57, "wickets": 0},
        "t20": {"matches": 98, "runs": 1617, "batting_avg": 37.60, "wickets": 0},
    },
    "jasprit bumrah": {
        "name": "Jasprit Bumrah",
        "nationality": "India",
        "place_of_birth": "Ahmedabad, Gujarat, India",
        "test": {"matches": 36, "runs": 212, "batting_avg": 6.62, "wickets": 159},
        "odi": {"matches": 89, "runs": 52, "batting_avg": 5.78, "wickets": 149},
        "t20": {"matches": 62, "runs": 28, "batting_avg": 4.67, "wickets": 74},
    },
    "steve smith": {
        "name": "Steve Smith",
        "nationality": "Australia",
        "place_of_birth": "Sydney, New South Wales, Australia",
        "test": {"matches": 109, "runs": 9514, "batting_avg": 57.33, "wickets": 19},
        "odi": {"matches": 155, "runs": 5418, "batting_avg": 44.04, "wickets": 28},
        "t20": {"matches": 65, "runs": 1108, "batting_avg": 26.38, "wickets": 18},
    },
    "david warner": {
        "name": "David Warner",
        "nationality": "Australia",
        "place_of_birth": "Paddington, Sydney, Australia",
        "test": {"matches": 112, "runs": 8786, "batting_avg": 44.59, "wickets": 0},
        "odi": {"matches": 161, "runs": 6932, "batting_avg": 45.30, "wickets": 0},
        "t20": {"matches": 99, "runs": 2894, "batting_avg": 32.88, "wickets": 0},
    },
    "pat cummins": {
        "name": "Pat Cummins",
        "nationality": "Australia",
        "place_of_birth": "Westmead, Sydney, Australia",
        "test": {"matches": 64, "runs": 1283, "batting_avg": 17.57, "wickets": 269},
        "odi": {"matches": 88, "runs": 378, "batting_avg": 12.19, "wickets": 141},
        "t20": {"matches": 52, "runs": 93, "batting_avg": 7.15, "wickets": 55},
    },
    "mitchell starc": {
        "name": "Mitchell Starc",
        "nationality": "Australia",
        "place_of_birth": "Baulkham Hills, Sydney, Australia",
        "test": {"matches": 89, "runs": 1845, "batting_avg": 22.20, "wickets": 346},
        "odi": {"matches": 121, "runs": 529, "batting_avg": 12.62, "wickets": 236},
        "t20": {"matches": 58, "runs": 79, "batting_avg": 7.18, "wickets": 73},
    },
    "joe root": {
        "name": "Joe Root",
        "nationality": "England",
        "place_of_birth": "Sheffield, South Yorkshire, England",
        "test": {"matches": 140, "runs": 11420, "batting_avg": 50.31, "wickets": 22},
        "odi": {"matches": 171, "runs": 6522, "batting_avg": 47.94, "wickets": 28},
        "t20": {"matches": 32, "runs": 893, "batting_avg": 35.72, "wickets": 6},
    },
    "ben stokes": {
        "name": "Ben Stokes",
        "nationality": "England",
        "place_of_birth": "Christchurch, New Zealand",
        "test": {"matches": 103, "runs": 6312, "batting_avg": 36.34, "wickets": 197},
        "odi": {"matches": 114, "runs": 3464, "batting_avg": 40.75, "wickets": 74},
        "t20": {"matches": 43, "runs": 585, "batting_avg": 21.67, "wickets": 26},
    },
    "jos buttler": {
        "name": "Jos Buttler",
        "nationality": "England",
        "place_of_birth": "Taunton, Somerset, England",
        "test": {"matches": 57, "runs": 2907, "batting_avg": 31.94, "wickets": 0},
        "odi": {"matches": 181, "runs": 5223, "batting_avg": 39.86, "wickets": 0},
        "t20": {"matches": 114, "runs": 2927, "batting_avg": 34.43, "wickets": 0},
    },
    "kane williamson": {
        "name": "Kane Williamson",
        "nationality": "New Zealand",
        "place_of_birth": "Tauranga, Bay of Plenty, New Zealand",
        "test": {"matches": 96, "runs": 8675, "batting_avg": 54.89, "wickets": 29},
        "odi": {"matches": 165, "runs": 6854, "batting_avg": 47.92, "wickets": 42},
        "t20": {"matches": 87, "runs": 2465, "batting_avg": 33.29, "wickets": 28},
    },
    "trent boult": {
        "name": "Trent Boult",
        "nationality": "New Zealand",
        "place_of_birth": "Rotorua, New Zealand",
        "test": {"matches": 78, "runs": 763, "batting_avg": 12.92, "wickets": 317},
        "odi": {"matches": 114, "runs": 268, "batting_avg": 8.38, "wickets": 211},
        "t20": {"matches": 55, "runs": 32, "batting_avg": 5.33, "wickets": 74},
    },
    "babar azam": {
        "name": "Babar Azam",
        "nationality": "Pakistan",
        "place_of_birth": "Lahore, Punjab, Pakistan",
        "test": {"matches": 52, "runs": 3772, "batting_avg": 47.15, "wickets": 0},
        "odi": {"matches": 117, "runs": 5729, "batting_avg": 56.95, "wickets": 0},
        "t20": {"matches": 109, "runs": 4023, "batting_avg": 41.47, "wickets": 0},
    },
    "shaheen afridi": {
        "name": "Shaheen Afridi",
        "nationality": "Pakistan",
        "place_of_birth": "Landi Kotal, Khyber Pakhtunkhwa, Pakistan",
        "test": {"matches": 27, "runs": 281, "batting_avg": 10.41, "wickets": 105},
        "odi": {"matches": 53, "runs": 180, "batting_avg": 8.57, "wickets": 104},
        "t20": {"matches": 65, "runs": 98, "batting_avg": 8.17, "wickets": 91},
    },
    "kagiso rabada": {
        "name": "Kagiso Rabada",
        "nationality": "South Africa",
        "place_of_birth": "Johannesburg, South Africa",
        "test": {"matches": 62, "runs": 719, "batting_avg": 11.98, "wickets": 291},
        "odi": {"matches": 102, "runs": 273, "batting_avg": 9.39, "wickets": 157},
        "t20": {"matches": 59, "runs": 38, "batting_avg": 5.43, "wickets": 58},
    },
    "quinton de kock": {
        "name": "Quinton de Kock",
        "nationality": "South Africa",
        "place_of_birth": "Johannesburg, South Africa",
        "test": {"matches": 54, "runs": 3300, "batting_avg": 38.82, "wickets": 0},
        "odi": {"matches": 155, "runs": 6770, "batting_avg": 45.74, "wickets": 0},
        "t20": {"matches": 80, "runs": 2277, "batting_avg": 32.53, "wickets": 0},
    },
    "rashid khan": {
        "name": "Rashid Khan",
        "nationality": "Afghanistan",
        "place_of_birth": "Nangarhar, Afghanistan",
        "test": {"matches": 5, "runs": 106, "batting_avg": 13.25, "wickets": 34},
        "odi": {"matches": 103, "runs": 1212, "batting_avg": 20.20, "wickets": 194},
        "t20": {"matches": 99, "runs": 508, "batting_avg": 12.70, "wickets": 140},
    },
    "shakib al hasan": {
        "name": "Shakib Al Hasan",
        "nationality": "Bangladesh",
        "place_of_birth": "Magura, Bangladesh",
        "test": {"matches": 66, "runs": 4456, "batting_avg": 39.43, "wickets": 233},
        "odi": {"matches": 247, "runs": 7570, "batting_avg": 37.61, "wickets": 317},
        "t20": {"matches": 117, "runs": 2382, "batting_avg": 23.82, "wickets": 140},
    },
    "kusal mendis": {
        "name": "Kusal Mendis",
        "nationality": "Sri Lanka",
        "place_of_birth": "Moratuwa, Sri Lanka",
        "test": {"matches": 61, "runs": 3528, "batting_avg": 36.75, "wickets": 0},
        "odi": {"matches": 121, "runs": 3637, "batting_avg": 32.47, "wickets": 0},
        "t20": {"matches": 62, "runs": 1277, "batting_avg": 22.80, "wickets": 0},
    },
}


def _normalize_name(name: str) -> str:
    return (name or "").strip().lower()


def find_cricketer(player_name: str) -> Optional[dict]:
    """Return cricketer record by name (fuzzy match on normalized name)."""
    key = _normalize_name(player_name)
    if key in CRICKETERS:
        return CRICKETERS[key].copy()
    for ckey, data in CRICKETERS.items():
        if key in ckey or ckey in key:
            return data.copy()
    return None


def list_cricketer_names() -> list[str]:
    """Return list of known cricketer names for hints."""
    seen = set()
    out = []
    for v in CRICKETERS.values():
        n = v["name"]
        if n not in seen:
            seen.add(n)
            out.append(n)
    return sorted(out)
