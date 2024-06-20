# fje/icons/icon_family_factory.py

from icons import *

class IconFamilyFactory:
    @staticmethod
    def get_icon_family(family_type):
        return globals()[family_type]
