
# Задача 1
with open('Recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for i in file:
        r_name = i.strip()
        ing_sum = file.readline()
        ingrs = []
        for p in range(int(ing_sum)):
            recepie = file.readline().strip().split(' | ')
            product, quantity, word = recepie
            ingrs.append({'prod': product, 'quant': quantity, 'meas': word})
        file.readline()
        cook_book[r_name] = ingrs
print(cook_book)
#Задача 2
def get_shop_list_by_dishes(person_count: int, dishes: list):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for cons in cook_book[dish]:
                if cons['prod'] in result:
                    result[cons['prod']]['quant'] += cons['quant'] * person_count
                else:
                    result[cons['prod']] = {'meas': cons['meas'],'quant': (cons['quant'] * person_count)}
        else:
            print('Такого блюда нет в книге')
    print(result)

get_shop_list_by_dishes(2, ['Запеченный картофель', 'Омлет'])






