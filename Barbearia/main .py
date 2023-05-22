from view.Interface import *


def Alternar():
    JanelaPrincipal.Alternar()
    JanelaSegundaria.Alternar()

app = CTk()
app.geometry("720x1200")
app.grid_columnconfigure(0,weight=1)
app.grid_rowconfigure(0,weight=1)



JanelaPrincipal= Frame(app)
JanelaPrincipal.place(x=0,y=0)
JanelaSegundaria = Frame2(app)


botao_alternar = CTkButton(app, text="Alternar", command=Alternar,fg_color="#660000",text_color="black",font=CTkFont(weight="bold",size=15),border_width=5,border_color="black")
botao_alternar.pack(pady=5)

app.mainloop()