from abc import ABC, abstractmethod
from typing import Iterable

from dto import House


class BaseStrategy(ABC):

    @abstractmethod
    def get_delivery_order(self, houses: Iterable[House]) -> list[House]:
        pass
