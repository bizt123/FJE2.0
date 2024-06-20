# fje/components/leaf.py
from .component import Component

class Leaf(Component):
    def __init__(self, icon, name):
        self.icon = icon
        self.name = name
        self.is_container = False

    def draw(self, style):
        style.draw(style,self)

    def accept(self, visitor):
        visitor.visit_leaf(self)
