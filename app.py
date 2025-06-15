import tkinter as tk
from tkinter import messagebox
import pickle as pkl
import os

from core.controller import Controller as mainCtrl

class Model:
    def __init__(self):
        self.__acc = {
            'name': '',
            'psswd': ''
        }

    def check_login(self, acc_name, acc_psswd):
        if not os.path.exists('data'):
            return False
        else:
            with open('data/acc.pkl', 'rb') as f:
                self.__acc = pkl.load(f)

            if acc_name == self.__acc['name'] and acc_psswd == self.__acc['psswd']:
                return True
            else:
                return False

class View:
    def __init__(self, controller):
        self.__controller = controller

        # faz a janela
        self.root = tk.Tk()
        #

        # configura a janela
        self.root.title('$hopkeeper')
        self.root.minsize(200, 150)
        self.root.resizable(False, False)
        #

        # login
        self.__login = tk.Frame(self.root)

        self.courtesy = tk.Label(self.__login, text='Por favor, insira as credenciais de login.')

        self.acc_name = tk.StringVar(value = '')
        self.acc_name.trace_add('write', self.verify_acc_name)
        self.__acc_name_entry = tk.Entry(self.__login, textvariable = self.acc_name)
        self.__acc_name_label = tk.Label(self.__login, text = 'Nome de usuário')

        self.acc_psswd = tk.StringVar(value = '')
        self.acc_psswd.trace_add('write', self.verify_acc_psswd)
        self.__acc_psswd_entry = tk.Entry(self.__login, textvariable = self.acc_psswd, show = '*')
        self.__acc_psswd_label = tk.Label(self.__login, text = 'Senha')
        
        self.__confirm_btn = tk.Button(self.__login, text = 'Confirmar', command = self.login)

        self.courtesy.pack()

        self.__acc_name_label.pack()
        self.__acc_name_entry.pack()
        self.__acc_psswd_label.pack()
        self.__acc_psswd_entry.pack()

        self.__confirm_btn.pack()

        self.__login.pack()
        #

        # inicia a janela
        self.root.mainloop()
        #

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

    def login(self):
        acc_name = self.acc_name.get()
        acc_psswd = self.acc_psswd.get()

        if acc_name == '' and acc_psswd != '':
            messagebox.showerror('Falha', 'O nome de usuário precisa ser informado.')
        elif acc_name != '' and acc_psswd == '':
            messagebox.showerror('Falha', 'A senha precisa ser informada.')
        elif acc_name == '' and acc_psswd == '':
            messagebox.showerror('Falha', 'As credenciais de login precisam ser informadas.')
        else:
            if(self.__controller.login(acc_name, acc_psswd)):
                messagebox.showinfo('Sucesso', 'Seja bem-vindo(a), ' + acc_name + '.')

                self.root.destroy()

                self.__controller.start_app()
            else:
                if(messagebox.askretrycancel('Falha', 'Credenciais de login inválidas.')):
                    self.acc_name.set('')
                    self.acc_psswd.set('')
                else:
                    self.root.destroy()

class Controller:
    def __init__(self):
        self.__model = Model()
        self.__view = View(self)

    def login(self, acc_name, acc_psswd):
        return self.__model.check_login(acc_name, acc_psswd)
    
    def start_app(self):
        mainController = mainCtrl()
            

def main():
    if not os.path.exists('data/acc.pkl'):
        print("Por favor, insira as credenciais de registro:")
        acc_name = input("Nome de usuário: ")
        password = input("Senha: ")

        acc = {'name': acc_name, 'psswd': password}

        if not os.path.exists('data'):
            os.makedirs('data')

        with open('data/acc.pkl', 'wb') as f:
            pkl.dump(acc, f)

    controller = Controller()

main()