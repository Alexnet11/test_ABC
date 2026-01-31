from abc import ABC, abstractmethod
from colorama import Fore, Style, init

init(autoreset=True)

class Discount(ABC):

    @abstractmethod
    def apply(self, price):
        pass

    @abstractmethod
    def get_details(self):
        pass


    def is_eligible(self, price):
        return price > 0


class PercentageDiscount(Discount):
    def __init__(self, percent):
        self.percent = percent

    def apply(self, price):
        return price - (price * self.percent / 100)


    def get_details(self):
        return f"Процентная скидка {self.percent}%"


class FixedDiscounter(Discount):
    def __init__(self, fixed):
        self.fixed = fixed

    def is_eligible(self, price):
        return price >= 1000

    def apply(self, price):
        return max(0, price - self.fixed)

    def get_details(self):
        return f"Фиксированная скидка: {self.fixed} руб."


class NoDiscount(Discount):

    def apply(self, price):
        return price

    def get_details(self):
        return "БЕЗ СКИДКИ!"


class SummerDiscount(Discount):
    def __init__(self):
        self.fix_disc = 100
        self.percent = 5


    def is_eligible(self, price):
        return price >= 1000

    def apply(self, price):
        reduction = price - self.fix_disc
        return reduction - (reduction * self.percent/100)

    def get_details(self):
        return f"{Fore.CYAN}Летнее комбо: -100 руб. и ещё - {self.percent}% сверху!"




def process_checkout(price, discount_system: Discount):
    if discount_system.is_eligible(price):
        final_price = discount_system.apply(price)
        detail = discount_system.get_details()
        print(f"{Fore.GREEN}Применён: {detail}")
        print(f"{Fore.BLUE}Итого к оплате: {final_price}")
    else:
        print(f"{Fore.RED} Скидка: {discount_system.get_details()} не доступна для этой суммы ")
    print('-'*20)


if __name__ == "__main__":
    discounts = [
        PercentageDiscount(10),
        FixedDiscounter(500),
        SummerDiscount(),
        NoDiscount()
    ]


    test_price = 1000

    print(f"{Style.BRIGHT} Проверка  корзины для суммы {test_price}")
    print('='*40)

    for d in discounts:
        process_checkout(test_price, d)


























