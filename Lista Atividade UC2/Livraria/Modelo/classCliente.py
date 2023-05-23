class Cliente:
    def __init__(self, Id, Nome, Telefone, Cpf):
        self._id=Id
        self._nome=Nome
        self._Telefone=Telefone
        self._Cpf=Cpf
    
    def inserirCliente(self):
        sql=f"""
        INSERT INTO "Cliente"
        Values(default,'{self._nome}','{self._Telefone}','{self._Cpf}')
        """
        
        return sql
    
    def atualizar(self):
        sql=f"""
        Update "Cliente"
        set
        "Nome_Cliente"='{self._nome}',
        "Telefone_Cliente"='{self._Telefone}',
        "Cpf_Cliente"='{self._Cpf}'
        where "id_Cliente" = '{self._id}'
        """

        return sql