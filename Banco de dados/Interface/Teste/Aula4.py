import customtkinter as ctk

janela = ctk.CTk()

# Tema
janela._set_appearance_mode("Dark")

# Configurando Janela principal
janela.title("App Teste")
janela.geometry("700x400")
janela.maxsize(1000,550)
janela.minsize(500,300)
janela.resizable(False,False)

# Multiplas Janelas
def novaTela():
    novaJanela= ctk.CTkToplevel(janela,fg_color="Gray")
    novaJanela.geometry("500x250")
    

btn =ctk.CTkButton(janela,text="Abrir Janela",command=novaTela).place(x=300,y=100)


janela.mainloop()