import tabula
import json


dados = tabula.read_pdf("strings/Notas dos alunos.pdf", encoding="latin-1",pages="all")
print(dados)
