"""Module for the main Movie Application logic."""

from typing import Dict, Any
from storage.istorage import IStorage
from omdb_api import get_movie_info

class MovieApp:
    """Main class for the Movie Application."""

    def __init__(self, storage: IStorage):
        """Initialize the MovieApp with a storage implementation."""
        self._storage = storage

    def _command_list_movies(self) -> None:
        """List all movies in the database."""
        movies = self._storage.list_movies()
        if not movies:
            print("No movies found.")
        else:
            for title, details in movies.items():
                print(f"{title}: {details['rating']}")

    def _command_add_movie(self) -> None:
        """Add a new movie to the database."""
        title = input("Enter movie title: ")
        movie_data = self._fetch_movie_data(title)

        if movie_data:
            try:
                self._storage.add_movie(
                    movie_data['Title'],
                    int(movie_data['Year']),
                    float(movie_data['imdbRating']),
                    movie_data['Poster']
                )
                print(f"Movie '{movie_data['Title']}' added successfully.")
            except TypeError as e:
                print(f"Error adding movie: {e}")
        else:
            print("Movie could not be found.")

    def _fetch_movie_data(self, title: str) -> Dict[str, Any]:
        """Fetch movie data from the OMDb API."""
        try:
            movie_info = get_movie_info(title)
            if movie_info and movie_info.get('Response') == 'True':
                return movie_info
            return None
        except Exception as e:
            print(f"Error retrieving movie data: {e}")
            return None

    def _command_delete_movie(self) -> None:
        """Delete a movie from the database."""
        title = input("Enter the title of the movie to delete: ")
        try:
            if self._storage.delete_movie(title):
                print(f"Movie '{title}' deleted successfully.")
            else:
                print(f"Movie '{title}' not found.")
        except TypeError as e:
            print(f"Error deleting movie: {e}")

    def _command_update_movie(self) -> None:
        """Update the rating of a movie in the database."""
        title = input("Enter the title of the movie to update: ")
        try:
            rating = float(input("Enter the new rating (0-10): "))
            if self._storage.update_movie(title, rating):
                print(f"Movie '{title}' updated successfully.")
            else:
                print(f"Movie '{title}' not found.")
        except ValueError:
            print("Invalid rating. Please enter a number.")
        except TypeError as e:
            print(f"Error updating movie: {e}")

    def _command_movie_stats(self) -> None:
        """Display movie statistics."""
        movies = self._storage.list_movies()
        if not movies:
            print("No movies in the database.")
            return

        avg_rating = sum(movie['rating'] for movie in movies.values()) / len(movies)
        print(f"Average rating: {avg_rating:.2f}")
        print(f"Number of movies: {len(movies)}")

    def _generate_website(self) -> None:
        """Generate a simple HTML website with movie data."""
        movies = self._storage.list_movies()
        html_content = self._create_html_content(movies)

        with open("index.html", "w", encoding='utf-8') as file:
            file.write(html_content)
        print("Website was generated successfully.")

    @staticmethod
    def _create_html_content(movies: Dict[str, Dict[str, Any]]) -> str:
        """Generate HTML content for the Movie Website."""
        html_template = """
        <html>
        <head>
            <title>My Movie App</title>
            <link rel="stylesheet" href="style.css"/>
        </head>
        <body>
            <div class="list-movies-title">
                <h1>My Movie App</h1>
            </div>
            <div>
                <ol class="movie-grid">
                    {movie_entries}
                </ol>
            </div>
        </body>
        </html>
        """

        movie_entries = "".join(
            f"""
            <li>
                <div class="movie">
                    <img class="movie-poster"
                         src="{details.get('poster', '')}" alt="{title} Poster"/>
                    <div class="movie-title">{title}</div>
                    <div class="movie-year">{details['year']}</div>
                </div>
            </li>
            """
            for title, details in movies.items()
        )

        return html_template.format(movie_entries=movie_entries)

    def run(self) -> None:
        """Run the main application loop."""

        commands = {
            "1": ("List movies", self._command_list_movies),
            "2": ("Add movie", self._command_add_movie),
            "3": ("Delete movie", self._command_delete_movie),
            "4": ("Update movie", self._command_update_movie),
            "5": ("Movie statistics", self._command_movie_stats),
            "6": ("Generate website", self._generate_website),
        }

        while True:
            print("\n== Movie App ==")
            for key, (description, _) in commands.items():
                print(f"{key}. {description}")
            print("0. Exit")

            choice = input("Enter your choice: ").lower()
            if choice == '0':  # Check for '0' to exit
                print("Goodbye!")
                break
            elif choice in commands:
                commands[choice][1]()
            else:
                print("Invalid choice. Please try again.")
