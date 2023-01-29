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
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name=name, author=author)
        self._pages = pages

    @property
    def pages(self):
        return self.pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("Число страниц должно быть int")
        if new_pages <= 0:
            raise ValueError("Число страниц не может быть отрицательным числом")
        self._pages = new_pages

    # Метод __str__ может быть унаследован из родительского класса,
    # так как он не зависит от того, бумажная она или звуковая

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"
    # Так как в данном методе содержится информация о том, как может быть инициализован экземпляр,
    # то он требует перезагрузки в дочернем классе


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name=name, author=author)
        self._duration = duration

    @property
    def duration(self):
        return self.duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, (int, float)):
            raise TypeError("Продолжительность аудиокниги должна быть int или float")
        if new_duration <= 0:
            raise ValueError("Продолжительность аудиокниги не может быть отрицательным числом")
        self._duration = new_duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"
