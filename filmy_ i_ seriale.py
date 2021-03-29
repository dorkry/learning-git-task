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
    
def get_movies(mov):
    movie_list = [i for i in mov if not isinstance(i, Series)]
    return movie_list
    
def get_series(ser):
    series_list = [i for i in ser if isinstance (i, Series)]
    return series_list

def search(lis2, title):
    title_list = [i for i in lis2 if i.title == title]
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
    
def top_titles(library, number):
    library = sorted(library, key = lambda x: x.views, reverse=True)
    return library[:number]

lib = [
    Movie("Shrek", "2001", "animated"),
    Movie("Skyfall", "2012", "action"),
    Series(1, 2, "The Crown", "2016", "history"),
    Series(11,4, "The Crown", "2020", "history")
]

#sprawdzam
print(lib[0])
print(lib[3])
print(get_movies(lib))
print(get_series(lib))
print(search(lib, "The Crown")) #ten search zwraca liste wszystkich pasujacych tytulow a nie tylko jeden element
lib = generate10(lib)  
for i in lib:
    print(f'{i.title} {i.views}')
print(top_titles(lib, 3))

    
