# arquivo python que gera arquivos de texto SQL para criar tabelas
# essas funções devem ser usado com a conexão banco.
import json

def CriarTodasTabelas(barbeariaDB):
    # função só funciona uma vez depois buga.
    # esta função serve para criar todas as tabelas que existe nesse arquivo. precisa importar classConexão e json
    try:
        with open("control\statusTabelas.json", 'r') as arquivoJson:
            chave = json.load(arquivoJson)
    
        if chave["status"] == "criada":
            pass
    except:
        try:
            resultadoCliente = barbeariaDB.manipularBanco(criarTabelaClientes())
            resultadoProduto = barbeariaDB.manipularBanco(criarTabelaProdutos())
            resultadoVendas = barbeariaDB.manipularBanco(criarTabelaVendas())
            resultadoItens = barbeariaDB.manipularBanco(criarTabelaItens())
            resultadoAgendamento = barbeariaDB.manipularBanco(criarTabelaAgendamentos())

            statusTabela = { "status" : "criada" }
            with open("control\statusTabelas.json", 'w') as arquivoJson:
                json.dump(statusTabela , arquivoJson, indent=2)
        except:
            print("verfique o banco de dados")

#__________________ tabelas sql __________________________

def criarTabelaClientes():
    sql ='''CREATE TABLE "clientes" (
    "cliente_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "cliente_nome" varchar(255) NOT NULL,
    "cliente_telefone" varchar(255) NOT NULL DEFAULT 'não informado',
    "cliente_email" varchar(255) NOT NULL DEFAULT 'não informado'
    );
    '''
    return sql

def criarTabelaProdutos():
    sql = '''CREATE TABLE "produtos" (
    "produto_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "produto_nome" varchar(255) NOT NULL,
    "produto_preco" numeric(6,2) NOT NULL,
    "produto_quantidade" int NOT NULL,
    "produto_tipo" varchar(255) NOT NULL DEFAULT 'Produto'
    );
    '''
    return sql


def criarTabelaVendas():
    sql = '''CREATE TABLE "vendas" (
    "venda_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "cliente_id" int NOT NULL,
    "venda_horario" varchar(255) NOT NULL,
    CONSTRAINT fk_cliente
        FOREIGN KEY ("cliente_id")
        REFERENCES "clientes"("cliente_id")
        ON DELETE CASCADE ON UPDATE CASCADE
    );
    '''
    return sql


def criarTabelaItens():
    sql = '''CREATE TABLE "itens" (
    "item_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "venda_id" int,
    "produto_id" int,
    "item_quantidade" int,
    CONSTRAINT fk_vendas
        FOREIGN KEY ("venda_id")
        REFERENCES "vendas"("venda_id")
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_produto
        FOREIGN KEY ("produto_id")
        REFERENCES "produtos"("produto_id")
        ON DELETE CASCADE ON UPDATE CASCADE
    );
    '''
    return sql

def criarTabelaAgendamentos():
    sql ='''CREATE TABLE "agendamentos" (
    "agendamento_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "cliente_id" int NOT NULL,
    "produto_id" int NOT NULL,
    "agendamento_horario" varchar(255),
    
    CONSTRAINT fk_cliente
        FOREIGN KEY ("cliente_id")
        REFERENCES "clientes"("cliente_id")
        ON DELETE CASCADE ON UPDATE CASCADE,
    
    CONSTRAINT fk_produto
        FOREIGN KEY ("produto_id")
        REFERENCES "produtos"("produto_id")
        ON DELETE CASCADE ON UPDATE CASCADE
    );
    '''
    return sql