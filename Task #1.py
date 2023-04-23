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
print(cook_book)