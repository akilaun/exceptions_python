import sqlite3  
from constantes import NOME_BANCO
from datetime import datetime

def inserir_cliente(name, cpf, email, fone, cidade, uf, created_at):
    conexao = sqlite3.connect(NOME_BANCO)
    cursor = conexao.cursor()
    cursor.execute(
        """
        INSERT INTO clientes 
        (name, cpf, email, fone, cidade, uf, created_at)
        VALUES (?,?,?,?,?,?,?)
        """, (name,cpf,email,fone,cidade,uf,datetime.now())
    )
    conexao.commit()
    conexao.close()

print("Seja bem vindo, digite as informações solicitadas")
nome = input("Digite seu nome: ")
cpf_i = input("CPF: ")
email_i = input("E-mail: ")
fone_i = input("Telefone: ")
cidade_i = input("Cidade: ")
estado = input("Estado: ")
criado_em = ()

inserir_cliente(nome, cpf_i, email_i, fone_i, cidade_i, estado, criado_em)

print("Dados cadastrados com sucesso!")