import zeep

# define a URL do WSDL
# troca
wsdl_url = "http://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"

# inicializa o cliente zeep
client = zeep.Client(wsdl=wsdl_url)

number = (input("Digite o Número:"))
# faz a chamada do serviço
# apenas troca essa função quando for usar
result = client.service.NumberToWords(
	ubiNum=number
)
# imprime o resultado
print(f"{result}")