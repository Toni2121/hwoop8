from .number_check_strategy import NumberCheckStrategy


class DefaultCase(NumberCheckStrategy):
    def check(self, number):
        return True

    def get_name(self):
        return "Other case"
