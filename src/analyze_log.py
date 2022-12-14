import csv
from collections import Counter


def analyze_log(path_to_file):
    restaurant = get_csv(path_to_file)

    most_request(restaurant)  # passar 'maria' como 2° param?
    many_times_request(restaurant)
    # never_request(restaurant)


def get_csv(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        with open(path_to_file) as infos_restaurant:
            restaurant_file = csv.reader(infos_restaurant)
            all_infos = [row for row in restaurant_file]

        return all_infos

    except (FileNotFoundError):
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


def most_request(restaurant):
    foods_request = []

    for client, food in restaurant:
        if client['maria']:
            foods_request.append(food)
    # retorna as 3 comidas e o n° de quantas vzs foi pedido em uma dict:
    foods = Counter(foods_request)
    # retorna a comida mais pedida - hamburguer -
    return foods.most_common(1)[0][0]


def many_times_request(restaurant):
    count = 0

    for client, food in restaurant:
        if client['arnaldo'] and food == 'hamburguer':
            count += 1
    return count


# def never_request(restaurant):
#     all_foods = []
#     foods_never_reequest = set()

#     for client, food in restaurant:
#         all_foods.append(food)
#         if client['joao'] and food != :
#             foods_never_reequest.add(food)
#     return foods_never_reequest
