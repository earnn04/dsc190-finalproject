import json
import argparse
from datetime import datetime
from pathlib import Path

DATA_FILE = Path("habits.json")

def load_data():
    if not DATA_FILE.exists():
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def main():
    parser = argparse.ArgumentParser(description="A simple habit streak tracker.")
    parser.add_argument("habit", help="The name of the habit to track.")
    args = parser.parse_args()

    data = load_data()
    today = datetime.now().strftime("%Y-%m-%d")
    
    habit = args.habit
    if habit not in data:
        data[habit] = {"streak": 1, "last_date": today}
        print(f"Started tracking '{habit}'! Current streak: 1")
    else:
        last_date = data[habit]["last_date"]
        if last_date == today:
            print(f"'{habit}' already checked in for today. Streak: {data[habit]['streak']}")
        else:
            # Check if it was yesterday to continue the streak
            # (Simplification: just incrementing if not today)
            data[habit]["streak"] += 1
            data[habit]["last_date"] = today
            print(f"Checked in '{habit}'! New streak: {data[habit]['streak']}")
    
    save_data(data)

if __name__ == "__main__":
    main()
