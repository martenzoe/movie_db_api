"""
Python Movie Database Application

This code implements a movie database management system in Python.
You can start the program with the command: python3 movies.py

Functions:
- display_menu(): Displays the main menu of the application.
- list_movies(movies): Lists all movies in the database.
- add_movie(movies): Adds a new movie to the database.
- delete_movie(movies): Deletes a movie from the database.
- update_movie(movies): Updates the rating of a movie in the database.
- stats(movies): Displays statistics about the movies in the database.
- random_movie_and_rating(movies): Selects and displays a random movie from the database.
- search_movie(movies): Searches for a movie in the database.
- movies_sorted_by_rating(movies): Displays movies sorted by their ratings.
- create_rating_histogram(movies): Creates a histogram of movie ratings.

Flow:
1. Initializes a sample movie database.
2. Displays a menu of options to the user.
3. Processes user input to perform the selected operation.
4. Repeats steps 2-3 until the user chooses to exit.

Libary Moduls explained:
- random: For selecting random movies.
- matplotlib: For creating the rating histogram.
- thefuzz: For fuzzy string matching in the search function.
- colorama: For colored console output.

Author: Marten Zöllner
Date: 25.10.2024
Version: 1.0

"""

import random
import matplotlib.pyplot as plt
from thefuzz import fuzz
from colorama import Fore, init
init() # Initialize colorama for cross-platform colored terminal text

# Define menu items for the main menu
menu_items = [
    "Menu:",
    "0. Exit",
    "1. List movies",
    "2. Add movie",
    "3. Delete movie",
    "4. Update movie",
    "5. Stats",
    "6. Random movie",
    "7. Search movie",
    "8. Movies sorted by rating",
    "9. Create Rating Histogram",

]
# Display the main menu of the application.
def display_menu():
    print(f"********** My Movies Database **********")
    print()  # Creates an empty line for better readability
    print(f"{Fore.BLUE}\n".join(menu_items))
    print(Fore.RESET)

# Display all movies and their ratings in the database.
def list_movies(movies):
    print("\nMovie List:")
    for movie in movies.values():
        print(f"{movie['title']} ({movie['year']}): {movie['rating']}")

# Add a new movie to the database with a rating.
def add_movie(movies):
    title = input(f"{Fore.GREEN}Enter new movie title:{Fore.RESET} ")
    while True:
        try:
            rating = float(input(f"{Fore.GREEN}Enter movie rating (0-10):{Fore.RESET} "))
            year = int(input(f"{Fore.GREEN}Enter release year:{Fore.RESET} "))
            if 0 <= rating <= 10 and 1800 <= year <= 2100:
                movies[title] = {"title": title, "rating": rating, "year": year}
                print(f"'{title}' ({year}) has been added with a rating of {rating}")
                return
            else:
                print(f"{Fore.RED}Invalid rating or year. Please try again.{Fore.RESET}")
        except ValueError:
            print(f"{Fore.RED}Please enter valid numbers for rating and year.{Fore.RESET}")

# Delete a movie from the database.
def delete_movie(movies):
    del_movie = input(f"{Fore.GREEN}Enter movie name to delete:{Fore.RESET} ")
    if del_movie in movies:
        del movies[del_movie]
        print(f"'{del_movie}' has been deleted from the movie list.")
    else:
        print(f"{Fore.RED}Error: Movie '{del_movie}' doesn't exist in the list.{Fore.RESET}")

# Update the rating of an existing movie in the database.
def update_movie(movies):
    upd_movie = input(f"{Fore.GREEN}Enter movie name:{Fore.RESET} ")
    if upd_movie in movies:
        while True:
            try:
                upd_rating = float(input(f"{Fore.GREEN}Enter new movie rating (0-10):{Fore.RESET} "))
                if 0 <= upd_rating <= 10:
                    movies[upd_movie] = upd_rating
                    print(f"'{upd_movie}' has been updated with a new rating of {upd_rating}")
                    return
                else:
                    print("Rating must be between 0 and 10.")
            except ValueError:
                print(f"{Fore.RED}Please enter a valid number for the rating.{Fore.RESET}")
    else:
        print(f"{Fore.RED}Error: Movie '{upd_movie}' doesn't exist in the list.{Fore.RESET}")

