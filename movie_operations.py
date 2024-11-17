import movie_storage
from colorama import Fore

def list_movies():
    """
    List all movies in the database.

    This function retrieves the list of movies from the database and displays
    each movie's title, year, and rating. If no movies are found, it informs
    the user that the database is empty.

    Args:
        None

    Returns:
        None: Prints the list of movies or an empty database message to the console.
    """
    movies = movie_storage.get_movies()
    if not movies:
        print(f"{Fore.RED}No movies found in the database.{Fore.RESET}")
        return
    print("\nMovie List:")
    for title, movie in movies.items():
        print(f"{title} ({movie['year']}): {movie['rating']}")

def add_movie():
    """
    Add a new movie to the database.

    This function prompts the user for a movie title, rating, and release year.
    It validates the input and adds the movie to the database if all inputs are valid.
    The user can cancel the operation at any time.

    Args:
        None

    Returns:
        None: Adds a movie to the database or returns to the main menu.
    """
    while True:
        title = input(f"{Fore.GREEN}Enter new movie title (or type 'cancel' to go back):{Fore.RESET} ").strip()
        if title.lower() == 'cancel':
            return
        if not title:
            print(f"{Fore.RED}Title cannot be empty. Please try again.{Fore.RESET}")
            continue
        while True:
            try:
                rating = float(input(f"{Fore.GREEN}Enter movie rating (0-10):{Fore.RESET} "))
                year = int(input(f"{Fore.GREEN}Enter release year (1800-2100):{Fore.RESET} "))
                if 0 <= rating <= 10 and 1800 <= year <= 2100:
                    movie_storage.add_movie(title, year, rating)
                    print(f"'{title}' ({year}) has been added with a rating of {rating}")
                    return
                else:
                    print(f"{Fore.RED}Invalid rating or year. Please try again.{Fore.RESET}")
            except ValueError:
                print(f"{Fore.RED}Please enter valid numbers for rating and year.{Fore.RESET}")

def delete_movie():
    """
    Delete a movie from the database.

    This function prompts the user for a movie title to delete. It validates
    the input and removes the movie from the database if it exists. The user can
    cancel the operation at any time.

    Args:
        None

    Returns:
        None: Deletes a movie from the database or returns to the main menu.
    """
    while True:
        title = input(f"{Fore.GREEN}Enter movie name to delete (or type 'cancel' to go back):{Fore.RESET} ").strip()
        if title.lower() == 'cancel':
            return
        if not title:
            print(f"{Fore.RED}Title cannot be empty. Please try again.{Fore.RESET}")
            continue
        if title.isdigit():
            print(f"{Fore.RED}Invalid input: Title cannot be a number. Please enter a valid movie title.{Fore.RESET}")
            continue
        if movie_storage.delete_movie(title):
            print(f"'{title}' has been deleted from the movie list.")
        else:
            print(f"{Fore.RED}Error: Movie '{title}' doesn't exist in the list.{Fore.RESET}")

def update_movie():
    """
    Update an existing movie's rating in the database.

    This function prompts the user for a movie title and new rating. It validates
    the input and updates the movie's rating if it exists in the database. The user
    can cancel the operation at any time.

    Args:
        None

    Returns:
        None: Updates a movie's rating or returns to the main menu.
    """
    while True:
        title = input(f"{Fore.GREEN}Enter movie title to update (or type 'cancel' to go back):{Fore.RESET} ").strip()
        if title.lower() == 'cancel':
            return
        if not title:
            print(f"{Fore.RED}Title cannot be empty. Please try again.{Fore.RESET}")
            continue
        movies = movie_storage.get_movies()
        if title in movies:
            while True:
                try:
                    rating = float(input(f"{Fore.GREEN}Enter new movie rating (0-10):{Fore.RESET} "))
                    if 0 <= rating <= 10:
                        movie_storage.update_movie(title, rating)
                        print(f"'{title}' has been updated with a new rating of {rating}")
                        return
                    else:
                        print(f"{Fore.RED}Rating must be between 0 and 10.{Fore.RESET}")
                except ValueError:
                    print(f"{Fore.RED}Please enter a valid number for the rating.{Fore.RESET}")
        else:
            print(f"{Fore.RED}Error: Movie '{title}' doesn't exist in the list.{Fore.RESET}")