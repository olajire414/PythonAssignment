
from datetime import datetime


def add_movie(movies, movie_name):

    movie_name = movie_name.strip()

    if movie_name == "":
        return False

    if movie_name in movies:
        return False

    movies[movie_name] = {
        "date_added": datetime.now(),
        "ratings": []
    }

    return True


def movie_exists(movies, movie_name):
    return movie_name in movies


def add_rating(movies, movie_name, rating):

    if movie_name not in movies:
        return False

    if rating < 1 or rating > 5:
        return False

    movies[movie_name]["ratings"].append(rating)

    return True


def get_average_rating(movies, movie_name):
   
    if movie_name not in movies:
        return None

    ratings = movies[movie_name]["ratings"]

    if len(ratings) == 0:
        return None

    total = sum(ratings)
    average = total / len(ratings)

    return average


def get_all_average_ratings(movies):

    averages = {}

    for movie_name in movies:
        average = get_average_rating(movies, movie_name)

        if average is not None:
            averages[movie_name] = average

    return averages
    
    
    
choice = -1
movies = {}
    
while choice != 4:  
     
    print("=" * 50)
    print("         ORION MOVIE RATING APP")
    print("=" * 50)

    print("\n1. Add a Movie")
    print("2. Rate a Movie")
    print("3. View Average Ratings")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    


    match choice :
        case 1:
            movie_name = input("Enter the movie name: ")

            if add_movie(movies, movie_name):
                print(f"Movie '{movie_name}' added!")
            else:
                print("Movie could not be added.")
                break

        case 2:
            movie_name = input("Enter the movie name: ")

            if not movie_exists(movies, movie_name):
                print("Movie does not exist.")
                

            rating_input = input("Enter your rating (1-5): ")

            if rating_input.isdigit():
                rating = int(rating_input)

                if add_rating(movies, movie_name, rating):
                    print(f"Rating added for '{movie_name}' {rating}")
                else:
                    print("Rating must be between 1 and 5.")
            else:
                print("Please enter a valid number.")
                break

        case 3:
            averages = get_all_average_ratings(movies)

            if len(averages) == 0:
                print("No movie ratings available.")
            else:
                print("\nAverage Ratings:")

                for movie_name in averages:
                    print(f"- {movie_name}: "
                        f"{averages[movie_name]:.2f}"
                    )
            if not movies:
                print("no movies yet")
            else:
                print("Available Movies")
                for movie_name in movies.keys():
                    print( {f"{movie_name}"})
                
                break

        case 4:
            print("Goodbye")
            choice = 4
        

        case _:
            print("Invalid choice")


