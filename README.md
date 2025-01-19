# Movie App

## Description
The Movie App is a simple application for managing a movie collection. It allows users to add, delete, update, and view statistics about their collection. The app uses the OMDb API to fetch movie information.

## Purpose
The goal of this project is to create a user-friendly application that makes it easy to manage movies and retrieve information about them. This is especially useful for movie enthusiasts and collectors.

## Requirements
- Python 3.x
- pip (Python Package Installer)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/username/movie-app.git
   cd movie-app

2. Create a virtual environment (optional):
   ```
    python -m venv venv
    source venv/bin/activate  # For macOS/Linux
    venv\Scripts\activate   # For Windows

3. Install dependencies:
   ```
    pip install -r requirements.txt

4. Create a .env file in the root directory and add your OMDb API key:
   ```
    OMDB_API_KEY=your_api_key_here
   
## Usage

1. Start the application:
   ```
    python main.py

2. Select an option from the menu:
   ```
    1: List movies
    2: Add a movie
    3: Delete a movie
    4: Update a movie
    5: View movie statistics
    6: Generate website
    0: Exit
   
## Features
- List Movies: View all movies in your collection.
- Add Movie: Add a new movie to the collection by providing details.
- Delete Movie: Remove a movie from the collection.
- Update Movie: Edit details of an existing movie.
- Statistics: View aggregated statistics, such as the total number of movies.
- Generate Website: Export your collection as a simple website.

## Contributing
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. If you encounter any issues, feel free to report them.