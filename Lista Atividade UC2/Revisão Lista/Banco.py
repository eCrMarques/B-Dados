# Agora, vocês serão dividos aleatoriamente em duplas. Vocês enviarão a
# documentação criada para seu parceiro e receberão a documentação
# criada por ele. Sua tarefa é criar uma aplicação Python capaz de ler o
# JSON do colega e exibi
# r as seguintes informações:
# 1. Lista de funcionários
# 2. Lista de departamentos
# 3. Informações específicas de um funcionário (por exemplo, o nome,
# idade e cargo de um funcionário com um determinado ID)
# 4. Quais funcionários fazem parte de um departamento específico
# (por exemplo, listar os funcionários que pertencem ao
# departamento de Desenvolvimento)
# Dicas:
# ● Use a biblioteca json do Python para ler o arquivo JSON.
# ● Crie funções separadas para cada uma das informações
# solicitadas.
# ● Use a estrutura de dados adequada para implementar as funções
# de busca e filtragem necessárias

import json

with open('dados.json','r') as dados:
    lista=json.load(dados)
    
while True:
    print("""
        1- Ver Funcionarios
        2- Ver Departamentos
        3- Procurar Funcionario
        4- Funcionarios por Departamentos
        0- Sair""")
    
    opção=input('')
    match opção:
        case '1':
            print('--------Funcionarios---------')
            for funcionario in lista['funcionarios']:
                print(f'Id:{funcionario["id"]:<4}Nome:{funcionario["nome"]:<10}Cargo:{funcionario["cargo"]:<15}Id_Departamento:{funcionario["id_departamento"]:<10} ')
            input()

        case '2':
            print('--------Departamentos---------')
            for departamento in lista['departamentos']:
                print(f'Id:{departamento["id"]:<4}Nome:{departamento["nome"]:<15}Descrição:{departamento["descricao"]:<10}')
            input()

        case '3':
            id=input('Id do Funcionario: ')
            if id.isnumeric()==False or int(id)>len(lista['funcionarios']):
                print('Id indisponivel ou Inexistente')
            else:
                for funcionario in lista['funcionarios']:
                    if int(id)==funcionario["id"]:
                        for departamento in lista['departamentos']:
                            if funcionario["id_departamento"]==departamento["id"]:
                                nomeDp=departamento["nome"]
                        print(f'Id:{funcionario["id"]:<4}Nome:{funcionario["nome"]:<10}Cargo:{funcionario["cargo"]:<15}Id_Departamento: {nomeDp} ')
                        break
            input()

        case '4':
            dp=input("Id do Departamento: ")
            if dp.isnumeric()==False or int(dp)>len(lista['departamentos']): 
                print("Id indisponivel ou inexistente")
            else:
                print('--------Departamento---------')
                for departamento in lista["departamentos"]:
                    if int(dp)==departamento["id"]:
                        print(f'Id:{departamento["id"]:<4}Nome:{departamento["nome"]:<15}Descrição: {departamento["descricao"]:<10}\n')
                        nomeDp=departamento["nome"]
                print('--------Funcionarios---------')
                for funcionario in lista['funcionarios']:
                    if funcionario["id_departamento"]==int(dp):
                        print(f'Id:{funcionario["id"]:<4}Nome:{funcionario["nome"]:<10}Cargo:{funcionario["cargo"]:<15} Departamento: {nomeDp} ')
            input()
        
        case '0':
            break

        case _:
            print('Digite uma opção valida')