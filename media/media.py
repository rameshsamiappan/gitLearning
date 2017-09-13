import webbrowser

class Movie():
    def __init__(self, movie_title, story_line, poster_url, trailor_url):
        self.movie_name = movie_title
        self.story_line = story_line
        self.poster_url = poster_url
        self.trailor_url = trailor_url

    def play_trailor(self):
        webbrowser.open(self.trailor_url)
    
