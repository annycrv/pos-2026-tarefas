from xml.dom.minidom import parse
import json

dom = parse("tarefa09/imobiliaria.xml")
imobiliaria = dom.documentElement

imoveis = imobiliaria.getElementsByTagName('imovel')

dados = []

for im in imoveis:
    pt = im.getElementsByTagName("proprietario")[0]
    end = im.getElementsByTagName("endereco")[0]
    car = im.getElementsByTagName("caracteristicas")[0]

    telefones = []
    for tel in pt.getElementsByTagName("telefone"):
        if tel.firstChild:
            telefones.append(tel.firstChild.data)

    email = None
    if pt.getElementsByTagName("email"):
        node = pt.getElementsByTagName("email")[0]
        if node.firstChild: 
            email = node.firstChild.data

    numero = None
    if end.getElementsByTagName("número"):
        node = end.getElementsByTagName("número")[0]
        if node.firstChild:
            numero = node.firstChild.data

    item = {
        "descricao": im.getElementsByTagName("descricao")[0].firstChild.data,

        "proprietario": {
            "nome": pt.getElementsByTagName("nome")[0].firstChild.data,
            "telefones": telefones,
            "email": email
        },

        "endereco": {
            "rua": end.getElementsByTagName("rua")[0].firstChild.data,
            "bairro": end.getElementsByTagName("bairro")[0].firstChild.data,
            "cidade": end.getElementsByTagName("cidade")[0].firstChild.data,
            "numero": numero
        },

        "caracteristicas": {
            "tamanho": car.getElementsByTagName("tamanho")[0].firstChild.data,
            "numQuartos": car.getElementsByTagName("numQuartos")[0].firstChild.data,
            "numBanheiros": car.getElementsByTagName("numBanheiros")[0].firstChild.data
        },

        "valor": im.getElementsByTagName("valor")[0].firstChild.data
    }

    dados.append(item)

with open("imobiliaria.json", "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=4)

    print("Dados convertidos!!!")
