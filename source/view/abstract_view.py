from abc import ABC, abstractmethod


class AbstractView(ABC):
    """
        La classe abstraite AbstractView.
        Elle dispose deux méthodes abstractes

    """
    @abstractmethod
    def display_info(self):
        pass
    @abstractmethod
    def make_choice(self):
        pass
