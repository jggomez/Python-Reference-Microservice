from abc import ABC
from abc import abstractmethod


class UseCase(ABC):
    """
    The UseCase interface declares a method for executing a usecase.
    """

    @abstractmethod
    def run(self, params=None):
        pass  # pragma: no coverColo
