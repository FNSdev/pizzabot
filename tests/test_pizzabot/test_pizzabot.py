from pizzabot import PizzaBot
from pizzabot.dto import House
from pizzabot.strategies import BaseStrategy

import pytest


class DummyStrategy(BaseStrategy):

    def get_delivery_order(self, houses):
        return houses


class TestPizzaBot:

    @pytest.mark.parametrize(
        'houses, strategy, expected_commands',
        [
            (
                [House(0, 0)],
                DummyStrategy(),
                ['D'],
            ),
            (
                [House(1, 1), House(1, 1), House(1, 1)],
                DummyStrategy(),
                ['E', 'N', 'D', 'D', 'D'],
            ),
            (
                [House(0, 0), House(1, 1), House(1, 1), House(0, 0), House(2, 2)],
                DummyStrategy(),
                ['D', 'E', 'N', 'D', 'D', 'W', 'S', 'D', 'E', 'E', 'N', 'N', 'D'],
            ),
        ],
    )
    def test_get_delivery_commands(self, houses, strategy, expected_commands):
        pizza_bot = PizzaBot(strategy=strategy)

        assert pizza_bot.get_delivery_commands(houses) == expected_commands

    def test_reset(self):
        pizza_bot = PizzaBot(strategy=DummyStrategy())
        pizza_bot.get_delivery_commands([House(1, 1), House(2, 2)])

        assert pizza_bot._x == 2
        assert pizza_bot._y == 2
        assert pizza_bot._commands == ['E', 'N', 'D', 'E', 'N', 'D']

        pizza_bot._reset()

        assert pizza_bot._x == 0
        assert pizza_bot._y == 0
        assert pizza_bot._commands == []
