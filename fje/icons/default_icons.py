# fje/icons/poker_face_icons.py
from .icon_family_interface import IIconFamily

class DefaultIconFamily(IIconFamily):
    def get_icon(self, is_leaf):
        return " "
