# Habit Tracker and Success Visualizer

This project is a Habit Tracker and Success Visualizer built in Python. It allows users to define daily habits, log their completion status, and analyze their performance over time using MySQL for storage, Pandas for data analysis, and Matplotlib for visualizations.

## Project Structure

```
habit_tracker&visualiser
├── db.py               # Handles database connection and schema management
├── models.py           # Defines data models for habits and logs
├── analysis.py         # Analyzes habit data using Pandas
├── visualize.py        # Generates visualizations of habit performance
├── main.py             # Command-line interface for user interaction
├── requirements.txt    # Lists project dependencies
└── README.md           # Project documentation
```

## Features

- **Add Habits**: Users can define new habits to track.
- **Log Completion Status**: Users can log whether they completed their habits each day.
- **Analyze Performance**: The application computes metrics such as total logs, current streaks, and average success rates.
- **Visualize Progress**: Users can view their habit performance through bar charts and line graphs.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd habit_tracker&visualiser
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up the MySQL database:
   - Create a database and update the connection details in `db.py`.

4. Run the application:
   ```
   python main.py
   ```

## Usage Guidelines

- Follow the prompts in the command-line interface to add habits, log their completion, and view analyses and visualizations.
- Ensure that the MySQL server is running and accessible.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.