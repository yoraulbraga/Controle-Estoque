import customtkinter
import tkinter as tk

app = customtkinter.CTk()
app.title("Controle de Estoque")
app.geometry("400x170")
app.resizable(False, False)

def entrada_produto():
    app.withdraw()  # Esconde a janela principal
    new_window = customtkinter.CTkToplevel()
    new_window.title("Entrada de Produto")
    new_window.geometry("400x250")
    new_window.resizable(False, False)

    text_nome = customtkinter.CTkLabel(master=new_window, text="Nome do Produto", font=("Roboto", 18))
    text_nome.pack(padx=0, pady=0)
    entry_add_product = customtkinter.CTkEntry(new_window, width=220)
    entry_add_product.pack(padx=0, pady=8)
    text_quant = customtkinter.CTkLabel(master=new_window, text="Quantidade", font=("Roboto", 18))
    text_quant.pack(padx=0, pady=0)
    entry_quant = customtkinter.CTkEntry(new_window, width=120)
    entry_quant.pack(padx=0, pady=8)

    button_salvar = customtkinter.CTkButton(master=new_window, text="Salvar", width=80)
    button_salvar.pack(padx=0, pady=9)

    def voltar_para_principal():
        new_window.withdraw()  # Esconde a janela de entrada
        app.deiconify()  # Mostra a janela principal

    # Adicione um botão para voltar à janela principal em uma posição diferente
    button_voltar = customtkinter.CTkButton(master=new_window, text="Voltar", width=80, command=voltar_para_principal)
    button_voltar.place(x=50, y=209)  # Ajuste as coordenadas x e y conforme necessário

def saida_produto():
    app.withdraw()  # Esconde a janela principal
    new_window = customtkinter.CTkToplevel()
    new_window.title("Saída de Produto")
    new_window.geometry("200x200")
    new_window.resizable(False, False)

    def voltar_para_principal():
        new_window.withdraw()  # Esconde a janela de saída
        app.deiconify()  # Mostra a janela principal

    # Adicione um botão para voltar à janela principal em uma posição diferente
    button_voltar = customtkinter.CTkButton(master=new_window, text="Voltar", command=voltar_para_principal)
    button_voltar.place(x=10, y=10)  # Ajuste as coordenadas x e y conforme necessário


# Estrutura tela principal

title_label1 = customtkinter.CTkLabel(master=app, text="Controle de Estoque", font=("Roboto", 20))
title_label1.pack(padx=0, pady=3)

button_app_entrada = customtkinter.CTkButton(master=app, text="Entrada de Produto", command=entrada_produto)
button_app_entrada.pack(padx=0, pady=5)

button_app_saida = customtkinter.CTkButton(master=app, text="Saída de Produto", command=saida_produto)
button_app_saida.pack(padx=0, pady=5)

button_app_mostrar = customtkinter.CTkButton(master=app, text="Estoque")
button_app_mostrar.pack(padx=0, pady=5)

creditos = customtkinter.CTkLabel(master=app, text="Desenvolvido por Raul Braga", text_color="red", font=("Roboto", 10))
creditos.pack(padx=0, pady=5)

app.mainloop()
