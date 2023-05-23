class Aluguel:
    def __init__(self, id, _idCliente, idLivro, Entregue):
        self._idAluguel =id
        self._idCliente =_idCliente
        self._idLivro = idLivro
        self._Entregue = Entregue

    def inserirAluguel(self):
        sql=f"""
        INSERT INTO "Aluguel"
        Values(default,'{self._idCliente}','{self._idLivro}',default)
        """

        return sql
    
    def Retirar(self,quantidade):
        sql=f"""
        Update "Livro"
        set "Quantidade" = '{int(quantidade)-1}'
        where "id_Livro"='{self._idLivro}' """

        return sql
