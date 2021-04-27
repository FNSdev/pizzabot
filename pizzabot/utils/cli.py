import re
from argparse import ArgumentTypeError

from dto import House
from strategies import BaseStrategy, ClosestNeighbourStrategy, DynamicProgrammingStrategy

INPUT_PATTERN = re.compile(r'^(0|[1-9][0-9]*)x(0|[1-9][0-9]*)(\((0|[1-9][0-9]*),(0|[1-9][0-9]*)\))+$')
HOUSE_COORDINATES_PATTERN = re.compile(r'(0|[1-9][0-9]*),(0|[1-9][0-9]*)')

STRATEGY_NAME_TO_CLASS_MAPPING = {
    'closest_neighbour': ClosestNeighbourStrategy,
    'dynamic_programming': DynamicProgrammingStrategy,
}


def pizzabot_input(value: str) -> list[House]:
    match = INPUT_PATTERN.match(value)
    if not match:
        raise ArgumentTypeError('Invalid PizzaBot input format. See --help for reference.')

    max_x = int(match.groups()[0])
    max_y = int(match.groups()[1])

    houses = []
    for house_match in HOUSE_COORDINATES_PATTERN.finditer(value):
        x, y = int(house_match.groups()[0]), int(house_match.groups()[1])
        if x > max_x or y > max_y:
            raise ArgumentTypeError(f'House coordinates ({x}x{y}) do not belong to the grid.')

        houses.append(House(x, y))

    return houses


def strategy(value: str) -> BaseStrategy:
    strategy_class = STRATEGY_NAME_TO_CLASS_MAPPING.get(value)
    if not strategy_class:
        raise ArgumentTypeError(f'Strategy {value} is not implemented')

    return strategy_class()  # type: ignore
