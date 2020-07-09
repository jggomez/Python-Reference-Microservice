from abc import ABC, abstractmethod


class UseCase(ABC):
    """
    The UseCase interface declares a method for executing a usecase.
    """

    @abstractmethod
    def run(self, params=None):
        pass # pragma: no coverColo
