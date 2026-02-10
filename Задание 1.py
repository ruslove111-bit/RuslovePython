# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from abc import ABC, abstractmethod

class UserAccount(ABC):
    def __init__(self, username: str, age: int):
        """
        Абстрактный класс пользовательского аккаунта

        :param username: Имя пользователя
        :param age: Возраст пользователя

        >>> acc = UserAccount("alex", 20)
        """
        if not isinstance(username, str):
            raise TypeError("Имя пользователя должно быть строкой")
        if not username:
            raise ValueError("Имя пользователя не может быть пустым")
        self.username = username

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть целым числом")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self.age = age

    @abstractmethod
    def login(self) -> bool:
        """
        Авторизация пользователя

        :return: Успешна ли авторизация

        >>> True
        """
        ...

    @abstractmethod
    def logout(self) -> None:
        """
        Выход пользователя из системы

        >>> None
        """
        ...

class FileStorage(ABC):
    def __init__(self, capacity_gb: float, used_gb: float):
        """
        Абстрактное файловое хранилище

        :param capacity_gb: Общий объём хранилища
        :param used_gb: Используемый объём

        >>> storage = FileStorage(100, 10)
        """
        if capacity_gb <= 0:
            raise ValueError("Объём хранилища должен быть положительным")
        self.capacity_gb = capacity_gb

        if used_gb < 0:
            raise ValueError("Используемый объём не может быть отрицательным")
        self.used_gb = used_gb

    @abstractmethod
    def upload_file(self, size_gb: float) -> None:
        """
        Загрузка файла в хранилище

        :param size_gb: Размер файла

        >>> None
        """
        ...

    @abstractmethod
    def delete_file(self, size_gb: float) -> None:
        """
        Удаление файла из хранилища

        :param size_gb: Размер файла

        >>> None
        """
        ...

class OnlineService(ABC):
    def __init__(self, service_name: str, is_available: bool):
        """
        Абстрактный онлайн-сервис

        :param service_name: Название сервиса
        :param is_available: Доступен ли сервис

        >>> service = OnlineService("Chat", True)
        """
        if not service_name:
            raise ValueError("Название сервиса не может быть пустым")
        self.service_name = service_name

        if not isinstance(is_available, bool):
            raise TypeError("Доступность должна быть bool")
        self.is_available = is_available

    @abstractmethod
    def start_service(self) -> None:
        """
        Запуск сервиса

        >>> None
        """
        ...

    @abstractmethod
    def stop_service(self) -> None:
        """
        Остановка сервиса

        >>> None
        """
        ...

if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest

