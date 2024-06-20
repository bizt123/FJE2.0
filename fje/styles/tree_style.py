# fje/styles/tree_style.py
from .style_interface import IStyle


class TreeStyle(IStyle):
    def draw(self, component):
        if component.level == "root":
            component.level = ""
            return
        print(component.level + "─" + component.icon + component.name)

    def change_front(self, prefix, id, num_children):
        prefix_child = ""
        if len(prefix) > 0:
            if prefix[-1] == "├":
                prefix_child = prefix[:-1] + "|" + "  "
            else:
                prefix_child = prefix[:-1] + " " + "  "
        if id + 1 == num_children:
            prefix_child += "└"
        else:
            prefix_child += "├"
        return prefix_child
