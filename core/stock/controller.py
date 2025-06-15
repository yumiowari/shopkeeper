from core.stock.model import Model
from core.stock.view import View

class Controller:
    def __init__(self, root):
        self.__model = Model()
        self.__view = View(self, root)