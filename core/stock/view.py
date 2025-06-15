import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class View:
    def __init__(self, controller, root):
        self.__controller = controller

        self.root = tk.Toplevel(root)

        # configura a janela
        self.root.title('Inventário')
        self.root.minsize(400, 300)
        self.root.resizable(False, False)
        #

        ## notebook
        self.__notebook = ttk.Notebook(self.root)

        self.__create = ttk.Frame(self.__notebook)
        self.__confer = ttk.Frame(self.__notebook)
        self.__update = ttk.Frame(self.__notebook)
        self.__delete = ttk.Frame(self.__notebook)

        # adicionar produto
        self.item_name = tk.StringVar(value = '')
        self.item_name.trace_add('write', self.verify_item_name)
        self.__item_name_entry = tk.Entry(self.__create, textvariable = self.item_name)
        self.__item_name_label = tk.Label(self.__create, text = 'Nome do produto')

        self.item_cost = tk.StringVar(value = '0,00')
        self.item_cost.trace_add('write', self.verify_item_cost)
        self.__item_cost_entry = tk.Entry(self.__create, textvariable = self.item_cost)
        self.__item_cost_label = tk.Label(self.__create, text = 'Custo do produto')

        self.item_price = tk.StringVar(value = '0,00')
        self.item_price.trace_add('write', self.verify_item_price)
        self.__item_price_entry = tk.Entry(self.__create, textvariable = self.item_price)
        self.__item_price_label = tk.Label(self.__create, text = 'Preço do produto')

        self.__create_confirm_btn = tk.Button(self.__create, text = 'Confirmar', command = self.create_item)

        self.__item_name_label.pack(padx=10, pady=5)
        self.__item_name_entry.pack(padx=10)
        self.__item_cost_label.pack(padx=10, pady=5)
        self.__item_cost_entry.pack(padx=10)
        self.__item_price_label.pack(padx=10, pady=5)
        self.__item_price_entry.pack(padx=10)

        self.__create_confirm_btn.pack(padx=10, pady=5)
        #

        # consultar produto

        #

        # atualizar produto

        #

        # remover produto

        #

        self.__notebook.add(self.__create, text = 'Adicionar')
        self.__notebook.add(self.__confer, text = 'Consultar')
        self.__notebook.add(self.__update, text = 'Atualizar')
        self.__notebook.add(self.__delete, text = 'Remover')

        self.__notebook.pack()
        ##

    # self.item_name observer
    def verify_item_name(self, var, index, mode):
        aux = self.item_name.get()

        if len(aux) > 30:
            aux = aux[:30]

        self.item_name.set(aux)
    #

    # self.item_cost observer
    def verify_item_cost(self, var, index, mode):
        aux = self.item_cost.get()

        # Remove tudo que não for dígito
        filtered_aux = ''.join(c for c in aux if c.isdigit())

        if filtered_aux:
            value = int(filtered_aux)
            formatted = f'{value / 100:.2f}'.replace('.', ',')
            self.item_cost.set(formatted)
        else:
            self.item_cost.set('')
    #

    # self.item_price observer
    def verify_item_price(self, var, index, mode):
        aux = self.item_price.get()

        # Remove tudo que não for dígito
        filtered_aux = ''.join(c for c in aux if c.isdigit())

        if filtered_aux:
            value = int(filtered_aux)
            formatted = f'{value / 100:.2f}'.replace('.', ',')
            self.item_price.set(formatted)
        else:
            self.item_price.set('')
    #

    def create_item(self):
        pass