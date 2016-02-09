class Video():
    """Video is a generic class to store title, storyline, image and trailer"""

    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url


class Movie(Video):
    """Movie class is inherited from Video. Along w/ Video details, it also store movie duration"""

    def __init__(self, movie_title, movie_storyline, movie_poster_image_url, movie_trailer_youtube_url, movie_duration):
        Video.__init__(self, movie_title, movie_storyline, movie_poster_image_url, movie_trailer_youtube_url)
        self.duration = movie_duration


class TVShow(Video):
    """TVShow class is inherited from Video. Along w/ Video details, it also store show's seasons and no. of episodes"""

    def __init__(self, tvshow_title, tvshow_storyline, tvshow_poster_image_url, tvshow_trailer_youtube_url,
                 tvshow_seasons, tvshow_episodes):
        Video.__init__(self, tvshow_title, tvshow_storyline, tvshow_poster_image_url, tvshow_trailer_youtube_url)
        self.seasons = tvshow_seasons
        self.episodes = tvshow_episodes
