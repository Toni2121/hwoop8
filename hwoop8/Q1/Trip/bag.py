from equipment import Equipment


class Bag(Equipment):
    def __init__(self, name):
        self.name = name
        self.contents = []

    def add(self, item):
        self.contents.append(item)

    def get_weight(self):
        return sum(item.get_weight() for item in self.contents)

    def __str__(self):
        return f"{self.name} - {self.get_weight()} kg"
