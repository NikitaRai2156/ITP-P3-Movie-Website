#importing webbrowser module
import webbrowser

class Movie():
    """This class provides a way to store movie-related information."""
    #This class provides a way to store movie related information
    #Title
    #Story line
    #Rating
    #Movie Poster
    #Trailer Link
    valid_ratings = ["G", "PG", "PG-13", "R"]
    def __init__(self, movie_title, movie_rating, poster_image, trailer_youtube):
        """This is the initialization function."""
        #initialize instance of the class Movie
        self.title = movie_title
        self.rate = movie_rating
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        """This function shows the trailer of the movie selected."""
        #to show trailer of the movie selected
        webbrowser.open(self.trailer_youtube_url)
