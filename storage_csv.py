import csv
from istorage import IStorage

class StorageCsv(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def list_movies(self):
        movies = {}
        try:
            with open(self.file_path, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    movies[row['title']] = {
                        'rating': float(row['rating']),
                        'year': int(row['year'])
                    }
        except FileNotFoundError:
            pass
        return movies

    def add_movie(self, title, year, rating, poster):
        movies = self.list_movies()
        movies[title] = {'year': year, 'rating': rating}
        self._save_movies(movies)

    def delete_movie(self, title):
        movies = self.list_movies()
        if title in movies:
            del movies[title]
            self._save_movies(movies)
            return True
        return False

    def update_movie(self, title, rating):
        movies = self.list_movies()
        if title in movies:
            movies[title]['rating'] = rating
            self._save_movies(movies)
            return True
        return False

    def _save_movies(self, movies):
        with open(self.file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['title', 'rating', 'year'])
            writer.writeheader()
            for title, data in movies.items():
                writer.writerow({
                    'title': title,
                    'rating': data['rating'],
                    'year': data['year']
                })
