import sqlite3  #IMPORTA SGBD SQLITE
from sqlite3 import Error

def conectar():
    try:
        global con, cur
        con = sqlite3.connect('Empresa_Sergio.db')  #CRIA CONEXAO PADRAO
        cur = con.cursor()  # CRIA CURSOR # PADRAO
    except Error as erro:
        print('Erro de conexão.')


def criartabela():
    try:
        conectar()
        cur.execute('create table materiais (codigo integer primary key,' \
             'nome varchar (100),' \
            'quantidade integer)')  # CRIA TABELA
        print('Tabela de materiais criada com sucesso no banco de dados.')
    except:
        pass