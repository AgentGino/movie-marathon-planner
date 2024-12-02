from datetime import datetime, timedelta
from itertools import combinations, product
from tabulate import tabulate


class MovieShowing:
    def __init__(self, name, start_time, duration):
        self.name = name
        self.start_time = datetime.strptime(start_time, "%H:%M")
        self.duration = int(duration)  # duration in minutes
        self.end_time = self.start_time + timedelta(minutes=self.duration)

    def __str__(self):
        return f"{self.name} ({self.start_time.strftime('%H:%M')}-{self.end_time.strftime('%H:%M')})"

    def get_info(self):
        return {
            'name': self.name,
            'start': self.start_time.strftime('%H:%M'),
            'end': self.end_time.strftime('%H:%M')
        }

    def has_conflict(self, other_showing):
        return (self.start_time < other_showing.end_time and
                other_showing.start_time < self.end_time)


class Movie:
    def __init__(self, name, timings, duration):
        self.name = name
        self.timings = timings
        self.duration = duration
        self.showings = [MovieShowing(name, time, duration) for time in timings]

    def __str__(self):
        times = ", ".join(self.timings)
        return f"{self.name} [{times}]"


def calculate_wait_time(movie1, movie2):
    """Calculate wait time between two movies in minutes"""
    wait_time = (movie2.start_time - movie1.end_time).total_seconds() / 60
    return max(0, wait_time)


def get_total_wait_time(combo):
    """Calculate total wait time for a combination of movies"""
    sorted_combo = sorted(combo, key=lambda x: x.start_time)
    total_wait = 0
    for i in range(len(sorted_combo) - 1):
        total_wait += calculate_wait_time(sorted_combo[i], sorted_combo[i + 1])
    return total_wait


def find_movie_combinations(movies, num_movies):
    valid_combinations = []

    for movie_combo in combinations(movies, num_movies):
        showing_options = [movie.showings for movie in movie_combo]

        for showing_combo in product(*showing_options):
            has_conflicts = False
            for i in range(len(showing_combo)):
                for j in range(i + 1, len(showing_combo)):
                    if showing_combo[i].has_conflict(showing_combo[j]):
                        has_conflicts = True
                        break
                if has_conflicts:
                    break

            if not has_conflicts:
                valid_combinations.append(showing_combo)

    # Sort combinations by total wait time
    valid_combinations.sort(key=get_total_wait_time)
    return valid_combinations


def create_combination_table(combinations):
    if not combinations:
        return "No valid combinations found!"

    headers = ['Combo #', 'Movies', 'Start Times', 'End Times', 'Wait Times', 'Total Wait']
    table_data = []

    for i, combo in enumerate(combinations, 1):
        # Sort movies by start time
        sorted_combo = sorted(combo, key=lambda x: x.start_time)

        # Get movie information
        movies = [show.name for show in sorted_combo]
        start_times = [show.start_time.strftime('%H:%M') for show in sorted_combo]
        end_times = [show.end_time.strftime('%H:%M') for show in sorted_combo]

        # Calculate wait times between movies
        wait_times = []
        for j in range(len(sorted_combo) - 1):
            wait = calculate_wait_time(sorted_combo[j], sorted_combo[j + 1])
            wait_times.append(f"{int(wait)} mins")
        wait_times.append("-")  # Add placeholder for last movie

        total_wait = get_total_wait_time(sorted_combo)

        # Format the data
        row = [
            f"#{i}",
            "\n".join(movies),
            "\n".join(start_times),
            "\n".join(end_times),
            "\n".join(wait_times),
            f"{int(total_wait)} mins"
        ]
        table_data.append(row)

    return tabulate(table_data, headers=headers, tablefmt='grid', stralign='center')


def print_available_movies(movies):
    headers = ['#', 'Movie', 'Showtimes']
    table_data = []

    for i, movie in enumerate(movies, 1):
        row = [
            i,
            movie.name,
            "\n".join(movie.timings)
        ]
        table_data.append(row)

    print("\nAvailable Movies:")
    print(tabulate(table_data, headers=headers, tablefmt='grid', stralign='center'))


def main():
    # Sample movies list with multiple showtimes
    movies = [
        Movie("Red One", ["12:40", "15:40", "19:05", "22:00"], 123),
        Movie("Gladiator II", ["14:15", "17:45", "18:45", "21:00"], 148)  # 18:45 is IMAX showing
        # Movie("Moana 2", ["12:45", "13:40", "15:10", "16:20", "19:05", "21:30"], 100)  # Combined all showtimes, IMAX at 13:40, 16:20
    ]

    while True:
        print_available_movies(movies)

        try:
            num_movies = int(input("\nHow many movies would you like to watch? (0 to exit): "))
            if num_movies == 0:
                break
            if num_movies < 0 or num_movies > len(movies):
                print(f"Please enter a number between 1 and {len(movies)}")
                continue

            combinations = find_movie_combinations(movies, num_movies)
            print(f"\nFound {len(combinations)} possible combinations (sorted by wait time):\n")
            print(create_combination_table(combinations))
            print()

        except ValueError:
            print("Please enter a valid number")


if __name__ == "__main__":
    main()