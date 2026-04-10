# Habit Tracker + Consistency Predictor

A pure Python, CLI-based Habit Tracker with an integrated statistical predictor. This tool helps you build and manage daily habits while using your past completion metrics to forecast your future consistency.

## 🚀 Features
- **Effortless Habit Tracking:** Add new habits in seconds.
- **Daily Check-ins:** Mark your habits as complete for today.
- **AI Consistency Predictor:** The system calculates your current streak, overall adherence, and uses a weighted moving average to predict your future consistency—without the overhead of heavy Machine Learning libraries!
- **Zero External Dependencies:** Built completely with Python standard libraries (`sqlite3`, `datetime`, `sys`).
- **Data Persistence:** Automatically manages a local SQLite Database to keep all your hard work safe.

## 🛠️ Project Structure
```text
HabitTrackerPredictor/
│
├── database.py   # Handles all SQLite initialization and queries
├── predictor.py  # Calculates streaks, rates, and predictions 
├── main.py       # Main CLI application and event loop
└── README.md     # Project documentation
```

## 🗄️ Database Schema
Data is safely stored in `habits.db` securely matching the following schema:

**`habits` Table**
- `id`: INTEGER (Primary Key)
- `name`: TEXT (Unique)
- `created_at`: DATE

**`completions` Table**
- `id`: INTEGER (Primary Key)
- `habit_id`: INTEGER (Foreign Key)
- `completion_date`: DATE
- *Constraint: Unique mapping for `(habit_id, completion_date)` prevents duplicate check-ins on the same day.*

## 💡 How The Predictor Works
The built-in predictor relies on pure statistical algorithms over bloated libraries:
1. **Overall Completion Rate:** Computes lifetime completions versus total days since you initiated the habit.
2. **Recency Bias:** Calculates your completion rate specifically for the last 7 days.
3. **Future Consistency Index:** Uses a weighted moving average (40% overall history, 60% recent history) to predict whether you are likely to stick to the habit.
4. **Current Streak:** Traverses your recent completions to precisely find how many consecutive days you've marked it done!

## 🏃‍♂️ How to Run

1. Open your terminal.
2. Navigate to the project folder:
   ```bash
   cd path/to/HabitTrackerPredictor
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## 📸 Example Usage

**Main Menu**
```text
========================================
  Habit Tracker + Consistency Predictor
========================================
1. Add a new habit
2. Mark habit as completed today
3. View progress and prediction
4. List all habits
5. Exit
========================================
Enter your choice (1-5):
```

**Insight & Prediction Generation**
```text
----------------------------------------
Progress for: Read 10 Pages (Started: 2026-04-10)
Total Completions: 5
Current Streak: 3 days
Overall Completion Rate: 80.0%
Recent Consistency (last 7 days): 100.0%
Predicted Future Consistency Index: 92.0

AI Insight: Excellent! You have a high probability of maintaining this habit.
----------------------------------------
```
