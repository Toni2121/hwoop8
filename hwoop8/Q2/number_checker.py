class NumberChecker:
    def __init__(self, strategies):
        self.strategies = strategies

    def run_check(self, number):
        for strategy in self.strategies:
            if strategy.check(number):
                return strategy.get_name()
        return "No Match"
