import os
from pprint import pprint

file_path = os.path.join(os.getcwd(), 'recipes.txt')

with open(file_path, encoding='UTF-8') as file:
    cook_book = {}
    while True:
        dish_name = file.readline().strip()
        if not dish_name:
            break
        else:
            ingredient_quantity = int(file.readline().strip())
            dish_list = []
            cook_book[dish_name] = dish_list
            for ingredient in range(ingredient_quantity):
                dish_dict = {}
                unpacked_dish = file.readline().split("|")
                dish_dict['ingredient_name'] = unpacked_dish[0].strip()
                dish_dict['quantity'] = unpacked_dish[1].strip()
                dish_dict['measure'] = unpacked_dish[2].strip()
                dish_list.append(dish_dict)
            file.readline()
            