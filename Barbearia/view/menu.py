
def visualizarMenu():
    print('''
        💈💇‍♂️🪒 sys Barber ✂️💇‍♀️💈

Sistema de gerenciamento de barbearia na palma da mão:
Escolha uma das opções[] abaixo e tecle [Enter↵]

[1]📝👪 Cadastrar clientes
[2]📝🗓️ Agendamento de serviço
[3]📝📦 Cadastrar produto
[4]📝💰 Efetuar venda
[5]👀👪 Visualizar lista de clientes
[6]👀🗓️️ Visualizar lista de agendamentos
[7]👀📦 Visualizar lista de produtos
[8]👀💰 Visualiazar lista de  venda
[0]🚪 Sair
    ''')

    op = input(": ")
    if op in "1|2|3|4|5|6|7|8|0":
        pass
    else:
        print("comando inválido, tente novamente")
        input("aperte [Enter↵] para continuar")
    
    return op

def mensagemDeConfirmacao(resultado):
    if resultado:
        print("Registro efetuado!")
        input("aperte [Enter↵] para continuar")
    else:
        print("O registro falhou")
        input("aperte [Enter↵] para continuar")

def buscarDadosEmTabela(bancoDeDados, nomeTabela, nomeColuna, id):
   
    item = bancoDeDados.consultarBanco(f"""
    Select * from "{nomeTabela}"
    where "{nomeColuna}" = '{id}'
    """)

    return item


# ______________________ trechos de código relacionados a clientes _______________
#_________________________________________________________________________________

def mensagemListaClientes(resultado):
    listaIdClientes = []
    print("id | nome | telefone | email")
    for cliente in resultado:
        print(f"{cliente[0]} | {cliente[1]} | {cliente[2]} | {cliente[3]}")
        listaIdClientes.append(cliente[0])
    
    return listaIdClientes

def mensagemEscolherDeletarOuAtualizarCliente():
    
    op = "rodarWhile"
    while not(op in "1|2|0"): 
        
        print("""
Deseja fazer alguma alteração na lista cliente?
Digite [1]Atualizar, [2]Deletar ou [0]sair.
    
    [1] Atualizar Cliente
    [2] Deletar Cliente
    [0] sair
    """)
        op = input(": ")
        match op:
            case "1":
                opEscolhida = "Atualizar"
            case "2":
                opEscolhida = "Deletar"
            case "0":
                opEscolhida = False
            case _:
                    print("comando inválido, tente novamente")
                    input("aperte [Enter↵] para continuar")
        
    return opEscolhida

def mensagemAtualizarCliente(listaIdClientes):
    
    op = "rodarWhile"
    while not(op in "1|0"):
        print("""
confirme atualização do cliente? Digite [1]Sim ou [0]Não.

[1] Sim
[0] Não
""")
        op = input(": ")
        match op:
            case "1":
                opcao = 0
                while not(opcao in listaIdClientes):
                    print("Digite o ID do Cliente a ser atualizado:")          
                    try:
                        opcao = int(input(": "))                
                        if opcao in listaIdClientes:
                            pass
                        else:
                            print("ID do Cliente não existe")
                            print("Voltando ao menu principal")
                            input("aperte [Enter↵] para continuar")
                            opcao = False
                            break
                    except:
                        print("comando invalido. Tente novamente")
            case "0":
                opcao = False
            case _:
                print("comando inválido, tente novamente")
                input("aperte [Enter↵] para continuar")
                op = "rodarWhile"
        
    return opcao

def mensagemDeletarCliente(listaIdClientes):
    
    op = "rodarWhile"
    while not(op in "1|0"):
        print("""
confirma deletar algum cliente? Digite [1]Sim ou [0]Não.

[1] Sim
[0] Não
""")
        op = input(": ")
        match op:
            case "1":
                opcao = 0
                while not(opcao in listaIdClientes):
                    print("Digite o ID do Cliente a ser deletado:")          
                    try:
                        opcao = int(input(": "))                
                        if opcao in listaIdClientes:
                            pass
                        else:
                            print("ID do Cliente não existe")
                            print("Voltando ao menu principal")
                            input("aperte [Enter↵] para continuar")
                            opcao = False
                            break
                    except:
                        print("comando invalido. Tente novamente")
            case "0":
                opcao = False
            case _:
                print("comando inválido, tente novamente")
                input("aperte [Enter↵] para continuar")
                op = "rodarWhile"
        
    return opcao

