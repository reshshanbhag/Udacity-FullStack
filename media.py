import webbrowser


# Create a class of type Movie
class Movie():
    # Constructor of the movie class
    def __init__(self, movie_title, movie_storyline,
                 movie_poster_image, movie_trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_trailer_youtube

    # Method to open the trailer url
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
