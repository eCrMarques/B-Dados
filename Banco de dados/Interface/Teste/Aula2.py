import customtkinter as ctk

janela = ctk.CTk()

janela._set_appearance_mode("Dark")

# Configurando Janela principal
janela.title("App Teste")
janela.geometry("700x400")
janela.maxsize(1000,550)
janela.minsize(500,300)
janela.resizable(False,False)


janela.mainloop()