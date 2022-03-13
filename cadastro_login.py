import mysql.connector
from acess import MysqlAcess


global user_acess
user_acess = MysqlAcess.user_acess()

global password_acess
password_acess = MysqlAcess.password_acess()

def cadastrar_mysql(nome,email, celular, senha):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='flask_server_login',
                                            user=user_acess,
                                            password=password_acess)
        
        mySql_insert_query = f"""INSERT INTO usuarios (nome, email, celular, senha) 
                            VALUES 
                            ('{nome}', '{email}', '{celular}', '{senha}') """
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        print(cursor.rowcount, "cadastro realizado com sucesso no Banco de dados")
        cursor.close()
        return True
    
    except mysql.connector.Error as error:
        print("Failed to insert record into Laptop table {}".format(error))
        return False

