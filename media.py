import webbrowser
class Movie():
    """This class stored releted movie information"""
    def __init__(self,movie_title,movie_story_line,movie_poster,movie_trailer):
        self.title = movie_title
        self.storyline = movie_story_line
        self.poster = movie_poster
        self.trailer = movie_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)    
