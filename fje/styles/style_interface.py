# fje/styles/style_interface.py

from abc import ABC, abstractmethod


class IStyle(ABC):
    @abstractmethod
    def draw(self, container):
        pass

    @abstractmethod
    def change_front(self, front, id, num_children):
        pass
