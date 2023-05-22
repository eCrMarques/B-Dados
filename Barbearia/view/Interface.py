from typing import Optional, Tuple, Union
from PIL import Image,ImageTk
from customtkinter import *
from datetime import *
from control.classConexao import *
from control.criarTabelas import *
from model.classAgenda import *
from model.classProduto import *
from model.classCliente import *

barbeariaDB = Conexao("barbearia2","localhost","5432","postgres","postgres")
agenda = Agendamentos()
cliente=Clientes()
Produto=Produtos()

mês=datetime.now()
primeiroDia=datetime(int(mês.strftime("%Y")),int(mês.strftime("%m")),1).strftime("%A")

Horario=["8:00","8:50","9:40","10:30","11:20","14:00","15:50","16:40","17:30","18:20"]
meses={"January":["Janeiro",31],"February":["Fevereiro",28],"March":["Março",31],"April":["Abril",30],"May":["Maio",31],"June":["Junho",30],"July":["Julho",31],"August":["Agosto",31],"September":["Setembro",30],"October":["Outubro",31],"November":["Novembro",30],"December":["Dezembro",31]}

set_appearance_mode("Dark")

class Frame(CTkFrame):
    def __init__(self,root):
        super().__init__(root)
        self.Visivel=True
        # Janela Principal
        Janela=CTkScrollableFrame(root,1200,720,scrollbar_fg_color="transparent",scrollbar_button_hover_color="#f6e1b6",scrollbar_button_color="#f6e1b6")
        Janela.place(x=0,y=0)
        self.principal=Janela
        self.bg=Image.open("view/Bg.png")
        self.bg=ImageTk.PhotoImage(self.bg)
        CTkLabel(Janela,image=self.bg).grid(column=0,row=0)
        self.root=root
        # Titulo (Barbearia)
        # CTkLabel(Janela,text="< = BARBEARIA = >",bg_color="transparent",text_color="black",font=CTkFont(weight="bold",size=20,family="Ancient Ad")).grid(column=0, row=0,sticky="nw",padx=210,pady=40)
        # Calendario
        bgCalendario=Image.open("view/Calendario.png")
        bgCalendario=ImageTk.PhotoImage(bgCalendario)
        Calendario=CTkLabel(Janela,image=bgCalendario,width=436,height=201,bg_color="transparent",text=None)
        Calendario.grid(column=0, row=0,sticky="nw",padx=(148,140),pady=600)
        CTkLabel(self,text=list(f'{meses[mês.strftime("%B")][0]}'),text_color="#111a25",font=CTkFont("Bahnschrift",weight="bold",size=23),corner_radius=20).pack()
        Semana=["D","S","T","Q","Q","S","S"]
        posx=75
        for i,dia in enumerate(Semana):
            CTkLabel(Calendario,fg_color="#f6e1b6",text_color="red",text=dia,font=CTkFont("Sketch  400",weight="bold",size=25)).place(y=5,x=posx)
            posx+=45
        # Cliente
        cliente = ClienteFrame(Janela)
        # Agenda
        Agenda = CTkScrollableFrame(Janela,460,285,bg_color="#d2dee5",fg_color="#d2dee5",scrollbar_fg_color="transparent",scrollbar_button_color="#d2dee5",scrollbar_button_hover_color="#d2dee5")
        Agenda.place(x=118,y=944)
        Agenda.grid_columnconfigure((0,1,2),weight=1)
        Agenda.grid_rowconfigure((0,1,2),weight=1)
        self.Agenda=Agenda
        #Titulo Agenda
        Titulos=[]
        Titulos.append(CTkLabel(Agenda,text="Nome",text_color="black",font=(CTkFont(size=20))).grid(row=0,column=0,padx=(20,45),pady=(0,8)))
        Titulos.append(CTkLabel(Agenda,text="Serviço",text_color="black",font=(CTkFont(size=20))).grid(row=0,column=1,padx=(20,0),pady=(0,8)))
        Titulos.append(CTkLabel(Agenda,text="Hora",text_color="black",font=(CTkFont(size=20))).grid(row=0,column=2,padx=(50,0),pady=(0,8)))
        # Separação
        pos=0.3
        for i in range(3):
            if i!=2:
                CTkFrame(Agenda,3,1000).place(relx=pos)
            CTkFrame(Agenda,10,3).grid(sticky="sew",row=0,column=i)
            pos+=0.4
        self.pos=[]
        for pos in ((20,45),(20,0),(50,0)):
             self.pos.append(pos)
        # Janelas 
        self.janela=None
        self.Marcado=[]
        self.preV=None
        self.preloc=''
        self.concluir=''

        # Serviços
        ServiçoFrame= CTkScrollableFrame(self.principal,200,25,fg_color="orange",orientation="horizontal",border_color="gray",border_width=3,scrollbar_button_color="orange")
        ServiçoFrame.place(x=360,y=510,anchor=CENTER)
        ServiçoFrame.grid_columnconfigure((0,1),weight=1)
        self.coluna=0
        self.serviço=ServiçoFrame
        self.novo=[]
        self.selectServiço=None
        for serviço in Serviços:
            self.coluna+=1
            Serviço=CTkLabel(self.serviço,text=f"{serviço}",font=CTkFont(weight="bold",size=15),text_color="black")
            Serviço.grid(pady=2,padx=15,column=self.coluna,row=0,sticky="we")
            Serviço.bind("<Button-1>", lambda e: self.selecionar(Serviço))
            self.novo.append(serviço)
        
        self.atualizado=True

        # Agenda
        self.Agendado=None
        self.listaAgenda=[]
        self.linha=0
        self.data=None
        locY=32
        locX=64
        btn=[]
        semanaComeço={"Sunday":0,"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6}
        locX=locX+(45*semanaComeço[primeiroDia])

        for i in range(int(meses[mês.strftime("%B")][1])):
            if i%(7-semanaComeço[primeiroDia])==0 and i!=0 and i==(7-semanaComeço[primeiroDia]):
                locY+=30
                locX=64
            elif i>(7-semanaComeço[primeiroDia]) and (i+semanaComeço[primeiroDia])%7==0:
                locY+=30
                locX=64

            btn.append(CTkButton(Calendario,25,25,fg_color="#f6e1b6",bg_color="#f6e1b6",text_color="black",text=str(i+1),font=CTkFont("Bahnschrift",weight="bold",size=22),corner_radius=12))
            btn[i].place(y=locY,x=locX)
            
            btn[i].configure(command=lambda index=(locX,locY,(btn[i].cget("text"))): self.button_click(index,data=index[2]))
            locX+=45
        self.atualizar()
    def Alternar(self):

        if self.Visivel:
            self.principal.place_forget()
            self.Visivel=False
        else:
            self.principal.place(x=0,y=0)


            for serviço in Serviços:
                if serviço not in self.novo:
                    self.coluna+=1
                    Serviço=CTkLabel(self.serviço,text=f"{serviço}",font=CTkFont(weight="bold",size=15),text_color="black",corner_radius=10)
                    Serviço.grid(pady=0,padx=15,column=self.coluna,row=0,sticky="ew")
                    Serviço.bind("<Button-1>", lambda e: self.selecionar(Serviço))
                    self.novo.append(serviço)

    def selecionar(self,Serviço):
        global serviçoSelecionado
        if self.selectServiço == None:
            Serviço.configure(fg_color="gray")
            serviçoSelecionado=Serviço.cget("text")
            self.selectServiço=Serviço
            self.id=barbeariaDB.consultarBanco(Produto.Buscar(serviçoSelecionado))[0][0]
        elif self.selectServiço==Serviço:
            self.selectServiço.configure(fg_color="transparent")
            self.selectServiço=None
            serviçoSelecionado=None
            self.id=None
        else:
            self.id=barbeariaDB.consultarBanco(Produto.Buscar(serviçoSelecionado))[0][0]
            self.selectServiço.configure(fg_color="transparent")
            Serviço.configure(fg_color="gray")
            self.selectServiço=Serviço
            serviçoSelecionado=Serviço.cget("text")
        print(self.id)

    def button_click(self,loc=None,data=None,status=None):

        if status=="Concluido":
             self.preV=None
        if self.janela == None:
            
            self.preloc=loc
            self.janela=CTkScrollableFrame(self.principal,150,100,bg_color="purple")
            self.janela.place(x=(loc[0]+180),y=(loc[1]+480))
            self.janela.grid_columnconfigure((0,1), weight=1)
            self.janela.grid_rowconfigure(tuple(range(4)),weight=1)

            coluna=0
            linha=0
            btn=[]
            for i,hora in enumerate(Horario):
                Ativo="blue"

                if f"{data}/{hora}" in self.Marcado:

                        Ativo="red"
                btn.append(CTkButton(self.janela,60,28,text=hora,fg_color=Ativo))
                btn[i].grid(row=linha,column=coluna,pady=10)
                btn[i].configure(command=lambda index=(btn[i],hora,data): self.Agendar(index))
                if coluna==1:
                        linha+=1
                        coluna=0  
                else:
                    coluna=1
        else:
            if self.preloc==loc or loc==None:
                self.janela.destroy()
                self.janela.place_forget()
                self.janela=None
                self.preV=None
                try:
                    Concluir.destroy()
                except: pass
            else:   
                    self.janela.place(x=(loc[0]+180),y=(loc[1]+480))
                    self.preloc=loc

    def Agendar(self,Botão):
        if nomeSelecionado==None or serviçoSelecionado==None:
            return
        self.preV
        global Concluir
        if f"{Botão[2]}/{Botão[1]}" in self.Marcado:
             self.preV=None
        try:
             Concluir.destroy()
        except:
             pass
        if self.preV==None:
            Botão[0].configure(fg_color="red")
            self.preV=Botão[0]
        else:
             if self.preV==Botão[0]:
                  Botão[0].configure(fg_color="blue")
                  self.preV=None
                  pass
             else:
                  if self.preV.cget("fg_color")=="red":
                       if f'{Botão[2]}/{self.preV.cget("text")}' not in self.Marcado:
                            self.preV.configure(fg_color="blue")
                       Botão[0].configure(fg_color="red")
                       self.preV=Botão[0]
        if Botão[0].cget("fg_color")=="red" and f"{Botão[2]}/{Botão[1]}" not in self.Marcado:
             Concluir= CTkFrame(self.principal,30,30,bg_color="#f6e1b6",fg_color="green",corner_radius=15)
             Concluir.place(x=525,y=615)
             Concluir.bind("<Button-1>", lambda Data=None: (Concluir.destroy(),self.button_click(status="Concluido"),self.adicionarAgenda((f"{nomeSelecionado}",serviçoSelecionado,f"{Botão[2]}/{Botão[1]}"))))
             

    def adicionarAgenda(self,Dados , Atualizar=None):
        if Atualizar==True:
            Dados=list(Dados)
            Dados[0]=barbeariaDB.consultarBanco(agenda.Buscar(Dados[0],"cliente"))[0][0]
            Dados[1]=barbeariaDB.consultarBanco(agenda.Buscar(Dados[1],"produto"))[0][0]
        for i,idCliente in enumerate(novoCliente):
            if nomeSelecionado==idCliente[1]:
                idCliente=idCliente[0]
                break
            elif i==(len(idCliente)-1):
                idCliente=(int(novoCliente[i][0])+1)
        if Atualizar==None:
            if nomeSelecionado == None or serviçoSelecionado ==None:
                return
            self.Marcado.append(Dados[2])
        self.linha+=1
        entrada=True
        for item in Dados:
            if item=='':
                entrada=False
        if entrada:
            Tabela=[]
            for i,item in enumerate(Dados):
                if item==Dados[2]:
                    item=Dados[2].split("/")[1]
                Tabela.append(CTkLabel(self.Agenda,text=f"{item}",text_color="black",font=(CTkFont(size=20))))                
                Tabela[i].grid(column=i,padx=self.pos[i],row=self.linha,pady=8)
                CTkFrame(self.Agenda,10,3).grid(sticky="sew",row=self.linha,column=i)
            self.listaAgenda.append(Tabela)
            if Atualizar==None:
                barbeariaDB.manipularBanco(agenda.inserirAgendamento(idCliente,self.id,Dados[2],"novo"))
        if Atualizar==None:
            self.selecionar(self.selectServiço)

    def atualizar(self):
        if self.atualizado:
            for item in novoAgendamento:
                self.adicionarAgenda(item[1::],True)
            try:
                self.Marcado.append(item[3])
            except:pass
            self.atualizado=False
            


class Frame2(CTkFrame):
    def __init__(self, root):
        super().__init__(root)         
        Janela=CTkScrollableFrame(root,1200,720,scrollbar_fg_color="transparent",scrollbar_button_hover_color="#f6e1b6",scrollbar_button_color="#f6e1b6")
        self.principal=Janela
        self.bg=Image.open("view/Bg2.png")
        self.bg=ImageTk.PhotoImage(self.bg)
        teste=CTkLabel(Janela,image=self.bg)
        teste.grid(column=0,row=0)
        self.root=root

        # Caixa
        CaixaFrame = CTkScrollableFrame(Janela,510,203,fg_color="#3b414b",bg_color="#3b414b")
        CaixaFrame.grid_columnconfigure((0,1,2,3),weight=1)
        CaixaFrame.grid_rowconfigure((0,1),weight=1)
        CaixaFrame.place(y=295,x=102)

       

        # Produtos
        tabela = Tabela(teste,CaixaFrame,self.root)
        self.Visivel=False
    def Alternar(self):
        if self.Visivel:
            self.principal.place_forget()
            self.Visivel=False
        else:
            self.principal.place(x=0,y=0)
            self.Visivel=True

class Tabela(CTkScrollableFrame):
    def __init__(self,root, Caixa=None, principal=None):
        super().__init__(root,width=500,height=300,corner_radius=15,border_color="brown",border_width=5)
        
        self.grid_columnconfigure((0,1,2),weight=1)
        self.grid_rowconfigure((0,1),weight=1)
        self.place(x=360,y=830, anchor=CENTER)
        self.root=principal
        self.caixa=Caixa
        CTkLabel(self,fg_color="gray",corner_radius=10,text="Produto",font=CTkFont(weight="bold",size=20)).grid(column=0,row=0,padx=5,sticky="ew",columnspan=4)

        entry=[]
        entry.append(CTkEntry(self,110,30,fg_color="white",text_color="black",font=CTkFont(size=15),placeholder_text="Nome"))
        entry[0].grid(pady=2,padx=5,column=0,row=1,sticky="w")
        entry.append(CTkEntry(self,120,30,fg_color="white",text_color="black",font=CTkFont(size=15),placeholder_text="Descrição"))
        entry[1].grid(pady=2,padx=5,column=1,row=1,sticky=EW)
        entry.append(CTkEntry(self,110,30,fg_color="white",text_color="black",font=CTkFont(size=15),placeholder_text="Quantidade"))
        entry[2].grid(pady=2,padx=5,column=2,row=1,sticky="e")

        self.quantidade=0
        self.destroir=None
        self.master=root
        self.JanelaCompra=None
        
        # Compras
        self.status=None
        self.compras=[]
        self.item=[]
        for tabela in entry:
            tabela.bind("<Return>", lambda e: self.adicionarTabela(entry)) 

        self.produtos=[]
        # Serviço
        self.coluna=0
        self.atualizar()

    def destruirTabela(self,Tables,All=False,pos=None):
        for produtos in novoProduto:
            if Tables[0].cget("text")==produtos[1]:
                idProduto=produtos[0]
        if self.destroir==None:
            self.destroir=CTkFrame(self,20,20,bg_color="gray",fg_color="red",corner_radius=10)
            self.destroir.place(relx=0.9,y=5)
            self.destroir.bind("<Button-1>", lambda e:self.destruirTabela(Tables,All=True,pos=pos))
            
        else:
            self.destroir.destroy()
            self.destroir=None
        if All:
            for tabela in Tables:
                prevTabela=Tables
                tabela.destroy()
                pass
            if len(listaprodutos)>1:
                mudar=False
                for produto in listaprodutos:
                    if produto==prevTabela:
                        mudar=True
                        listaprodutos.remove(produto)
                    elif mudar:
                        produto[0].grid(row=pos)
                        produto[1].grid(row=pos)
                        produto[2].grid(row=pos)
                        pos+=1
            try:
                barbeariaDB.manipularBanco(Produto.deletarProduto(idProduto))
            except:pass
                        


    def adicionarTabela(self, tabela , caixa=None):
        global listaprodutos
        global posLinha
        posLinha+=1
        entrada=True
        if caixa==None:
            root=self
            for item in tabela:
                if item.get()=='':
                    entrada=False
                tabela2=tabela[2].get()
                tabela1=tabela[1].get()
        elif caixa=="Atualizar":
            root=self
            tabela2='1'
            tabela1="1.1"
        else:
            root= self.caixa
            tabela2='1'
            tabela1="1.1"

        global Serviços
        if entrada and (tabela2.isnumeric() or tabela2=="Serviço") and ('.' in tabela1):
            Tabela=[]
            for i,item in enumerate(tabela):
                if caixa==None:
                    Nome=item.get()
                    if item==tabela[1] and tabela[2].get()==("Serviço" or "serviço" or "servico"):
                        self.coluna+=1
                        nomeServiço=tabela[0].get()
                        Serviços.append(nomeServiço)
                    
                else:
                    Nome=tabela[i]
                if i==2:
                    posItem=posLinha    
                Tabela.append(CTkLabel(root,text=f"{Nome}",font=CTkFont(weight="bold",size=15)))
                Tabela[i].grid(pady=2,padx=5,column=i,row=posLinha,sticky="n")
                if root== self.caixa:
                    if i==2:
                        preço=self.Info(Tabela[(i-1)].cget("text"))
                        CTkLabel(root,text=f"R${(int(Nome)*float(preço)):.2f}",font=CTkFont(weight="bold",size=15)).grid(pady=2,padx=5,column=(i+1),row=posLinha,sticky="n")
                        
                if caixa ==None or caixa=="Atualizar":
                    Tabela[i].bind("<Double-Button-1>", lambda index: (self.destruirTabela(Tabela,pos=posLinha)))
                    Tabela[i].bind("<Button-1>", lambda index: (self.AtualizarCompra((posItem,Tabela))))

            listaprodutos.append(Tabela)
            if caixa==None:
                if Tabela[2].cget("text")=="Serviço":
                    Tipo=0
                    tipagem="Serviço"
                else:
                    Tipo=Tabela[2].cget("text")
                    tipagem=True
                barbeariaDB.manipularBanco(Produto.inserirNovoProduto(Tabela[0].cget("text"),Tabela[1].cget("text"),Tipo,tipagem))
            if '.' in Tabela[1].cget("text"):
                Tabela[1].configure(text=f'{Tabela[1].cget("text")+"R$"}')

    def AtualizarCompra(self,pos):
        try:
            if self.Dados!=[item.cget("text") for item in pos[1]] and self.quantidade>0:
                self.item.append([f'{nomeSelecionado}',self.Dados[0],self.quantidade])
                self.quantidade=0
        except:pass
        self.Dados=[item.cget("text") for item in pos[1]]
        
        if self.status==None:
            aumentar=CTkFrame(self,10,10,fg_color="green")
            aumentar.grid(pady=(1,5),column=2,row=pos[0],sticky="en")
            aumentar.bind("<Button-1>", lambda e: self.Comprar("Aumentar",[item for item in pos[1]]))
            diminuir=CTkFrame(self,10,10,fg_color="red")
            diminuir.grid(pady=(1,5),column=2,row=pos[0],sticky="es")
            diminuir.bind("<Button-1>", lambda e: self.Comprar("Diminuir",[item for item in pos[1]]))
            self.status=[aumentar,diminuir]
        else:
            for status in self.status:
                status.destroy()
            self.status=None
    def Comprar(self, status, Dados):
        if nomeSelecionado==None or int(Dados[2].cget('text'))<=0:
            return
        match status:
            case "Aumentar":
                self.quantidade+=1
                Dados[2].configure(text=f"{int(Dados[2].cget('text'))-1}")
            case "Diminuir":
                self.quantidade-=1
                Dados[2].configure(text=f"{int(Dados[2].cget('text'))+1}")
                if self.quantidade<=0:
                    self.quantidade=0
        if self.quantidade>0:
            if self.JanelaCompra==None:
                Concluir=CTkLabel(self.root,25,25,text=f"{self.quantidade}",fg_color="green",font=CTkFont(weight="bold"))
                Concluir.place(relx=0.9)
                self.JanelaCompra=Concluir
                Concluir.bind("<Button-1>", lambda e:(self.EfetuarCompra([f'{nomeSelecionado}',self.Dados[0],self.quantidade])))

            self.JanelaCompra.configure(text=f'{self.quantidade}')
        elif self.quantidade<=0:
            self.JanelaCompra.destroy()
            self.JanelaCompra=None

    def EfetuarCompra(self,item):
        if nomeSelecionado == None:
            return
        self.item.append(item)
        for compra in self.item:
            self.adicionarTabela(compra,True)
        self.item=[]
        try:
            self.JanelaCompra.destroy()
            self.JanelaCompra=None
            for status in self.status:
                status.destroy()
            self.status=None
            self.destroir.destroy()
            self.destroir=None
            self.quantidade=0
        except:pass

    def atualizar(self):
        global novoProduto
        global Serviço
        for i,produto in enumerate(novoProduto):
            if produto not in self.produtos:
                if produto[4] =="Serviço":
                    produto=list(produto)
                    produto[3]="Serviço"
                    Serviços.append(produto[1])
                self.adicionarTabela(produto[1:4:],caixa="Atualizar")
                self.produtos.append(produto)
    def Info(self ,nome):
        novoProduto=[item for item in barbeariaDB.consultarBanco(Produto.verProduto())]
        for produto in novoProduto:
                if produto[1]==nome:
                    if produto[2]:
                        return produto[2]

class ClienteFrame(CTkScrollableFrame):
    def __init__(self,master):
        global novoCliente
        super().__init__(master=master,width=436,height=300,corner_radius=10,border_width=5,border_color="black")
        self.grid_columnconfigure((0,1,2),weight=1)
        self.grid_rowconfigure((0,1),weight=1)
        self.place(x=360,y=300,anchor=CENTER)

        

        CTkLabel(self,fg_color="gray",corner_radius=10,text="Clientes",font=CTkFont(weight="bold",size=20)).grid(column=0,row=0,padx=5,sticky="ew",columnspan=4)


        pesquisa=CTkEntry(self,70,20,fg_color="white",placeholder_text="Pesquisar")
        self.pesquisa=pesquisa
        self.teste=pesquisa
        pesquisa.grid(pady=2,padx=5,column=0,row=1,columnspan=3,sticky="ew")
        pesquisa.bind("<Return>", lambda e: self.Pesquisar(pesquisa.get())) 
        self.pesquisaCliente=None
        self.destroir=None

        # Adicionar Cliente
        adicionarCliente=CTkFrame(self,25,25,fg_color="blue",bg_color="gray",corner_radius=10)
        adicionarCliente.place(relx=0.9, y=2)
        adicionarCliente.bind("<Button-1>", lambda e: self.table(pesquisa))
        self.JanelaAdicionar=None

        self.destroir=None
        self.Cliente=[]
        self.selecionado=None

        self.atualizar(novoCliente)

    def Pesquisar(self, informação):
        Cliente=False
        if informação !='' and len(informação)>1:
            for cliente in self.Cliente:
                for dados in cliente:
                    if dados.cget("text").lower()==informação.lower():
                        Cliente=True
                        pos=cliente
                        break
            if Cliente==True:
                Tabela=[]
                fundo=CTkFrame(self,height=30,fg_color="green")
                fundo.grid(pady=2,padx=5,column=0,row=2,sticky="ew",columnspan=3)
                self.fundo=fundo
                for i,info in enumerate(pos):

                    nome=info.cget("text")
                    Tabela.append(CTkLabel(self,text=f'{nome}',font=CTkFont(size=15),bg_color="green",text_color="black"))
                    Tabela[i].grid(pady=2,padx=5,column=i,row=2,sticky="we")
                    self.pesquisaCliente=Tabela
                global nomeSelecionado
                nomeSelecionado=pos[0].cget("text")
        else:
            for pesquisa in self.pesquisaCliente:
                self.fundo.destroy()
                pesquisa.destroy()
                nomeSelecionado=None


    def table(self,janelaPesquisa):
        if self.JanelaAdicionar== None:
            entry=[]
            entry.append(CTkEntry(self,70,20,fg_color="white",placeholder_text="Nome"))
            entry[0].grid(pady=2,padx=5,column=0,row=1,sticky="ew")
            entry.append(CTkEntry(self,70,20,fg_color="white",placeholder_text="Telefone"))
            entry[1].grid(pady=2,padx=5,column=1,row=1,sticky=EW)
            entry.append(CTkEntry(self,120,20,fg_color="white",placeholder_text="Email"))
            entry[2].grid(pady=2,padx=5,column=2,row=1,sticky="we")
            for tabela in entry:
                tabela.bind("<Return>", lambda e: self.adicionarTabela(entry)) 
            self.JanelaAdicionar= entry
            self.pesquisa.destroy()
        else:
            for item in self.JanelaAdicionar:
                item.destroy()
            self.JanelaAdicionar=None
            self.pesquisa=CTkEntry(self,70,20,fg_color="white",placeholder_text="Pesquisar")
            self.pesquisa.grid(pady=2,padx=5,column=0,row=1,columnspan=3,sticky="ew")
            self.pesquisa.bind("<Return>", lambda e: self.Pesquisar(self.pesquisa.get()))

    def destruirTabela(self,Tables,All=False,pos=None):
        if self.destroir==None:
            self.destroir=CTkFrame(self,23,23,bg_color="gray",fg_color="red",corner_radius=10)
            self.destroir.place(x=20,y=4)
            self.destroir.bind("<Button-1>", lambda e:self.destruirTabela(Tables,All=True,pos=pos))
            
        else:
            self.destroir.destroy()
            self.destroir=None
        if All:
            for tabela in Tables:
                prevTabela=Tables
                tabela.destroy()
                pass
            if len(self.Cliente)>1:
                mudar=False
                for produto in self.Cliente:
                    if produto==prevTabela:

                        mudar=True
                    elif mudar:
                        produto[0].grid(row=pos)
                        produto[1].grid(row=pos)
                        produto[2].grid(row=pos)
                        pos+=1
            self.Cliente.remove(Tables)
            for dados in novoCliente:
                if dados[2]==Tables[1].cget("text"):
                    barbeariaDB.manipularBanco(cliente.deletarCliente(dados[0]))
                


    def adicionarTabela(self, tabela ,tipo=None):
        global posLinha
        posLinha+=1
        entrada=True
        if tipo == None:
            for item in tabela:
                if item.get()=='':
                    entrada=False
                tabela2=tabela[1].get()
        else:
            tabela2='123456789'
        if entrada and tabela2.isnumeric() and len(tabela2)==9:
            Tabela=[]
            for i,item in enumerate(tabela):
                if tipo ==None:
                    item=item.get()
                Tabela.append(CTkLabel(self,text=f"{item}",font=CTkFont(size=15)))
                Tabela[i].grid(pady=2,padx=5,column=i,row=posLinha,sticky="ew")
                Tabela[i].bind("<Button-1>", lambda e: self.selecionar(Tabela))

                Tabela[i].bind("<Double-Button-1>", lambda e: self.destruirTabela(Tabela,pos=posLinha))
            if tipo ==None:
                barbeariaDB.manipularBanco(cliente.inserirNovoCliente("novo",Tabela[0].cget("text"),Tabela[2].cget("text"),Tabela[1].cget("text")))
            self.Cliente.append(Tabela)
    def selecionar(self,Frames):
        global nomeSelecionado
        if self.selecionado==None:
            Frames[0].configure(fg_color="green")
            Frames[0].configure(corner_radius=13)
            nomeSelecionado=Frames[0].cget("text")
            self.selecionado=Frames[0]
        elif self.selecionado == Frames[0]:
            self.selecionado.configure(fg_color="transparent")
            self.selecionado=None
            nomeSelecionado=None
        else:
            self.selecionado.configure(fg_color="transparent")
            Frames[0].configure(fg_color="green")
            nomeSelecionado=Frames[0].cget("text")
            self.selecionado=Frames[0]

    def atualizar(self,item):
        global listaCliente
        global novoCliente
        for cliente in novoCliente:
            if cliente not in listaCliente:
                self.adicionarTabela(cliente[1::],"tipo")
                listaCliente.append(cliente)
    
    def Info(self, Labels):
        Frames=[item.cget("text") for item in Labels]
        for cliente in novoCliente:
            if cliente[1] == Frames[0] and cliente[2] == Frames[1]:
                return cliente[0]
                

posLinha=1

listaCliente=[]
Agenda=[]
Caixa=[]

novoCliente=[item for item in barbeariaDB.consultarBanco(cliente.verCliente())]
listaprodutos=[]

novoProduto=[item for item in barbeariaDB.consultarBanco(Produto.verProduto())]
Serviços=[]

novoAgendamento=[item for item in barbeariaDB.consultarBanco(agenda.verAgenda())]

nomeSelecionado=None

    
serviçoSelecionado=None

