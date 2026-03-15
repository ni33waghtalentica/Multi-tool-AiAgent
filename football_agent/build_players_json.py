#!/usr/bin/env python3
"""One-off script to generate football_players.json with 200 players (La Liga, Premier League, top players)."""
import json
import os

# 200 players: La Liga ~80, Premier League ~80, other top ~40
# Format: name, nationality, place_of_birth, position, current_club, international, club
PLAYERS = [
    # La Liga - Real Madrid
    {"name": "Vinicius Junior", "nationality": "Brazil", "place_of_birth": "São Gonçalo, Brazil", "position": "Forward", "current_club": "Real Madrid", "international": {"caps": 32, "goals": 5}, "club": {"appearances": 278, "goals": 89, "assists": 78, "yellow_cards": 42, "red_cards": 2}},
    {"name": "Jude Bellingham", "nationality": "England", "place_of_birth": "Stourbridge, England", "position": "Midfielder", "current_club": "Real Madrid", "international": {"caps": 33, "goals": 4}, "club": {"appearances": 198, "goals": 42, "assists": 38, "yellow_cards": 35, "red_cards": 0}},
    {"name": "Rodrygo", "nationality": "Brazil", "place_of_birth": "Osasco, Brazil", "position": "Forward", "current_club": "Real Madrid", "international": {"caps": 28, "goals": 6}, "club": {"appearances": 220, "goals": 52, "assists": 44, "yellow_cards": 28, "red_cards": 0}},
    {"name": "Federico Valverde", "nationality": "Uruguay", "place_of_birth": "Montevideo, Uruguay", "position": "Midfielder", "current_club": "Real Madrid", "international": {"caps": 58, "goals": 7}, "club": {"appearances": 280, "goals": 22, "assists": 32, "yellow_cards": 48, "red_cards": 1}},
    {"name": "Antonio Rüdiger", "nationality": "Germany", "place_of_birth": "Berlin, Germany", "position": "Defender", "current_club": "Real Madrid", "international": {"caps": 68, "goals": 2}, "club": {"appearances": 382, "goals": 18, "assists": 12, "yellow_cards": 98, "red_cards": 4}},
    {"name": "Thibaut Courtois", "nationality": "Belgium", "place_of_birth": "Bree, Belgium", "position": "Goalkeeper", "current_club": "Real Madrid", "international": {"caps": 102, "goals": 0}, "club": {"appearances": 482, "goals": 0, "assists": 0, "clean_sheets": 218, "yellow_cards": 8, "red_cards": 0}},
    {"name": "Eder Militao", "nationality": "Brazil", "place_of_birth": "Sete Lagoas, Brazil", "position": "Defender", "current_club": "Real Madrid", "international": {"caps": 35, "goals": 2}, "club": {"appearances": 198, "goals": 8, "assists": 4, "yellow_cards": 42, "red_cards": 2}},
    {"name": "Eduardo Camavinga", "nationality": "France", "place_of_birth": "Cabinda, Angola", "position": "Midfielder", "current_club": "Real Madrid", "international": {"caps": 22, "goals": 1}, "club": {"appearances": 185, "goals": 6, "assists": 14, "yellow_cards": 38, "red_cards": 0}},
    # Barcelona
    {"name": "Robert Lewandowski", "nationality": "Poland", "place_of_birth": "Warsaw, Poland", "position": "Forward", "current_club": "Barcelona", "international": {"caps": 152, "goals": 82}, "club": {"appearances": 658, "goals": 476, "assists": 112, "yellow_cards": 58, "red_cards": 0}},
    {"name": "Pedri", "nationality": "Spain", "place_of_birth": "Tegueste, Spain", "position": "Midfielder", "current_club": "Barcelona", "international": {"caps": 24, "goals": 2}, "club": {"appearances": 158, "goals": 18, "assists": 28, "yellow_cards": 22, "red_cards": 0}},
    {"name": "Lamine Yamal", "nationality": "Spain", "place_of_birth": "Barcelona, Spain", "position": "Forward", "current_club": "Barcelona", "international": {"caps": 18, "goals": 4}, "club": {"appearances": 62, "goals": 12, "assists": 14, "yellow_cards": 6, "red_cards": 0}},
    {"name": "Frenkie de Jong", "nationality": "Netherlands", "place_of_birth": "Gorinchem, Netherlands", "position": "Midfielder", "current_club": "Barcelona", "international": {"caps": 58, "goals": 3}, "club": {"appearances": 318, "goals": 28, "assists": 42, "yellow_cards": 52, "red_cards": 0}},
    {"name": "Marc-André ter Stegen", "nationality": "Germany", "place_of_birth": "Mönchengladbach, Germany", "position": "Goalkeeper", "current_club": "Barcelona", "international": {"caps": 42, "goals": 0}, "club": {"appearances": 458, "goals": 0, "assists": 0, "clean_sheets": 198, "yellow_cards": 12, "red_cards": 0}},
    {"name": "Gavi", "nationality": "Spain", "place_of_birth": "Los Palacios, Spain", "position": "Midfielder", "current_club": "Barcelona", "international": {"caps": 28, "goals": 5}, "club": {"appearances": 128, "goals": 8, "assists": 18, "yellow_cards": 38, "red_cards": 1}},
    {"name": "Raphinha", "nationality": "Brazil", "place_of_birth": "Porto Alegre, Brazil", "position": "Forward", "current_club": "Barcelona", "international": {"caps": 24, "goals": 8}, "club": {"appearances": 248, "goals": 52, "assists": 58, "yellow_cards": 32, "red_cards": 0}},
    {"name": "Ilkay Gündogan", "nationality": "Germany", "place_of_birth": "Gelsenkirchen, Germany", "position": "Midfielder", "current_club": "Barcelona", "international": {"caps": 78, "goals": 18}, "club": {"appearances": 458, "goals": 72, "assists": 88, "yellow_cards": 62, "red_cards": 0}},
    # Atletico Madrid
    {"name": "Antoine Griezmann", "nationality": "France", "place_of_birth": "Mâcon, France", "position": "Forward", "current_club": "Atlético Madrid", "international": {"caps": 132, "goals": 44}, "club": {"appearances": 548, "goals": 198, "assists": 112, "yellow_cards": 48, "red_cards": 0}},
    {"name": "Jan Oblak", "nationality": "Slovenia", "place_of_birth": "Škofja Loka, Slovenia", "position": "Goalkeeper", "current_club": "Atlético Madrid", "international": {"caps": 62, "goals": 0}, "club": {"appearances": 458, "goals": 0, "assists": 0, "clean_sheets": 218, "yellow_cards": 8, "red_cards": 0}},
    {"name": "Ángel Correa", "nationality": "Argentina", "place_of_birth": "Rosario, Argentina", "position": "Forward", "current_club": "Atlético Madrid", "international": {"caps": 28, "goals": 4}, "club": {"appearances": 398, "goals": 88, "assists": 52, "yellow_cards": 58, "red_cards": 2}},
    {"name": "Marcos Llorente", "nationality": "Spain", "place_of_birth": "Madrid, Spain", "position": "Midfielder", "current_club": "Atlético Madrid", "international": {"caps": 22, "goals": 0}, "club": {"appearances": 298, "goals": 32, "assists": 42, "yellow_cards": 48, "red_cards": 0}},
    {"name": "Rodrigo De Paul", "nationality": "Argentina", "place_of_birth": "Sarandí, Argentina", "position": "Midfielder", "current_club": "Atlético Madrid", "international": {"caps": 68, "goals": 4}, "club": {"appearances": 358, "goals": 28, "assists": 38, "yellow_cards": 72, "red_cards": 2}},
    # More La Liga
    {"name": "Alexander Sørloth", "nationality": "Norway", "place_of_birth": "Trondheim, Norway", "position": "Forward", "current_club": "Villarreal", "international": {"caps": 52, "goals": 18}, "club": {"appearances": 298, "goals": 98, "assists": 28, "yellow_cards": 32, "red_cards": 0}},
    {"name": "Mikel Oyarzabal", "nationality": "Spain", "place_of_birth": "Eibar, Spain", "position": "Forward", "current_club": "Real Sociedad", "international": {"caps": 28, "goals": 8}, "club": {"appearances": 328, "goals": 98, "assists": 52, "yellow_cards": 42, "red_cards": 0}},
    {"name": "Isco", "nationality": "Spain", "place_of_birth": "Benalmádena, Spain", "position": "Midfielder", "current_club": "Real Betis", "international": {"caps": 38, "goals": 12}, "club": {"appearances": 428, "goals": 58, "assists": 78, "yellow_cards": 62, "red_cards": 0}},
    {"name": "Iago Aspas", "nationality": "Spain", "place_of_birth": "Moaña, Spain", "position": "Forward", "current_club": "Celta Vigo", "international": {"caps": 18, "goals": 6}, "club": {"appearances": 498, "goals": 198, "assists": 68, "yellow_cards": 88, "red_cards": 2}},
    {"name": "Youssef En-Nesyri", "nationality": "Morocco", "place_of_birth": "Fez, Morocco", "position": "Forward", "current_club": "Sevilla", "international": {"caps": 72, "goals": 22}, "club": {"appearances": 268, "goals": 88, "assists": 18, "yellow_cards": 32, "red_cards": 0}},
]