#______________________ trechos de código relacionados a Produto ___________________
#____________________________________________________________________________________
def mensagemListaProdutos(resultado):
    listaIdProdutos = []
    print("id | nome | preço | quantidade")
    for produto in resultado:
        print(f"{produto[0]} | {produto[1]} | {produto[2]} | {produto[3]}")
        listaIdProdutos.append(produto[0])
    
    return listaIdProdutos

def mensagemEscolherDeletarOuAtualizarProduto():
    
    op = "rodarWhile"
    while not(op in "1|2|0"): 
        
        print("""
Deseja fazer alguma alteração na lista de Produtos e serviços?
Digite [1]Atualizar, [2]Deletar ou [0]sair.
    
    [1] Atualizar produtos/serviços
    [2] Deletar produtos/serviços
    [0] sair
    """)
        op = input(": ")
        match op:
            case "1":
                opEscolhida = "Atualizar"
            case "2":
                opEscolhida = "Deletar"
            case "0":
                opEscolhida = False
            case _:
                    print("comando inválido, tente novamente")
                    input("aperte [Enter↵] para continuar")
        
    return opEscolhida

def mensagemAtualizarProduto(listaIdProdutos):
    
    op = "rodarWhile"
    while not(op in "1|0"):
        print("""
Deseja atualizar algum Produto? Digite [1]Sim ou [0]Não.

[1] Sim
[0] Não
""")
        op = input(": ")
        match op:
            case "1":
                opcao = 0
                while not(opcao in listaIdProdutos):
                    print("Digite o ID do produto a ser atualizado:")          
                    try:
                        opcao = int(input(": "))                
                        if opcao in listaIdProdutos:
                            pass
                        else:
                            print("ID do produto não existe")
                            print("Voltando ao menu principal")
                            input("aperte [Enter↵] para continuar")
                            opcao = False
                            break
                    except:
                        print("comando invalido. Tente novamente")
            case "0":
                opcao = False
            case _:
                print("comando inválido, tente novamente")
                input("aperte [Enter↵] para continuar")
                op = "rodarWhile"
        
    return opcao

def mensagemDeletarProduto(listaIdClientes):
    
    op = "rodarWhile"
    while not(op in "1|0"):
        print("""
Deseja deletar algum Produto? Digite [1]Sim ou [0]Não.

[1] Sim
[0] Não
""")
        op = input(": ")
        match op:
            case "1":
                opcao = 0
                while not(opcao in listaIdClientes):
                    print("Digite o ID do Produto a ser apagado:")          
                    try:
                        opcao = int(input(": "))                
                        if opcao in listaIdClientes:
                            pass
                        else:
                            print("ID do Cliente não existe")
                            print("Voltando ao menu principal")
                            input("aperte [Enter↵] para continuar")
                            opcao = False
                            break
                    except:
                        print("comando invalido. Tente novamente")
            case "0":
                opcao = False
            case _:
                print("comando inválido, tente novamente")
                input("aperte [Enter↵] para continuar")
                op = "rodarWhile"
        
    return opcao

# __________________________ trecho de códigos da agenda ______________________
#____________________________________________________________________________________

def mensagemAgendamento(frases):
    
    match frases:
        case "fraseI":
            print("escolha o ID do Cliente")
            opcao = input(": ")
        case "fraseII":
            print("Escolha o ID do serviço")
            opcao = input(": ")
    
    return opcao


