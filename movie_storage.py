import json

JSON_FILE = "data.json"


def get_movies():
    """Returns a dictionary of dictionaries that contains the movies information."""
    try:
        with open(JSON_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_movies(movies):
    """Saves movies to the JSON file."""
    with open(JSON_FILE, 'w') as file:
        json.dump(movies, file, indent=4)


def add_movie(title, year, rating):
    """Adds a movie to the movies database."""
    # Überprüfen auf ungültige Eingaben
    if not title or rating < 0 or rating > 10 or year < 1800 or year > 2100:
        return False  # Ungültige Eingabe

    movies = get_movies()

    # Wenn der Film bereits existiert, aktualisieren wir die Bewertung
    if title in movies:
        movies[title]["rating"] = rating
    else:
        movies[title] = {"year": year, "rating": rating}

    save_movies(movies)
    return True  # Erfolgreiches Hinzufügen oder Aktualisieren


def delete_movie(title):
    """Deletes a movie from the movies database."""
    if not title:  # Überprüfen auf leeren Titel
        return False

    movies = get_movies()

    if title in movies:
        del movies[title]
        save_movies(movies)
        print(f"'{title}' has been deleted from the movie list.")
        return True  # Erfolgreiches Löschen
    else:
        print(f"Error: Movie '{title}' doesn't exist in the list.")
        return False  # Film nicht gefunden


def update_movie(title, rating):
    """Updates a movie's rating in the movies database."""
    if not title or rating < 0 or rating > 10:  # Überprüfen auf ungültige Eingaben
        return False

    movies = get_movies()

    if title in movies:
        movies[title]["rating"] = rating
        save_movies(movies)
        return True  # Erfolgreiches Aktualisieren
    else:
        print(f"Error: Movie '{title}' doesn't exist in the list.")
        return False  # Film nicht gefunden