# fje/main.py
from explorer import FunnyJsonExplorer


def main():
    json_file = "data/sample.json"
    style = "rectangle"
    icon_family = "poker-face"
    icon_family = "DefaultIconFamily"

    fje = FunnyJsonExplorer(json_file, style, icon_family)
    fje.load()
    fje.show()


if __name__ == "__main__":
    json_file = "data/sample.json"
    styles = ["RectangleStyle", "TreeStyle"]
    icon_familys = ["PokerFaceIconFamily", "DefaultIconFamily"]

    for style in styles:
        for icon_family in icon_familys:
            fje = FunnyJsonExplorer(json_file, style, icon_family)
            fje.load()
            fje.show()
