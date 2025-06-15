from core.model import Model
from core.view import View

from core.settings.controller import Controller as CtrlSettings
from core.stock.controller import Controller as CtrlStock

class Controller:
    def __init__(self):
        self.__model = Model()
        self.__view = View(self)

    # rotina de encerramento do programa
    def safe_exit(self):
        print('Encerrando aplicação...')
    #

    # inicia a janela de preferências
    def open_settings(self, root):
        self.__ctrlSettings = CtrlSettings(root)
    #

    # inicia a janela de estoque
    def open_stock(self, root):
        self.__ctrlStock = CtrlStock(root)
    #
    #