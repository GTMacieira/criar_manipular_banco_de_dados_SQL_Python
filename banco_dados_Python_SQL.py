#Projeto baseado em 'https://www.freecodecamp.org/portuguese/news/como-criar-e-manipular-bancos-de-dados-sql-com-python/' de 26/08/2022
#password = Pyth0n&SQLP@ss
#Biblioteca para que o Python e o sql se comuniquem
#pip install mysql-connector-python
#Biblioteca pandas
#pip install pandas

#importar o mysql.connector e o pandas para o projeto, a função Error foi importada separada para fácil acesso
import mysql.connector
from mysql.connector import Error
import pandas as pd

#Função que para conectar no MySQL Server
def create_server_connection(host_name, user_name, user_password):
    #Encerra qualquer conexão
    connection = None
    #Tenta criar a conxão
    try:
        connection=mysql.connector.connect(
            host=host_name,
            port=3306,
            user=user_name,
            #passwd=user_password
        )
        print("MySQL Dtabase connection successful")
    #Texto caso não consiga conectar
    except Error as err:
        print(f"Error: {err}")
    return connection


#Função que recebe dois argumentos e executa uma consulta no servidor através da conexão
def create_database(connection, query):
    cursor = connection.cursor()
    #tentar criar banco de dados
    try:
        cursor.execute(query)
        print("Dtabase created succrssfully")
    #Texto caso não consiga
    except Error as err:
        print(f'Error: {err}')

#conectar diretamente em um banco de dados especifico
def create_db_connection(host_name,user_name,User_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            port=3306,
            user = user_name,
            #passwd = user_password,
            database = db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f'Error: {err}')
    return connection

#garante que os comandao detalhados na consulta SQK sajam implementados
def execute_query(connection,query):
    cursor=connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('Query successful')
    except Error as err:
        print(f'Error: {err}')

create_titles_table = """"
CREATE TABLE titles(
    title_id INT PRIMARY KEY,
    title_name VARCHAR(40) NOT NULL,
    jp_title VARCHAR(100) NOT NULL,
    released_chaps INT NOT NULL,
    read_chaps INT,
    last_down DATE NOT NULL,
    kindle VARCHAR(3),
    status INT
    );
    """

pw= 'Pyth0n&SQLP@ss'
connection = create_db_connection('localhost', 'root', pw, 'lista_de_mangás')
#create_database_query = "CREATE DATABASE lista_de_mangás"
#create_database(connection,create_database_query)
execute_query(connection,create_titles_table)


