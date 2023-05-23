class Livro:
    def __init__(self, id, nome, quantidade, lançamento):
        self._id=id
        self._nome=nome
        self._lançamento=lançamento
        self._quantidade= quantidade
    def inserirLivro(self):
        sql=f"""
        INSERT INTO "Livro"
        Values(default,'{self._nome}','{self._lançamento}','{self._quantidade}')
        """
        
        return sql

    def atualizar(self):
        sql=f"""
        Update "Livro"
        set
        "Nome_Livro"='{self._nome}',
        "Lançamento_Livro"='{self._lançamento}',        
        "Quantidade"='{self._quantidade}'
        where "id_Livro" = '{self._id}'
        """
        
        return sql