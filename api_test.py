# Завдання 2:
#
# У Postman надішліть запит GET lists. Отриманий body збережіть у
# файл з назвою list.json і додайте його до вашого проєкту.
#
# Ваше завдання — зчитати файл lists.json, знайти всі об'єкти
# lists і вивести на екран їхні ID та name.

import json

with open('api/get_lists.json', 'r') as json_file:
    data = json.load(json_file)
    for el in data['lists']:
        print(f"Name: {el['name']}\nID: {el['id']}")
