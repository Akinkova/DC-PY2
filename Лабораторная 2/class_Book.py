from pydantic import BaseModel

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book

'''Честная реализация с конструктором'''

class Book:
    '''
    Класс, описывающий книгу.

    Атрибуты:
    :id_: идентификатор книги
    :name: Название книги
    :pages: Количество страниц в книге
    '''

    def __init__(self, id_: int, name: str, pages: int):
        '''Инициализация объекта класса Book'''
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        '''Метод, описываюший поведение экземпляра при вызове функции print'''
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        '''
        Метод, позволяющий получить строку,
        по которой можно создать копию экземпляра
        '''

        return f'{self.__class__.__name__}(id_={self.id_}, name={self.name!r}, pages={self.pages})'


'''Реализация с использованием pydantic'''

# class Book(BaseModel):
#     id_: int
#     name: str
#     pages: int
#
#     def __str__(self) -> str:
#         return f'Книга "{self.name}"'


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
