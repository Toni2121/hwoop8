from equipment import Equipment


class Item(Equipment):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def get_weight(self):
        return self.weight

    def __str__(self):
        return f"{self.name} ({self.weight} kg)"
