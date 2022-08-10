from typing import Union

import requests
from . import types as ttypes


class MovieAPI:
    def __init__(self, services: list):
        self.services = ','.join(_ for _ in services) if services != []\
            else 'kodik,collaps,bazon,alloha,lookbase,hdvb,videocdn,iframe,pleer,ustore,cdnmovies,kholobok,kinotochka,trailer,vk,ext,nf'
        self.session = requests.Session()

    def get_by_kinopoisk(self, movie_id: int) -> dict:

        headers = {
            'authority': 'kinobd.ru',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'dnt': '1',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        }

        data = {
            'kinopoisk': str(movie_id),
            'bg': '#000',
            'resize': '1',
            'player': self.services,
            'button': 'videocdn: {Q} {T}, hdvb: {Q} {T}, bazon: {Q} {T}, ustore: {Q} {T}, alloha: {Q} {T}, kodik: {Q} {T}, iframe: {Q} {T}, collaps: {Q} {T}, kinotochka: {Q} {T}, cdnmovies: {Q} {T}',
            'button_limit': '5',
            'button_size': '1',
            'separator': ',',
        }

        response = requests.post('https://kinobd.ru/playerdata?c690', data=data, headers=headers)
        return response.json()

    def search_kinopoisk(self, query: str, limit: int = 3) -> Union[list, dict]:

        headers = {
            'authority': 'graphql.kinopoisk.ru',
            'accept': '*/*',
            'accept-language': 'ru,en;q=0.9',
            'dnt': '1',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'service-id': '25',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        }

        params = {
            'operationName': 'SuggestSearch',
        }

        json_data = {
            'operationName': 'SuggestSearch',
            'variables': {
                'keyword': query,
                'yandexCityId': 132,
                'limit': limit,
            },
            'query': 'query SuggestSearch($keyword: String!, $yandexCityId: Int, $limit: Int) { suggest(keyword: $keyword) { top(yandexCityId: $yandexCityId, limit: $limit) { topResult { global { ...SuggestMovieItem ...SuggestPersonItem ...SuggestCinemaItem ...SuggestMovieListItem __typename } __typename } movies { movie { ...SuggestMovieItem __typename } __typename } persons { person { ...SuggestPersonItem __typename } __typename } cinemas { cinema { ...SuggestCinemaItem __typename } __typename } movieLists { movieList { ...SuggestMovieListItem __typename } __typename } __typename } __typename } } fragment SuggestMovieItem on Movie { id title { russian original __typename } rating { kinopoisk { isActive value __typename } __typename } poster { avatarsUrl fallbackUrl __typename } viewOption { buttonText isAvailableOnline: isWatchable(filter: {anyDevice: false, anyRegion: false}) purchasabilityStatus subscriptionPurchaseTag type availabilityAnnounce { groupPeriodType announcePromise availabilityDate type __typename } __typename } ... on Film { type productionYear __typename } ... on TvSeries { releaseYears { end start __typename } __typename } ... on TvShow { releaseYears { end start __typename } __typename } ... on MiniSeries { releaseYears { end start __typename } __typename } __typename } fragment SuggestPersonItem on Person { id name originalName birthDate poster { avatarsUrl fallbackUrl __typename } __typename } fragment SuggestCinemaItem on Cinema { id ctitle: title city { id name geoId __typename } __typename } fragment SuggestMovieListItem on MovieListMeta { id cover { avatarsUrl __typename } coverBackground { avatarsUrl __typename } name url description movies(limit: 0) { total __typename } __typename } ',
        }

        response = self.session.post('https://graphql.kinopoisk.ru/graphql/', params=params,
                                 headers=headers, json=json_data)
        if response.ok:
            response_json: dict = response.json()
            if response_json.get('data'):
                if response_json['data'].get('suggest'):
                    d_data: dict = response_json.get('data').get('suggest').get('top')
                    return d_data
                else:
                    return response_json
            else:
                return response_json

        else:
            response_json: dict = response.json()

            return response_json

    def get_info_by_id(self, movie_id: int) -> ttypes.MovieInfo:
        url = 'https://kinomore.vercel.app/_next/data/O-mszkdtIHq9MBA6p5W4a/film/{0}.json?id={0}'.format(movie_id)
        response = self.session.get(url)
        return ttypes.MovieInfo(response.json())
