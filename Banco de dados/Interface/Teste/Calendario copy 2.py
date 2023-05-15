from PIL import Image,ImageTk
import customtkinter as ctk
import datetime as time
mês=time.datetime.now()
primeiroDia=time.datetime(int(mês.strftime("%Y")),int(mês.strftime("%m")),1).strftime("%A")

Horario=["8:00","8:50","9:40","10:30","11:20","14:00","15:50","16:40","17:30","18:20"]
meses={"January":["Janeiro",31],"February":["Fevereiro",28],"March":["Março",31],"April":["Abril",30],"May":["Maio",31],"June":["Junho",30],"July":["Julho",31],"August":["Agosto",31],"September":["Setembro",30],"October":["Outubro",31],"November":["Novembro",30],"December":["Dezembro",31]}

class Frame(ctk.CTkFrame):
    def __init__(self,root):
        super().__init__(root)
        # Janela Principal
        Janela=ctk.CTkScrollableFrame(root,1200,720,scrollbar_fg_color="transparent")
        Janela.place(x=0,y=0)
        self.bg=Image.open("Bg.png")
        self.bg=ImageTk.PhotoImage(self.bg)
        ctk.CTkLabel(Janela,image=self.bg).grid(column=0,row=0)
        
        # Titulo (Barbearia)
        ctk.CTkLabel(Janela,text="< = BARBEARIA = >",bg_color="transparent",text_color="black",font=ctk.CTkFont(weight="bold",size=20,family="Ancient Ad")).grid(column=0, row=0,sticky="nw",padx=210,pady=40)
    
        # Calendario
        bgCalendario=Image.open("Calendario.png")
        bgCalendario = bgCalendario.resize((429, 203), Image.ANTIALIAS)
        bgCalendario=ImageTk.PhotoImage(bgCalendario)
        Calendario=ctk.CTkLabel(Janela,image=bgCalendario,width=400,height=320,bg_color="transparent",text=None)
        Calendario.grid(column=0, row=0,sticky="nw",padx=210,pady=200)
        ctk.CTkLabel(Calendario,bg_color="#cae6f0",text=list(f'{meses[mês.strftime("%B")][0]}'),text_color="#111a25",font=ctk.CTkFont("Bahnschrift",weight="bold",size=23),corner_radius=20).place(relx=0.5,rely=0.05,anchor="center")
        Semana=["D","S","T","Q","Q","S","S"]
        posx=78
        for i,dia in enumerate(Semana):
            ctk.CTkLabel(Calendario,bg_color="#cae6f0",text_color="red",text=dia,font=ctk.CTkFont("Bahnschrift",weight="bold",size=25)).place(y=35,x=posx)
            posx+=40
        
        locY=72
        locX=55
        btn=[]
        semanaComeço={"Sunday":0,"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6}
        locX=locX+(55*semanaComeço[primeiroDia])
        print(locY,semanaComeço[primeiroDia])
        for i in range(int(meses[mês.strftime("%B")][1])):
            print(semanaComeço[primeiroDia])
            if i%(7-semanaComeço[primeiroDia])==0 and i!=0 and i==(7-semanaComeço[primeiroDia]):
                locY+=35
                locX=65
            elif i>(7-semanaComeço[primeiroDia]) and (i+semanaComeço[primeiroDia])%7==0:
                locY+=35
                locX=65

            btn.append(ctk.CTkButton(Calendario,25,25,fg_color="#161f31",bg_color="#161f31",text=str(i+1),font=ctk.CTkFont("Bahnschrift",weight="bold",size=18),corner_radius=12))
            btn[i].place(y=locY,x=locX)
            btn[i].configure(command=lambda index=(locX,locY): (print(index,index)))
            locX+=40

app = ctk.CTk()
app.geometry("720x1200")
app.grid_columnconfigure(0,weight=1)
app.grid_rowconfigure(0,weight=1)


calendario= Frame(app)
calendario.place(x=0,y=0)


app.mainloop()