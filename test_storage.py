from storage_json import StorageJson


def test_storage():
    storage = StorageJson('movies.json')

    # Test list_movies
    print("Initial movies:", storage.list_movies())

    # Test add_movie
    storage.add_movie("Inception", 2010, 8.8, "inception_poster.jpg")
    print("After adding a movie:", storage.list_movies())

    # Test update_movie
    storage.update_movie("Inception", 9.0)
    print("After updating a movie:", storage.list_movies())

    # Test delete_movie
    storage.delete_movie("Inception")
    print("After deleting a movie:", storage.list_movies())


if __name__ == "__main__":
    test_storage()
