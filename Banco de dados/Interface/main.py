import customtkinter as ctk


def opções():
    global opção
    if opção is None:
        opção=ctk.CTkFrame(program,120,300,bg_color="red")
        opção.place(relx=0,y=65)
    else:
        opção.destroy()
        opção=None

bg="#2f2f2f"
program = ctk.CTk(fg_color=bg)
program.geometry("900x600")
program.minsize(900,600)

opção=None

Nome = ctk.CTkLabel(program,10,10,font=("Bahnschrift",26),text="-\t--\tBarbearia\t--\t-",text_color="#86463d").pack(pady=5)
Separação = ctk.CTkFrame(program,1400,4,fg_color="black").pack(pady=0)

Frame_Opções=ctk.CTkFrame(program,40,40,bg_color="red",cursor="hand2")
Frame_Opções.place(x=0,y=5)
Frame_Opções.bind("<Button-1>", lambda e: opções())

Frame_Perfil = ctk.CTkFrame(program, width=40, height=40, bg_color="blue").place(relx=1, rely=0.01, anchor="ne")
Nome_Perfil = ctk.CTkLabel(program,text="Nome",text_color="red",font=("Arial",18)).place(relx=1,rely=0.08,anchor="ne")


Agendamento= ctk.CTkLabel(program,font=("Arial",30),text_color="red",text="Agendamento").place(x=150,y=100)
Texto= ctk.CTkLabel(program,font=("Arial",15),text_color="red",text="Texto teste para saber \nate onde vai Teste Teste").place(x=175,y=140)
Calendario = ctk.CTkFrame(program, width=330, height=180, bg_color="blue").place(relx=0.9, rely=0.15, anchor="ne")


texto = ctk.CTkLabel(program,text="Produtos", font=("Arial", 26),text_color="green")
texto.place(relx=0.5, y=350, anchor="center")

localx=0.195
localy=380
for i in range(6):
    if i%3==0 and i!=0:
        localx=0.195
        localy=600
    Produtos=ctk.CTkFrame(program,150,150,fg_color="Purple").place(relx=localx,y=localy)
    localx+=0.25
    
program.mainloop()
