from istorage import IStorage


class MovieApp:
    def __init__(self, storage: IStorage):
        self._storage = storage

    def _command_list_movies(self):
        """List all movies in the database."""
        movies = self._storage.list_movies()
        if not movies:
            print("No movies found.")
        else:
            for title, details in movies.items():
                print(f"{title}: {details['rating']}")

    def _command_add_movie(self):
        """Add a new movie to the database."""
        title = input("Enter movie title: ")
        year = int(input("Enter movie year: "))
        rating = float(input("Enter movie rating (0-10): "))
        poster = input("Enter movie poster URL: ")
        self._storage.add_movie(title, year, rating, poster)
        print(f"Movie '{title}' added successfully.")

    def _command_delete_movie(self):
        """Delete a movie from the database."""
        title = input("Enter movie title to delete: ")
        if self._storage.delete_movie(title):
            print(f"Movie '{title}' deleted successfully.")
        else:
            print(f"Movie '{title}' not found.")

    def _command_update_movie(self):
        """Update a movie's rating in the database."""
        title = input("Enter movie title to update: ")
        rating = float(input("Enter new rating (0-10): "))
        if self._storage.update_movie(title, rating):
            print(f"Movie '{title}' updated successfully.")
        else:
            print(f"Movie '{title}' not found.")

    def _command_movie_stats(self):
        """Display movie statistics."""
        movies = self._storage.list_movies()
        if not movies:
            print("No movies in the database.")
            return

        avg_rating = sum(movie['rating'] for movie in movies.values()) / len(movies)
        print(f"Average rating: {avg_rating:.2f}")
        print(f"Total movies: {len(movies)}")

    def _generate_website(self):
        """Generate a simple HTML website with movie data."""
        movies = self._storage.list_movies()
        html_content = "<html><head><title>My Movie App</title></head><body>"
        html_content += "<h1>My Movie Collection</h1>"
        for title, details in movies.items():
            html_content += f"<h2>{title}</h2>"
            html_content += f"<p>Year: {details['year']}</p>"
            html_content += f"<p>Rating: {details['rating']}</p>"
            html_content += f"<img src='{details['poster']}' alt='{title} poster'>"
        html_content += "</body></html>"

        with open("movie_website.html", "w") as file:
            file.write(html_content)
        print("Website generated as 'movie_website.html'")

    def run(self):
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
            print("q. Quit")

            choice = input("Enter your choice: ").lower()
            if choice == 'q':
                print("Goodbye!")
                break
            elif choice in commands:
                commands[choice][1]()
            else:
                print("Invalid choice. Please try again.")
