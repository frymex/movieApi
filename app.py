from api.api import MovieAPI

app = MovieAPI([])

kinopoisk_id = 1
query = ''


def get_player() -> dict:
    var = app.get_by_kinopoisk(kinopoisk_id)
    return var


def get_infos() -> dict:
    var = app.get_info_by_id(kinopoisk_id)
    return var.as_dict()


def search_by_query() -> dict:
    var = app.search_kinopoisk(query)
    return var
