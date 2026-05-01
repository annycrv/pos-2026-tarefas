import json

with open('imobiliaria.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

imoveis = dados

print('----- Imovéis ----- :')
for i in range(len(imoveis)):
    print(i + 1, '-', imoveis[i]['descricao'])

opcao = int(input('\nEscolha um imóvel entre as opções: '))

imovel = imoveis[opcao - 1]

print('\n----- Proprietário ----- \n')
proprietario = imovel['proprietario']
print('Nome:', proprietario['nome'])

if proprietario['email'] != None:
    print('Email:', proprietario['email'])
else:
    print('Email: Não informado')

if len(proprietario['telefones']) > 0:
    print('Telefone(s):', ', '.join(proprietario['telefones']))
else:
    print('Telefone(s): Não informado')

print('\n----- Endereço -----\n')

endereco = imovel['endereco']
print('Rua:', endereco['rua'])
print('Bairro:', endereco['bairro'])
print('Cidade:', endereco['cidade'])

if endereco['numero'] != None:
    print('Número:', endereco['numero'])
else:
    print('Número: S/N')

print('\n----- Características ----- \n')
caracteristicas = imovel['caracteristicas']
print('Descrição:', imovel['descricao'])
print('Tamanho:', caracteristicas['tamanho'])
print('Quartos:', caracteristicas['numQuartos'])
print('Banheiros:', caracteristicas['numBanheiros'])
print('Valor:', imovel['valor'])