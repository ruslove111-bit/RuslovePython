if __name__ == "__main__":
    class Animal:
        """Базовый класс животного."""

        def __init__(self, name: str, age: int):
            """
            Создать объект животного.

            :param name: Кличка животного.
            :param age: Возраст животного.
            """
            self.name = name
            self.age = age

        def __str__(self) -> str:
            """
            Вернуть строковое представление объекта для пользователя.

            :return: Строка с основной информацией о животном.
            """
            return f"Животное: {self.name}, возраст: {self.age}"

        def __repr__(self) -> str:
            """
            Вернуть строковое представление объекта для разработчика.

            :return: Строка с названием класса и параметрами объекта.
            """
            return f"{self.__class__.__name__}(name={self.name!r}, age={self.age!r})"

        def make_sound(self) -> str:
            """
            Издать звук.

            :return: Звук животного.
            """
            return "Неизвестный звук"

        def eat(self) -> str:
            """
            Описать процесс приема пищи.

            :return: Сообщение о том, что животное ест.
            """
            return f"{self.name} ест."


    class Dog(Animal):
        """Дочерний класс собаки."""

        def __init__(self, name: str, age: int, breed: str):
            """
            Создать объект собаки.

            :param name: Кличка собаки.
            :param age: Возраст собаки.
            :param breed: Порода собаки.
            """
            super().__init__(name, age)
            self.breed = breed

        def __str__(self) -> str:
            """
            Вернуть строковое представление собаки для пользователя.

            :return: Строка с основной информацией о собаке.
            """
            return f"Собака: {self.name}, возраст: {self.age}, порода: {self.breed}"

        def __repr__(self) -> str:
            """
            Вернуть строковое представление собаки для разработчика.

            :return: Строка с названием класса и параметрами объекта.
            """
            return (
                f"{self.__class__.__name__}(name={self.name!r}, "
                f"age={self.age!r}, breed={self.breed!r})"
            )

        def make_sound(self) -> str:
            """
            Издать звук собаки.

            Метод перегружен, потому что собака издает конкретный звук,
            в отличие от общего базового поведения класса Animal.

            :return: Звук собаки.
            """
            return "Гав!"

        # Метод eat() унаследован без изменений.
    pass
