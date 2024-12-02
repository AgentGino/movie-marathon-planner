# Movie Marathon Planner

A Python script that helps you plan the perfect movie marathon by finding all possible combinations of movies based on their showtimes while minimizing wait times between films.

## Features

- Input multiple movies with multiple showtimes
- Find all possible combinations for a specified number of movies
- Automatically checks for time conflicts between movies
- Calculates wait times between movies
- Sorts combinations by total wait time
- Displays results in a clean, formatted table
- Easy-to-read output showing start times, end times, and wait durations

## Requirements

Python 3.6 or higher is required.

## Installation

1. Clone this repository:
```bash
git clone https://github.com/AgentGino/movie-marathon-planner.git
cd movie-marathon-planner
```

2. Create a virtual environment (optional but recommended):
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies from requirements.txt:
```bash
pip3 install -r requirements.txt
```

## Usage

1. Run the script:
```bash
python3 main.py
```

2. The program will display available movies with their showtimes

3. Enter the number of movies you want to watch

4. Review the possible combinations, sorted by wait time between movies

### Adding/Modifying Movies

To add or modify movies, edit the `movies` list in the `main()` function:

```python
movies = [
    Movie("Movie Name", ["14:30", "18:00", "21:30"], 148),
    # Add more movies...
]
```

Each movie needs:
- Name (string)
- List of showtimes (list of strings in 24-hour format "HH:MM")
- Duration (integer, in minutes)

## Sample Output

```
Available Movies:
+---+-------------+-------------------+
| # |    Movie    |    Showtimes     |
+---+-------------+-------------------+
| 1 |  Inception  | 14:30            |
|   |             | 18:00            |
|   |             | 21:30            |
+---+-------------+-------------------+

Found X possible combinations (sorted by wait time):
+----------+-------------+------------+-----------+------------+------------+
| Combo #  |   Movies    |Start Times | End Times |Wait Times  |Total Wait  |
+----------+-------------+------------+-----------+------------+------------+
|   #1     | Inception   |   14:30    |   16:58   | 30 mins    | 30 mins    |
|          | The Matrix  |   17:30    |   19:46   | -          |            |
+----------+-------------+------------+-----------+------------+------------+
```

## Project Structure

```
movie-marathon-planner/
│
├── main.py     # Main script
├── requirements.txt      # Project dependencies
└── README.md            # This file
```


## License

This project is licensed under the MIT License