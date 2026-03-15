"""
Multi-tool Cricket Stats Agent using Google ADK and Gemini.
Describes international cricketers' stats (ODI, Test, T20) and bio (nationality, place of birth).
"""

from google.adk.agents import Agent
from .cricket_data import find_cricketer, list_cricketer_names


def get_cricketer_international_stats(player_name: str) -> dict:
    """Retrieves international cricket statistics for a player across Test, ODI, and T20 formats.

    Args:
        player_name (str): Full or partial name of the cricketer (e.g. 'Virat Kohli', 'Kohli').

    Returns:
        dict: status; on success: test, odi, t20 stats (matches, runs, batting_avg, wickets); on failure: error_message.
    """
    player = find_cricketer(player_name)
    if not player:
        return {
            "status": "error",
            "error_message": f"No international cricketer found for '{player_name}'. Try: {', '.join(list_cricketer_names()[:10])}...",
        }
    return {
        "status": "success",
        "player_name": player["name"],
        "test": player["test"],
        "odi": player["odi"],
        "t20": player["t20"],
    }


def get_cricketer_bio(player_name: str) -> dict:
    """Retrieves nationality and place of birth for an international cricketer.

    Args:
        player_name (str): Full or partial name of the cricketer.

    Returns:
        dict: status; on success: nationality, place_of_birth; on failure: error_message.
    """
    player = find_cricketer(player_name)
    if not player:
        return {
            "status": "error",
            "error_message": f"No international cricketer found for '{player_name}'. Try: {', '.join(list_cricketer_names()[:10])}...",
        }
    return {
        "status": "success",
        "player_name": player["name"],
        "nationality": player["nationality"],
        "place_of_birth": player["place_of_birth"],
    }


def list_available_cricketers() -> dict:
    """Returns the list of cricketers available for stats and bio queries.

    Returns:
        dict: status and list of player names.
    """
    names = list_cricketer_names()
    return {"status": "success", "cricketers": names}


root_agent = Agent(
    name="cricket_stats_agent",
    model="gemini-2.5-flash",
    description=(
        "Agent that describes international cricketers' stats (ODI, Test, T20) "
        "and their nationality and place of birth. Use the tools to look up players."
    ),
    instruction=(
        "You are a helpful cricket expert. When the user asks about a cricketer, "
        "use get_cricketer_international_stats to get Test, ODI, and T20 statistics "
        "(matches, runs, batting average, wickets) and get_cricketer_bio to get "
        "nationality and place of birth. Summarize the information clearly. "
        "If the user asks who you can look up, use list_available_cricketers. "
        "If a player is not found, suggest they try a name from the available list."
    ),
    tools=[get_cricketer_international_stats, get_cricketer_bio, list_available_cricketers],
)
