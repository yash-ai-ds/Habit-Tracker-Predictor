# Habit Tracker + Predictor

A CLI-based Habit Tracker written in Python. It uses a built-in statistical predictor estimating your future consistency based on your past completion data.

## Features
- **Add Habits:** Keep track of new habits you want to build.
- **Mark Daily Completion:** Easily record when you have completed your habit for the day.
- **Progress & Prediction:** Tracks your overall completion rate, current streak, recent consistency, and provides an AI/statistical insight to predict your future adherence to the habit.
- **Data Persistence:** Uses a local SQLite database to safely store your habits and completion records.

## Requirements
- Python 3.7+
- Native `sqlite3` (no external dependencies required)

## Database Schema
The SQLite database (`habits.db`) contains two tables:

### 1. `habits`
- `id`: INTEGER PRIMARY KEY AUTOINCREMENT
- `name`: TEXT UNIQUE NOT NULL
- `created_at`: DATE NOT NULL

### 2. `completions`
- `id`: INTEGER PRIMARY KEY AUTOINCREMENT
- `habit_id`: INTEGER NOT NULL (Foreign Key to `habits.id`)
- `completion_date`: DATE NOT NULL
- *Unique Constraint on `(habit_id, completion_date)`*

## How to Run
1. Make sure Python is installed.
2. Navigate to the project directory in your terminal.
3. Run the following command:
   ```bash
   python main.py
   ```

## Prediction Algorithm Context
The AI feature calculates consistency using purely statistical means without relying on heavyweight machine learning libraries, making the app extremely fast:
- **Overall consistency:** Total completions / Total days since habit creation.
- **Recency Bias:** Consistency in the last 7 days.
- **Weighted Moving Average:** Prioritizes recent behavior over aggregate historical data.
