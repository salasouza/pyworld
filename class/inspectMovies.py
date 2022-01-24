class watchedMovies:
    "Descriptor the movies"
    
    def __init__(self, movie=None, genre=None, streaming=None):
        self.m = movie
        self.g = genre
        self.s = streaming

z = watchedMovies('Batman','HQ','HBOmax')

print('Movie:',z.m,'|','Genre:',z.g,'|','Streaming:',z.s)
