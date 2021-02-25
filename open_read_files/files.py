import os
from pprint import pprint


def file_to_dict(file_name):
    cook_book = {}
    with open(file_name, 'r', encoding='utf-8') as f:
        x = f.readlines()
        ls = [0, ]
        i = 0
        while i < len(x):
            y = int(x[i+1])
            i += y+3
            ls.append(i)

    with open(file_name, 'r', encoding='utf-8') as f:
        x = f.readlines()
        for i in range(len(ls)-1):
            start = ls[i]
            stop = ls[i+1]
            ingridients_list = []
            ingr_dict = {}
            j = start+2
            k = 0
            while j <= stop-2:
                ingr_dict['ingredient_name'] = x[j].split('|')[0].strip()
                ingr_dict['quantity'] = int(x[j].split('|')[1].strip())
                ingr_dict['measure'] = x[j].split('|')[2].strip()
                ingridients_list.append(ingr_dict)
                ingr_dict = {}
                k += 1
                j += 1

            cook_book[x[start].strip()] = ingridients_list
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    dic = {}
    for dish in dishes:
        if dish in cookbook:
            for ingr in cookbook[dish]:
                if ingr['ingredient_name'] not in dic:
                    dic[(ingr['ingredient_name'])] = {
                        'measure': ingr['measure'], 'quantity': ingr['quantity'] * person_count}
                else:
                    double = dic[(ingr['ingredient_name'])]['quantity']
                    dic[(ingr['ingredient_name'])] = {
                        'measure': ingr['measure'], 'quantity': ingr['quantity'] * person_count + double}
        else:
            print('Ошибка, нет такого блюда в книге!')
    pprint(dic)


cookbook = file_to_dict('files/recipes.txt')
# pprint(cookbook)
# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
get_shop_list_by_dishes(['Фахитос', 'Омлет'], 1)
