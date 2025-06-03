from .number_check_strategy import NumberCheckStrategy


class IsEven(NumberCheckStrategy):
    def check(self, number):
        return number % 2 == 0

    def get_name(self):
        return "Even number"
