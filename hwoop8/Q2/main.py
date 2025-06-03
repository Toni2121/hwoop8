from strategies.between_1_and_10 import Between1And10
from strategies.is_even import IsEven
from strategies.divisible_by_5 import DivisibleBy5
from strategies.default_case import DefaultCase
from number_checker import NumberChecker

strategies = [
    Between1And10(),
    IsEven(),
    DivisibleBy5(),
    DefaultCase()
]

checker = NumberChecker(strategies)

numbers = [3, 17, 12, 100, 23, 121]
results = {n: checker.run_check(n) for n in numbers}

print(results)
