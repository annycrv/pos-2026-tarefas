from xml.dom.minidom import parse

dom = parse("tarefa08/cardapio.xml")
cardapio = dom.documentElement

pratos = cardapio.getElementsByTagName('prato')

print("----- MENU -----\n")

for prato in pratos:
    id = prato.getAttribute('id')
    nome = prato.getElementsByTagName('nome')[0].firstChild.nodeValue
    print(f"{id} - {nome}")

id_prato = input("Digite o id do prato para saber mais: ")

for prato in pratos:
    if prato.getAttribute('id') == id_prato:
        nome = prato.getElementsByTagName('nome')[0].firstChild.nodeValue
        descricao = prato.getElementsByTagName('descricao')[0].firstChild.nodeValue
        preco = prato.getElementsByTagName('preco')[0].firstChild.nodeValue
        calorias = prato.getElementsByTagName('calorias')[0].firstChild.nodeValue
        tempoPreparo = prato.getElementsByTagName('tempoPreparo')[0].firstChild.nodeValue

        print(f"\nNome: {nome}")
        print(f"Descrição: {descricao}")

        print("Ingredientes:")
        ingredientes = prato.getElementsByTagName('ingrediente')
        for ing in ingredientes:
            print(f"{ing.firstChild.nodeValue}")

        print(f"Preço: R${preco}")
        print(f"Calorias: {calorias}kcal")
        print(f"Tempo de preparo: {tempoPreparo}")