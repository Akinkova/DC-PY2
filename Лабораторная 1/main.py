from typing import Union
import doctest


class Cat:
    def __init__(self, cat_name: str, weight: Union[int, float]):
        """
        Создание объекта класса "Котик"

        :param cat_name: Кличка кота
        :param weight: Масса кота, кг

        Пример:
        >>> goose = Cat("Гуся", 4) # инициализация экземпляра класса
        """
        self.cat_name = cat_name
        self.weight = None
        self.init_weight(weight)  # проверка массы в отдельном методе

    def init_weight(self, weight: Union[int, float]) -> None:
        """
        Функция, проверяющая массу котика при инициализации

        :param weight: Масса кота,кг
        :raise TypeError: Если в качестве массы введено не число, то вызываем ошибку
        :raise ValueError: Если масса отрицательная, нулевая или превышает разумное значение, то вызываем ошибку
        """
        if not isinstance(weight, (int, float)):
            raise TypeError("Масса котика должна быть целым числом или десятичной дробью")
        if weight <= 0:
            raise ValueError("Масса может быть только положительным числом")
        if weight > 20:
            raise ValueError("Таких больших котов не бывает")
        self.weight = weight

    def feed_the_cat(self) -> None:
        """
        Специальная функция для кормления кота
        Если у кота нет проблем с лишним весом, то можно смело его кормить

        Пример:
        >>> goose = Cat("Гуся", 4)
        >>> goose.feed_the_cat()
        """
        if (self.weight + 0.1) > 20:
            print("Котику пора на диету!")
        else:
            self.weight += 0.1
        ...

    def pet_the_cat(self) -> None:
        """
        Возможность погладить котика

        Пример:
        >>> goose = Cat("Гуся", 4)
        >>> goose.pet_the_cat()
        """
        ...


class Wallet:
    def __init__(self, cash: Union[int, float], card_balance: Union[int, float]):
        """
        Создание объекта вида "Кошелёк"

        :param cash: Количество наличных в кошельке
        :param card_balance: Количество денег на счету карты. Может быть отрицательным (кредит)

        Пример:
        >>> wallet = Wallet(1000, 5000)
        """
        self.cash = None
        self.init_cash(cash)
        self.card_balance = None
        self.init_card_balance(card_balance)

    def init_cash(self, cash: Union[int, float]) -> None:
        """
        Функция, проверяющая введённое количество наличных

        :raise TypeError: Если введено не число, то вызываем ошибку
        :raise ValueError: Если количество наличных отрицательное, то вызываем ошибку
        """
        if not isinstance(cash, (int, float)):
            raise TypeError("Количество наличных может быть только числом")
        if cash < 0:
            raise ValueError("Не может быть отрицательное количество наличных")
        self.cash = cash

    def init_card_balance(self, card_balance: Union[int, float]) -> None:
        """
        Функция, проверяющая введённое количество денег на счету

        :raise TypeError: Если введено не число, то вызываем ошибку
        """
        if not isinstance(card_balance, (int, float)):
            raise TypeError("Количество денег на счету может быть только числом")
        self.card_balance = card_balance

    def is_there_some_cash(self) -> bool:
        """
        Проверка наличия наличных в кошельке

        :return: Есть ли наличные в кошельке

        Пример:
        >>> wallet = Wallet(0, 5000)
        >>> wallet.is_there_some_cash()
        """
        if self.cash > 0:
            return True

    def get_salary(self, salary: Union[int, float]) -> None:
        """
        Получение зарплаты

        :param salary: Зарплата в рублях

        :raise TypeError: Если введено не число, то вызываем ошибку
        :raise ValueError: Если зарплата - отрицательное число, то вызываем ошибку

        Пример:
        >>> wallet = Wallet(1000, 20000)
        >>> wallet.get_salary(50000)
        """
        ...

    def pay_for_restaurant(self, restaurant_bill:  Union[int, float]) -> None:
        """
        Оплата счёта в ресторане
        Можно дополнить выбором способа оплаты

        :param restaurant_bill: Сумма, указанная в счёте

        :raise TypeError: Если введено не число, то вызываем ошибку
        :raise ValueError: Если сумма - отрицательное число, то вызываем ошибку

        Пример:
        >>> wallet = Wallet(1000, 20000)
        >>> wallet.pay_for_restaurant(3000)
        """
        ...


class Lamp:
    def __init__(self, brand: str, power: Union[int, float], color: str):
        """
        Создание объекта класса "Лампочка"

        :param brand: Производитель
        :param power: Мощность лампы, Вт
        :param color: Цвет лампочки

        Пример:
        >>> led_lamp = Lamp("Osram", 5, "Warm white")
        """
        if not isinstance(brand, str):
            raise TypeError("Название бренда должно быть строкой")
        self.brand = brand

        if not isinstance(power, (int, float)):
            raise TypeError("Мощность лампы должна быть числом")
        if power <= 0:
            raise ValueError("Мощность не может быть нулевой или отрицательной")
        self.power = power

        if not isinstance(color, str):
            raise TypeError("Цвет должен быть строкой")
        self.color = color

    def turn_on_the_lamp(self) -> None:
        """
        Включение лампочки

        Пример:
        >>> led_lamp = Lamp("Yeelight", 10, "Cold white")
        >>> led_lamp.turn_on_the_lamp()
        """
        ...

    def check_the_lamp(self) -> bool:
        """
        Проверка лампы на работоспособность

        :return: Работает ли лампочка

        Пример:
        >>> led_lamp = Lamp("Rexant", 3, "Red")
        >>> led_lamp.check_the_lamp()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
