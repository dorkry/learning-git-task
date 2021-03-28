# filmy i seriale
import random

class Movie:
    def __init__(self, title, year, movie_type):
        self.title = title
        self.year = year
        self.movie_type = movie_type
        self.views = 0

    def play(self):
        self.plays += 1
        return
    
    def __str__(self):
        return f'{self.title} ({self.year})'
    
    def __repr__(self):
        return str(self)

class Series(Movie):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f'{self.title} S{self.season:02}E{self.episode:02}'
    
def get_movies(m):
    movie_list = []
    for i in m:
        if not isinstance(i, Series):
            movie_list.append(i)
    return movie_list
    
def get_series(s):
    series_list = []
    for i in s:
        if isinstance(i, Series):
            series_list.append(i)
    return series_list

def search(l, title):
    title_list = []
    for i in l:
        if i.title == title:
            title_list.append(i)
    return title_list

def generate_views(library):
    library[random.randint(0, len(library)-1)].views += random.randint(1, 100)
    return library

def generate10(library):
    for i in range(10):
        library = generate_views(library)
        #sprawdzam
        print("|")
    return library
    
def top_title(library, number):
    library = sorted(library, key = lambda x: x.views, reverse=True)
    return library[:number]

library = [
Movie("Shrek", "2001", "animated"),
Movie("Skyfall", "2012", "action"),
Series(1, 2, "The Crown", "2016", "history"),
Series(11,4, "The Crown", "2020", "history")
]

#sprawdzam
print(library[0])
print(library[3])
print(get_movies(library))
print(get_series(library))
print(search(library, "The Crown"))
library = generate10(library)  
for i in library:
    print(f'{i.title} {i.views}')
print(top_title(library, 3))

    
