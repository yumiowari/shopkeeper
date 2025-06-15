import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class View:
    def __init__(self, controller, root):
        self.__controller = controller

        self.root = tk.Toplevel(root)

        # configura a janela
        self.root.title('Preferências')
        self.root.minsize(400, 300)
        self.root.resizable(False, False)
        #

        ## notebook
        self.__notebook = ttk.Notebook(self.root)

        self.__set_acc = ttk.Frame(self.__notebook)

        # definições de conta
        self.acc_name = tk.StringVar(value = '')
        self.acc_name.trace_add('write', self.verify_acc_name)
        self.__acc_name_entry = tk.Entry(self.__set_acc, textvariable = self.acc_name)
        self.__acc_name_label = tk.Label(self.__set_acc, text = 'Nome de usuário')

        self.acc_psswd = tk.StringVar(value = '')
        self.acc_psswd.trace_add('write', self.verify_acc_psswd)
        self.__acc_psswd_entry = tk.Entry(self.__set_acc, textvariable = self.acc_psswd, show = '*')
        self.__acc_psswd_label = tk.Label(self.__set_acc, text = 'Senha')

        self.acc_psswd_twin = tk.StringVar(value = '')
        self.acc_psswd_twin.trace_add('write', self.verify_acc_psswd_twin)
        self.__acc_psswd_twin_entry = tk.Entry(self.__set_acc, textvariable = self.acc_psswd_twin, show = '*')
        self.__acc_psswd_twin_label = tk.Label(self.__set_acc, text = 'Confirmar senha')

        self.__confirm_btn = tk.Button(self.__set_acc, text = 'Confirmar', command = self.update_acc)

        self.__acc_name_label.pack(padx=10, pady=5)
        self.__acc_name_entry.pack(padx=10)
        self.__acc_psswd_label.pack(padx=10, pady=5)
        self.__acc_psswd_entry.pack(padx=10)
        self.__acc_psswd_twin_label.pack(padx=10, pady=5)
        self.__acc_psswd_twin_entry.pack(padx=10)

        self.__confirm_btn.pack(padx=10, pady=5)
        #

        self.__notebook.add(self.__set_acc, text = 'Conta')

        self.__notebook.pack()
        ##

    # self.acc_name observer
    def verify_acc_name(self, var, index, mode):
        aux = self.acc_name.get()

        if len(aux) > 15:
            aux = aux[:15]

        self.acc_name.set(aux)
    #

    # self.acc_psswd observer
    def verify_acc_psswd(self, var, index, mode):
        aux = self.acc_psswd.get()

        if len(aux) > 15:
            aux = aux[:15]

        self.acc_psswd.set(aux)
    #

    # self.acc_psswd_twin observer
    def verify_acc_psswd_twin(self, var, index, mode):
        aux = self.acc_psswd_twin.get()

        if len(aux) > 15:
            aux = aux[:15]

        self.acc_psswd_twin.set(aux)
    #

    def update_acc(self):
        acc_name = self.acc_name.get()
        acc_psswd = self.acc_psswd.get()
        acc_psswd_twin = self.acc_psswd_twin.get()

        if messagebox.askyesno(title = 'Confirmação', message = 'Deseja atualizar os dados de login no banco de dados?', icon = 'warning'):        
            if acc_name == '' and acc_psswd != '' and acc_psswd_twin != '':
                messagebox.showerror('Falha', 'O nome de usuário precisa ser informado.')
            elif acc_name != '' and acc_psswd == '' and acc_psswd_twin != '':
                messagebox.showerror('Falha', 'A senha precisa ser informada.')
            elif acc_name != '' and acc_psswd != '' and acc_psswd_twin == '':
                messagebox.showerror('Falha', 'A confirmação para a senha precisa ser informada.')
            elif acc_name != '' and acc_psswd == '' and acc_psswd_twin == '':
                messagebox.showerror('Falha', 'A senha e a confirmação para a senha precisam ser informadas.')
            elif acc_name == '' and acc_psswd != '' and acc_psswd_twin == '':
                messagebox.showerror('Falha', 'O nome de usuário e a confirmação para a senha precisam ser informados.')
            elif acc_name == '' and acc_psswd == '' and acc_psswd_twin != '':
                messagebox.showerror('Falha', 'O nome de usuário e a senha precisam ser informados.')
            elif acc_name == '' and acc_psswd == '' and acc_psswd_twin == '':
                messagebox.showerror('Falha', 'As credenciais de login precisam ser informadas.')
            else:
                if acc_psswd != acc_psswd_twin:
                    messagebox.showerror('Falha', 'A senha e a confirmação para a senha precisam ser iguais.')
                else:
                    self.__controller.update_acc(acc_name, acc_psswd)

                    messagebox.showinfo('Sucesso', 'As credenciais de login foram atualizadas.')