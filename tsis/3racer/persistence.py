import json, os

# File paths for saving data
LEADERBOARD_FILE = "leaderboard.json"
SETTINGS_FILE = "settings.json"

DEFAULT_SETTINGS = {"sound": True, "car_color": "default", "difficulty": "normal"}

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE) as f:
            return json.load(f)
        # Return default settings if file not found
    return DEFAULT_SETTINGS.copy()

def save_settings(s):
    # Save settings to JSON file
    with open(SETTINGS_FILE, "w") as f:
        json.dump(s, f, indent=2)

def load_leaderboard():
    # Load leaderboard data if file exists
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE) as f:
            return json.load(f)
    return []

def save_score(name, score, distance):
    # Load existing leaderboard
    lb = load_leaderboard()
    
    # Add new score entry
    lb.append({"name": name, "score": score, "distance": int(distance)})
    lb.sort(key=lambda x: x["score"], reverse=True) # Sort by highest score first
    lb = lb[:10] # Keep only top 10 scores
    with open(LEADERBOARD_FILE, "w") as f: # Save updated leaderboard back to file
        json.dump(lb, f, indent=2)