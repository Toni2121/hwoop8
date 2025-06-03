from .number_check_strategy import NumberCheckStrategy


class Between1And10(NumberCheckStrategy):
    def check(self, number):
        return 1 <= number <= 10

    def get_name(self):
        return "Number is between 1 and 10"
