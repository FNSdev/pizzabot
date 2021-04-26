from typing import Iterable

from .base import BaseStrategy
from dto import House


class ClosestNeighbourStrategy(BaseStrategy):
    """
    Force PizzaBot to visit the closest house from the it's current position until all the pizza is delivered.
    Route might not be the most optimal (in terms of distance travelled).
    O(n^2) calculation's time complexity.
    """

    def get_delivery_order(self, houses: Iterable[House]) -> list[House]:
        pizza_bot_x = 0
        pizza_bot_y = 0
        not_visited_houses = {house: None for house in houses}
        ordered_houses: list[House] = []

        while len(not_visited_houses):
            costs = {}
            for house in not_visited_houses:
                cost = abs(pizza_bot_x - house.x) + abs(pizza_bot_y - house.y)
                costs[cost] = house  # it's okay to override if cost is the same

            closest_house = costs[min(costs)]
            pizza_bot_x = closest_house.x
            pizza_bot_y = closest_house.y
            not_visited_houses.pop(closest_house, None)
            ordered_houses.append(closest_house)

        return ordered_houses
