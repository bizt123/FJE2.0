# fje/components/iterator.py
from abc import ABC, abstractmethod


class IIterator(ABC):
    @abstractmethod
    def first(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def is_done(self):
        pass

    @abstractmethod
    def current_item(self):
        pass

    @abstractmethod
    def length(self):
        pass


class ComponentIterator(IIterator):
    def __init__(self, container):
        self._container = container
        self._index = 0

    def first(self):
        return self._container.children[0] if self._container.children else None

    def next(self):
        self._index += 1
        if self._index < self.length():
            return self._container.children[self._index]
        return None

    def is_done(self):
        return self._index >= self.length()

    def current_item(self):
        if self._index < self.length():
            return self._container.children[self._index]
        return None

    def length(self):
        return len(self._container.children)
