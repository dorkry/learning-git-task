# filmy i seriale
class Movie:
    def __init__(self, title, year, movie_type):
        self.title = title
        self.year = year
        self.movie_type = movie_type
        self.plays = 0

    def play(self):
        self.plays += 1
        return
    
    def __str__(self):
        return f'{self.title} ({self.year})'

class Series(Movie):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f'{self.title} S{self.season}E{self.episode}'

library = []
library.append(Movie("Shrek", "2001", "animated"))
library.append(Movie("Skyfall", "2012", "action"))
library.append(Series("01","02", "The Crown", "2016", "history"))
print(library[0])
print(library[2])

    

    