# This function calculates and displays various statistics about the movie
def stats(movies):
    if not movies:
        print("The Database is empty.")
        return

    ratings = list(movies.values())
    num_movies = len(movies)

    # Average Rating
    average_rating = sum(ratings) / num_movies

    # Median Rating
    sorted_ratings = sorted(ratings)
    if num_movies % 2 == 0:
        median_rating = (sorted_ratings[num_movies // 2 - 1] + sorted_ratings[num_movies // 2]) / 2
    else:
        median_rating = sorted_ratings[num_movies // 2]

    # Max and min Rating
    max_rating = max(ratings)
    min_rating = min(ratings)
    best_movies = [movie for movie, rating in movies.items() if rating == max_rating]
    worst_movies = [movie for movie, rating in movies.items() if rating == min_rating]

    # Display statistics
    print(f"Number of movies: {num_movies}")
    print(f"Average rating: {average_rating:.2f}")
    print(f"Median rating: {median_rating:.2f}")

    print("\nBest movie(s):")
    for movie in best_movies:
        print(f"- {movie} ({movies[movie]})")

    print("\nWorst movie(s):")
    for movie in worst_movies:
        print(f"- {movie} ({movies[movie]})")

# Select and display a random movie and its rating from the database.
def random_movie_and_rating(movies):
    movie, rating = random.choice(list(movies.items())) # random.choice to select a random movie from the database
    print(f"Random movie: {movie}, Rating: {rating}")

# Search for a movie in the database using partial name matching.
# It displays exact matches and similar matches with their similarity scores.
# Uses the Fuzz Modul from the Library
def search_movie(movies):
    search_input = input(f"{Fore.GREEN}Enter part of the movie name:{Fore.RESET} ")
    found_movies = [] # Initialize lists to store exact matches and similar matches
    similar_movies = []

    for movie, rating in movies.items():
        similarity = fuzz.ratio(search_input.lower(), movie.lower()) # fuzz.ratio returns a value between 0 and 100.
        if similarity == 100: # If there's a perfect match (100% similarity), add to found_movies.
            found_movies.append((movie, rating))
        elif similarity > 60:  # If similarity is above 60%, consider it a similar match.
            similar_movies.append((movie, rating, similarity))

    # Display exact matches if any are found
    if found_movies:
        print("\nExact matches:")
        for movie, rating in found_movies:
            print(f"{movie}: {rating}")
    elif similar_movies: # If no exact matches, display similar matches
        print("\nNo exact matches found. Did you mean:")
        for movie, rating, similarity in sorted(similar_movies, key=lambda x: x[2], reverse=True): # Sort similar movies by similarity score in descending order.
            print(f"{movie}: {rating} (Similarity: {similarity}%)")
    else:
        print(f"{Fore.RED}No movies found matching or similar to your search.{Fore.RESET}")

# Display all movies sorted by their ratings in descending order.
def movies_sorted_by_rating(movies):
    sorted_movies = sorted(movies.items(), key=lambda x: x[1], reverse=True)

    print("Movies sorted by rating (highest to lowest):")
    for movie, rating in sorted_movies:
        print(f"{movie}: {rating}")

# Create and save a histogram of movie ratings.
# This function uses matplotlib to create a histogram of the movie ratings.
# It prompts the user for a filename to save the histogram as an image.
def create_rating_histogram(movies):
    ratings = list(movies.values()) # Extract all ratings from the movies dictionary into a list.

    plt.figure(figsize=(10, 6)) # Create a new figure with a size of 10x6 inches
    # Create a histogram of the ratings
    # bins=10: Divide the data into 10 equal-width bins
    # range=(0, 10): Set the range of the x-axis from 0 to 10
    # edgecolor='black': Set the color of the edges of each bar to black
    plt.hist(ratings, bins=10, range=(0, 10), edgecolor='black')
    plt.title('Movie Ratings Histogram') # Set the title of the histogram
    plt.xlabel('Rating') # Label the x-axis
    plt.ylabel('Number of Movies') # Label the y-axis

    # Prompt the user to enter a filename for saving the histogram
    filename = input("Enter the filename to save the histogram (e.g., histogram.png): ")
    plt.savefig(filename)
    plt.close()
    print(f"Histogram saved as {filename}")


def exit_program(movies):
    print("Bye!")
    return True



# Main function to run the movie database application.
def main():
    # Dictionary to store the movies and the rating
    movies = {
        "The Shawshank Redemption": {
            "title": "The Shawshank Redemption",
            "rating": 9.5,
            "year": 1994
        },
        "Pulp Fiction": {
            "title": "Pulp Fiction",
            "rating": 8.8,
            "year": 1994
        },
        "The Room": {
            "title": "The Room",
            "rating": 3.6,
            "year": 2003
        },
        "The Godfather": {
            "title": "The Godfather",
            "rating": 9.2,
            "year": 1972
        },
        "The Godfather: Part II": {
            "title": "The Godfather: Part II",
            "rating": 9.0,
            "year": 1974
        },
        "The Dark Knight": {
            "title": "The Dark Knight",
            "rating": 9.0,
            "year": 2008
        },
        "12 Angry Men": {
            "title": "12 Angry Men",
            "rating": 8.9,
            "year": 1957
        },
        "Everything Everywhere All At Once": {
            "title": "Everything Everywhere All At Once",
            "rating": 8.9,
            "year": 2022
        },
        "Forrest Gump": {
            "title": "Forrest Gump",
            "rating": 8.8,
            "year": 1994
        },
        "Star Wars: Episode V": {
            "title": "Star Wars: Episode V - The Empire Strikes Back",
            "rating": 8.7,
            "year": 1980
        }
    }

    # Dictionary mapping menu choices to functions
    menu_option_choice = {
        0: exit_program,
        1: list_movies,
        2: add_movie,
        3: delete_movie,
        4: update_movie,
        5: stats,
        6: random_movie_and_rating,
        7: search_movie,
        8: movies_sorted_by_rating,
        9: create_rating_histogram
    }
# Menu is supposed to be displayed all the time so we are using a while Loop to do that
    while True:
        display_menu()
        try:
            choice = int(input("Enter choice (0-9): "))
            if choice in menu_option_choice:
                if choice == 0:
                    exit_program(movies)
                    break
                menu_option_choice[choice](movies)
            else:
                print("Invalid choice. Please enter a number between 0 and 9.")

        except ValueError:
            print(f"{Fore.RED}Please enter a valid number.{Fore.RESET}")

        if input("Do you want to continue? (y/n): ").lower() != 'y': # Asking User if he want´s to continue giving input after every command
            break

if __name__ == "__main__":
    main()