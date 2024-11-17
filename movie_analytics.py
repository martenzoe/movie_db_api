import movie_storage
import random
import matplotlib.pyplot as plt
from thefuzz import fuzz
from colorama import Fore, init

def stats():
    """
    Calculate and display various statistics about the movies in the database.

    This function computes and prints:
    - Total number of movies
    - Average rating
    - Best rated movie(s)
    - Worst rated movie(s)

    If the database is empty, it prints a message indicating so.

    Args:
        None

    Returns:
        None: This function prints the statistics to the console.
    """
    movies = movie_storage.get_movies()

    if not movies:
        print("The Database is empty.")
        return

    ratings = [movie["rating"] for movie in movies.values()]
    num_movies = len(movies)

    average_rating = sum(ratings) / num_movies
    sorted_ratings = sorted(ratings)

    median_rating = (sorted_ratings[num_movies // 2 - 1] +
                     sorted_ratings[num_movies // 2]) / 2 if num_movies % 2 == 0 else sorted_ratings[num_movies // 2]

    max_rating = max(ratings)
    min_rating = min(ratings)

    print(f"Number of movies: {num_movies}")
    print(f"Average rating: {average_rating:.2f}")

    print("\nBest movie(s):")
    for title, movie in movies.items():
        if movie["rating"] == max_rating:
            print(f"- {title} ({movie['year']}): {movie['rating']}")

    print("\nWorst movie(s):")
    for title, movie in movies.items():
        if movie["rating"] == min_rating:
            print(f"- {title} ({movie['year']}): {movie['rating']}")

def random_movie_and_rating():
    """
    Select and display a random movie with its rating from the database.

    Args:
        None

    Returns:
        None: This function prints the selected movie and its rating to the console.

    Raises:
        IndexError: If the movie database is empty.
    """
    movies = movie_storage.get_movies()
    if not movies:
        print("The database is empty.")
        return
    movie = random.choice(list(movies.keys()))
    rating = movies[movie]["rating"]
    print(f"Random movie: {movie}, Rating: {rating}")

def search_movie():
    """
    Search for a movie using partial name matching.

    This function prompts the user to enter a part of a movie title,
    then searches the database for matches. It displays exact matches
    and similar matches based on fuzzy string matching.

    Args:
        None

    Returns:
        None: This function prints the search results to the console.
    """
    while True:
        search_input = input(f"{Fore.GREEN}Enter part of the movie name (or type 'cancel' to go back):{Fore.RESET} ").strip()
        if search_input.lower() == 'cancel':
            return
        if not search_input:
            print(f"{Fore.RED}Input cannot be empty. Please try again.{Fore.RESET}")
            continue

        movies = movie_storage.get_movies()
        found_movies = []
        similar_movies = []

        for title, movie in movies.items():
            similarity = fuzz.ratio(search_input.lower(), title.lower())
            if similarity == 100:
                found_movies.append((title, movie))
            elif similarity > 60:
                similar_movies.append((title, movie, similarity))

        if found_movies:
            print("\nExact matches:")
            for title, movie in found_movies:
                print(f"{title} ({movie['year']}): {movie['rating']}")
        elif similar_movies:
            print("\nNo exact matches found. Did you mean:")
            for title, movie, similarity in sorted(similar_movies, key=lambda x: x[2], reverse=True):
                print(f"{title} ({movie['year']}): {movie['rating']} (Similarity: {similarity}%)")
        else:
            print(f"{Fore.RED}No movies found matching or similar to your search.{Fore.RESET}")

        break

def movies_sorted_by_rating():
    """
    Display all movies sorted by their ratings in descending order.

    Args:
        None

    Returns:
        None: This function prints the sorted list of movies to the console.
    """
    movies = movie_storage.get_movies()

    if not movies:
        print("The Database is empty.")
        return

    sorted_movies = sorted(movies.items(), key=lambda x: x[1]["rating"], reverse=True)

    print("Movies sorted by rating (highest to lowest):")
    for title, movie in sorted_movies:
        print(f"{title} ({movie['year']}): {movie['rating']}")

def create_rating_histogram():
    """
    Create and save a histogram of movie ratings.

    This function generates a histogram of movie ratings and saves it as an image file.
    The user is prompted to enter a filename for the saved image.

    Args:
        None

    Returns:
        None: This function saves the histogram as an image file and prints a confirmation message.

    Raises:
        ValueError: If there are no movies in the database.
    """
    movies = movie_storage.get_movies()
    if not movies:
        print("The database is empty. Cannot create histogram.")
        return

    ratings = [movie["rating"] for movie in movies.values()]
    plt.figure(figsize=(10, 6))
    plt.hist(ratings, bins=10, range=(0, 10), edgecolor="black")
    plt.title("Movie Ratings Histogram")
    plt.xlabel("Rating")
    plt.ylabel("Number of Movies")
    filename = input("Enter the filename to save the histogram (e.g., histogram.png): ")
    plt.savefig(filename)
    plt.close()
    print(f"Histogram saved as {filename}")