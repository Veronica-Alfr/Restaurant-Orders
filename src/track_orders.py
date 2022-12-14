from src.analyze_log import (
    most_request,
    never_request,
    never_went_restaurant,
)


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        return self.orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        return most_request(self.orders, customer)

    def get_never_ordered_per_customer(self, customer):
        return never_request(self.orders, customer)

    def get_days_never_visited_per_customer(self, customer):
        return never_went_restaurant(self.orders, customer)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
