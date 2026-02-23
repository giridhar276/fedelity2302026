

teams = {
    "TeamA": [
        {"name": "Alice", "role": "Batsman"},
        {"name": "Bob", "role": "Bowler"}
    ],
    "TeamB": [
        {"name": "Charlie", "role": "Allrounder"},
        {"name": "Dave", "role": "Wicketkeeper"}
    ]
}

for team,info in teams.items():   # key: TeamA    # value : [{"name": "Alice", "role": "Batsman"},{"name": "Bob", "role": "Bowler"}]  
    print(team)
    print("-------------")
    for playerinfo in info:
        print(playerinfo['name'])
