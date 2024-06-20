# fje/visitor/visitor.py
from abc import ABC, abstractmethod


class IVisitor(ABC):
    @abstractmethod
    def visit_leaf(self, leaf):
        pass

    @abstractmethod
    def visit_container(self, container):
        pass


class DrawVisitor(IVisitor):
    def __init__(self, style):
        self.style = style

    def visit_leaf(self, leaf):
        leaf.draw(self.style)

    def visit_container(self, container):
        container.draw(self.style)
        iterator = container.create_iterator()
        idx = 0
        child = iterator.first()
        while not iterator.is_done():
            child.level = self.style.change_front(
                self.style, container.level, idx, iterator.length()
            )
            child.accept(self)
            idx += 1
            child = iterator.next()
