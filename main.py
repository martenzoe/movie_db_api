"""
Python Movie Database Application

This module implements a comprehensive movie database management system
that allows users to:
- List existing movies
- Add new movies
- Delete movies
- Update movie ratings
- View movie statistics
- Perform random movie selection
- Search for movies
- Sort movies by rating
- Create rating histograms

Key Features:
- Interactive command-line interface
- Persistent movie storage
- Fuzzy search functionality
- Basic movie analytics

Dependencies:
- movie_storage: Handles movie data persistence
- thefuzz: Provides fuzzy string matching
- matplotlib: Generates rating histograms
- colorama: Enables colored terminal output

Author: Marten Zöllner
Date: 17.11.2024
Version: 2.0
"""

from movie_analytics import (
    create_rating_histogram,
    movies_sorted_by_rating,
    search_movie,
    random_movie_and_rating,
    stats
)
from movie_operations import (
    list_movies,
    add_movie,
    delete_movie,
    update_movie
)
from menu import display_menu

from colorama import Fore, init

init()  # Initialize colorama for cross-platform colored terminal text


def exit_program():
    """
    Gracefully exit the movie database application.

    Prints a farewell message and signals the program to terminate.

    Returns:
        bool: Always returns True to indicate program termination.
    """
    print("Bye!")
    return True


def main():
    """
    Main entry point for the movie database application.

    Manages the primary program loop, handling user interactions and menu navigation.
    Provides a menu-driven interface for various movie database operations.

    The function:
    - Displays the menu
    - Captures user input
    - Validates and executes selected operations
    - Handles potential input errors
    - Offers continuous interaction until user chooses to exit

    Args:
        None

    Returns:
        None: Runs the application until user decides to exit.

    Raises:
        ValueError: If user enters a non-numeric menu choice.
    """
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