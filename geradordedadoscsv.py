import csv
import random
from faker import Faker

fake = Faker('pt_BR')

# Gerar tabela de vendas
vendas = []
for i in range(1, 501):
    venda = [
        i,
        fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d'),
        fake.word(),
        fake.word(),
        fake.name(),
        fake.name(),
        random.choice(['A', 'B', 'C']),
        random.randint(1, 10),
        round(random.uniform(10, 100), 2),
        0
    ]
    venda[-1] = round(venda[7] * venda[8], 2)  # Calcular valor total
    vendas.append(venda)

# Gerar tabela de produtos
produtos = []
for i in range(1, 21):
    produto = [
        i,
        fake.word(),
        fake.word()
    ]
    produtos.append(produto)

# Gerar tabela de clientes
clientes = []
for i in range(1, 101):
    cliente = [
        i,
        fake.name(),
        fake.phone_number(),
        fake.email()
    ]
    clientes.append(cliente)

# Gerar tabela de vendedores
vendedores = []
for i in range(1, 11):
    vendedor = [
        i,
        fake.name(),
        fake.phone_number(),
        fake.email()
    ]
    vendedores.append(vendedor)

# Gerar tabela de filiais
filiais = [
    ['A', 'Endereço A'],
    ['B', 'Endereço B'],
    ['C', 'Endereço C']
]

# Escrever tabelas em arquivos CSV
with open('dados/vendas.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Id', 'Data da Venda', 'Produto', 'Categoria', 'Cliente', 'Vendedor', 'Filial', 'Quantidade', 'Valor Unitário', 'Valor Total'])
    writer.writerows(vendas)

with open('dados/produtos.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Id', 'Produto', 'Categoria'])
    writer.writerows(produtos)

with open('dados/clientes.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Id', 'Nome', 'Telefone', 'Email'])
    writer.writerows(clientes)

with open('dados/vendedores.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Id', 'Nome', 'Telefone', 'Email'])
    writer.writerows(vendedores)

with open('dados/filiais.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Filial', 'Endereço'])
    writer.writerows(filiais)
