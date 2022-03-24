import os

file_path_dish = os.path.join(os.getcwd(), 'recipes.txt')

with open(file_path_dish, encoding='UTF-8') as file:
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


def dish_count(dishes, persons):
    shopping_list = {}
    for dish in cook_book.keys():
        if dish in dishes:
            for purchase in cook_book[dish]:
                name = purchase['ingredient_name']
                measure = purchase['measure']
                number = int(purchase['quantity'])
                if name not in shopping_list:
                    shopping_list[name] = {'measure': measure, 'quantity': number * persons}
                else:
                    shopping_list[name]['quantity'] += number * persons
    return shopping_list


print(dish_count(["Омлет", "Фахитос", "Утка по-пекински", "Запеченный картофель"], 3))