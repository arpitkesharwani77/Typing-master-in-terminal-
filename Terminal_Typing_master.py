import time
import json

# ANSI escape codes for text color
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
END_COLOR = "\033[0m"

# Load words from JSON file into dict
def load_words_from_json(filename):
    with open(filename) as f:
        return json.load(f)

# Load categories data from an external file
categories_data_filename = 'words.json'
words_dict = load_words_from_json(categories_data_filename)

# Update leaderboard 
def update_leaderboard(username, words_typed, time_taken, wpm):
    leaderboard_file = 'leaderboard.json'
    
    try:
        with open(leaderboard_file, 'r') as f:
            leaderboard = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        leaderboard = {}

    leaderboard[username] = {
        f"Words Typed " : words_typed,
        "Time Taken": f"{time_taken:.2f} seconds",
        "Words Per Minute": f"{wpm} WPM "
    }

    with open(leaderboard_file, 'w') as f:
        json.dump(leaderboard, f, indent=4)  
