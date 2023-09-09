import sqlite3
from constantes import  NOME_BANCO

conexao = sqlite3.connect(NOME_BANCO)  # Crear la base de datos
cursor = conexao.cursor()  # Manipulación de la base de datos
cursor.execute(
    """
    CREATE TABLE clientes (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) NOT NULL,
    email VARCHAR(30) NOT NULL,
    fone VARCHAR(11),
    cidade VARCHAR(30) NOT NULL,
    uf VARCHAR(2) NOT NULL,
    created_at DATE DEFAULT CURRENT_TIMESTAMP
    );
    """
)
print("Tabla creada con éxito!")