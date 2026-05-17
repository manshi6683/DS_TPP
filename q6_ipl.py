<<<<<<< HEAD
import os
import json

# IPL 2025 Referral Dataset
ipl_matches = [
    {
        "match_id": 1,
        "teams": ["Mumbai Indians", "Chennai Super Kings"],
        "stadium": "Wankhede Stadium",
        "city": "Mumbai",
        "score": {
            "Mumbai Indians": "189/5",
            "Chennai Super Kings": "182/7"
        },
        "winner": "Mumbai Indians"
    },
    {
        "match_id": 2,
        "teams": ["Royal Challengers Bangalore", "Kolkata Knight Riders"],
        "stadium": "M. Chinnaswamy Stadium",
        "city": "Bangalore",
        "score": {
            "Royal Challengers Bangalore": "201/4",
            "Kolkata Knight Riders": "198/8"
        },
        "winner": "Royal Challengers Bangalore"
    },
    {
        "match_id": 3,
        "teams": ["Rajasthan Royals", "Delhi Capitals"],
        "stadium": "Sawai Mansingh Stadium",
        "city": "Jaipur",
        "score": {
            "Rajasthan Royals": "176/6",
            "Delhi Capitals": "170/9"
        },
        "winner": "Rajasthan Royals"
    }
]

# Create Stadium Object Format
stadium_objects = {}

for match in ipl_matches:
    stadium_objects[match["stadium"]] = {
        "city": match["city"],
        "hosted_match": match["teams"]
    }

# Print Sequential Layered Data
print("\n================ IPL 2025 DATA PROCESSING ================\n")

for index, match in enumerate(ipl_matches, start=1):

    print(f"---------------- MATCH LAYER {index} ----------------")

    print(f"Match ID        : {match['match_id']}")
    print(f"Teams           : {match['teams'][0]} VS {match['teams'][1]}")
    print(f"Stadium         : {match['stadium']}")
    print(f"City            : {match['city']}")

    print("\nScore Layer")
    print("--------------------")

    for team, score in match["score"].items():
        print(f"{team} -> {score}")

    print("\nWinner Layer")
    print("--------------------")
    print(f"Winner : {match['winner']}")

    print("\nObject Layer")
    print("--------------------")

    match_object = {
        "match_id": match["match_id"],
        "stadium_object": {
            "stadium_name": match["stadium"],
            "city": match["city"]
        },
        "teams_object": {
            "team_1": match["teams"][0],
            "team_2": match["teams"][1]
        }
    }

    print(json.dumps(match_object, indent=4))

    print("\n====================================================\n")

# Create Local Folder
folder_name = "IPL_2025_Scores"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Create Individual Files for Each Match
for match in ipl_matches:

    file_name = f"{folder_name}/match_{match['match_id']}.txt"

    with open(file_name, "w") as file:

        file.write("IPL 2025 MATCH REPORT\n")
        file.write("========================\n\n")

        file.write(f"Match ID : {match['match_id']}\n")
        file.write(f"Teams    : {match['teams'][0]} VS {match['teams'][1]}\n")
        file.write(f"Stadium  : {match['stadium']}\n")
        file.write(f"City     : {match['city']}\n\n")

        file.write("Scores\n")
        file.write("------------\n")

        for team, score in match["score"].items():
            file.write(f"{team} : {score}\n")

        file.write(f"\nWinner : {match['winner']}\n")

print("All individual score files created successfully inside 'IPL_2025_Scores' folder.")
=======
import os
import json

# IPL 2025 Referral Dataset
ipl_matches = [
    {
        "match_id": 1,
        "teams": ["Mumbai Indians", "Chennai Super Kings"],
        "stadium": "Wankhede Stadium",
        "city": "Mumbai",
        "score": {
            "Mumbai Indians": "189/5",
            "Chennai Super Kings": "182/7"
        },
        "winner": "Mumbai Indians"
    },
    {
        "match_id": 2,
        "teams": ["Royal Challengers Bangalore", "Kolkata Knight Riders"],
        "stadium": "M. Chinnaswamy Stadium",
        "city": "Bangalore",
        "score": {
            "Royal Challengers Bangalore": "201/4",
            "Kolkata Knight Riders": "198/8"
        },
        "winner": "Royal Challengers Bangalore"
    },
    {
        "match_id": 3,
        "teams": ["Rajasthan Royals", "Delhi Capitals"],
        "stadium": "Sawai Mansingh Stadium",
        "city": "Jaipur",
        "score": {
            "Rajasthan Royals": "176/6",
            "Delhi Capitals": "170/9"
        },
        "winner": "Rajasthan Royals"
    }
]

# Create Stadium Object Format
stadium_objects = {}

for match in ipl_matches:
    stadium_objects[match["stadium"]] = {
        "city": match["city"],
        "hosted_match": match["teams"]
    }

# Print Sequential Layered Data
print("\n================ IPL 2025 DATA PROCESSING ================\n")

for index, match in enumerate(ipl_matches, start=1):

    print(f"---------------- MATCH LAYER {index} ----------------")

    print(f"Match ID        : {match['match_id']}")
    print(f"Teams           : {match['teams'][0]} VS {match['teams'][1]}")
    print(f"Stadium         : {match['stadium']}")
    print(f"City            : {match['city']}")

    print("\nScore Layer")
    print("--------------------")

    for team, score in match["score"].items():
        print(f"{team} -> {score}")

    print("\nWinner Layer")
    print("--------------------")
    print(f"Winner : {match['winner']}")

    print("\nObject Layer")
    print("--------------------")

    match_object = {
        "match_id": match["match_id"],
        "stadium_object": {
            "stadium_name": match["stadium"],
            "city": match["city"]
        },
        "teams_object": {
            "team_1": match["teams"][0],
            "team_2": match["teams"][1]
        }
    }

    print(json.dumps(match_object, indent=4))

    print("\n====================================================\n")

# Create Local Folder
folder_name = "IPL_2025_Scores"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Create Individual Files for Each Match
for match in ipl_matches:

    file_name = f"{folder_name}/match_{match['match_id']}.txt"

    with open(file_name, "w") as file:

        file.write("IPL 2025 MATCH REPORT\n")
        file.write("========================\n\n")

        file.write(f"Match ID : {match['match_id']}\n")
        file.write(f"Teams    : {match['teams'][0]} VS {match['teams'][1]}\n")
        file.write(f"Stadium  : {match['stadium']}\n")
        file.write(f"City     : {match['city']}\n\n")

        file.write("Scores\n")
        file.write("------------\n")

        for team, score in match["score"].items():
            file.write(f"{team} : {score}\n")

        file.write(f"\nWinner : {match['winner']}\n")

print("All individual score files created successfully inside 'IPL_2025_Scores' folder.")
>>>>>>> 0a37d2ea2e0c746b420f97eccb9689fdeea510b4
