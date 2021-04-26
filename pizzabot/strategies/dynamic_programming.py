from typing import Iterable

from .base import BaseStrategy
from dto import House

INFINITY = 1e12


class DynamicProgrammingStrategy(BaseStrategy):
    """
    Force PizzaBot to visit all the houses in the most optimal order (in terms of distance travelled).
    O(n^2 * 2^n) calculation's time complexity.
    """

    def get_delivery_order(self, houses: Iterable[House]) -> list[House]:
        unique_coordinates_set = set((house.x, house.y) for house in houses)
        unique_coordinates_set.add((0, 0))  # include starting coordinates
        unique_coordinates = tuple(unique_coordinates_set)  # preserve ordering

        n = len(unique_coordinates)

        distances = [[INFINITY for _ in range(n)] for _ in range(n)]
        for i, pair in enumerate(unique_coordinates):
            for j, other_pair in enumerate(unique_coordinates):
                if i == j:
                    continue

                distances[i][j] = abs(pair[0] - other_pair[0]) + abs(pair[1] - other_pair[1])

        dp = [[INFINITY for _ in range(n)] for _ in range(2 ** n)]

        initial_position_index = unique_coordinates.index((0, 0))
        dp[2 ** initial_position_index][initial_position_index] = 0

        # dp[mask][i] - length of minimal path from (0, 0) to house with index i (in unique_coordinates), if robot
        #               has visited all the houses in the mask.
        #
        # each mask's bit tells us whether the robot has visited house with index == bit
        for mask in range(1, 2 ** n):
            for i in range(n):
                if dp[mask][i] == INFINITY:
                    continue

                for j in range(n):
                    # check if house with index = j is not in the mask (not visited)
                    if (mask & (2 ** j)) == 0:
                        cost = distances[i][j]
                        mask_j = mask ^ (2 ** j)  # make bit j in mask = 1
                        dp[mask_j][j] = min(dp[mask_j][j], dp[mask][i] + cost)  # try to optimize route's length

        # Restore path going backwards
        current_mask = 2 ** n - 1
        last_house_index = 0
        answer = INFINITY
        for i, e in enumerate(dp[current_mask]):
            if answer > e:
                answer = e
                last_house_index = i

        route = [last_house_index]
        while current_mask != 2 ** initial_position_index:
            # Find house where robot came from
            for i in range(n):
                cost = dp[current_mask ^ (2 ** last_house_index)][i] + distances[i][last_house_index]
                if dp[current_mask][last_house_index] == cost:
                    route.append(i)
                    current_mask ^= 2 ** last_house_index
                    last_house_index = i
                    break

        ordered_houses = []
        for index in reversed(route):
            coordinates = unique_coordinates[index]
            for house in houses:
                if coordinates == (house.x, house.y):
                    # we might have multiple houses with same coordinates, so there is no need to break
                    ordered_houses.append(house)

        return ordered_houses
