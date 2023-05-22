
class Agendamentos:
    def __init__(self):
        self._id = "id"
        self._agendaHorarios = [
        '08:00', '08:30', '09:00', '09:30', '10:00', '10:30'
        , '11:00', '11:30', '14:00', '14:30', '15:00', '15:30',
        '16:00', '16:30', '17:00', '17:30', '18:00', '18:30'
        ]
        self._clienteID = "clienteID"
        self._produtoID = "servicoID"
        self._horario = "horário"

    def _inputAgenda(self):
        
        self._clienteID = input("Insira o ID do cliente: ")
        self._produtoID= input("Insira o ID do serviço: ")
        self._horario = input("Insira o horário do agendamento: ")

    def verAgenda(self):
        sql = f'''
        SELECT * FROM "agendamentos"
        ORDER BY "agendamento_id" ASC
        '''
        return sql
    def Buscar(self, id, tipo):
        sql=f'''
        Select "{tipo}_nome" from "{tipo}s"
        where "{tipo}_id" = '{id}'
        '''
        return sql

    def ListaHorariosAgenda(self,resultado):
        listaHorasAgenda = []
        for agendamento in resultado:
            listaHorasAgenda.append(agendamento[3])
        return listaHorasAgenda

    def inserirAgendamento(self,clienteID, servicoID, Horario, tipo=None):
        if tipo == None:
            Horario=self._horario

        sql = f'''
        INSERT INTO "agendamentos"
        Values(default, '{clienteID}', '{servicoID}', '{Horario}')
        '''
        return sql

    def atualizarAgenda(self, agendaID):   
        opCampo = "rodar while"
        while not(opCampo in "1|2|3|4|0"):
            print('''
            qual campo deseja atualizar do agendamento?
            
            [1] 🔤 ID do Cliente
            [2] 📱 ID do serviço
            [3] 📧 Horário
            [4] Todos
            [0] ↩️ Voltar ao menu principal
            ''')
            opCampo = input(": ")
            match opCampo:
                case "1":
                    self.cliente_id = input("Insira o ID do cliente: ")
                    sql = f'''
                        UPDATE "agendamentos"
                        SET "cliente_id" = '{self._clienteID}'
                        WHERE "agendamento_id" = '{agendaID}';
                        '''
                case "2":
                    self._produtoID = input("Insira o número de telefone do cliente: ")
                    sql = f'''
                        UPDATE "agendamentos"
                        SET "produto_id" = '{self._produtoID}'
                        WHERE "agendamento_id" = '{agendaID}';
                        '''
                case "3":
                    self._horario = input("Insira o email do cliente: ")
                    sql = f'''
                        UPDATE "agendamentos"
                        SET "agendamento_horario" = '{self._horario}'
                        WHERE "agendamento_id" = '{agendaID}';
                        '''
                case "4":
                    self._inputAgenda()
                    sql = f'''
                    UPDATE "agendamentos"
                    SET "cliente_id" = '{self._clienteID}',
                        "produto_id" = '{self._produtoID}',
                        "agendamento_horario" = '{self._horario}'
                    WHERE "agendamento_id" = '{agendaID}';
                    '''
                case "0":
                    sql = None
                case _:
                    print("comando inválido Tente novamente")
                    input("aperte [Enter↵] para continuar")

            return sql

    def deletarAgenda(self,agendaID):
            sql = f''' DELETE 
        FROM "agendamentos"
        WHERE "agendamento_id" = '{agendaID}';
        '''
            return sql

    def deletarTodaAgenda(self):
            sql = f''' DELETE 
        FROM "agendamentos";
        '''
            return sql