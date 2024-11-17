import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import main

class TestMovieDatabase(unittest.TestCase):

    @patch('builtins.input', side_effect=['', 'Test Movie', '8.5', '2020', 'n'])
    @patch('movie_storage.add_movie')
    def test_add_movie(self, mock_add_movie, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main.add_movie()
        self.assertTrue(mock_add_movie.called)
        self.assertIn("'Test Movie' (2020) has been added with a rating of 8.5", fake_out.getvalue())

    @patch('builtins.input', side_effect=['', 'Existing Movie', 'n', 'n'])
    @patch('movie_storage.delete_movie', return_value=True)
    def test_delete_movie(self, mock_delete_movie, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main.delete_movie()
        self.assertTrue(mock_delete_movie.called)
        self.assertIn("'Existing Movie' has been deleted from the movie list.", fake_out.getvalue())

    @patch('builtins.input', side_effect=['', 'Existing Movie', '9.0', 'n'])
    @patch('movie_storage.update_movie')
    @patch('movie_storage.get_movies', return_value={'Existing Movie': {'year': 2020, 'rating': 8.0}})
    def test_update_movie(self, mock_get_movies, mock_update_movie, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main.update_movie()
        self.assertTrue(mock_update_movie.called)
        self.assertIn("'Existing Movie' has been updated with a new rating of 9.0", fake_out.getvalue())

    @patch('movie_storage.get_movies', return_value={
        'Movie1': {'year': 2020, 'rating': 8.5},
        'Movie2': {'year': 2019, 'rating': 7.0}
    })
    def test_stats(self, mock_get_movies):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main.stats()
        output = fake_out.getvalue()
        self.assertIn("Number of movies: 2", output)
        self.assertIn("Average rating: 7.75", output)
        self.assertIn("Best movie(s):", output)
        self.assertIn("Worst movie(s):", output)

    @patch('builtins.input', side_effect=['part', 'n'])
    @patch('movie_storage.get_movies', return_value={
        'Partial Match': {'year': 2020, 'rating': 8.5},
        'No Match': {'year': 2019, 'rating': 7.0}
    })
    def test_search_movie(self, mock_get_movies, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main.search_movie()
        output = fake_out.getvalue()
        self.assertTrue("Partial Match" in output or "No movies found matching or similar to your search." in output)

    @patch('movie_storage.get_movies', return_value={
        'Movie1': {'year': 2020, 'rating': 8.5},
        'Movie2': {'year': 2019, 'rating': 7.0}
    })
    def test_movies_sorted_by_rating(self, mock_get_movies):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main.movies_sorted_by_rating()
        output = fake_out.getvalue()
        self.assertIn("Movie1", output)
        self.assertIn("Movie2", output)
        self.assertTrue(output.index("Movie1") < output.index("Movie2"))

    def test_exit_program(self):
        self.assertTrue(main.exit_program())

if __name__ == '__main__':
    unittest.main()