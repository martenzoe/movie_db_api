import unittest
import os
from movie_storage import add_movie, get_movies, delete_movie


class TestMovieStorage(unittest.TestCase):

    def test_add_movie(self):
        result = add_movie("Inception", 2010, 8.8)
        self.assertTrue(result)  # Sollte True zurückgeben
        movies = get_movies()
        self.assertIn("Inception", movies)
        self.assertEqual(movies["Inception"]["year"], 2010)
        self.assertEqual(movies["Inception"]["rating"], 8.8)

    def test_add_duplicate_movie(self):
        add_movie("Inception", 2010, 8.8)
        result = add_movie("Inception", 2010, 9.0)  # Versuch, einen Duplikat hinzuzufügen
        self.assertTrue(result)  # Sollte True zurückgeben (Film existiert jetzt)

        movies = get_movies()
        self.assertEqual(len(movies), 1)  # Sollte immer noch nur einen Film haben
        self.assertEqual(movies["Inception"]["rating"], 9.0)  # Letzte Bewertung sollte gespeichert werden

    def test_delete_movie(self):
        add_movie("Inception", 2010, 8.8)
        self.assertTrue(delete_movie("Inception"))  # Film sollte erfolgreich gelöscht werden
        movies = get_movies()
        self.assertNotIn("Inception", movies)  # Film sollte nicht mehr vorhanden sein

    def test_delete_nonexistent_movie(self):
        result = delete_movie("Nonexistent Movie")  # Versuch, einen nicht existierenden Film zu löschen
        self.assertFalse(result)  # Sollte False zurückgeben

    def test_get_movies_empty(self):
        movies = get_movies()
        self.assertEqual(movies, {})  # Sollte ein leeres Dictionary zurückgeben

    def test_invalid_rating(self):
        result = add_movie("Inception", 2010, -1)  # Ungültige Bewertung
        self.assertFalse(result)  # Sollte False zurückgeben

if __name__ == '__main__':
    unittest.main()