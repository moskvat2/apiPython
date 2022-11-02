from flask import Flask, request, jsonify
from api.data.database import connDatabase
from api.main import app

    # Funcoes da API
def getPerson():
    users = []
    try:
        conn = connDatabase()
        cursor = conn.cursor()

        cursor.execute("SELECT @@version;") 
        row = cursor.fetchone() 
        while row: 
            print(row[0])
            row = cursor.fetchone()
    except:
        users = []
    return users
