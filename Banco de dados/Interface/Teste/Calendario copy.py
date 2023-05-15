import customtkinter as ctk
import datetime as time
mês=time.datetime.now()
primeiroDia=time.datetime(int(mês.strftime("%Y")),int(mês.strftime("%m")),1).strftime("%A")

Horario=["8:00","8:50","9:40","10:30","11:20","14:00","15:50","16:40","17:30","18:20"]
meses={"January":["Janeiro",31],"February":["Fevereiro",28],"March":["Março",31],"April":["Abril",30],"May":["Maio",31],"June":["Junho",30],"July":["Julho",31],"August":["Agosto",31],"September":["Setembro",30],"October":["Outubro",31],"November":["Novembro",30],"December":["Dezembro",31]}


def texts(txt):
            print(txt)

class CustomFrame(ctk.CTkFrame):
    def __init__(self, parent):
        ctk.CTkFrame.__init__(self, parent, height=280, width=400, fg_color="#cae6f0",border_width=5,border_color="black",corner_radius=10)
        self.pack(pady=30)
        
        print(self.size.__dict__)
        ctk.CTkLabel(self,bg_color="#cae6f0",text=list(f'{meses[mês.strftime("%B")][0]}'),text_color="#111a25",font=ctk.CTkFont("Bahnschrift",weight="bold",size=23),corner_radius=20).place(x=200,y=20,anchor="center")
        ctk.CTkFrame(self,410,240,bg_color="transparent",fg_color="#161f31",corner_radius=10).place(x=-5,y=60)
        
        Semana=["D","S","T","Q","Q","S","S"]
        posx=30
        for i,dia in enumerate(Semana):
            ctk.CTkLabel(self,bg_color="#cae6f0",text_color="red",text=dia,font=ctk.CTkFont("Bahnschrift",weight="bold",size=18)).place(y=30,x=posx)
            posx+=55
janela=None
Marcado=[]
preV=None
def Agendar(Botão):
        global Marcado
        global preV
        global Concluir
        if Botão[1] in Marcado:
             preV=None
        print("Zero")
        try:
             Concluir.destroy()
        except:
             pass
        if preV==None:
            Botão[0].configure(fg_color="red")
            preV=Botão[0]
            print("Zero")
        else:
             if preV==Botão[0]:
                  Botão[0].configure(fg_color="blue")
                  print("igual")
                  preV=None
                  pass
             else:
                  if preV.cget("fg_color")=="red":
                       if preV.cget("text") not in Marcado:
                            preV.configure(fg_color="blue")
                       Botão[0].configure(fg_color="red")
                       preV=Botão[0]
        if Botão[0].cget("fg_color")=="red" and Botão[1] not in Marcado:
             Concluir= ctk.CTkFrame(frame,20,20,bg_color="#161f31",fg_color="green")
             Concluir.place(x=370,y=10)
             Concluir.bind("<Button-1>", lambda preV=None: (Marcado.append(Botão[1]),Concluir.destroy(),button_click(),))
             

        
            
def button_click(loc=None):
      global janela
      global Marcado
      print(janela)
      print(Marcado)
      if janela == None:
            global preloc
            preloc=loc
            janela=ctk.CTkScrollableFrame(root,150,100,bg_color="purple")
            janela.place(x=(loc[0]+200),y=(loc[1]+30))
            janela.grid_columnconfigure((0,1), weight=1)
            janela.grid_rowconfigure(tuple(range(4)),weight=1)

            coluna=0
            linha=0
            btn=[]
            for i,hora in enumerate(Horario):
                Ativo="blue"

                if hora in Marcado:
                     print("asdas")
                     Ativo="red"
                btn.append(ctk.CTkButton(janela,60,28,text=hora,fg_color=Ativo))
                btn[i].grid(row=linha,column=coluna,pady=10)
                btn[i].configure(command=lambda index=(btn[i],hora): Agendar(index))
                if coluna==1:
                     linha+=1
                     coluna=0  
                else:
                    coluna=1
      else:
            if preloc==loc or loc==None:
                janela.destroy()
                janela.place_forget()
                janela=None
            else:
                 janela.place(x=(loc[0]+200),y=(loc[1]+30))
                 preloc=loc
def loc(s):
    print(s)

root = ctk.CTk()
root.geometry("720x1280")

frame=CustomFrame(root)

locY=72
locX=18
btn=[]
semanaComeço={"Sunday":0,"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6}
locX=locX+(55*semanaComeço[primeiroDia])
print(locY,semanaComeço[primeiroDia])
for i in range(int(meses[mês.strftime("%B")][1])):
    if i%(7-semanaComeço[primeiroDia])==0 and i!=0 and i<(7-semanaComeço[primeiroDia]):
        locY+=45
        locX=18
    elif i>(7-semanaComeço[primeiroDia]) and (i+semanaComeço[primeiroDia])%7==0:
         locY+=45
         locX=18    
    if (i+1)==14 or i==14:
         print(locY,locX)
    print(i)
    btn.append(ctk.CTkButton(frame,35,35,fg_color="#161f31",bg_color="#161f31",text=str(i+1),font=ctk.CTkFont("Bahnschrift",weight="bold",size=15),corner_radius=12))
    btn[i].place(y=locY,x=locX)
    btn[i].configure(command=lambda index=(locX,locY): (button_click(index),loc(index)))
    locX+=55


root.mainloop()
