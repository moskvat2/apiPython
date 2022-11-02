from flask import Flask, request, jsonify #added to top of file
from flask_cors import CORS #added to top of file
import json, pymssql

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

    # funcao de conexao com bando de dados
def connDB():
    server = '192.168.5.10' 
    database = 'gestao_publica_buriti_alegre' 
    username = 'sa' 
    password = 'sigep@2019' 

    conn = pymssql.connect(server, username, password, database)
    if not conn:
        print('Falha de comunicacao')
        
    return conn

    # Funcoes da API
def getPerson():
    users = []
    try:
        conn = connDB()
        cursor = conn.cursor()
        query = ''' select nome as name, 
                        cpf,
                        cnpj,
                        email,
                        id_tipo_pessoa as type_person
                    from pessoa p where 1 = 1'''
        cursor.execute(query) 
        
        row = cursor.fetchall() 
        print("Total rows are:", len(row))
        for registers in row:
            person = (registers[0], registers[1], registers[2], registers[3], registers[4])
            users.append(person)

        cursor.close()
    except:
        users = []
    return users

def get_user_by_id(nome):
    user = {}
    try:
        conn = connDB()
        cursor = conn.cursor()
        query = " select nome as name, \
                        cpf, \
                        cnpj, \
                        email, \
                        id_tipo_pessoa as type_person \
                    from pessoa p where nome like '?' "
        cursor.execute(query, (nome,))
        row = cursor.fetchone()

        # convert row object to dictionary
        user["nome"] = row["nome"]
    except:
        user = {}

    return user

    # Defnir as rotas da API
@app.route('/')
def start():
    return "API is running"

@app.route('/api/users', methods=['GET'])
def apiGetPerson():
    return jsonify(getPerson())

@app.route('/api/users/name=<nome>', methods=['GET'])
def api_get_user(nome):
    return jsonify(get_user_by_id(nome))

if __name__ == "__main__":
    app.debug = True
    #app.run(debug=True)
    app.run() #run app