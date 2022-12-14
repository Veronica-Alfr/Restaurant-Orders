import csv
from collections import Counter


def analyze_log(path_to_file):
    restaurant = get_csv(path_to_file)

    result_campaign = f'''{most_request(restaurant)}
{many_times_request(restaurant)}
{never_request(restaurant)}
{never_went_restaurant(restaurant)}'''

    return save_in_txt(result_campaign)


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

    for client, food, day in restaurant:
        if client == 'maria':
            foods_request.append(food)
    # retorna as 3 comidas e o n° de quantas vzs foi pedido em uma dict:
    foods = Counter(foods_request)
    # retorna a comida mais pedida - hamburguer -
    return foods.most_common(1)[0][0]


def many_times_request(restaurant):
    count = 0

    for client, food, day in restaurant:
        if client == 'arnaldo' and food == 'hamburguer':
            count += 1
    return count


def never_request(restaurant):
    all_foods = set()
    joao_foods = set()

    for client, food, day in restaurant:
        all_foods.add(food)
        if client == 'joao':
            joao_foods.add(food)

    return all_foods - joao_foods


def never_went_restaurant(restaurant):
    all_days = set()
    day_in_restaurant = set()

    for client, food, day in restaurant:
        all_days.add(day)
        if client == 'joao':
            day_in_restaurant.add(day)

    return all_days - day_in_restaurant


def save_in_txt(result_campaign):
    with open('data/mkt_campaign.txt', 'w') as campaign:
        campaign.write(result_campaign)
