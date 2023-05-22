class Clientes:
    def __init__(self):
        self._id = "id"
        self._nome = "nome"
        self._telefone = "telefone"
        self._email = "email" # ideia! mudar email para endereço eletronico qualquer, como instagram, facebook e etc

    def _inputCliente(self):
        
        self._nome = input("Insira o nome do cliente: ")
        self._telefone = input("Insira o número de telefone do cliente: ")
        self._email = input("Insira o email do cliente: ")
    
    def verCliente(self):
        # ideia! talvez mudar o ordenamento da lista por nome(ordem alfabética) do que por ID
        sql = f'''
        SELECT * FROM "clientes"
        ORDER BY "cliente_id" ASC
        '''
        return sql

    def inserirNovoCliente(self, tipo=None, nomecliente=None, telefone=None, email=None):
        if tipo ==None:
            print("Insira os dados do Cliente")
            
            self._inputCliente()

        sql = f'''
        INSERT INTO "clientes"
        Values(default, '{nomecliente}', '{telefone}', '{email}')
        '''
        return sql

    def atualizarCliente(self, clienteID):   
        opCampo = "a"
        while not(opCampo in "1|2|3|4|0"):
            print('''
            qual campo deseja atualizar do Cliente?
            
            [1] 🔤 Nome
            [2] 📱 Telefone
            [3] 📧 Email
            [4] Todos
            [0] ↩️ Voltar ao menu principal
            ''')
            opCampo = input(": ")
            match opCampo:
                case "1":
                    self._nome = input("Insira o nome do cliente: ")
                    sql = f'''
                        UPDATE "clientes"
                        SET "cliente_nome" = '{self._nome}'
                        WHERE "cliente_id" = '{clienteID}';
                        '''
                case "2":
                    self._telefone = input("Insira o número de telefone do cliente: ")
                    sql = f'''
                        UPDATE "clientes"
                        SET "cliente_telefone" = '{self._telefone}'
                        WHERE "cliente_id" = '{clienteID}';
                        '''
                case "3":
                    self._email = input("Insira o email do cliente: ")
                    sql = f'''
                        UPDATE "clientes"
                        SET "cliente_email" = '{self._email}'
                        WHERE "cliente_id" = '{clienteID}';
                        '''
                case "4":
                    self._inputCliente()
                    sql = f'''
                    UPDATE "clientes"
                    SET "cliente_nome" = '{self._nome}',
                        "cliente_telefone" = '{self._telefone}',
                        "cliente_email" = '{self._email}'
                    WHERE "cliente_id" = '{clienteID}';
                    '''
                case "0":
                    sql = None
                case _:
                    print("comando inválido Tente novamente")
                    input("aperte [Enter↵] para continuar")

            return sql
    
    def deletarCliente(self,clienteID):
        sql = f''' DELETE 
    FROM "clientes"
    WHERE "cliente_id" = '{clienteID}';
    '''
        return sql