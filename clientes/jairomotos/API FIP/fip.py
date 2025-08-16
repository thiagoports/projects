import requests
import unicodedata

# Funções de consulta Fipe
def buscar_marcas():
    url = "https://parallelum.com.br/fipe/api/v1/motos/marcas"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return []

def buscar_modelos(codigo_marca):
    url = f"https://parallelum.com.br/fipe/api/v1/motos/marcas/{codigo_marca}/modelos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["modelos"]
    return []

def buscar_anos(codigo_marca, codigo_modelo):
    url = f"https://parallelum.com.br/fipe/api/v1/motos/marcas/{codigo_marca}/modelos/{codigo_modelo}/anos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return []

def buscar_valor(codigo_marca, codigo_modelo, codigo_ano):
    url = f"https://parallelum.com.br/fipe/api/v1/motos/marcas/{codigo_marca}/modelos/{codigo_modelo}/anos/{codigo_ano}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["Valor"]
    return None

def remover_acentos(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

def encontrar_codigo(lista, nome):
    for item in lista:
        if remover_acentos(nome.lower()) in remover_acentos(item['nome'].lower()):
            return item['codigo']
    return None

# Programa principal
def main():
    print("=== Jairo Motos - Consulta Fipe ===")
    operacao = input("Deseja Compra ou Troca? (C/T): ").upper()

    # Marca
    nome_marca = input("Digite o nome da marca da moto: ")
    marcas = buscar_marcas()
    codigo_marca = encontrar_codigo(marcas, nome_marca)
    if not codigo_marca:
        print("Marca não encontrada.")
        return

    # Ano
    ano_input = input("Digite o ano da moto (ex: 2022): ")

    # Buscar todos os modelos da marca
    modelos = buscar_modelos(codigo_marca)

    # Filtrar modelos disponíveis para o ano digitado
    modelos_disponiveis = []
    for m in modelos:
        anos_modelo = buscar_anos(codigo_marca, m['codigo'])
        for a in anos_modelo:
            if a['nome'].startswith(ano_input):
                modelos_disponiveis.append(m)
                break

    if not modelos_disponiveis:
        print(f"Nenhum modelo encontrado para o ano {ano_input}.")
        return

    # Listar modelos para escolha
    print("\nModelos disponíveis nesse ano:")
    for idx, m in enumerate(modelos_disponiveis, 1):
        print(f"{idx}. {m['nome']}")

    while True:
        escolha = input("Digite o número do modelo correto (ou '0' para cancelar): ")
        if escolha == '0':
            print("Operação cancelada pelo usuário.")
            return
        if escolha.isdigit():
            num = int(escolha)
            if 1 <= num <= len(modelos_disponiveis):
                codigo_modelo = modelos_disponiveis[num - 1]['codigo']
                break
        print("Opção inválida. Tente novamente.\n")

    # Filtrar anos exatos do modelo escolhido
    anos_disponiveis = buscar_anos(codigo_marca, codigo_modelo)
    codigo_ano = None
    for a in anos_disponiveis:
        if a['nome'].startswith(ano_input):
            codigo_ano = a['codigo']
            break
    if not codigo_ano:
        print("Ano não encontrado para o modelo selecionado.")
        return

    # Valor Fipe
    valor_fipe = buscar_valor(codigo_marca, codigo_modelo, codigo_ano)
    if not valor_fipe:
        print("Não foi possível obter o valor da Fipe.")
        return
    print(f"\nValor Fipe da moto: {valor_fipe}")

    # Lógica de Compra ou Troca
    desconto = 1500
    valor_fipe_float = float(valor_fipe.replace("R$", "").replace(".", "").replace(",", "."))

    if operacao == "C":
        valor_final = valor_fipe_float - desconto
        print(f"Valor para compra (descontando R$ {desconto}): R$ {valor_final:.2f}")
    elif operacao == "T":
        valor_sua_moto = int(input("Digite o valor da sua moto: R$ "))
        valor_cliente = int(valor_fipe_float - desconto)
        print(f"Valor da moto do cliente após desconto: R$ {valor_cliente}")

        if valor_cliente > valor_sua_moto:
            diferenca = valor_cliente - valor_sua_moto
            print(f"Você deve devolver R$ {diferenca}")
        else:
            diferenca = valor_sua_moto - valor_cliente
            print(f"O cliente deve pagar R$ {diferenca}")
    else:
        print("Operação inválida.")

if __name__ == "__main__":
    main()
