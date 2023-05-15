import customtkinter as ctk
def toggle_frame():
    global Frame_Vermelho
    if Frame_Vermelho is None:
        Frame_Vermelho = ctk.CTkFrame(program, width=150, height=400, bg_color="red")
        Frame_Vermelho.place(relx=0,y=70)
    else:
        Frame_Vermelho.destroy()
        Frame_Vermelho = None

bg="#2f2f2f"
program = ctk.CTk(fg_color=bg)
program.geometry("800x600")

Frame_Vermelho = None

Nome = ctk.CTkLabel(program,10,10,font=("Bahnschrift",26),text="-\t--\tBarbearia\t--\t-",text_color="#86463d").pack(pady=5)
Separação = ctk.CTkFrame(program,1400,4,fg_color="black").pack(pady=0)

Frame_Opções = ctk.CTkFrame(program,40,40,bg_color="green", cursor="hand2")
Frame_Opções.place(x=0,y=5)
Frame_Opções.bind("<Button-1>", lambda e: toggle_frame())

Frame_Perfil = ctk.CTkFrame(program, width=40, height=40, bg_color="blue").place(relx=1, rely=0.01, anchor="ne")
Nome_Perfil = ctk.CTkLabel(program,text="Nome",text_color="red",font=("Arial",18)).place(relx=1,rely=0.08,anchor="ne")

Agendamento= ctk.CTkLabel(program,font=("Arial",30),text_color="red",text="Agendamento").place(x=150,y=100)
Texto= ctk.CTkLabel(program,font=("Arial",15),text_color="red",text="Texto teste para saber \nate onde vai Teste Teste").place(x=175,y=140)
Calendario = ctk.CTkFrame(program, width=330, height=180, bg_color="blue").place(relx=0.9, rely=0.15, anchor="ne")

Produtos = ctk.CTkFrame(program,200,200,fg_color="red").place(relx=0.5,rely=0.8,anchor="center")

program.mainloop()
