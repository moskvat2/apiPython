
  
  
import sqlite3
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao banco de dados SQLite com FastAPI"}

@app.get("/criar-db")
def criar_banco_dados():
    conn = sqlite3.connect('produtos.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE produtos (
            id	INTEGER,
            nome	TEXT,
            preco	REAL,
            PRIMARY KEY(id)
    )""")
    conn.commit()
    conn.close()
    return {"message": "Banco de dados criado com sucesso!"}

@app.get("/adicionar-itens")
def adicionar_itens():
    conn = sqlite3.connect('produtos.db')
    c = conn.cursor()
    c.execute("INSERT INTO produtos VALUES (1, 'Arroz', 5.00)")
    c.execute("INSERT INTO produtos VALUES (2, 'Feijao', 3.50)")
    c.execute("INSERT INTO produtos VALUES (3, 'Carne', 8.00)")
    c.execute("INSERT INTO produtos VALUES (4, 'Salada', 2.50)")
    c.execute("INSERT INTO produtos VALUES (5, 'Bebida', 4.00)")
    conn.commit()
    conn.close()
    return {"message": "Itens adicionados com sucesso!"}

@app.get("/listar-itens")
def listar_itens():
    conn = sqlite3.connect('produtos.db')
    c = conn.cursor()
    c.execute("SELECT * FROM produtos")
    itens = c.fetchall()
    conn.close()
    return itens

@app.post("/adicionar-itens-pedido")
def adicionar_itens_pedido(id_item: int):
    conn = sqlite3.connect('produtos.db')
    c = conn.cursor()
    c.execute("SELECT * FROM produtos WHERE id = ?", (id_item,))
    item = c.fetchone()
    c.execute("INSERT INTO itensPedido VALUES (?)", (item[0],))
    conn.commit()
    conn.close()
    return {"message": "Item adicionado com sucesso!"}