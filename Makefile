install-dev:
	pip install -r requirements.dev.txt

test:
	PYTHONPATH=./pizzabot pytest

check-typing:
	mypy -p pizzabot
