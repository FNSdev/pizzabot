from pizzabot.dto import House
from pizzabot.strategies import DynamicProgrammingStrategy

import pytest


class TestDynamicProgrammingStrategy:

    @pytest.mark.parametrize(
        'houses, expected_delivery_order',
        [
            (
                [House(0, 0, '1')],
                [House(0, 0, '1')],
            ),
            (
                [
                    House(0, 0, '1'),
                    House(0, 1, '2'),
                    House(0, 2, '3'),
                    House(3, 3, '4'),
                    House(2, 1, '5'),
                    House(1, 4, '6'),
                ],
                [
                    House(0, 0, '1'),
                    House(0, 1, '2'),
                    House(0, 2, '3'),
                    House(1, 4, '6'),
                    House(3, 3, '4'),
                    House(2, 1, '5'),
                ],
            ),
            (
                [
                    House(1, 0, '1'),
                    House(2, 0, '2'),
                    House(3, 0, '3'),
                    House(1, 1, '4'),
                    House(2, 2, '5'),
                    House(0, 0, '6'),
                ],
                [
                    House(0, 0, '6'),
                    House(1, 0, '1'),
                    House(1, 1, '4'),
                    House(2, 2, '5'),
                    House(2, 0, '2'),
                    House(3, 0, '3'),
                ],
            ),
            (
                [
                    House(1, 1, '1'),
                    House(1, 2, '2'),
                    House(1, 3, '3'),
                    House(1, 4, '4'),
                    House(1, 5, '5'),
                    House(3, 1, '6'),
                ],
                [
                    House(1, 1, '1'),
                    House(3, 1, '6'),
                    House(1, 2, '2'),
                    House(1, 3, '3'),
                    House(1, 4, '4'),
                    House(1, 5, '5'),
                ],
            ),
        ],
    )
    def test_get_delivery_order(self, houses, expected_delivery_order):
        self._assert_delivery_order(houses, expected_delivery_order)

    @pytest.mark.parametrize(
        'houses, expected_delivery_order',
        [
            (
                [House(0, 0, '1'), House(0, 0, '2'), House(0, 0, '3')],
                [House(0, 0, '1'), House(0, 0, '2'), House(0, 0, '3')],
            ),
            (
                [
                    House(2, 2, '3'),
                    House(1, 1, '1'),
                    House(2, 2, '4'),
                    House(1, 1, '2'),
                    House(3, 3, '5'),
                ],
                [
                    House(1, 1, '1'),
                    House(1, 1, '2'),
                    House(2, 2, '3'),
                    House(2, 2, '4'),
                    House(3, 3, '5'),
                ],
            ),
        ],
    )
    def test_get_delivery_order_multiple_houses_with_same_coordinates(self, houses, expected_delivery_order):
        self._assert_delivery_order(houses, expected_delivery_order)

    def _assert_delivery_order(self, houses, expected_delivery_order):
        strategy = DynamicProgrammingStrategy()
        delivery_order = strategy.get_delivery_order(houses)

        assert delivery_order == expected_delivery_order
