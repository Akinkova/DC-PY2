from datetime import date

class YandexFoodUser:
    """
    Класс для описания пользователя приложения "Яндекс.Еда".

    Атрибуты:
    name: Имя пользователя
    phone: Номер телефона в формате "+7XXXXXXXXXX"
    birthday: День рождения в формате "DD.MM.YYYY"

    """

    def __init__(self, name: str, phone: str, birthday: str):
        """Инициализация экземпляра класса"""
        self.name = name
        self._phone = phone
        self._birthday = birthday

    @property
    def phone(self) -> str:
        """Печать номера телефона пользователя"""
        return self._phone

    @phone.setter
    def phone(self, phone: str) -> None:
        """
        Проверка формата номера телефона.
        Если данные введены корректно, то номер сохраняется

        """
        if not isinstance(phone, str):
            raise TypeError('Номер должен быть в формате строки')
        if not (phone[:2] == '+7' and len(phone) == 12):
            raise ValueError('Номер должен иметь формат "+7ХХХХХХХХХХ"')
        self._phone = phone


    @property
    def birthday(self) -> str:
        """
        Метод для получения даты рождения.
        Дату рождения нельзя изменить без документального подтверждения

        """
        return self._birthday

    def __str__(self) -> str:
        """Метод, описываюший поведение экземпляра при вызове функции print"""
        return f'Имя пользователя: {self.name}, телефон: {self.phone}'

    def __repr__(self) -> str:
        """Метод, позволяющий получить строку, по которой можно создать копию экземпляра"""
        return f'{self.__class__.__name__}(name={self.name!r}, phone={self._phone!r}, '\
               f'birthday={self._birthday!r})'

    def is_birthday(self) -> bool:
        b = self.birthday.split('.')
        bday = '.'.join([ b[0].replace('0', ''), b[1].replace('0', '') ])
        today = date.today()
        return (bday == f'{today.day}.{today.month}')


class YandexFoodClient(YandexFoodUser):
    """
    Класс для описания клиента сервиса "Яндекс.Еда".

    Атрибуты:
    name: Имя пользователя
    phone: Номер телефона в формате "+7XXXXXXXXXX"
    birthday: День рождения в формате "DD.MM.YYYY"
    restaurant: Ресторан, в котором оформлен заказ
    order: Заказ клиента

    """

    def __init__(self, name: str, phone: str, birthday: str,\
                 restaraunt: str, order: list):
        """Инициализация экземпляра класса"""
        super().__init__(name, phone, birthday)
        self.restaraunt = restaraunt
        self.order = order

    def __str__(self) -> str:
        """
        Метод, описываюший поведение экземпляра при вызове функции print.
        Помимо информации о клиенте указан ресторан, в котором оформлен заказ.
        """
        return f'{super().__str__()}\n' + f'Оформлен заказ из ресторана "{self.restaraunt}"'

    def __repr__(self) -> str:
        """Метод, позволяющий получить строку, по которой можно создать копию экземпляра"""
        return f'{self.__class__.__name__}(name={self.name!r}, phone={self._phone!r}, '\
               f'birthday={self._birthday!r}, restaraunt={self.restaraunt!r}, '\
               f'order={self.order}'


if __name__ == "__main__":

    user_1 = YandexFoodUser('Арсений', '+79990000000', '03.12.1988')
    print(user_1.__repr__())

    client_1 = YandexFoodClient('Андрей', '+79990000001', '12.02.1998', 'Дед Хо', ['Супь', 'Другой супь'])
    print(client_1.__repr__())
    print(client_1.is_birthday())

