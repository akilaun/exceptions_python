import sqlite3
from constantes import NOME_BANCO

conexao = sqlite3.connect(NOME_BANCO)
cursor = conexao.cursor()
cursor.execute(
    """
    INSERT INTO clientes (name, cpf, email, fone, cidade, uf)
    VALUES ('AKILA VISQUE BINDILATTI', 343147311800, 'akila_bindi@msn.com', 19981398833, 'Piracicaba', 'SP')
    ;
    """
)
conexao.commit()
conexao.close()
print("Insert realizado com sucesso")