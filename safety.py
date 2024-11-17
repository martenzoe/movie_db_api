"""
Python Movie Database Application

This module implements a movie database management system.
It allows users to manage a collection of movies, including adding,
deleting, updating, and viewing movie information.

Usage: python3 movies.py

Author: Marten Zöllner
Date: 25.10.2024
Version: 1.0
"""

import movie_storage
import random
import matplotlib.pyplot as plt
from thefuzz import fuzz
from colorama import Fore, init

init()  # Initialize colorama for cross-platform colored terminal text

MENU_ITEMS = [
    "Menu:",
    "0. Exit",
    "1. List movies",
    "2. Add movie",
    "3. Delete movie",
    "4. Update movie",
    "5. Stats",
    "6. Random movie",
    "7. Search movie",
    "8. Movies sorted by rating",
    "9. Create Rating Histogram",
]


def display_menu():
    """Display the main menu of the application."""
    print("********** My Movies Database **********")
    print()
    print(f"{Fore.BLUE}\n".join(MENU_ITEMS))
    print(Fore.RESET)


def list_movies():
    movies = movie_storage.get_movies()
    print("\nMovie List:")
    for title, movie in movies.items():
        print(f"{title} ({movie['year']}): {movie['rating']}")


def add_movie():
    title = input(f"{Fore.GREEN}Enter new movie title:{Fore.RESET} ")
    while True:
        try:
            rating = float(input(f"{Fore.GREEN}Enter movie rating (0-10):{Fore.RESET} "))
            year = int(input(f"{Fore.GREEN}Enter release year:{Fore.RESET} "))
            if 0 <= rating <= 10 and 1800 <= year <= 2100:
                movie_storage.add_movie(title, year, rating)  # Hier wird die Funktion aufgerufen
                print(f"'{title}' ({year}) has been added with a rating of {rating}")
                return
            else:
                print(f"{Fore.RED}Invalid rating or year. Please try again.{Fore.RESET}")
        except ValueError:
            print(f"{Fore.RED}Please enter valid numbers for rating and year.{Fore.RESET}")


def delete_movie():
    """Delete a movie from the database."""
    title = input(f"{Fore.GREEN}Enter movie name to delete:{Fore.RESET} ")
    movie_storage.delete_movie(title)  # Aufruf der delete_movie Funktion aus movie_storage


def update_movie():
    """Update the rating of an existing movie in the database."""
    title = input(f"{Fore.GREEN}Enter movie title:{Fore.RESET} ")

    movies = movie_storage.get_movies()  # Filme abrufen

    if title in movies:
        while True:
            try:
                rating = float(input(f"{Fore.GREEN}Enter new movie rating (0-10):{Fore.RESET} "))
                if 0 <= rating <= 10:
                    movie_storage.update_movie(title, rating)  # Aufruf der update_movie Funktion aus movie_storage
                    print(f"'{title}' has been updated with a new rating of {rating}")
                    return
                else:
                    print(f"{Fore.RED}Rating must be between 0 and 10.{Fore.RESET}")
            except ValueError:
                print(f"{Fore.RED}Please enter a valid number for the rating.{Fore.RESET}")
    else:
        print(f"{Fore.RED}Error: Movie '{title}' doesn't exist in the list.{Fore.RESET}")


def stats():
    """Calculate and display various statistics about the movies."""
    movies = movie_storage.get_movies()
    if not movies:
        print("The Database is empty.")
        return

    ratings = [movie["rating"] for movie in movies.values()]
    num_movies = len(movies)
    average_rating = sum(ratings) / num_movies
    sorted_ratings = sorted(ratings)
    median_rating = (sorted_ratings[num_movies // 2 - 1] +
                     sorted_ratings[num_movies // 2]) / 2
    max_rating = max(ratings)
    min_rating = min(ratings)

    print(f"Number of movies: {num_movies}")
    print(f"Average rating: {average_rating:.2f}")
    print(f"Median rating: {median_rating:.2f}")

    print("\nBest movie(s):")
    for movie in movies.values():
        if movie["rating"] == max_rating:
            print(f"- {movie['title']} ({movie['year']}): {movie['rating']}")

    print("\nWorst movie(s):")
    for movie in movies.values():
        if movie["rating"] == min_rating:
            print(f"- {movie['title']} ({movie['year']}): {movie['rating']}")


def random_movie_and_rating():
    movies = movie_storage.get_movies()
    movie = random.choice(list(movies.keys()))
    rating = movies[movie]["rating"]
    print(f"Random movie: {movie}, Rating: {rating}")


def search_movie():
    """Search for a movie using partial name matching."""
    movies = movie_storage.get_movies()
    search_input = input(f"{Fore.GREEN}Enter part of the movie name:{Fore.RESET} ")
    found_movies = []
    similar_movies = []

    for title, movie in movies.items():
        similarity = fuzz.ratio(search_input.lower(), title.lower())
        if similarity == 100:
            found_movies.append(movie)
        elif similarity > 60:
            similar_movies.append((movie, similarity))

    if found_movies:
        print("\nExact matches:")
        for movie in found_movies:
            print(f"{movie['title']} ({movie['year']}): {movie['rating']}")
    elif similar_movies:
        print("\nNo exact matches found. Did you mean:")
        for movie, similarity in sorted(similar_movies, key=lambda x: x[1], reverse=True):
            print(f"{movie['title']} ({movie['year']}): {movie['rating']} (Similarity: {similarity}%)")
    else:
        print(f"{Fore.RED}No movies found matching or similar to your search.{Fore.RESET}")


def movies_sorted_by_rating():
    """Display all movies sorted by their ratings in descending order."""
    movies = movie_storage.get_movies()

    if not movies:
        print("The Database is empty.")
        return

    # Sortiere die Filme nach ihrer Bewertung (rating)
    sorted_movies = sorted(movies.items(), key=lambda x: x[1]["rating"], reverse=True)

    print("Movies sorted by rating (highest to lowest):")
    for title, movie in sorted_movies:
        print(f"{title} ({movie['year']}): {movie['rating']}")


def create_rating_histogram():
    """Create and save a histogram of movie ratings."""
    movies = movie_storage.get_movies()
    ratings = [movie["rating"] for movie in movies.values()]
    plt.figure(figsize=(10, 6))
    plt.hist(ratings, bins=10, range=(0, 10), edgecolor="black")
    plt.title("Movie Ratings Histogram")
    plt.xlabel("Rating")
    plt.ylabel("Number of Movies")
    filename = input("Enter the filename to save the histogram (e.g., histogram.png): ")
    plt.savefig(filename)
    plt.close()
    print(f"Histogram saved as {filename}")


def exit_program():
    """Exit the program."""
    print("Bye!")
    return True


# Main function to run the movie database application.
def main():
    menu_option_choice = {
        0: exit_program,
        1: list_movies,
        2: add_movie,
        3: delete_movie,
        4: update_movie,
        5: stats,
        6: random_movie_and_rating,
        7: search_movie,
        8: movies_sorted_by_rating,
        9: create_rating_histogram
    }

    while True:
        display_menu()
        try:
            choice = int(input("Enter choice (0-9): "))
            if choice in menu_option_choice:
                if choice == 0:
                    if exit_program():
                        break
                else:
                    menu_option_choice[choice]()
            else:
                print("Invalid choice. Please enter a number between 0 and 9.")
        except ValueError:
            print(f"{Fore.RED}Please enter a valid number.{Fore.RESET}")

        if input("Do you want to continue? (y/n): ").lower() != 'y':
            break

    print("Program ended.")


if __name__ == "__main__":
    main()