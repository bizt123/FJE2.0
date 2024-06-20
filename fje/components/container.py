# fje/components/container.py
from .component import Component

class Container(Component):
    def __init__(self, icon, name, level):
        self.icon = icon
        self.name = name
        self.is_container = True
        self.level = level
        self.children = []

    def draw(self, style):
        style.draw(style,self)

    def add(self, component):
        self.children.append(component)

    def accept(self, visitor):
        visitor.visit_container(self)

    def create_iterator(self):
        from .iterator import ComponentIterator
        return ComponentIterator(self)
