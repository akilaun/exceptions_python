from cliente import Cliente, Conta

try:
    #Preencher os dados do cliente
    consumer = Cliente(
        nome = str(input("Insira um nome: ")),
        cpf = int(input("Insira a CPF: ")),
        rg = str(input("Insira o RG: ")),
        email = str(input("Insira o email: "))
    )
    consumer.ativado() #Ativa o cliente
    

    #Preencher dados do banco do cliente
    bank = Conta(
        nome = str(input("Insira o nome do banco: ")),
        descricao = str(input("Insira o tipo da conta: "))
    )
    bank.sacar(
        valor = float(input("Insira o valor do saque: ")),
    )
    bank.depositar(
        valor = float(input("Insira o valor do deposito: ")),
    )
    print(f"\n{consumer}")
    print(f"\n{bank}\n")
    bank.exibir_extrato()
    print("\n")
    

except Exception as e:
    print(f"\nOcorreu um erro, {e}")