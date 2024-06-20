# fje/icons/icon_family_interface.py
from abc import ABC, abstractmethod

class IIconFamily(ABC):
    @abstractmethod
    def get_icon(self, is_leaf):
        pass
