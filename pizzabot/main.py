import argparse

from pizzabot import PizzaBot
from utils.cli import pizzabot_input, strategy


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'houses',
        metavar='H',
        type=pizzabot_input,
        help='PizzaBot`s input. e.g. "5x5(1,2)(4,5)(3,2)"',
    )
    parser.add_argument(
        '--strategy',
        metavar='S',
        type=strategy,
        required=True,
    )
    args = parser.parse_args()
    pizza_bot = PizzaBot(strategy=args.strategy)
    commands = pizza_bot.get_delivery_commands(args.houses)
    print(''.join(commands))


if __name__ == '__main__':
    main()
