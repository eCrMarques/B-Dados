import psycopg2
from Controle.ConexãoClass import Conexão
from Modelo.classAluguél import Aluguel
from Modelo.classCliente import Cliente
from Modelo.classLivro import Livro

def Atualizar(tipo):
    op=input("Deseja Alterar? s/n\n")
    if op =='s':
        dados=conexaoBanco.consultarBanco(f"""
        select * from "{tipo}" """)
        id=input(f"Digite o Id do {tipo}: ")
        Select=conexaoBanco.consultarBanco(f"""
        select * from "{tipo}" where "id_{tipo}" = '{id}' """)[0]
        if int(id) in [item[0] for item in dados]:
            if tipo == "Cliente":
                NovoCliente=Cliente(id,input("Digite O Nome: "),input("Telefone Ex:(123456789): "), input("Cpf: "))
                for i,val in enumerate(NovoCliente.__dict__.keys()):
                    if NovoCliente.__dict__[val]=='':
                        NovoCliente.__dict__[val]=Select[i]
                conexaoBanco.manipularBanco(NovoCliente.atualizar())
            elif tipo =="Livro":
                NovoLivro=Livro(id,input("Digite O Nome: "),input("Data Lançamento Ex(Ano-Mês-Dia): "),input("Quantidade: "))
                print(NovoLivro.__dict__)
                print(Select)
                for i,val in enumerate(NovoLivro.__dict__.keys()):
                    if NovoLivro.__dict__[val]=='':
                        NovoLivro.__dict__[val]=Select[i]
                print(NovoLivro.__dict__)
                conexaoBanco.manipularBanco(NovoLivro.atualizar())

def Excluir(tipo):
    Visualizar(tipo)
    id=input(f"Id do {tipo}: ")
    resultado=conexaoBanco.manipularBanco(f"""
        Delete From "{tipo}"
        where "id_{tipo}"={id}""")
    existente=conexaoBanco.consultarBanco(f"""select * from "{tipo} where "id_{tipo}" = '{id}' """)
    if existente:
        print("Removido Com Sucesso")
    else:
        print("Falha ao Remover") 
    

def AdicionarLivro():
    
    NovoLivro=Livro(None,input("Digite O Nome: "),input("Quantidade: "), input("Data Lançamento Ex(Ano-Mês-Dia): "))
    try:
        conexaoBanco.manipularBanco(NovoLivro.inserirLivro())
    except:
        print('Invalido')

def AdicionarCliente():
    
    NovoCliente=Cliente(None,input("Digite O Nome: "),input("Telefone Ex:(123456789): "), input("Cpf: "))
    try:
        conexaoBanco.manipularBanco(NovoCliente.inserirCliente())

    except:
        print('Invalido')

def AdicionarAluguel():
    print('----Cliente----')
    Visualizar('Cliente')
    print('----Livros----')
    Visualizar('Livro')
    
    livro=input("Digite o id do Livro: ")
    quantidade=conexaoBanco.consultarBanco(f"""Select "Quantidade" from "Livro" where "id_Livro" = '{livro}' """)[0][0]
    if quantidade==0:
        print("Livro Indisponivel")
    else:
        NovoAluguel=Aluguel(None,input("Digite o id do Cliente: "),livro,None)
        try:
            conexaoBanco.manipularBanco(NovoAluguel.inserirAluguel())
            conexaoBanco.manipularBanco(NovoAluguel.Retirar(quantidade))
        except:
            print('Invalido')

def Visualizar(tipo,pos=None):
    if pos==None:
        Lista=conexaoBanco.consultarBanco(f"""
        Select * from "{tipo}"
        order by "id_{tipo}" asc
        """)
    else:
        Lista=conexaoBanco.consultarBanco(f"""
        Select * from "{tipo}" where "id_{tipo}" = '{pos}'
        """)
    Nome='Nome'
    Lançamento='Lançamento'
    Quantidade='Quantidade'

    if tipo =='Cliente':
        Lançamento='Telefone'
        Quantidade='Cpf'
    
    elif tipo =='Aluguel':
        Lançamento='Livro'
        Quantidade='Entregue'
        Nome = 'Cliente'
    for item in Lista:
        if tipo == "Aluguel":
            Cliente=conexaoBanco.consultarBanco(f"""select "Nome_Cliente" from "Cliente" where "id_Cliente" = '{item[1]}' """)[0][0]
            Livro=conexaoBanco.consultarBanco(f"""select "Nome_Livro" from "Livro" where "id_Livro" = '{item[2]}' """)[0][0]
            item=list(item)
            item[1],item[2]=Cliente,Livro
        print(f'Id: {item[0]} | {Nome}: {item[1]} | {Lançamento}: {item[2]} | {Quantidade}: {item[3]}')
while True:
    try:
        conexaoBanco=Conexão("Livraria","localhost","5432","postgres","postgres")
        op = input('''
        1- Ver Livros
        2- Ver Clientes
        3- Ver Alugados
        4- Adicionar 
        5- Remover
        6- Sair   
        ''')

        match op:
            case '1':
                Visualizar('Livro')
                Atualizar("Livro")
            case '2':
                Visualizar('Cliente')
                Atualizar("Cliente")
            case '3':
                Visualizar('Aluguel')
                
            case '4':
                op= input('1-Adicionar Livro \n2-Adicionar Cliente\n3-Alugar Livro\n')
                match op:
                    case '1':
                        AdicionarLivro()
                    case '2':
                        AdicionarCliente()                        
                    case '3':
                        AdicionarAluguel()                        
            case '5':
                op=input("\t-Remover-\n1-Cliente\n2-Livro\n")
                match op:
                    case '1':
                        Excluir("Cliente")
                    case '2':
                        Excluir("Livro")
                    case _:
                        print()
                        
            case '6':
                break
            case _:
                print("Opção Incorreta")

    except(psycopg2.Error,Exception) as error:
        print("Conexão Erro ", error)

