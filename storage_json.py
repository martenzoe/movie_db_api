"""Module for JSON-based storage of movie data."""

import json
from typing import Dict, Any
from istorage import IStorage

class StorageJson(IStorage):
    """Implements JSON storage for the movie database."""

    def __init__(self, file_path: str):
        """Initialize the JSON storage.

        Args:
            file_path (str): Path to the JSON file.
        """
        self.file_path = file_path

    def list_movies(self) -> Dict[str, Dict[str, Any]]:
        """List all movies in the database.

        Returns:
            Dict[str, Dict[str, Any]]: A dictionary of movies.
        """
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def add_movie(self, title: str, year: int, rating: float, poster: str) -> None:
        """Add a movie to the database.

        Args:
            title (str): The title of the movie.
            year (int): The release year of the movie.
            rating (float): The rating of the movie.
            poster (str): The URL of the movie poster.
        """
        movies = self.list_movies()
        movies[title] = {"year": year, "rating": rating, "poster": poster}
        self._save_movies(movies)

    def delete_movie(self, title: str) -> bool:
        """Delete a movie from the database.

        Args:
            title (str): The title of the movie to delete.

        Returns:
            bool: True if the movie was deleted, False otherwise.
        """
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
        """
        movies = self.list_movies()
        if title in movies:
            movies[title]["rating"] = rating
            self._save_movies(movies)
            return True
        return False

    def _save_movies(self, movies: Dict[str, Dict[str, Any]]) -> None:
        """Save the movies to the JSON file.

        Args:
            movies (Dict[str, Dict[str, Any]]): The movies to save.
        """
        with open(self.file_path, 'w') as file:
            json.dump(movies, file, indent=4)
