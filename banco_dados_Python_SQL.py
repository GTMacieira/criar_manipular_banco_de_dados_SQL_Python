#Projeto baseado em 'https://www.freecodecamp.org/portuguese/news/como-criar-e-manipular-bancos-de-dados-sql-com-python/' de 26/08/2022
#password = Pyth0n&SQLP@ss
#Biblioteca para que o Python e o sql se comuniquem
#pip install mysql-connector-python
#Biblioteca pandas
#pip install pandas

#importar o mysql.connector e o pandas para o projeto, a função Error foi importada separada para fácil acesso
from unittest import result
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

#garante que os comandao detalhados na consulta SQL sajam implementados
def execute_query(connection,query):
    cursor=connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('Query successful')
    except Error as err:
        print(f'Error: {err}')


create_titles_table = """
CREATE TABLE titles (
    title_id INT PRIMARY KEY,
    title_name VARCHAR(40) NOT NULL,
    jp_title VARCHAR(40) NOT NULL,
    genre_type VARCHAR(20),
    abstract_title VARCHAR(100),    
    publish_comp VARCHAR(50),
    released_chaps INT NOT NULL,
    author_name VARCHAR(40),
    designer_name VARCHAR (40),
    read_chaps INT,
    last_down_date DATE NOT NULL,
    kindle BOOLEAN,
    status VARCHAR(15) NOT NULL
    );
"""

create_authors_table = """
CREATE TABLE authors (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(40) NOT NULL
    );
"""

create_designers_table = """
CREATE TABLE designers (
    designer_id INT PRIMARY KEY,
    designer_name VARCHAR(40) NOT NULL
    );
"""

create_genres_table = """
CREATE TABLE genres (
    genre_id INT PRIMARY KEY,
    type_genre VARCHAR(20) NOT NULL,
    genre_description VARCHAR(100)
    );
"""

create_status_table = """
CREATE TABLE status (
    status_id INT PRIMARY KEY,
    status_name VARCHAR(15)
    );
"""

alter_titles = """
ALTER TABLE titles
ADD FOREIGN KEY(author_name)
REFERENCES authors(author_name)
ON DELETE SET NULL;
"""
create_takestitles_table = """
CREATE TABLE take_titles (
    title_id INT,
    authors_id INT,
    desingners_id INT,
    genres_id INT,
    status_id INT,
    PRIMARY KEY(title_id,authors_id,desingners_id,genres_id,status_id),
    FOREIGN KEY(title_id) REFERENCES title(title_id) ON DELETE CASCADE,
    FOREIGN KEY(authors_id) REFERENCES title(authors_id) ON DELETE CASCADE,
    FOREIGN KEY(desingners_id) REFERENCES title(desingners_id) ON DELETE CASCADE,
    FOREIGN KEY(genres_id) REFERENCES title(genres_id) ON DELETE CASCADE,
    FOREIGN KEY(status_id) REFERENCES title(status_id) ON DELETE CASCADE
);
"""

pop_titles="""
INSERT INTO titles VALUES
(1, 'title_name', 'jp_title', 'genre_type', 'bstract_title', 'publish_comp(editora)', 'released_chaps', 'author_name', 'designer_name', 'read_chaps', 'last_down_date', 'kindle', 'status'),
(2, 'title_name', 'jp_title', 'genre_type', 'bstract_title', 'publish_comp(editora)', 'released_chaps', 'author_name', 'designer_name', 'read_chaps', 'last_down_date', 'kindle', 'status'),
(3, 'title_name', 'jp_title', 'genre_type', 'bstract_title', 'publish_comp(editora)', 'released_chaps', 'author_name', 'designer_name', 'read_chaps', 'last_down_date', 'kindle', 'status');
"""

pop_authors="""
INSERT INTO authors VALUES
(1001, 'authors_name'),
(1014, 'authors_name'),
(1015, 'authors_name');
"""

pop_designers="""
INSERT INTO designers VALUES
(2001, 'designer_name'),
(2002, 'designer_name'),
(2003, 'designer_name');

"""

pop_genres="""  
INSERT INTO genres VALUES
(3001, 'type_genre', 'genre_description'),
(3002, 'type_genre', 'genre_description'),
(3003, 'type_genre', 'genre_description'),
(3004, 'type_genre', 'genre_description');
"""

pop_status="""
INSERT INTO status VALUES
(4001, 'Não lido'),
(4002, 'Em leitura'),
(4003, 'Concluído');
"""

pop_taketitles="""
INSERT INTO take_titles VALUES
(1,1001,2001,3001,4001),
(2,1002,2002,3002,4002),
(3,1003,2003,3003,4003),
(4,1004,2004,3004,4004),
(5,1005,2005,3005,4005),
(6,1006,2006,3006,4006),
(7,1007,2007,3007,4007),
(8,1008,2008,3008,4008),
(9,1009,2009,3009,4009),
(10,1010,2010,3010,4010),
(11,1011,2011,3011,4011),
(12,1012,2012,3012,4012),
(13,1013,2013,3013,4013),
(14,1014,2014,3014,4014),
(15,1015,2015,3015,4015),
"""

pw= 'Pyth0n&SQLP@ss'

#criar conexão com o MySQL
#connection = create_server_connection("localhost","root",pw)

#Ceiar banco de dados lista_de_mangas
#create_database_query = "CREATE DATABASE lista_de_mangas"

#Acessa MySQL e cria lista_de _mangas no MySQL
#create_database(connection,create_database_query)

connection = create_db_connection('localhost', 'root', pw, 'lista_de_mangas')

#Criar tabelas
# execute_query(connection,create_titles_table)
# execute_query(connection,create_authors_table)
# execute_query(connection,create_designers_table)
# execute_query(connection,create_genres_table)
#execute_query(connection,create_status_table)

# execute_query(connection, alter_titles)
# execute_query(connection, create_takestitle_table)

#execute_query(connection, pop_titles)
# execute_query(connection, pop_authors)
# execute_query(connection, pop_designers)
# execute_query(connection, pop_genres)
execute_query(connection, pop_status)

#Leitura de dados

import mysql.connector
from mysql.connector import Error
import pandas as pd

def ready_query(connection, query):
    cursor = connection.curso()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f'Error: {err}')

#Selecionar toda a tabela titles
q1 = """
SELECT *
FROM titles;
"""
connection = creste_db_connection("localhost","root",pw, db)
results = ready_query(connection, q1)

for result in results:
    print(result)

##Formatar resultado em uma lista
#inicializa lista vazia
from_db=[]

#prcorrer os resultados e inseri-los á lista
#Retorna uma lista de tuplas
for result in results:
    result = result
    from_db.append(result)

##Formatar resultado em uma lista de listas
from_db = []

for result in results:
    result = list(result)
    from_db.append(result)

print(from_db)

##Formatar resultado em um DataFrame do Pandas
#Retorna uma lista de lista e cria um DataFrame do Pandas
from_db = []

for result in results:
    result = list(result)
    from_db.append(result)

columns = ['title_id', 'tile_name', 'author_name', 'kindle']
df = pd.DataFrame(from_db, columns=columns)
display(df)

#Atualizar registros
#Se executado sem o WHERE, todos os autores de todos o titulos serão alterados
update="""
UPDATE titles
SET author = 'nome aleatório'
WHERE title_id = 1;
"""
connection = create_db_connection('localhost', 'root', pw, db)
execute_query(connection, update)

#Apagar registro
delete_title = """
DELETE FROM titles
WHERE title_ID = 1;
"""

connection = create_db_connection('localhost', 'root', pw, db)
execute_query(connection, delete_title)