import pymssql

def connDatabase():
    server = '192.168.5.10' 
    database = 'gestao_publica_buriti_alegre' 
    username = 'sa' 
    password = 'sigep@2019' 

    conn = pymssql.connect(server, username, password, database)
    #cursor = conn.cursor()

    #cursor.execute("SELECT @@version;") 
    #row = cursor.fetchone() 
    #while row: 
    #	print(row[0])
    #	row = cursor.fetchone()

    return conn