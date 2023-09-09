from faker import Faker
import sqlite3
from constantes import NOME_BANCO


fake = Faker("pt_BR")
conexao = sqlite3.connect(NOME_BANCO)
cursor = conexao.cursor()


for _ in range (5001):
    cursor.execute(    
        """
        INSERT INTO clientes 
        (name, cpf, email, fone, cidade, uf)
        VALUES (?,?,?,?,?,?)
        """, (fake.name(),
              fake.ssn(),
              fake.company_email(),
              fake.phone_number(),
              fake.city(),
              fake.country_code()
            )
    )

conexao.commit()
conexao.close()