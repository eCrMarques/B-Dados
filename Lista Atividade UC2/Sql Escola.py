import psycopg2

try:
    conn = psycopg2.connect(dbname="Escola 2",host='localhost',port='5432', user='postgres', password= 'postgres')

    cursor= conn.cursor()
    print("Conectado com Sucesso")

    cursor.execute("""
    CREATE TABLE "Aluno"(
    "NroMatricula" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome" varchar(255) NOT NULL,
    "Cpf" char(11) NOT NULL,
    "Endereço" varchar(255) default 'Não Informado',
    "Telefone" char(11) default 'xx-xxxx',
    "Ano Nascimento" int,
    Primary key ("NroMatricula")
    )
    """)

    
    cursor.execute("""
    CREATE TABLE "Disciplina"(
    "CodDisciplina" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "nome_Disciplina" varchar(255) NOT NULL,
    "cod_Curso" int NOT NULL default '0'
    )
    """)

    cursor.execute("""
    CREATE TABLE "Matricula"(
    "NroMatricula" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "CodDisciplina" varchar(255) NOT NULL,
    "Semestre" varchar(255) NOT NULL,
    "Ano" int default 'Não Informado',
    "Nota" numeric default 'xx-xxxx',
    "NroFaltas" int,
    Primary key ("NroMatricula")
    )
    """)

    conn.commit()
    conn.close()
except(Exception,psycopg2.Error) as error:
    print('Algo deu errado',error)