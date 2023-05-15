def Agendar(Botão):
        global Marcado
        global preV
        if preV==False:
                preV=Botão[0]
                print(preV)
                preV.configure(fg_color="blue")
                Botão[0].configure(fg_color="red")
                Concluir = ctk.CTkFrame(frame,20,20,bg_color="#161f31",fg_color="green")
                Concluir.place(x=370,y=10)
                Concluir.bind("<Button-1>", lambda e: (Marcado.append(Botão[1]),button_click(),Botão[0].configure(fg_color="red")))
        else:
             if preV==Botão[0]:
                  Botão[0].configure(fg_color="blue")


def Agendar(Botão):
     global Marcado
     global Concluir , preV
     if preV==Botão[0]:
        if Botão[0].cget("fg_color")=="white" and Botão[0].cget("fg_color")!="red":
            if Botão[0].cget("fg_color")=="white":
                Botão[0].configure(fg_color="blue")
                Concluir.destroy()
                preV=None
            else:
                 Botão[0].configure(fg_color="white")
                 preV=None
                 Agendar((Botão[0],Botão[1]))
     else:
            try:
                 if preV.cget("fg_color")=="white":
                      preV.configure(fg_color="blue")
            except:
                 pass
            Botão[0].configure(fg_color="white")
            Concluir= ctk.CTkFrame(frame,20,20,bg_color="#161f31",fg_color="green")
            Concluir.place(x=370,y=10)
            Concluir.bind("<Button-1>", lambda e: (Marcado.append(Botão[1]),Concluir.destroy(),button_click()))
          
     preV = Botão[0]
     print("fim")