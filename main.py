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
from movie_analytics import create_rating_histogram, movies_sorted_by_rating, search_movie, random_movie_and_rating, stats
from movie_operations import list_movies, add_movie, delete_movie, update_movie
from menu import display_menu

from colorama import Fore, init

init()  # Initialize colorama for cross-platform colored terminal text


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
            choice = input("Enter choice (0-9): ").strip()
            if not choice.isdigit():
                raise ValueError("Not a number")

            choice = int(choice)
            if choice in menu_option_choice:
                if choice == 0:
                    if exit_program():
                        break
                else:
                    menu_option_choice[choice]()
            else:
                print(f"{Fore.YELLOW}Invalid choice. Please enter a number between 0 and 9.{Fore.RESET}")
        except ValueError:
            print(f"{Fore.RED}Please enter a valid number.{Fore.RESET}")

        if input("Do you want to continue? (y/n): ").lower().strip() != 'y':
            break

    print("Program ended.")


if __name__ == "__main__":
    main()