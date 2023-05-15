import customtkinter as ctk

class CustomFrame(ctk.CTkFrame):
    def __init__(self, parent):
        ctk.CTkFrame.__init__(self, parent, height=400, width=600, fg_color="blue")
        
        # Cria um label com texto e fonte personalizados
        self.label = ctk.CTkLabel(self, text="Calendario", font=("Arial", 18), bg_color="gray")
        
        # Configura o posicionamento do label acima do centro do frame
        self.label.place(relx=0.5, rely=0.1, anchor="center")
        
        # Configura as colunas do frame com peso igual para que o botão fique centralizado
        self.columnconfigure((0,1), weight=1)
        
        # Configura as linhas do frame com peso igual
        self.rowconfigure(tuple(range(5)), weight=1)

# Cria a janela principal
root = ctk.CTk()

# Adiciona o frame customizado à janela principal
calendar = CustomFrame(root)
calendar.place(relx=0.2, rely=0.2)

# Cria 35 frames dentro do CustomFrame
for i in range(35):
    if i==31:
        break
    elif i<4:
        continue
    row = i // 7
    col = i % 7
    frame = ctk.CTkFrame(calendar, width=50, height=50, bg_color="white")
    frame.grid(row=row, column=col, padx=5, pady=5)


# Inicia o loop da interface gráfica
root.mainloop()
