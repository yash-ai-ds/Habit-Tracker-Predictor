import sys
from database import initialize_database, add_habit, get_habits, mark_completion, get_completions, get_habit_by_id
from predictor import predict_consistency

def print_menu():
    print("\n" + "="*40)
    print("  Habit Tracker + Consistency Predictor")
    print("="*40)
    print("1. Add a new habit")
    print("2. Mark habit as completed today")
    print("3. View progress and prediction")
    print("4. List all habits")
    print("5. Exit")
    print("="*40)

def main():
    initialize_database()
    print("Database initialized successfully.")
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            name = input("Enter habit name: ")
            if name.strip():
                if add_habit(name.strip()):
                    print(f"Habit '{name.strip()}' added successfully!")
                else:
                    print("Habit already exists!")
            else:
                print("Habit name cannot be empty.")
                
        elif choice == '2':
            habits = get_habits()
            if not habits:
                print("No habits found. Please add a habit first.")
                continue
            
            print("\nYour Habits:")
            for h in habits:
                print(f"[{h[0]}] {h[1]}")
                
            try:
                habit_id = int(input("Enter habit ID to mark completed for today: "))
                if mark_completion(habit_id):
                    print("Completion recorded successfully!")
                else:
                    print("Already marked as completed for today, or invalid ID.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                
        elif choice == '3':
            habits = get_habits()
            if not habits:
                print("No habits found.")
                continue
                
            try:
                habit_id = int(input("Enter habit ID to view progress: "))
                habit = get_habit_by_id(habit_id)
                
                if not habit:
                    print("Habit not found!")
                    continue
                    
                completions = get_completions(habit_id)
                prediction = predict_consistency(habit[2], completions)
                
                print("\n" + "-"*40)
                print(f"Progress for: {habit[1]} (Started: {habit[2]})")
                print(f"Total Completions: {len(completions)}")
                
                if isinstance(prediction, str):
                    print(f"\nMessage: {prediction}")
                else:
                    print(f"Current Streak: {prediction['current_streak']} days")
                    print(f"Overall Completion Rate: {prediction['overall_rate']}%")
                    print(f"Recent Consistency (last 7 days): {prediction['recent_rate']}%")
                    print(f"Predicted Future Consistency Index: {prediction['predicted_rate']}")
                    print(f"\nAI Insight: {prediction['prediction_text']}")
                print("-"*40)
                
            except ValueError:
                print("Invalid input.")
                
        elif choice == '4':
            habits = get_habits()
            if not habits:
                print("No habits found.")
            else:
                print("\nAll Habits:")
                for h in habits:
                    print(f"- [{h[0]}] {h[1]} (Started: {h[2]})")
                    
        elif choice == '5':
            print("Exiting... Have a productive day!")
            sys.exit(0)
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
