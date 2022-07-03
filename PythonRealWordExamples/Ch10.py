import random

dishwasher = ['plate', 'bowl', 'cup','knife']

for dish in list(dishwasher):
    if not random.randint(0,3):
        print("Out of space")
        break
    else:
        print(f'Putting {dish} into the cabinet..')
        dishwasher.remove(dish)