def mensagemListaAgenda(resultado,bancoDeDados):
    listaHorasAgenda = []
    listaIdAgenda = []
    print("serviços agendados para hoje\n")
    for agendamento in resultado:
        listaHorasAgenda.append(agendamento[3])
        listaIdAgenda.append(agendamento[0])
        
        print(f"ID do agendamento: {agendamento[0]}")

        listaCliente = buscarDadosEmTabela(bancoDeDados,"clientes",'cliente_id',f"{agendamento[1]}")
        print(f"Nome do cliente: {listaCliente[0][1]}")

        # produto_id | produto_nome | produto_preco | produto_quantidade
        listaProduto = buscarDadosEmTabela(bancoDeDados,"produtos","produto_id",f"{agendamento[2]}")
        print("serviço escolhido:",listaProduto[0][1])

        print(f"hora marcada: {agendamento[3]}")
        print("__________________________________________________")

    if listaHorasAgenda:
        pass
    else:
        print("Todos os horários estão diponíveis")

    return listaHorasAgenda, listaIdAgenda

def mensagemMarcarHora(objAgenda,listaHorasAgenda):
        
        print(f"""
código | hora | situação
        """)
        for indice, hora in enumerate(objAgenda._agendaHorarios):
            if hora in listaHorasAgenda:
                print(f"🔴[{indice}] {hora} Reservado")
            else:
               print(f"🟢[{indice}] {hora} Disponível")
        
        op = input("""
        digite o código do horário:
        """)
        for indice, hora in enumerate(objAgenda._agendaHorarios):
            if str(op) == str(indice):
               objAgenda._horario = hora
        

def mensagemEscolherDeletarOuAtualizarAgenda():
    
    op = "rodarWhile"
    while not(op in "1|2|0"): 
        
        print("""
Deseja fazer alguma alteração na lista de horários da Agenda?
Digite [1]Atualizar, [2]Deletar ou [0]sair.
    
    [1] Atualizar horário da agenda
    [2] Deletar horário da agenda
    [0] sair
    """)
        op = input(": ")
        match op:
            case "1":
                opEscolhida = "Atualizar"
            case "2":
                opEscolhida = "Deletar"
            case "0":
                opEscolhida = False
            case _:
                    print("comando inválido, tente novamente")
                    input("aperte [Enter↵] para continuar")
        
    return opEscolhida

def mensagemAtualizarAgenda(listaHoraAgenda):
    
    op = "rodarWhile"
    while not(op in "1|0"):
        print("""
confirme atualização da Agenda? Digite [1]Sim ou [0]Não.

[1] Sim
[0] Não
""")    
        op = input(": ")
        match op:
            case "1":
                opcao = 0
                while not(opcao in listaHoraAgenda):
                    print("Digite o ID  do  horário ser atualizado:")          
                    try:
                        opcao = int(input(": "))                
                        if opcao in listaHoraAgenda:
                            pass
                        else:
                            print("ID do horário não existe")
                            print("Voltando ao menu principal")
                            input("aperte [Enter↵] para continuar")
                            opcao = False
                            break
                    except:
                        print("comando invalido. Tente novamente")
            case "0":
                opcao = False
            case _:
                print("comando inválido, tente novamente")
                input("aperte [Enter↵] para continuar")
                op = "rodarWhile"
        
    return opcao

def mensagemDeletarAgenda(listaIdClientes):
    
    op = "rodarWhile"
    while not(op in "1|0"):
        print("""
confirma deletar algum horário da agenda? Digite [1]Sim ou [0]Não.

[1] Sim
[0] Não
""")
        op = input(": ")
        match op:
            case "1":
                opcao = 0
                while not(opcao in listaIdClientes):
                    print("Digite o ID do horário da agenda a ser deletado:")          
                    try:
                        opcao = int(input(": "))                
                        if opcao in listaIdClientes:
                            pass
                        else:
                            print("ID do horário da agenda não existe")
                            print("Voltando ao menu principal")
                            input("aperte [Enter↵] para continuar")
                            opcao = False
                            break
                    except:
                        print("comando invalido. Tente novamente")
            case "0":
                opcao = False
            case _:
                print("comando inválido, tente novamente")
                input("aperte [Enter↵] para continuar")
                op = "rodarWhile"
        
    return opcao


# ________________ Trecho relacionado a vendas ________________________________
#____________________________________________________________________________________

