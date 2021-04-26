from typing import Iterable

from dto import House
from strategies import BaseStrategy


class PizzaBot:

    def __init__(self, strategy: BaseStrategy):
        """
        :param strategy: Delivering strategy.
        """
        self._strategy = strategy
        self._x = 0
        self._y = 0
        self._commands: list[str] = []

    def get_delivery_commands(self, houses: Iterable[House]) -> list[str]:
        """
        Returns list of PizzaBot commands required to visit all the houses using given strategy.
        :param houses: List of houses to visit.
        :return: List of commands (e.g. ['N', 'W', 'D', 'D', 'W', 'D'])
        """
        self._reset()

        ordered_houses = self._strategy.get_delivery_order(houses)
        for house in ordered_houses:
            while True:
                if self._x == house.x and self._y == house.y:
                    self._drop()
                    break
                elif self._x < house.x:
                    self._go_east()
                elif self._x > house.x:
                    self._go_west()
                elif self._y < house.y:
                    self._go_north()
                else:
                    self._go_south()

        return self._commands

    def _reset(self):
        self._x = 0
        self._y = 0
        self._commands = []

    def _drop(self):
        self._commands.append('D')

    def _go_east(self):
        self._commands.append('E')
        self._x += 1

    def _go_west(self):
        self._commands.append('W')
        self._x -= 1

    def _go_north(self):
        self._commands.append('N')
        self._y += 1

    def _go_south(self):
        self._commands.append('S')
        self._y -= 1
