from storage_json import StorageJson
from movie_app import MovieApp

def main():
    # Create a StorageJson object
    storage = StorageJson('movies.json')

    # Create a MovieApp object with the StorageJson object
    movie_app = MovieApp(storage)

    # Run the app
    movie_app.run()

if __name__ == "__main__":
    main()
