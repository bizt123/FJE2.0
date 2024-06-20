# fje/explorer.py
import json
from styles.style_factory import StyleFactory
from icons.icon_family_factory import IconFamilyFactory
from components.container import Container
from components.leaf import Leaf
from visitor.visitor import DrawVisitor


class FunnyJsonExplorer:
    def __init__(self, json_file, style_type, icon_family_type):
        self.json_file = json_file
        self.style = StyleFactory.get_style(style_type)
        self.icon_family = IconFamilyFactory.get_icon_family(icon_family_type)
        self.root = None

    def load(self):
        with open(self.json_file, "r") as file:
            data = json.load(file)
            self.root = Container(
                self.icon_family.get_icon(self.icon_family, False), "", 0
            )
            self.root.level = "root"
            for key, value in data.items():
                self.root.add(self._parse_json(key, value, 1))

    def _parse_json(self, key, data, level):
        if isinstance(data, dict):
            container = Container(
                self.icon_family.get_icon(self.icon_family, False), key, level
            )
            for key_, value in data.items():
                container.add(self._parse_json(key_, value, level + 1))
            return container
        else:
            value = f": {data}" if data is not None else ""
            return Leaf(self.icon_family.get_icon(self.icon_family, True), key + value)

    def show(self):
        if self.root:
            visitor = DrawVisitor(self.style)
            self.root.accept(visitor)
