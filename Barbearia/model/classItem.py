class Itens:
    def __init__(self):
        self._id = "id"
        self._produtoId= "produtoId"
        self._vendaId = "vendaID"
        self._quantidade = "quantidade"
    
    def setQuantidade(self,quantidade):
        self._quantidade = quantidade
    
    def setProdutoId(self,produtoID):
        self._produtoId = produtoID

    def setVendaId(self,listaIdVendas):
        self._vendaId = listaIdVendas[-1]


    def criarItem(self,):
        sql = f'''
        INSERT INTO "itens"
        Values(default, '{self._vendaId}', '{self._produtoId}', '{self._quantidade}')
        '''
        return sql