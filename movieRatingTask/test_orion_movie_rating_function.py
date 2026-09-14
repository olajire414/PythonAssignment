
import unittest

from movie_rating_system import*


class TestMovieRatingSystem(unittest.TestCase):


    def test_add_movie(self):
        result = add_movie(movies, "Koto Aye")

        assertTrue(result)
        

    def test_movie_does_not_exist(self):
        result = movie_exists(movies, "Koto Aye")

        assertFalse(result)

    def test_add_rating(self):
        add_movie(movies, "Koto Aye")

        result = add_rating(movies, "Koto Aye", 5)

        assertEqual(movies["Koto Aye"]["ratings"],[5])

   
    def test_get_average_rating(self):
        add_movie(movies, "Koto Aye")

        add_rating(movies, "Koto Aye", 5)
        add_rating(movies, "Koto Aye", 4)
        add_rating(movies, "Koto Aye", 3)

        result = get_average_rating(movies,"Koto Aye")

        assertEqual(result, 4.0)


    def test_get_all_average_ratings(self):
        add_movie(movies, "Koto Aye")
        add_movie(movies, "Ipadabo Abija")

        add_rating(movies, "Koto Aye", 5)
        add_rating(movies, "Koto Aye", 4)

        add_rating(movies, "Ipadabo Abija", 4)
        add_rating(movies, "Ipadabo Abija", 2)

        result = get_all_average_ratings(movies)

        expected = {"Koto Aye": 4.0,"Ipadabo Abija": 3.0}

        assertEqual(result, expected)

    def test_all_average_ratings_movies(self):
        add_movie(movies, "Koto Aye")
        add_movie(movies, "Ipadabo Abija")

        add_rating(movies, "Koto Aye", 5)

        result = get_all_average_ratings(movies)

        expected = {"Koto Aye": 5.0}

        assertEqual(result, expected)



