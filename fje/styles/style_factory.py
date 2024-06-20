# fje/styles/style_factory.py
from styles import *

class StyleFactory:
    @staticmethod
    def get_style(style_type):
        return globals()[style_type]