def mensagemVenda(frases):
    
    match frases:
        case "fraseI":
            print("escolha qual produto será vendido")
            opcao = None
        case "fraseII":
            print("Escolha o ID do produto a ser vendido")
            opcao = input(": ")
        case "fraseIII":
            print("Escolha a quantidade a ser vendida.")
            opcao = input(": ")
        case "fraseIV":
            op = "rodarWhile"
            while op != "sair":
                print("""
Deseja Adicionar outro Item a compra? Digite [1]Sim ou [0]Não.

[1] Sim
[0] Não
""")
                opcao = input(": ")
                match opcao:
                    case "1" | "0":
                        op = "sair"
                        opcao
                    case _:
                        print("comando inválido, tente novamente")
                        input("aperte [Enter↵] para continuar")
        case "fraseV":
            print("Escolha o ID do cliente")
            opcao = input(": ")
    return opcao

def mensagemListaVendas(resultado,opcaoPrint,bancoDeDados):
    if 1 == opcaoPrint:
        listaIdVendas = []
        for venda in resultado:
            listaIdVendas.append(venda[0])
    
    elif 2 == opcaoPrint:
        listaIdVendas = []
        somaValores = 0
        for venda in resultado:
            print(f"ID Venda:[{venda[0]}] horário da venda: {venda[2]}")
            
            listaCliente = buscarDadosEmTabela(bancoDeDados,"clientes",'cliente_id',f"{venda[1]}")
            print(f"Nome do cliente: {listaCliente[0][1]}",)

            itensDaVenda = buscarDadosEmTabela(bancoDeDados,"itens","venda_id",f"{venda[0]}")
            subTotalCliente = 0
            print("qtd * produto ( Valor do produto ) = sub Total")
            for item in itensDaVenda:
                # item_ID | venda_ID | produto_ID | item_quantidade
                print("",item[3], end=" * ") # quantidade Vendida, esse ""no print serve para organização do texto
                
                listaProduto = buscarDadosEmTabela(bancoDeDados,"produtos","produto_id",f"{item[2]}")
                # produto_id | produto_nome | produto_preco | produto_quantidade
                subTotalItem = item[3] * listaProduto[0][2]
                subTotalCliente += subTotalItem
                print(listaProduto[0][1],"(",listaProduto[0][2],") =",subTotalItem) # nome, preço, subtotal

            print("valor total da compra:",subTotalCliente)
            print("____________________________________________") # pular uma linha
            somaValores += subTotalCliente
            subTotalCliente = 0

        print("\nvalor total arrecadado",somaValores,"\n")
        somaValores = 0

    else:
        print("comando inválido")

    return listaIdVendas

def mensagemEscolherDeletarOuAtualizarVenda():
    
    op = "rodarWhile"
    while not(op in "1|0"): 
        
        print("""
Deseja Deletar alguma Vendas?
Digite [1]Deletar ou [0]sair.
    
    [1] Deletar Vendas
    [0] sair
    """)
        op = input(": ")
        match op:
            case "1":
                opEscolhida = "Deletar"
            case "0":
                opEscolhida = False
            case _:
                    print("comando inválido, tente novamente")
                    input("aperte [Enter↵] para continuar")
        
    return opEscolhida

def mensagemDeletarVenda(listaIdVendas):
    
    op = "rodarWhile"
    while not(op in "1|0"):
        print("""
Deseja deletar alguma Venda? Digite [1]Sim ou [0]Não.

[1] Sim
[0] Não
""")
        op = input(": ")
        match op:
            case "1":
                opcao = 0
                while not(opcao in listaIdVendas):
                    print("Digite o ID da Venda a ser apagada:")          
                    try:
                        opcao = int(input(": "))                
                        if opcao in listaIdVendas:
                            pass
                        else:
                            print("ID da Venda não existe")
                            print("Voltando ao menu principal")
                            input("aperte [Enter↵] para continuar")
                            opcao = False
                            break
                    except:
                        print("comando invalido. Tente novamente")
            case "0":
                opcao = False
            case _:
                print("comando inválido, tente novamente")
                input("aperte [Enter↵] para continuar")
                op = "rodarWhile"
        
    return opcao