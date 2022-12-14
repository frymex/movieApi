### MovieAPI — обертка кинопоиска и kinobd для Python. 

------

##### Возможности

- Получение плееров для просмотра фильмов и сериалов
- Извлечение информации через кинопоиск по ID сериала / фильма
- Поиск информации по ключевым слова

##### Методы и примеры

|     Функция      |  Класс   |                           Описание                           |
| :--------------: | :------: | :----------------------------------------------------------: |
|        -         | MovieAPI |    Основной элемент для работы с оберткой: `MovieAPI([])`    |
| get_by_kinopoisk | MovieAPI | Получение плееров для просмотра фильмов и сериалов: `get_by_kinopoisk(<movie_id: int>)` возращает `<type: dict>` |
|  get_info_by_id  | MovieAPI | Извлечение информации через кинопоиск по ID сериала / фильма: `get_info_by_id(<movie_id: int>)` возращает `<type: dict>` |
| search_kinopoisk | MovieAPI | Поиск информации по ключевым слова: `search_kinopoisk(<query: str>)` возращает `<type: api.types.MovieInfo>` |

