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
