from .number_check_strategy import NumberCheckStrategy


class DivisibleBy5(NumberCheckStrategy):
    def check(self, number):
        return number % 5 == 0

    def get_name(self):
        return "Divisible by 5"
