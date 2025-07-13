class Habit:
    def __init__(self, habit_id, name):
        self.habit_id = habit_id
        self.name = name

class HabitLog:
    def __init__(self, habit_id, log_date, status):
        self.habit_id = habit_id
        self.log_date = log_date
        self.status = status

def add_habit(db_connection, name):
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO habits (name) VALUES (%s)", (name,))
    db_connection.commit()
    cursor.close()

def log_habit(db_connection, habit_id, log_date, status):
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO habit_logs (habit_id, log_date, status) VALUES (%s, %s, %s)", 
                   (habit_id, log_date, status))
    db_connection.commit()
    cursor.close()

def get_habits(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM habits")
    habits = cursor.fetchall()
    cursor.close()
    return [Habit(habit_id, name) for habit_id, name in habits]

def get_habit_logs(db_connection, habit_id):
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM habit_logs WHERE habit_id = %s", (habit_id,))
    logs = cursor.fetchall()
    cursor.close()
    return [HabitLog(habit_id, log_date, status) for habit_id, log_date, status in logs]