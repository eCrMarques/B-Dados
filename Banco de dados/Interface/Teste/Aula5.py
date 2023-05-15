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

# Frame
frame1 = ctk.CTkFrame(master = janela,width=200,height=330,fg_color="teal",border_width=5,corner_radius=10).place(x=10,y=60)

frame2 = ctk.CTkFrame(janela,200,330,fg_color="green",border_width=5,corner_radius=10).place(x=230,y=60)

frame3 = ctk.CTkFrame(janela,200,330,fg_color="purple",border_width=5,corner_radius=10).place(x=450,y=60)



janela.mainloop()