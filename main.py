"""Main entry point for the Movie Database Application."""

from movie_app import MovieApp
from storage.storage_csv import StorageCsv
import os

def main():
    """
    Initialize and run the Movie Database Application.

    This function creates a CSV storage instance and a MovieApp instance,
    then runs the application.
    """
    # Define the path to the CSV file
    csv_file_path = 'data/movies.csv'

    # Check if the directory exists
    data_directory = os.path.dirname(csv_file_path)
    if not os.path.exists(data_directory):
        print(f"Error: The directory '{data_directory}' does not exist.")
        return

    # Create a StorageCsv instance
    try:
        storage = StorageCsv(csv_file_path)
        movie_app = MovieApp(storage)
        movie_app.run()
    except Exception as e:
        print(f"Error initializing the application: {e}")

if __name__ == "__main__":
    main()
