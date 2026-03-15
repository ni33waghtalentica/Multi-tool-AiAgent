"""
Multi-tool Football Stats Agent using Google ADK and Gemini.
Describes international footballers' stats (club & international) and bio.
"""

from google.adk.agents import Agent
from .football_data import find_footballer, list_footballer_names


def get_football_player_stats(player_name: str) -> dict:
    """Retrieves football statistics for a player: international (caps, goals) and club (appearances, goals, assists, cards).

    Args:
        player_name (str): Full or partial name of the footballer (e.g. 'Messi', 'Cristiano Ronaldo').

    Returns:
        dict: status; on success: international (caps, goals), club stats; on failure: error_message.
    """
    player = find_footballer(player_name)
    if not player:
        return {
            "status": "error",
            "error_message": f"No footballer found for '{player_name}'. Try: {', '.join(list_footballer_names()[:10])}...",
        }
    return {
        "status": "success",
        "player_name": player["name"],
        "international": player["international"],
        "club": player["club"],
    }


def get_football_player_bio(player_name: str) -> dict:
    """Retrieves nationality, place of birth, position, and current club for a footballer.

    Args:
        player_name (str): Full or partial name of the footballer.

    Returns:
        dict: status; on success: nationality, place_of_birth, position, current_club; on failure: error_message.
    """
    player = find_footballer(player_name)
    if not player:
        return {
            "status": "error",
            "error_message": f"No footballer found for '{player_name}'. Try: {', '.join(list_footballer_names()[:10])}...",
        }
    return {
        "status": "success",
        "player_name": player["name"],
        "nationality": player["nationality"],
        "place_of_birth": player["place_of_birth"],
        "position": player["position"],
        "current_club": player["current_club"],
    }


def list_available_footballers() -> dict:
    """Returns the list of footballers available for stats and bio queries.

    Returns:
        dict: status and list of player names.
    """
    names = list_footballer_names()
    return {"status": "success", "footballers": names}


root_agent = Agent(
    name="football_stats_agent",
    model="gemini-2.5-flash",
    description=(
        "Agent that describes international footballers' stats (club and international) "
        "and their bio: nationality, place of birth, position, current club. Use the tools to look up players."
    ),
    instruction=(
        "You are a helpful football expert. When the user asks about a footballer, "
        "use get_football_player_stats to get international (caps, goals) and club statistics "
        "(appearances, goals, assists, yellow/red cards, clean sheets for goalkeepers) "
        "and get_football_player_bio to get nationality, place of birth, position, and current club. "
        "Summarize the information clearly. "
        "For comparisons between two or more players (e.g. 'compare X and Y', 'Neymar vs Ronaldo'), "
        "always format the comparison as markdown tables so it displays clearly in the app. "
        "Use tables like: | Statistic | Player A | Player B | followed by a separator line |---|---| and then data rows. "
        "If the user asks who you can look up, use list_available_footballers. "
        "If a player is not found, suggest they try a name from the available list."
    ),
    tools=[
        get_football_player_stats,
        get_football_player_bio,
        list_available_footballers,
    ],
)
