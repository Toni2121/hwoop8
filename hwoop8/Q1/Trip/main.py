from item import Item
from bag import Bag

# Items
bread = Item("Bread", 1)
cheese = Item("Cheese", 0.5)
bamba = Item("Bamba", 0.3)
bisli = Item("Bisli", 0.4)
marshmallow = Item("Marshmallow", 0.2)
water_bottle = Item("Water Bottle", 1)
corn = Item("Corn", 1.2)

# Bags
snacks_bag = Bag("Snacks Bag")
snacks_bag.add(bamba)
snacks_bag.add(bisli)
snacks_bag.add(marshmallow)
snacks_bag.add(water_bottle)

healthy_food_bag = Bag("Healthy Food Bag")
healthy_food_bag.add(bread)
healthy_food_bag.add(cheese)
healthy_food_bag.add(snacks_bag)

main_bag = Bag("Main Bag")
main_bag.add(healthy_food_bag)
main_bag.add(corn)

print(f"Total weight of all equipment: {main_bag.get_weight()} kg")
