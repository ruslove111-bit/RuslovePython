class Book:
    """Базовый класс книги."""
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Бумажная книга."""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("pages должно быть целым числом (int)")
        if value <= 0:
            raise ValueError("pages должно быть положительным числом")
        self._pages = value

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}. Страниц: {self.pages}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """Аудиокнига."""
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # через property setter с проверками

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value: float) -> None:
        if not isinstance(value, float):
            raise TypeError("duration должно быть числом с плавающей запятой (float)")
        if value <= 0:
            raise ValueError("duration должно быть положительным числом")
        self._duration = value

    def __str__(self) -> str:
        # Переопределяем, чтобы показать duration
        return f"Книга {self.name}. Автор {self.author}. Длительность: {self.duration}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"