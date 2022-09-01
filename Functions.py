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