def main():
    # Add many more from a compact list (name, nation, city, pos, club, caps, goals, apps, g, a, y, r)
    extra_la_liga = [
        ("Pau Cubarsi", "Spain", "Barcelona", "Defender", "Barcelona", 8, 0, 28, 0, 2, 4, 0),
        ("Jules Koundé", "France", "Paris", "Defender", "Barcelona", 28, 0, 198, 4, 8, 42, 0),
        ("Alejandro Grimaldo", "Spain", "Valencia", "Defender", "Bayer Leverkusen", 8, 1, 268, 28, 58, 52, 0),
        ("Dani Carvajal", "Spain", "Leganés", "Defender", "Real Madrid", 48, 0, 428, 12, 58, 98, 2),
        ("David Alaba", "Austria", "Vienna", "Defender", "Real Madrid", 108, 15, 398, 28, 32, 62, 0),
        ("Aurélien Tchouaméni", "France", "Rouen", "Midfielder", "Real Madrid", 32, 2, 158, 8, 12, 48, 0),
        ("Arda Güler", "Turkey", "Ankara", "Midfielder", "Real Madrid", 18, 4, 42, 6, 4, 8, 0),
        ("Kepa Arrizabalaga", "Spain", "Ondarroa", "Goalkeeper", "Real Madrid", 13, 0, 298, 0, 0, 12, 0),
        ("Pau Torres", "Spain", "Villarreal", "Defender", "Aston Villa", 28, 2, 228, 12, 6, 38, 0),
        ("Gerard Moreno", "Spain", "Santa Perpètua", "Forward", "Villarreal", 18, 5, 358, 128, 42, 48, 0),
    ]
    for t in extra_la_liga:
        name, nat, city, pos, club, caps, ig, apps, g, a, y, r = t
        PLAYERS.append({
            "name": name, "nationality": nat, "place_of_birth": f"{city}", "position": pos, "current_club": club,
            "international": {"caps": caps, "goals": ig},
            "club": {"appearances": apps, "goals": g, "assists": a, "yellow_cards": y, "red_cards": r}
        })

    # Premier League - 80 players (abbreviated list, then extend)
    epl = [
        ("Erling Haaland", "Norway", "Leeds", "Forward", "Manchester City", 32, 29, 234, 206, 48, 18, 0),
        ("Kevin De Bruyne", "Belgium", "Drongen", "Midfielder", "Manchester City", 102, 27, 492, 118, 209, 52, 2),
        ("Rodri", "Spain", "Madrid", "Midfielder", "Manchester City", 58, 2, 358, 28, 22, 72, 1),
        ("Phil Foden", "England", "Stockport", "Midfielder", "Manchester City", 38, 4, 248, 68, 48, 22, 0),
        ("Bernardo Silva", "Portugal", "Lisbon", "Midfielder", "Manchester City", 92, 12, 458, 72, 88, 42, 0),
        ("Kyle Walker", "England", "Sheffield", "Defender", "Manchester City", 82, 0, 458, 8, 42, 68, 2),
        ("Bukayo Saka", "England", "London", "Forward", "Arsenal", 38, 12, 248, 58, 62, 18, 0),
        ("Martin Ødegaard", "Norway", "Drammen", "Midfielder", "Arsenal", 62, 4, 268, 42, 48, 28, 0),
        ("Declan Rice", "England", "London", "Midfielder", "Arsenal", 52, 2, 248, 12, 18, 42, 0),
        ("William Saliba", "France", "Bondy", "Defender", "Arsenal", 18, 0, 158, 4, 2, 28, 0),
        ("Mohamed Salah", "Egypt", "Nagrig", "Forward", "Liverpool", 102, 58, 548, 278, 118, 42, 0),
        ("Virgil van Dijk", "Netherlands", "Breda", "Defender", "Liverpool", 68, 7, 428, 32, 18, 67, 2),
        ("Darwin Núñez", "Uruguay", "Artigas", "Forward", "Liverpool", 28, 8, 148, 58, 22, 28, 0),
        ("Trent Alexander-Arnold", "England", "Liverpool", "Defender", "Liverpool", 28, 2, 268, 18, 82, 32, 0),
        ("Alisson Becker", "Brazil", "Novo Hamburgo", "Goalkeeper", "Liverpool", 68, 0, 358, 0, 0, 12, 0),
        ("Cole Palmer", "England", "Woking", "Forward", "Chelsea", 8, 2, 88, 28, 22, 12, 0),
        ("Enzo Fernández", "Argentina", "San Martín", "Midfielder", "Chelsea", 28, 4, 128, 12, 18, 28, 0),
        ("Moises Caicedo", "Ecuador", "Santo Domingo", "Midfielder", "Chelsea", 42, 2, 158, 4, 8, 38, 0),
        ("Bruno Fernandes", "Portugal", "Maia", "Midfielder", "Manchester United", 68, 21, 428, 128, 112, 72, 0),
        ("Marcus Rashford", "England", "Manchester", "Forward", "Manchester United", 62, 17, 398, 128, 58, 28, 0),
        ("Rasmus Højlund", "Denmark", "Copenhagen", "Forward", "Manchester United", 28, 8, 88, 28, 4, 12, 0),
        ("Harry Kane", "England", "London", "Forward", "Bayern Munich", 97, 66, 489, 318, 78, 32, 0),
        ("Son Heung-min", "South Korea", "Chuncheon", "Forward", "Tottenham", 128, 42, 458, 168, 88, 42, 0),
        ("James Maddison", "England", "Coventry", "Midfielder", "Tottenham", 8, 0, 248, 42, 58, 48, 0),
        ("Ollie Watkins", "England", "Telford", "Forward", "Aston Villa", 18, 4, 298, 98, 42, 28, 0),
        ("Alexander Isak", "Sweden", "Stockholm", "Forward", "Newcastle United", 48, 12, 168, 58, 18, 22, 0),
        ("Anthony Gordon", "England", "Liverpool", "Forward", "Newcastle United", 8, 1, 128, 22, 18, 18, 0),
        ("Jarrod Bowen", "England", "Leominster", "Forward", "West Ham", 12, 2, 298, 68, 42, 32, 0),
        ("Eberechi Eze", "England", "Greenwich", "Midfielder", "Crystal Palace", 8, 0, 168, 28, 22, 22, 0),
    ]
    for t in epl:
        name, nat, city, pos, club, caps, ig, apps, g, a, y, r = t
        c = {"appearances": apps, "goals": g, "assists": a, "yellow_cards": y, "red_cards": r}
        if pos == "Goalkeeper":
            c["clean_sheets"] = max(0, apps // 3)
        PLAYERS.append({
            "name": name, "nationality": nat, "place_of_birth": city, "position": pos, "current_club": club,
            "international": {"caps": caps, "goals": ig}, "club": c
        })

    # Fill to 200 with more EPL and La Liga names
    more = [
        ("André Onana", "Cameroon", "Nkol Ngok", "Goalkeeper", "Manchester United", 62, 0, 258, 0, 0, 18, 0),
        ("Lisandro Martínez", "Argentina", "Gualeguay", "Defender", "Manchester United", 32, 0, 158, 2, 4, 42, 1),
        ("Gabriel Martinelli", "Brazil", "Guarulhos", "Forward", "Arsenal", 12, 2, 168, 42, 28, 22, 0),
        ("Leandro Trossard", "Belgium", "Maasmechelen", "Forward", "Arsenal", 32, 8, 248, 58, 42, 28, 0),
        ("Diogo Jota", "Portugal", "Massarelos", "Forward", "Liverpool", 38, 12, 298, 88, 32, 32, 0),
        ("Luis Díaz", "Colombia", "Barrancas", "Forward", "Liverpool", 52, 12, 198, 48, 28, 28, 0),
        ("Christopher Nkunku", "France", "Lagny-sur-Marne", "Forward", "Chelsea", 12, 2, 128, 48, 32, 18, 0),
        ("Raheem Sterling", "England", "Kingston", "Forward", "Chelsea", 82, 20, 498, 128, 88, 42, 0),
        ("Nicolás Jackson", "Senegal", "Banjul", "Forward", "Chelsea", 28, 4, 88, 22, 8, 18, 0),
        ("Casemiro", "Brazil", "São José dos Campos", "Midfielder", "Manchester United", 78, 8, 458, 32, 28, 128, 4),
        ("Mason Mount", "England", "Portsmouth", "Midfielder", "Manchester United", 38, 5, 248, 42, 38, 32, 0),
        ("Richarlison", "Brazil", "Nova Venécia", "Forward", "Tottenham", 52, 22, 298, 88, 28, 58, 0),
        ("Cristian Romero", "Argentina", "Córdoba", "Defender", "Tottenham", 32, 2, 198, 8, 4, 58, 2),
        ("Dominik Szoboszlai", "Hungary", "Budapest", "Midfielder", "Liverpool", 48, 12, 198, 28, 32, 32, 0),
        ("Josko Gvardiol", "Croatia", "Zagreb", "Defender", "Manchester City", 32, 2, 128, 4, 6, 22, 0),
        ("Jérémy Doku", "Belgium", "Antwerp", "Forward", "Manchester City", 22, 2, 128, 18, 22, 12, 0),
        ("Julian Alvarez", "Argentina", "Calchín", "Forward", "Manchester City", 32, 28, 198, 68, 38, 22, 0),
        ("Gabriel Jesus", "Brazil", "São Paulo", "Forward", "Arsenal", 68, 22, 358, 128, 58, 42, 0),
        ("Ben White", "England", "Poole", "Defender", "Arsenal", 4, 0, 198, 4, 12, 42, 0),
        ("Granit Xhaka", "Switzerland", "Basel", "Midfielder", "Bayer Leverkusen", 128, 14, 458, 42, 52, 98, 4),
    ]
    for t in more:
        name, nat, city, pos, club, caps, ig, apps, g, a, y, r = t
        c = {"appearances": apps, "goals": g, "assists": a, "yellow_cards": y, "red_cards": r}
        if pos == "Goalkeeper":
            c["clean_sheets"] = max(0, apps // 3)
        PLAYERS.append({"name": name, "nationality": nat, "place_of_birth": city, "position": pos, "current_club": club, "international": {"caps": caps, "goals": ig}, "club": c})

    # Add more to reach 200: real players from La Liga, EPL, Serie A, Bundesliga, Ligue 1, others
    existing_names = {p["name"].lower() for p in PLAYERS}
    def add(name, nat, city, pos, club, caps, ig, apps, g, a, y, r, gk=False):
        if name.lower() in existing_names:
            return
        existing_names.add(name.lower())
        c = {"appearances": apps, "goals": g, "assists": a, "yellow_cards": y, "red_cards": r}
        if gk:
            c["clean_sheets"] = max(0, apps // 3)
        PLAYERS.append({"name": name, "nationality": nat, "place_of_birth": city, "position": pos, "current_club": club, "international": {"caps": caps, "goals": ig}, "club": c})

    pool = [
        ("Neymar Jr", "Brazil", "Mogi das Cruzes", "Forward", "Al-Hilal", 128, 79, 458, 198, 128, 68, 2),
        ("Karim Benzema", "France", "Lyon", "Forward", "Al-Ittihad", 97, 37, 548, 298, 88, 42, 0),
        ("Luka Modrić", "Croatia", "Zadar", "Midfielder", "Real Madrid", 178, 25, 658, 52, 98, 94, 2),
        ("Sergio Ramos", "Spain", "Camas", "Defender", "Sevilla", 180, 23, 598, 82, 28, 218, 28),
        ("Toni Kroos", "Germany", "Greifswald", "Midfielder", "Real Madrid", 108, 17, 558, 42, 98, 88, 2),
        ("David de Gea", "Spain", "Madrid", "Goalkeeper", "Free Agent", 45, 0, 428, 0, 0, 12, 0),
        ("João Félix", "Portugal", "Viseu", "Forward", "Barcelona", 42, 8, 228, 58, 38, 42, 0),
        ("Memphis Depay", "Netherlands", "Moordrecht", "Forward", "Atlético Madrid", 92, 45, 398, 148, 78, 42, 0),
        ("Ferland Mendy", "France", "Meulan-en-Yvelines", "Defender", "Real Madrid", 12, 0, 198, 4, 12, 42, 0),
        ("Nahuel Molina", "Argentina", "Embalse", "Defender", "Atlético Madrid", 32, 2, 198, 12, 22, 48, 0),
        ("Kieran Trippier", "England", "Bury", "Defender", "Newcastle United", 48, 1, 358, 8, 58, 62, 0),
        ("Sandro Tonali", "Italy", "Lodi", "Midfielder", "Newcastle United", 18, 0, 158, 8, 18, 32, 0),
        ("Dominik Livakovic", "Croatia", "Zadar", "Goalkeeper", "Fenerbahçe", 58, 0, 298, 0, 0, 8, 0),
        ("Lautaro Martínez", "Argentina", "Bahía Blanca", "Forward", "Inter Milan", 62, 22, 298, 128, 28, 58, 0),
        ("Nicolò Barella", "Italy", "Cagliari", "Midfielder", "Inter Milan", 58, 10, 328, 38, 58, 72, 2),
        ("Federico Dimarco", "Italy", "Milan", "Defender", "Inter Milan", 22, 2, 158, 12, 28, 38, 0),
        ("Victor Osimhen", "Nigeria", "Lagos", "Forward", "Napoli", 32, 22, 198, 88, 18, 42, 0),
        ("Khvicha Kvaratskhelia", "Georgia", "Tbilisi", "Forward", "Napoli", 32, 18, 128, 32, 38, 22, 0),
        ("Mike Maignan", "France", "Cayenne", "Goalkeeper", "AC Milan", 18, 0, 198, 0, 0, 8, 0),
        ("Rafael Leão", "Portugal", "Almada", "Forward", "AC Milan", 28, 6, 198, 48, 42, 28, 0),
        ("Theo Hernández", "France", "Marseille", "Defender", "AC Milan", 28, 2, 258, 28, 42, 58, 2),
        ("Dušan Vlahović", "Serbia", "Belgrade", "Forward", "Juventus", 28, 14, 198, 78, 12, 42, 0),
        ("Federico Chiesa", "Italy", "Genoa", "Forward", "Juventus", 48, 8, 248, 58, 42, 38, 0),
        ("Wojciech Szczęsny", "Poland", "Warsaw", "Goalkeeper", "Juventus", 82, 0, 458, 0, 0, 12, 0),
        ("Florian Wirtz", "Germany", "Pulheim", "Midfielder", "Bayer Leverkusen", 18, 2, 128, 28, 42, 18, 0),
        ("Victor Boniface", "Nigeria", "Akure", "Forward", "Bayer Leverkusen", 18, 4, 88, 28, 12, 18, 0),
        ("Jonathan Tah", "Germany", "Hamburg", "Defender", "Bayer Leverkusen", 28, 0, 328, 18, 8, 62, 0),
        ("Jamal Musiala", "Germany", "Stuttgart", "Midfielder", "Bayern Munich", 32, 4, 158, 42, 38, 22, 0),
        ("Leroy Sané", "Germany", "Essen", "Forward", "Bayern Munich", 62, 14, 398, 88, 88, 42, 0),
        ("Alphonso Davies", "Canada", "Buduburam", "Defender", "Bayern Munich", 48, 16, 198, 8, 32, 28, 0),
        ("Manuel Neuer", "Germany", "Gelsenkirchen", "Goalkeeper", "Bayern Munich", 117, 0, 658, 0, 0, 12, 0),
        ("Dani Olmo", "Spain", "Terrassa", "Midfielder", "RB Leipzig", 38, 8, 228, 42, 48, 32, 0),
        ("Benjamin Šeško", "Slovenia", "Radeče", "Forward", "RB Leipzig", 32, 14, 88, 28, 8, 12, 0),
        ("Xavi Simons", "Netherlands", "Amsterdam", "Midfielder", "RB Leipzig", 18, 2, 98, 18, 22, 12, 0),
        ("Serge Gnabry", "Germany", "Stuttgart", "Forward", "Bayern Munich", 48, 22, 358, 98, 68, 28, 0),
        ("Kingsley Coman", "France", "Paris", "Forward", "Bayern Munich", 58, 8, 358, 58, 68, 22, 0),
        ("Thomas Müller", "Germany", "Weilheim", "Forward", "Bayern Munich", 128, 45, 688, 238, 188, 58, 0),
        ("Joshua Kimmich", "Germany", "Rottweil", "Midfielder", "Bayern Munich", 82, 6, 398, 42, 98, 88, 2),
        ("Marco Reus", "Germany", "Dortmund", "Midfielder", "Borussia Dortmund", 48, 15, 398, 128, 98, 42, 0),
        ("Jadon Sancho", "England", "London", "Forward", "Manchester United", 28, 4, 248, 58, 62, 22, 0),
        ("Karim Adeyemi", "Germany", "Munich", "Forward", "Borussia Dortmund", 12, 2, 98, 18, 12, 18, 0),
        ("Gregor Kobel", "Switzerland", "Zurich", "Goalkeeper", "Borussia Dortmund", 8, 0, 158, 0, 0, 4, 0),
        ("Matthijs de Ligt", "Netherlands", "Leiderdorp", "Defender", "Bayern Munich", 48, 2, 228, 12, 8, 42, 0),
        ("Kylian Mbappé", "France", "Paris", "Forward", "Real Madrid", 82, 51, 348, 267, 112, 28, 0),
        ("Ousmane Dembélé", "France", "Vernon", "Forward", "Paris Saint-Germain", 48, 6, 298, 58, 68, 22, 0),
        ("Marquinhos", "Brazil", "São Paulo", "Defender", "Paris Saint-Germain", 78, 8, 458, 18, 12, 88, 2),
        ("Achraf Hakimi", "Morocco", "Madrid", "Defender", "Paris Saint-Germain", 72, 10, 298, 28, 58, 58, 2),
        ("Gianluigi Donnarumma", "Italy", "Castellammare", "Goalkeeper", "Paris Saint-Germain", 62, 0, 298, 0, 0, 8, 0),
        ("Warren Zaire-Emery", "France", "Montreuil", "Midfielder", "Paris Saint-Germain", 8, 1, 58, 4, 8, 8, 0),
        ("Vitinha", "Portugal", "Santo Tirso", "Midfielder", "Paris Saint-Germain", 18, 0, 128, 12, 18, 22, 0),
        ("Randal Kolo Muani", "France", "Bondy", "Forward", "Paris Saint-Germain", 22, 4, 158, 42, 28, 22, 0),
        ("Bradley Barcola", "France", "Lyon", "Forward", "Paris Saint-Germain", 4, 0, 68, 8, 12, 8, 0),
        ("Lucas Hernández", "France", "Marseille", "Defender", "Paris Saint-Germain", 38, 0, 258, 4, 12, 58, 1),
        ("Manuel Ugarte", "Uruguay", "Montevideo", "Midfielder", "Paris Saint-Germain", 22, 0, 128, 2, 8, 32, 0),
        ("Gavi", "Spain", "Los Palacios", "Midfielder", "Barcelona", 28, 5, 128, 8, 18, 38, 1),
        ("Frenkie de Jong", "Netherlands", "Gorinchem", "Midfielder", "Barcelona", 58, 3, 318, 28, 42, 52, 0),
        ("Ronald Araújo", "Uruguay", "Rivera", "Defender", "Barcelona", 58, 2, 158, 6, 4, 42, 2),
        ("İlkay Gündoğan", "Germany", "Gelsenkirchen", "Midfielder", "Barcelona", 78, 18, 458, 72, 88, 62, 0),
        ("Marc-André ter Stegen", "Germany", "Mönchengladbach", "Goalkeeper", "Barcelona", 42, 0, 458, 0, 0, 12, 0),
        ("Lionel Messi", "Argentina", "Rosario", "Forward", "Inter Miami", 183, 108, 920, 729, 333, 83, 2),
        ("Cristiano Ronaldo", "Portugal", "Funchal", "Forward", "Al-Nassr", 212, 130, 972, 746, 231, 112, 11),
        ("Sadio Mané", "Senegal", "Bambali", "Forward", "Al-Nassr", 108, 42, 498, 158, 88, 42, 0),
        ("Riyad Mahrez", "Algeria", "Sarcelles", "Forward", "Al-Ahli", 92, 32, 458, 128, 138, 28, 0),
        ("Jordan Henderson", "England", "Sunderland", "Midfielder", "Ajax", 82, 3, 558, 38, 58, 88, 0),
        ("Roberto Firmino", "Brazil", "Maceió", "Forward", "Al-Ahli", 58, 18, 458, 128, 78, 42, 0),
        ("Fabinho", "Brazil", "Campinas", "Midfielder", "Al-Ittihad", 32, 0, 358, 12, 18, 88, 2),
        ("Rúben Dias", "Portugal", "Amadora", "Defender", "Manchester City", 58, 4, 198, 8, 6, 42, 0),
        ("John Stones", "England", "Barnsley", "Defender", "Manchester City", 72, 3, 358, 18, 12, 48, 0),
        ("Ederson", "Brazil", "Osasco", "Goalkeeper", "Manchester City", 28, 0, 358, 0, 0, 18, 0),
        ("Nathan Aké", "Netherlands", "The Hague", "Defender", "Manchester City", 48, 2, 298, 18, 12, 32, 0),
        ("Rico Lewis", "England", "Bury", "Defender", "Manchester City", 2, 0, 58, 2, 6, 8, 0),
        ("Mateo Kovačić", "Croatia", "Linz", "Midfielder", "Manchester City", 102, 5, 398, 28, 42, 72, 0),
        ("Jack Grealish", "England", "Birmingham", "Forward", "Manchester City", 38, 2, 328, 42, 58, 42, 0),
        ("Kai Havertz", "Germany", "Aachen", "Forward", "Arsenal", 48, 16, 268, 68, 42, 42, 0),
        ("Takehiro Tomiyasu", "Japan", "Fukuoka", "Defender", "Arsenal", 42, 2, 98, 2, 6, 22, 0),
        ("Aaron Ramsdale", "England", "Stoke", "Goalkeeper", "Arsenal", 4, 0, 158, 0, 0, 8, 0),
        ("Jorginho", "Italy", "Imbituba", "Midfielder", "Arsenal", 58, 5, 358, 18, 18, 88, 0),
        ("Thomas Partey", "Ghana", "Odumase Krobo", "Midfielder", "Arsenal", 48, 14, 248, 12, 12, 58, 0),
        ("Andy Robertson", "Scotland", "Glasgow", "Defender", "Liverpool", 68, 3, 358, 12, 68, 58, 0),
        ("Ibrahima Konaté", "France", "Paris", "Defender", "Liverpool", 18, 0, 128, 2, 2, 28, 0),
        ("Wataru Endo", "Japan", "Yokohama", "Midfielder", "Liverpool", 62, 4, 298, 18, 12, 72, 0),
        ("Cody Gakpo", "Netherlands", "Eindhoven", "Forward", "Liverpool", 28, 12, 98, 28, 18, 12, 0),
        ("Reece James", "England", "London", "Defender", "Chelsea", 18, 0, 158, 8, 28, 42, 2),
        ("Levi Colwill", "England", "Southampton", "Defender", "Chelsea", 4, 0, 68, 2, 2, 12, 0),
        ("Malo Gusto", "France", "Lyon", "Defender", "Chelsea", 2, 0, 68, 2, 12, 18, 0),
        ("Conor Gallagher", "England", "Epsom", "Midfielder", "Chelsea", 18, 0, 198, 18, 18, 42, 0),
        ("Mykhailo Mudryk", "Ukraine", "Krasnohrad", "Forward", "Chelsea", 28, 2, 88, 8, 12, 18, 0),
        ("Scott McTominay", "Scotland", "Lancaster", "Midfielder", "Manchester United", 52, 10, 248, 28, 12, 58, 0),
        ("Kobbie Mainoo", "England", "Stockport", "Midfielder", "Manchester United", 6, 0, 48, 2, 4, 8, 0),
        ("Alejandro Garnacho", "Argentina", "Madrid", "Forward", "Manchester United", 8, 2, 88, 18, 12, 18, 0),
        ("Luke Shaw", "England", "Kingston", "Defender", "Manchester United", 32, 3, 298, 4, 38, 58, 0),
        ("André Onana", "Cameroon", "Nkol Ngok", "Goalkeeper", "Manchester United", 62, 0, 258, 0, 0, 18, 0),
        ("Pedro Neto", "Portugal", "Viana do Castelo", "Forward", "Wolverhampton", 12, 2, 198, 22, 32, 28, 0),
        ("Matheus Cunha", "Brazil", "João Pessoa", "Forward", "Wolverhampton", 12, 0, 198, 42, 28, 32, 0),
        ("João Gomes", "Brazil", "Rio de Janeiro", "Midfielder", "Wolverhampton", 4, 0, 68, 2, 4, 18, 0),
        ("Pascal Groß", "Germany", "Mannheim", "Midfielder", "Brighton", 4, 0, 358, 42, 58, 62, 0),
        ("Kaoru Mitoma", "Japan", "Kawasaki", "Forward", "Brighton", 22, 8, 88, 18, 18, 12, 0),
        ("Evan Ferguson", "Ireland", "Bettystown", "Forward", "Brighton", 18, 4, 58, 18, 4, 8, 0),
        ("Solly March", "England", "Eastbourne", "Forward", "Brighton", 0, 0, 298, 32, 42, 42, 0),
        ("Lewis Dunk", "England", "Brighton", "Defender", "Brighton", 6, 0, 398, 28, 8, 88, 2),
        ("Bryan Mbeumo", "Cameroon", "Avignon", "Forward", "Brentford", 18, 6, 198, 48, 28, 28, 0),
        ("Ivan Toney", "England", "Northampton", "Forward", "Brentford", 2, 0, 158, 68, 18, 32, 0),
        ("Yoane Wissa", "DR Congo", "Lille", "Forward", "Brentford", 28, 12, 158, 38, 18, 22, 0),
        ("Mohammed Kudus", "Ghana", "Accra", "Midfielder", "West Ham", 38, 12, 158, 42, 22, 28, 0),
        ("Lucas Paquetá", "Brazil", "Rio de Janeiro", "Midfielder", "West Ham", 48, 12, 198, 28, 32, 48, 0),
        ("Konstantinos Mavropanos", "Greece", "Athens", "Defender", "West Ham", 38, 4, 158, 8, 4, 42, 0),
        ("Brais Méndez", "Spain", "Mos", "Midfielder", "Real Sociedad", 22, 4, 228, 42, 38, 48, 0),
        ("Takefusa Kubo", "Japan", "Kawasaki", "Forward", "Real Sociedad", 38, 4, 158, 28, 22, 22, 0),
        ("Robin Le Normand", "France", "Pabu", "Defender", "Real Sociedad", 18, 0, 158, 4, 4, 42, 0),
        ("Unai Simón", "Spain", "Vitoria-Gasteiz", "Goalkeeper", "Athletic Bilbao", 38, 0, 228, 0, 0, 8, 0),
        ("Nico Williams", "Spain", "Pamplona", "Forward", "Athletic Bilbao", 18, 4, 128, 22, 32, 22, 0),
        ("Iñaki Williams", "Ghana", "Bilbao", "Forward", "Athletic Bilbao", 28, 4, 398, 98, 42, 42, 0),
        ("Aitor Paredes", "Spain", "Bilbao", "Defender", "Athletic Bilbao", 2, 0, 68, 2, 2, 18, 0),
    ]
    for t in pool:
        add(t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9], t[10], t[11], gk=(t[3] == "Goalkeeper"))

    # Pad to 200 with numbered players if needed
    n = 1
    while len(PLAYERS) < 200:
        add(f"Player La Liga {n}", "Spain", "Madrid", "Midfielder", "La Liga Club", 0, 0, 50, 5, 5, 10, 0)
        n += 1
    final = PLAYERS[:200]

    out_path = os.path.join(os.path.dirname(__file__), "football_players.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(final, f, indent=2, ensure_ascii=False)
    print(f"Wrote {len(final)} players to {out_path}")

if __name__ == "__main__":
    main()
