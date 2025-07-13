import matplotlib.pyplot as plt
import pandas as pd
from db import get_habit_logs

def plot_habit_progress(habit_id):
    logs = get_habit_logs(habit_id)
    if logs.empty:
        print("No logs found for this habit.")
        return

    logs['log_date'] = pd.to_datetime(logs['log_date'])
    logs.set_index('log_date', inplace=True)

    success_rate = logs['status'].value_counts(normalize=True).get('completed', 0) * 100
    print(f"Success rate for habit ID {habit_id}: {success_rate:.2f}%")

    plt.figure(figsize=(10, 5))
    plt.plot(logs.index, logs['status'].replace({'completed': 1, 'not completed': 0}), marker='o')
    plt.title('Habit Progress Over Time')
    plt.xlabel('Date')
    plt.ylabel('Completion Status (1 = Completed, 0 = Not Completed)')
    plt.xticks(rotation=45)
    plt.grid()
    plt.tight_layout()
    plt.show()

def plot_habit_comparison(habit_ids):
    all_logs = pd.concat([get_habit_logs(habit_id) for habit_id in habit_ids], ignore_index=True)
    all_logs['log_date'] = pd.to_datetime(all_logs['log_date'])
    all_logs.set_index('log_date', inplace=True)

    success_rates = all_logs.groupby('habit_id')['status'].value_counts(normalize=True).unstack().fillna(0)
    success_rates = success_rates['completed'] * 100

    success_rates.plot(kind='bar', figsize=(10, 5))
    plt.title('Habit Success Rates Comparison')
    plt.xlabel('Habit ID')
    plt.ylabel('Success Rate (%)')
    plt.xticks(rotation=0)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()