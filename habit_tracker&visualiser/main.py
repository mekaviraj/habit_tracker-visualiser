import sys
from models import HabitModel
from analysis import analyze_habits
from visualize import visualize_habits

def main_menu():
    print("Welcome to the Habit Tracker and Success Visualizer!")
    print("1. Add a new habit")
    print("2. Log habit completion")
    print("3. Analyze habits")
    print("4. Visualize habits")
    print("5. Exit")

def main():
    while True:
        main_menu()
        choice = input("Select an option (1-5): ")

        if choice == '1':
            habit_name = input("Enter the name of the habit: ")
            HabitModel.add_habit(habit_name)
            print(f"Habit '{habit_name}' added successfully.")
        
        elif choice == '2':
            habit_id = int(input("Enter the habit ID: "))
            log_date = input("Enter the log date (YYYY-MM-DD): ")
            status = input("Enter the completion status (completed/not completed): ")
            HabitModel.log_habit(habit_id, log_date, status)
            print("Habit completion logged successfully.")
        
        elif choice == '3':
            analyze_habits()
        
        elif choice == '4':
            visualize_habits()
        
        elif choice == '5':
            print("Exiting the Habit Tracker. Goodbye!")
            sys.exit()
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()