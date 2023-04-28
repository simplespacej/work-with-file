with open('recipes.txt', 'rt') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        amount_ingridients = int(file.readline().strip())
        ingridients = []
        for _ in range(amount_ingridients):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            ingridients.append({
                'ingredient_name' : ingredient_name,
                'quantity' : quantity,
                'measure' : measure
            })
        file.readline()
        cook_book[dish_name] = ingridients

def get_shop_list_by_dishes(dishes, person_count):
    order = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = int(ingredient['quantity']) * person_count
            if name in order:
                order[name]['quantity'] += quantity
            else:
                order[name] = {'measure': measure, 'quantity': quantity}
    return order