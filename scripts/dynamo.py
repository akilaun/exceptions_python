import boto3

#Acesso ao dynamo
#DEV
access_key_id = ''
secret_access_key = ''
region = 'us-east-2'

#Escolher a tabela que eu quero conectar
table_name = 'tabela'

# Aqui será necessário colocar todas as informações dos atributos da tabela
consumer_id = 0000000 #ID do consumidor
tipo = 'cash' #Forma de pagamento bloqueada

# Criar o cliente do DynamoDB e conectar à tabela selecionada
try:
    dynamodb = boto3.client('dynamodb', region_name=region, aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

    # Consultar o item usando a chave primária como um dicionário
    response = dynamodb.get_item(
        TableName=table_name,
        Key={
            'consumerId': {'N': str(consumer_id)}, # Tipo numero
            'type': {'S': tipo} # Tipo string
        }
    )
    # Verificar se o item foi encontrado
    if 'Item' in response:
        item = response['Item']
        print("Item encontrado:")
        print(item)
    else: # Se não foi encontrado
        print("Item não encontrado.")
except Exception as e:
    print("Erro ao conectar-se ao DynamoDB:", e)