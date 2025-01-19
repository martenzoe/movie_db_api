"""Main entry point for the Movie Database Application."""

from movie_app import MovieApp
from storage.storage_csv import StorageCsv


def main():
    """
    Initialize and run the Movie Database Application.

    This function creates a CSV storage instance and a MovieApp instance,
    then runs the application.
    """
    storage = StorageCsv('data/movies.csv')
    movie_app = MovieApp(storage)
    movie_app.run()


if __name__ == "__main__":
    main()
