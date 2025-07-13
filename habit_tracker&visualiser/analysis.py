import pandas as pd
import mysql.connector
from mysql.connector import Error
from datetime import datetime, timedelta

def get_habit_logs(habit_id):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='habit_tracker',
            user='your_username',
            password='your_password'
        )
        query = "SELECT log_date, status FROM habit_logs WHERE habit_id = %s"
        df = pd.read_sql(query, connection, params=(habit_id,))
        return df
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            connection.close()

def compute_success_rate(habit_id):
    df = get_habit_logs(habit_id)
    if df.empty:
        return 0
    success_count = df['status'].sum()
    total_count = len(df)
    return success_count / total_count

def compute_current_streak(habit_id):
    df = get_habit_logs(habit_id)
    if df.empty:
        return 0
    
    df['log_date'] = pd.to_datetime(df['log_date'])
    df = df.sort_values(by='log_date', ascending=False)
    
    streak = 0
    for index, row in df.iterrows():
        if row['status'] == 1:  # Assuming 1 means completed
            streak += 1
        else:
            break
    return streak

def total_logs(habit_id):
    df = get_habit_logs(habit_id)
    return len(df)