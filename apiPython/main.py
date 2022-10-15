from flask import Flask, request, jsonify #added to top of file
from flask_cors import CORS #added to top of file
import json, sqlite3

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

    # funcao de conexao com bando de dados
def connect_to_db():
        conn = sqlite3.connect('database.db')
        return conn

    # Funcoes da API
def create_db_table():
    try:
        conn = connect_to_db()
        conn.execute('''CREATE TABLE users (
            user_id INTEGER PRIMARY KEY NOT NULL,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            address TEXT NOT NULL,
            country TEXT NOT NULL); ''')

        conn.commit()
        print("User table created successfully")
    except:
        print("User table creation failed - Maybe table")
    finally:
        conn.close()

def insert_user(user):
    inserted_user = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        query = '''INSERT INTO users (username, password) VALUES (?, ?);'''
        cur.execute(query, (user["username"],user["password"]))
        conn.commit()
        inserted_user = get_user_by_id(cur.lastrowid)
    except:
        conn().rollback()
    finally:
        conn.close()

    return inserted_user

def get_users():
    users = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        query = "SELECT * FROM users;"
        cur.execute(query)

        rows = cur.fetchall()

        for i in rows:
            user = {}
            user["user_id"] = i["user_id"]
            user["username"] = i["username"]
            user["password"] = i["password"]
            users.append(user)
    except:
        users = []
    return users

def get_user_by_id(user_id):
    user = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        query = "SELECT * FROM users WHERE user_id = ?"
        cur.execute(query, (user_id,))
        row = cur.fetchone()

        # convert row object to dictionary
        user["user_id"] = row["user_id"]
        user["username"] = row["username"]
        user["password"] = row["password"]
    except:
        user = {}

    return user

def update_user(user):
    updated_user = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        query = '''UPDATE users SET username = ?, password = ? WHERE user_id =?'''
        cur.execute(query, (user["username"], user["password"], user["user_id"],))

        conn.commit()
        updated_user = get_user_by_id(user["user_id"])

    except:
        conn.rollback()
        updated_user = {}
    finally:
        conn.close()

    return updated_user

def delete_user(user_id):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE from users WHERE user_id = ?",     
                      (user_id,))
        conn.commit()
        message["status"] = "User deleted successfully"
    except:
        conn.rollback()
        message["status"] = "Cannot delete user"
    finally:
        conn.close()

    return message

    # Defnir as rotas da API
@app.route('/')
def start():
    return "API is running"

@app.route('/api/users', methods=['GET'])
def api_get_users():
    return jsonify(get_users())

@app.route('/api/users/<user_id>', methods=['GET'])
def api_get_user(user_id):
    return jsonify(get_user_by_id(user_id))

@app.route('/api/users/add',  methods = ['POST'])
def api_add_user():
    user = request.get_json()
    return jsonify(insert_user(user))

@app.route('/api/users/update',  methods = ['PUT'])
def api_update_user():
    user = request.get_json()
    return jsonify(update_user(user))

@app.route('/api/users/delete/<user_id>',  methods = ['DELETE'])
def api_delete_user(user_id):
    return jsonify(delete_user(user_id))

if __name__ == "__main__":
    app.debug = True
    #app.run(debug=True)
    app.run() #run app