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


def list_movies(movies):
    """Display all movies and their ratings."""
    print("\nMovie List:")
    for movie in movies.values():
        print(f"{movie['title']} ({movie['year']}): {movie['rating']}")


def add_movie(movies):
    """Add a new movie to the database with a rating."""
    title = input(f"{Fore.GREEN}Enter new movie title:{Fore.RESET} ")
    while True:
        try:
            rating = float(input(f"{Fore.GREEN}Enter movie rating (0-10):{Fore.RESET} "))
            year = int(input(f"{Fore.GREEN}Enter release year:{Fore.RESET} "))
            if 0 <= rating <= 10 and 1800 <= year <= 2100:
                movies[title] = {"title": title, "rating": rating, "year": year}
                print(f"'{title}' ({year}) has been added with a rating of {rating}")
                return
            print(f"{Fore.RED}Invalid rating or year. Please try again.{Fore.RESET}")
        except ValueError:
            print(f"{Fore.RED}Please enter valid numbers for rating and year.{Fore.RESET}")


def delete_movie(movies):
    """Delete a movie from the database."""
    del_movie = input(f"{Fore.GREEN}Enter movie name to delete:{Fore.RESET} ")
    if del_movie in movies:
        del movies[del_movie]
        print(f"'{del_movie}' has been deleted from the movie list.")
    else:
        print(f"{Fore.RED}Error: Movie '{del_movie}' doesn't exist in the list.{Fore.RESET}")


def update_movie(movies):
    """Update the rating of an existing movie in the database."""
    title = input(f"{Fore.GREEN}Enter movie title:{Fore.RESET} ")
    if title in movies:
        while True:
            try:
                rating = float(input(f"{Fore.GREEN}Enter new movie rating (0-10):{Fore.RESET} "))
                if 0 <= rating <= 10:
                    movies[title]["rating"] = rating
                    print(f"'{title}' has been updated with a new rating of {rating}")
                    return
                print(f"{Fore.RED}Rating must be between 0 and 10.{Fore.RESET}")
            except ValueError:
                print(f"{Fore.RED}Please enter a valid number for the rating.{Fore.RESET}")
    else:
        print(f"{Fore.RED}Error: Movie '{title}' doesn't exist in the list.{Fore.RESET}")


def stats(movies):
    """Calculate and display various statistics about the movies."""
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


def random_movie_and_rating(movies):
    movie = random.choice(list(movies.keys()))
    rating = movies[movie]["rating"]
    print(f"Random movie: {movie}, Rating: {rating}")


def search_movie(movies):
    """Search for a movie using partial name matching."""
    search_input = input(f"{Fore.GREEN}Enter part of the movie name:{Fore.RESET} ")
    found_movies = []
    similar_movies = []

    for movie in movies.values():
        similarity = fuzz.ratio(search_input.lower(), movie["title"].lower())
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


def movies_sorted_by_rating(movies):
    """Display all movies sorted by their ratings in descending order."""
    sorted_movies = sorted(movies.values(), key=lambda x: x["rating"], reverse=True)
    print("Movies sorted by rating (highest to lowest):")
    for movie in sorted_movies:
        print(f"{movie['title']} ({movie['year']}): {movie['rating']}")


def create_rating_histogram(movies):
    """Create and save a histogram of movie ratings."""
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


def exit_program(movies):
    """Exit the program."""
    print("Bye!")
    return True


# Main function to run the movie database application.
def main():
    """Main function to run the movie database application."""
    movies = {
        "The Shawshank Redemption": {
            "title": "The Shawshank Redemption",
            "rating": 9.5,
            "year": 1994
        },
        "Pulp Fiction": {
            "title": "Pulp Fiction",
            "rating": 8.8,
            "year": 1994
        },
        "The Room": {
            "title": "The Room",
            "rating": 3.6,
            "year": 2003
        },
        "The Godfather": {
            "title": "The Godfather",
            "rating": 9.2,
            "year": 1972
        },
        "The Godfather: Part II": {
            "title": "The Godfather: Part II",
            "rating": 9.0,
            "year": 1974
        },
        "The Dark Knight": {
            "title": "The Dark Knight",
            "rating": 9.0,
            "year": 2008
        },
        "12 Angry Men": {
            "title": "12 Angry Men",
            "rating": 8.9,
            "year": 1957
        },
        "Everything Everywhere All At Once": {
            "title": "Everything Everywhere All At Once",
            "rating": 8.9,
            "year": 2022
        },
        "Forrest Gump": {
            "title": "Forrest Gump",
            "rating": 8.8,
            "year": 1994
        },
        "Star Wars: Episode V": {
            "title": "Star Wars: Episode V - The Empire Strikes Back",
            "rating": 8.7,
            "year": 1980
        }
    }

    # Dictionary mapping menu choices to functions
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
# Menu is supposed to be displayed all the time so we are using a while Loop to do that
    while True:
        display_menu()
        try:
            choice = int(input("Enter choice (0-9): "))
            if choice in menu_option_choice:
                if choice == 0:
                    exit_program(movies)
                    break
                menu_option_choice[choice](movies)
            else:
                print("Invalid choice. Please enter a number between 0 and 9.")

        except ValueError:
            print(f"{Fore.RED}Please enter a valid number.{Fore.RESET}")

        if input("Do you want to continue? (y/n): ").lower() != 'y': # Asking User if he want´s to continue giving input after every command
            break

if __name__ == "__main__":
    main()