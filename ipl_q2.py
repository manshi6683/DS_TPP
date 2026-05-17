import json
from collections import deque

# ---------------- IPL KNOWLEDGE BASE ---------------- #

teams_data = {
    "Mumbai Indians": {
        "home_ground": "Wankhede Stadium",
        "players": [
            "Rohit Sharma",
            "Suryakumar Yadav",
            "Hardik Pandya",
            "Jasprit Bumrah"
        ]
    },

    "Chennai Super Kings": {
        "home_ground": "M. A. Chidambaram Stadium",
        "players": [
            "MS Dhoni",
            "Ruturaj Gaikwad",
            "Ravindra Jadeja",
            "Deepak Chahar"
        ]
    },

    "Royal Challengers Bangalore": {
        "home_ground": "M. Chinnaswamy Stadium",
        "players": [
            "Virat Kohli",
            "Faf du Plessis",
            "Glenn Maxwell",
            "Mohammed Siraj"
        ]
    },

    "Kolkata Knight Riders": {
        "home_ground": "Eden Gardens",
        "players": [
            "Shreyas Iyer",
            "Andre Russell",
            "Sunil Narine",
            "Rinku Singh"
        ]
    },

    "Rajasthan Royals": {
        "home_ground": "Sawai Mansingh Stadium",
        "players": [
            "Sanju Samson",
            "Jos Buttler",
            "Yuzvendra Chahal",
            "Trent Boult"
        ]
    },

    "Delhi Capitals": {
        "home_ground": "Arun Jaitley Stadium",
        "players": [
            "Rishabh Pant",
            "David Warner",
            "Axar Patel",
            "Kuldeep Yadav"
        ]
    }
}

# ---------------- IPL MATCH SEQUENCE ---------------- #

ipl_sequence = [
    ("Mumbai Indians", "Chennai Super Kings"),
    ("Royal Challengers Bangalore", "Kolkata Knight Riders"),
    ("Rajasthan Royals", "Delhi Capitals"),
    ("Mumbai Indians", "Royal Challengers Bangalore"),
    ("Chennai Super Kings", "Delhi Capitals")
]

# ---------------- RAG SYSTEM ---------------- #

class IPLRAGSystem:

    def __init__(self, knowledge_base, sequence):

        self.knowledge_base = knowledge_base
        self.sequence = deque(sequence)

    # Retrieve next match
    def retrieve_next_match(self):

        if len(self.sequence) > 0:
            return self.sequence[0]

        return None

    # Allocate stadium based on home team
    def allocate_stadium(self, home_team):

        return self.knowledge_base[home_team]["home_ground"]

    # Get player sequence
    def get_players(self, team):

        return self.knowledge_base[team]["players"]

    # Process match
    def process_next_match(self):

        next_match = self.retrieve_next_match()

        if not next_match:
            print("No Matches Remaining")
            return

        home_team = next_match[0]
        away_team = next_match[1]

        stadium = self.allocate_stadium(home_team)

        home_players = self.get_players(home_team)
        away_players = self.get_players(away_team)

        # Sequential Process Output
        print("\n================ NEXT IPL MATCH ==================\n")

        print("STEP 1 -> MATCH RETRIEVAL")
        print("--------------------------------")
        print(f"Upcoming Match : {home_team} VS {away_team}")

        print("\nSTEP 2 -> STADIUM ALLOCATION")
        print("--------------------------------")
        print(f"Allocated Stadium : {stadium}")

        print("\nSTEP 3 -> HOME TEAM PLAYERS")
        print("--------------------------------")

        for index, player in enumerate(home_players, start=1):
            print(f"{index}. {player}")

        print("\nSTEP 4 -> AWAY TEAM PLAYERS")
        print("--------------------------------")

        for index, player in enumerate(away_players, start=1):
            print(f"{index}. {player}")

        print("\nSTEP 5 -> OBJECT FORMAT")
        print("--------------------------------")

        processed_object = {

            "match": {
                "home_team": home_team,
                "away_team": away_team
            },

            "stadium_details": {
                "stadium": stadium,
                "host_team": home_team
            },

            "players": {
                "home_team_players": home_players,
                "away_team_players": away_players
            }
        }

        print(json.dumps(processed_object, indent=4))

        # Save match file locally
        file_name = f"{home_team.replace(' ', '_')}_vs_{away_team.replace(' ', '_')}.json"

        with open(file_name, "w") as file:
            json.dump(processed_object, file, indent=4)

        print("\nLocal Match File Created Successfully")
        print(f"Saved File : {file_name}")

        print("\n==================================================\n")

        # Remove processed match from sequence
        self.sequence.popleft()


# ---------------- EXECUTION ---------------- #

rag_system = IPLRAGSystem(teams_data, ipl_sequence)

# Process all sequential matches

while len(rag_system.sequence) > 0:
    rag_system.process_next_match()