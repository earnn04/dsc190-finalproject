# Habit Streak Tracker

A simple command-line tool for tracking daily habit streaks. Log a habit each day to build and maintain your streak — miss a day and it starts over.

## Usage

Run the script by passing the name of the habit you want to log as an argument:

```bash
python main.py <habit>
```

**Examples:**

Log a habit for the first time:
```bash
python main.py meditation
# Started tracking 'meditation'! Current streak: 1
```

Check in on a habit you've already started tracking (increments your streak):
```bash
python main.py meditation
# Checked in 'meditation'! New streak: 2
```

Check in on a habit you've already logged today (no double-counting):
```bash
python main.py meditation
# 'meditation' already checked in for today. Streak: 2
```

Track multiple habits independently:
```bash
python main.py exercise
python main.py reading
python main.py meditation
```

All habit data is saved automatically to `habits.json` in the same directory.