import media
import fresh_tomatoes


# Create instances of the movie class.

# Movie 1 - Moana
moana = media.Movie("Moana",
                    "Story of the strong-willed daughter of a"
                    "chief of a Polynesian village",
                    "https://upload.wikimedia.org/wikipedia/en/2/26/Moana_Teaser_Poster.jpg",  # noqa
                    "https://www.youtube.com/watch?v=LKFuXETZUsI")


# Movie 2 - Wonder Woman
wonder_woman = media.Movie("Wonder Woman",
                           "Wonder Woman is a 2017 American superhero film"
                           "based on the DC Comics character of the same name",
                           "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",  # noqa
                           "https://www.youtube.com/watch?v=1Q8fG0TtVAY")


# Movie 3 - Hidden Figures
hidden_figures = media.Movie("Hidden Figures",
                             "Story of African-American women who worked"
                             "at NASA during the space race",
                             "https://upload.wikimedia.org/wikipedia/en/4/4f/The_official_poster_for_the_film_Hidden_Figures%2C_2016.jpg",  # noqa
                             "https://www.youtube.com/watch?v=5wfrDhgUMGI")

# Movie 4 - Star Wars - The Force Awakens
star_wars = media.Movie("Star Wars The Force Awakens",
                        "Follows the character Rey against Kylo Ren"
                        "and the First Order",
                        "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",  # noqa
                        "https://www.youtube.com/watch?v=erLk59H86ww")

# Movie 5 - League of their own
league_own = media.Movie("A League Of Their Own",
                         "A fictionalized account of the real-life All-"
                         "American Girls Professional Baseball League",
                         "https://upload.wikimedia.org/wikipedia/en/5/5f/League_of_their_own_ver2.jpg",  # noqa
                         "https://www.youtube.com/watch?v=UqgBV6kGdjk")

# Movie 6 - Bend It Like Beckham
bend_beckham = media.Movie("Bend It Like Beckham",
                           "Story of an Indian girl in London who loves"
                            "football",
                           "https://upload.wikimedia.org/wikipedia/en/1/1c/Bend_It_Like_Beckham_movie.jpg",  # noqa
                           "https://www.youtube.com/watch?v=3IwGeYMepvM")

# Store the movie objects in a list to be provided to the open_movies_page().
# This in turn is the input to build the HTML file to display the website.

movies = [moana, wonder_woman, hidden_figures, star_wars,
          league_own, bend_beckham]
fresh_tomatoes.open_movies_page(movies)
