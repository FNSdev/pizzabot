# PizzaBot

Given a grid (where each point on the grid is one house) and a list of points representing houses in need of pizza delivery, return a list of
instructions for getting Pizzabot to those locations and delivering.

## Requirements

- Python 3.9
- [Optional] make 4.1

## Pizza delivering strategies

Given problem can be reduced into the Travelling Salesman Problem.
Traveling Salesman Problem can be solved using brute force with O(n!) time complexity.

However, it is possible to speed it up using dynamic programming and bitmasks 
(if we need minimize distance travelled).

### Closest neighbour

Forces PizzaBot to visit the closest house from its current position until all the pizza is delivered.
Route might not be the most optimal (in terms of distance travelled).

O(n^2) calculation's time complexity.

### Dynamic programming strategy
Force PizzaBot to visit all the houses in the most optimal order (in terms of distance travelled).
O(n^2 * 2^n) calculation's time complexity. It is also heavily memory-consuming.

## How to use it

### Clone repository
```
git clone https://github.com/FNSdev/pizzabot.git
```

### Install dependencies
```
make install-dev
```

### Run main.py
```
cd pizzabot/
python main.py "5x5(0,0)(1,3)(4,4)(4,2)(4,2)(0,1)(3,2)(2,3)(4,1)" --strategy="dynamic_programming"
```

Valid strategy choices are:
- dynamic_programming
- closest_neighbour

### [Optional] Run tests
```
make test
```

### [Optional] Run mypy
```
make check-typing
```
