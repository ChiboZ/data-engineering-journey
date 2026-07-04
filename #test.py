football_icons = {
    "real madrid": "ronaldo",
    "AC milan": "pirlo",
    "barca": "messi",
    "inter milan": "lukaku",
    "ATM": "grizou",
    "liverpool": "salah",
    "bayern": "kimmich",
    "hilal": "neymar",
    "france": "zidane",
    "germany": "kroos",
}

football_icons["man united"] = "paul pogba"
del football_icons["barca"]

for team, player in football_icons.items():
    print(f"Team: {team} -> Icon: {player}")

print(football_icons.get("real madrid"))
