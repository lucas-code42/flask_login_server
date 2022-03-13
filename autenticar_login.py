import mysql.connector
from acess import MysqlAcess


global user_acess
user_acess = MysqlAcess.user_acess()

global password_acess
password_acess = MysqlAcess.password_acess()

def autenticar_mysql(user, password):
    lista = []
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='flask_server_login',
                                            user=user_acess,
                                            password=password_acess)

        sql_query = f'SELECT nome FROM usuarios WHERE nome="{user}"'
        cursor = connection.cursor()
        cursor.execute(sql_query)
        records_user = cursor.fetchall()

        sql_query = f'SELECT senha FROM usuarios WHERE senha="{password}"'
        cursor = connection.cursor()
        cursor.execute(sql_query)
        records_pass = cursor.fetchall()

        for i in records_user:
            for j in i:
                record_user = j

        for i in records_pass:
            for j in i:
                record_pass = j

        lista.append(record_user)
        lista.append(record_pass)
        print('ok')
        return lista
    
    except:
        print('Erro de conexão com banco de dados / usuário ou senha não senha não encontrados.')
        return False

# user = input('user: ')
# password = input('pass: ')
# obj = autenticar(user, password)