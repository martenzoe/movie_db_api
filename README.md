# Python Movie Database Application

## Overview

This application is a movie database management system that allows users to manage a collection of movies. Users can add, delete, update, and view movie information, as well as perform various analyses on the movie data.

## Features

- List all movies in the database
- Add new movies with title, year, and rating
- Delete existing movies
- Update movie ratings
- Display statistics about the movies
- Randomly select a movie from the database
- Search for movies using partial name matching
- Sort movies by rating
- Create and save a histogram of movie ratings

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   
2. Ensure you have Python 3 installed on your machine.
3. Install the required packages:
pip install colorama matplotlib thefuzz


Error Handling
The application includes robust error handling to manage invalid user inputs effectively. Here are some key aspects:
Input Validation:
When adding or updating a movie, the application checks that the title is not empty and that the rating is within the range of 0 to 10.
The release year must be between 1800 and 2100.

Try-Except Blocks:
The application uses try-except blocks to catch ValueError exceptions when converting user input to numbers (for rating and year). This prevents crashes due to invalid input types.

User Feedback:
If an invalid input is detected (e.g., empty title or out-of-range values), appropriate error messages are displayed to guide the user in correcting their input.
Example of Error Handling in Code
Here’s an example of how error handling is implemented when adding a movie:

while True:
    try:
        rating = float(input(f"{Fore.GREEN}Enter movie rating (0-10):{Fore.RESET} "))
        year = int(input(f"{Fore.GREEN}Enter release year (1800-2100):{Fore.RESET} "))
        if 0 <= rating <= 10 and 1800 <= year <= 2100:
            movie_storage.add_movie(title, year, rating)
            print(f"'{title}' ({year}) has been added with a rating of {rating}")
            return
        else:
            print(f"{Fore.RED}Invalid rating or year. Please try again.{Fore.RESET}")
    except ValueError:
        print(f"{Fore.RED}Please enter valid numbers for rating and year.{Fore.RESET}")

Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.
Author
Marten Zöllner
License
This project is licensed under the MIT License 