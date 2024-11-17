import json

JSON_FILE = "data.json"

def get_movies():
    """
    Retrieve the movies from the JSON file.

    This function attempts to load the movie data from a JSON file.
    If the file does not exist, it returns an empty dictionary.

    Args:
        None

    Returns:
        dict: A dictionary of movies, where each key is the movie title
              and the value is a dictionary containing 'year' and 'rating'.
    """
    try:
        with open(JSON_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_movies(movies):
    """
    Save the movies to the JSON file.

    This function takes a dictionary of movies and writes it to a JSON file.

    Args:
        movies (dict): A dictionary of movies to be saved.

    Returns:
        None: This function does not return a value.
    """
    with open(JSON_FILE, 'w') as file:
        json.dump(movies, file, indent=4)

def add_movie(title, year, rating):
    """
    Add a movie to the movies database.

    This function checks for valid input and adds a movie to the database.
    If the movie already exists, it updates its rating.

    Args:
        title (str): The title of the movie.
        year (int): The release year of the movie.
        rating (float): The rating of the movie (0-10).

    Returns:
        bool: True if the movie was added or updated successfully, False otherwise.
    """
    # Check for invalid inputs
    if not title or rating < 0 or rating > 10 or year < 1800 or year > 2100:
        return False  # Invalid input

    movies = get_movies()

    # If the movie already exists, update its rating
    if title in movies:
        movies[title]["rating"] = rating
    else:
        movies[title] = {"year": year, "rating": rating}

    save_movies(movies)
    return True  # Successful addition or update

def delete_movie(title):
    """
    Delete a movie from the movies database.

    This function removes a specified movie from the database if it exists.

    Args:
        title (str): The title of the movie to be deleted.

    Returns:
        bool: True if the movie was deleted successfully, False otherwise.
    """
    if not title:  # Check for empty title
        return False

    movies = get_movies()

    if title in movies:
        del movies[title]
        save_movies(movies)
        print(f"'{title}' has been deleted from the movie list.")
        return True  # Successful deletion
    else:
        print(f"Error: Movie '{title}' doesn't exist in the list.")
        return False  # Movie not found

def update_movie(title, rating):
    """
    Update a movie's rating in the movies database.

    This function changes the rating of an existing movie if it is found in
    the database.

    Args:
        title (str): The title of the movie to be updated.
        rating (float): The new rating for the movie (0-10).

    Returns:
        bool: True if the movie's rating was updated successfully, False otherwise.
    """
    if not title or rating < 0 or rating > 10:  # Check for invalid inputs
        return False

    movies = get_movies()

    if title in movies:
        movies[title]["rating"] = rating
        save_movies(movies)
        return True  # Successful update
    else:
        print(f"Error: Movie '{title}' doesn't exist in the list.")
        return False  # Movie not found