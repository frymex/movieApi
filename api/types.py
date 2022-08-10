
class TrailersDef:
    def __init__(self, obj: dict):
        self.url: str = obj.get('url')
        self.name: str = obj.get('name')
        self.site: str = obj.get('site')


class Persons:
    def __init__(self, obj: dict):
        self.id = obj.get('id')
        self.name = obj.get('name')
        self.enName = obj.get('enName')
        self.description = obj.get('description')
        self.enProfession = obj.get('enProfession')
        self.photo = obj.get('photo')

    def as_dict(self) -> dict:
        return self.__dict__


class MovieInfo:
    def __init__(self, obj: dict):

        main_data: dict = obj.get('pageProps').get('initialReduxState').get('kinomoreAPI').get('queries')
        getFilmById = None

        for x in main_data.keys():
            getFilmById = x
            break

        data_second: dict = main_data.get(getFilmById)
        movie_data: dict = data_second.get('data')

        self.posterFull: str = movie_data.get('poster').get('url')
        self.posterPreview: str = movie_data.get('poster').get('previewUrl')

        self.rating_kp: float = movie_data.get('rating').get('kp')
        self.rating_imdb: float = movie_data.get('rating').get('imdb')
        self.rating_filmCritics: [float, int] = movie_data.get('rating').get('filmCritics')
        self.rating_russianFilmCritics: [float, int] = movie_data.get('rating').get('russianFilmCritics')
        self.rating_await: [float, int] = movie_data.get('rating').get('await')

        self.votes_kp: float = movie_data.get('votes').get('kp')
        self.votes_imdb: float = movie_data.get('votes').get('imdb')
        self.votes_filmCritics: [float, int] = movie_data.get('votes').get('filmCritics')
        self.votes_russianFilmCritics: [float, int] = movie_data.get('votes').get('russianFilmCritics')
        self.votes_await: [float, int] = movie_data.get('votes').get('await')

        self.videos: list[TrailersDef] = []
        [self.videos.append(TrailersDef(x)) for x in movie_data.get('videos').get('trailers')]

        self.movieId: [int, None] = movie_data.get('id')
        self.movieType: [str, None] = movie_data.get('type')
        self.movieName: [str, None] = movie_data.get('name')
        self.movieDescription: [str, None] = movie_data.get('description')
        self.movieSlogan: [str, None] = movie_data.get('slogan')
        self.movieYear: [int, None] = movie_data.get('year')

        self.movieFacts: list = movie_data.get('facts')
        self.movieGenres: list = movie_data.get('genres')
        self.movieCountries: list = movie_data.get('countries')

        self.persons: list[Persons] = []
        [self.persons.append(Persons(x)) for x in movie_data.get('persons')]

        self.sequelsAndPrequels: list[dict] = movie_data.get('sequelsAndPrequels')

    def as_dict(self) -> dict:
        return self.__dict__












