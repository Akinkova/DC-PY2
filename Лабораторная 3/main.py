class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int = None):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages) -> None:
        if not isinstance(pages, int):
            raise TypeError('Количество страниц должно быть целым числом')
        if pages <= 0:
            raise ValueError('Количество страниц должно быть больше нуля')
        self._pages = pages

    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}. Количество страниц: {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float = None):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration) -> None:
        if not isinstance(duration, (int, float)):
            raise TypeError('Продолжительность записи должна быть числом')
        if duration <= 0:
            raise ValueError('Продолжительность записи должна быть больше нуля')
        self._duration = duration

    def __str__(self):
        return f"Аудиокнига {self.name}. Автор {self.author}. Продолжительность: {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"
