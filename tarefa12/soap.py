import requests
from xml.dom.minidom import parseString
# URL do serviço SOAP
url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

codigo = input("Digite o código do país:")
operacao = input("1 telefone, 2 moeda 3 nome país:")
if operacao == "1":
    funcao = "CountryIntPhoneCode"
elif operacao == "2":
    funcao = "CountryCurrency"
elif operacao == "3":
    funcao = "CountryName"
else:
    print("erro")
    exit()

# XML estruturado
payload = f"""<?xml version=\"1.0\" encoding=\"utf-8\"?>
			<soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">
				<soap:Body>
					<{funcao} xmlns=\"http://www.oorsprong.org/websamples.countryinfo\">
						<sCountryISOCode>{codigo}</sCountryISOCode>
					</{funcao}>
				</soap:Body>
			</soap:Envelope>"""
# headers
headers = {
	'Content-Type': 'text/xml; charset=utf-8'
}
# request POST
response = requests.request("POST", url, headers=headers, data=payload)

# imprime a resposta
# print(response.text)
dom = parseString(response.text)
if operacao == "1":
    response = dom.documentElement.getElementsByTagName("m:CountryIntPhoneCodeResult")[0].firstChild.nodeValue
elif operacao == "2":
    response = dom.documentElement.getElementsByTagName("m:sName")[0].firstChild.nodeValue
elif operacao == "3":
    response = dom.documentElement.getElementsByTagName("m:CountryNameResult")[0].firstChild.nodeValue 
print(response)