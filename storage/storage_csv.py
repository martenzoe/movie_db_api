import csv
import os
from storage.istorage import IStorage

class StorageCsv(IStorage):
    """Implements CSV storage for the movie database."""

    def __init__(self, file_path: str):
        """Initialize the CSV storage.

        Args:
            file_path (str): Path to the CSV file.
        """
        self.file_path = file_path
        self._ensure_data_directory()

    def _ensure_data_directory(self) -> None:
        """Ensure that the data directory exists."""
        data_directory = os.path.dirname(self.file_path)
        if not os.path.exists(data_directory):
            os.makedirs(data_directory)

    def list_movies(self) -> dict:
        """List all movies in the database.

        Returns:
            dict: A dictionary of movies.
        """
        movies = {}
        try:
            with open(self.file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    movies[row['title']] = {
                        'year': int(row['year']),
                        'rating': float(row['rating']),
                        'poster': row['poster']
                    }
            return movies
        except FileNotFoundError:
            return {}

    def add_movie(self, title: str, year: int, rating: float, poster: str) -> None:
        """Add a movie to the database.

        Args:
            title (str): The title of the movie.
            year (int): The release year of the movie.
            rating (float): The rating of the movie.
            poster (str): The URL of the movie poster.

        Raises:
            TypeError: If any argument is of the wrong type.
        """
        # Datentypüberprüfungen
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        if not isinstance(year, int):
            raise TypeError("Year must be an integer.")
        if not isinstance(rating, (float, int)):  # Allow both float and int for ratings
            raise TypeError("Rating must be a float or an integer.")
        if not isinstance(poster, str):
            raise TypeError("Poster must be a string.")

        movies = self.list_movies()
        movies[title] = {"year": year, "rating": rating, "poster": poster}
        self._save_movies(movies)

    def delete_movie(self, title: str) -> bool:
        """Delete a movie from the database.

        Args:
            title (str): The title of the movie to delete.

        Returns:
            bool: True if the movie was deleted, False otherwise.

        Raises:
            TypeError: If title is not a string.
        """
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")

        movies = self.list_movies()
        if title in movies:
            del movies[title]
            self._save_movies(movies)
            return True
        return False

    def update_movie(self, title: str, rating: float) -> bool:
        """Update the rating of a movie in the database.

        Args:
            title (str): The title of the movie to update.
            rating (float): The new rating of the movie.

        Returns:
            bool: True if the movie was updated, False otherwise.

        Raises:
            TypeError: If title is not a string or rating is not a float.
        """
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        if not isinstance(rating, (float, int)):
            raise TypeError("Rating must be a float or an integer.")

        movies = self.list_movies()
        if title in movies:
            movies[title]["rating"] = rating
            self._save_movies(movies)
            return True
        return False

    def _save_movies(self, movies: dict) -> None:
        """Save the movies to the CSV file.

        Args:
            movies (dict): The movies to save.
        """
        with open(self.file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['title', 'year', 'rating', 'poster'])
            writer.writeheader()
            for title, details in movies.items():
                writer.writerow({
                    'title': title,
                    'year': details['year'],
                    'rating': details['rating'],
                    'poster': details['poster']
                })
