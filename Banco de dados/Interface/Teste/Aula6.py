import customtkinter as ctk

janela = ctk.CTk()

# Tema

# Configurando Janela principal
janela.title("App Teste")
janela.geometry("700x400")
janela.maxsize(1000,550)
janela.minsize(500,300)
janela.resizable(False,False)

# Tabviews (Abas)
tabview= ctk.CTkTabview(janela,400)
tabview.pack()
tabview.add("Nomes")
tabview.add("Idades")
tabview.add("Genero")

tabview.tab("Nomes").grid_columnconfigure(0,weight=1)
tabview.tab("Idades").grid_columnconfigure(0,weight=1)
tabview.tab("Genero").grid_columnconfigure(0,weight=1)

# Adicionando elementos na nossa tab
text = ctk.CTkLabel(tabview.tab("Nomes"),text_color="red",bg_color="transparent",text="Salvador \nEduardo \nAntonia").pack(side="left")
text = ctk.CTkLabel(tabview.tab("Idades"),text_color="red",bg_color="transparent",text="15 \n20 \n30").pack(side="left")

janela.mainloop()