# fje/components/components.py
from abc import ABC, abstractmethod


class Component(ABC):
    icon = ""
    name = ""
    level = ""
    is_container = False

    @abstractmethod
    def draw(self, style):
        pass

    @abstractmethod
    def accept(self, visitor):
        pass
