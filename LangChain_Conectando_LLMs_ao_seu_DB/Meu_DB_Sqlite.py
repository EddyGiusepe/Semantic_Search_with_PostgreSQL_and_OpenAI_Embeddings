"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro


LangChain: Connecting LLMs To Your Database
===========================================

Este script foi baseado no Tutorial do "Prince Krampah".
Este script apenas me permite fazer a conexão com meu DB Sqlite.
Aqui usamos a Extensão do VSC: "SQLite3 Editor". Esta extensão me permitirá inserir dados
pela interface gráfica.

Instalar as dependências:

$ pip install -r requirements.txt
"""
import sqlite3

conn = sqlite3.connect('product_db.db')
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS products
          (
            [id] INTEGER PRIMARY KEY, 
            [name] TEXT, 
            [supplier] TEXT, 
            [store] TEXT
          )
          ''')

c.execute('''
          CREATE TABLE IF NOT EXISTS prices
          (
              [id] INTEGER PRIMARY KEY, 
              [price] INTEGER,
              [discount_pcnt] INTEGER
          )
          ''')

conn.commit()
