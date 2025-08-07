def mesCorrespondente():
    try:
        mesEscolhido = int(input("Digite um número de 1 a 12:\n"))
        match mesEscolhido:
            case 1:
                print("Janeiro")
            case 2:
                print("Fevereiro")
            case 3:
                print("Março")
            case 4:
                print("Abril")
            case 5:
                print("Maio")
            case 6:
                print("Junho")
            case 7:
                print("Julho")
            case 8:
                print("Agosto")
            case 9:
                print("Setembro")
            case 10:
                print("Outubro")
            case 11:
                print("Novembro")
            case 12:
                print("Dezembro")
            case _:
                print("Mês desconhecido")
    except Exception:
        print("A resposta deve ser um número")

#mesCorrespondente()

def mediaSimples():
    try:
        valorUm = int(input("Digite o primeiro valor:"))
        valorDois = int(input("Digite o segundo valor:"))
        valorTres = int(input("Digite o terceiro valor:"))

        if not valorUm or not valorDois or not valorTres:
            print(False)
            return
        
        if valorUm != 0 and valorDois != 0 and valorTres != 0:
            media = (valorUm + valorDois + valorTres) / 3
            print(f"A média é: {media}")
        else:
            print(False)
    except Exception:
        print(False)

#mediaSimples()

def parOuImpar():
    try:
        valorUm = int(input("Digite o primeiro valor:"))
        valorDois = int(input("Digite o segundo valor:"))
        valorTres = int(input("Digite o terceiro valor:"))
        valorQuatro = int(input("Digite o quarto valor:"))
        valorCinco = int(input("Digite o quinto valor:"))
        numerosPares = 0
        
        if valorUm != 0 and valorUm %2 == 0: 
            numerosPares = numerosPares + 1

        if valorDois != 0 and valorDois %2 == 0: 
            numerosPares = numerosPares + 1

        if valorTres != 0 and valorTres %2 == 0: 
            numerosPares = numerosPares + 1

        if valorQuatro != 0 and valorQuatro %2 == 0:
            numerosPares = numerosPares + 1

        if valorCinco != 0 and valorCinco %2 == 0:
            numerosPares = numerosPares + 1

        print(f"Número(s) pares: {numerosPares}")
    except Exception:
        print("Erro encontrado durante o processamento")

#parOuImpar()

def inverterString():
    texto = input("Digite algo para ser invertido: ")
    textoInvertido = texto[:: -1]

    print(textoInvertido)

#inverterString()

def substituirCaracteres():
    vogais = ['a', 'e', 'i', 'o', 'u']
    palavra = input("Digite uma palavra: ")

    palavra = palavra.lower()

    for vogal in vogais:
        palavra = palavra.replace(vogal, '?')

    print(palavra)

#substituirCaracteres()

def ordenarArray():
    valorUm = int(input("Digite o primeiro valor:"))
    valorDois = int(input("Digite o segundo valor:"))
    valorTres = int(input("Digite o terceiro valor:"))
    valorQuatro = int(input("Digite o quarto valor:"))
    valorCinco = int(input("Digite o quinto valor:"))
    valorSeis = int(input("Digite o sexto valor:"))

    listaInputs = [valorUm, valorDois, valorTres, valorQuatro, valorCinco, valorSeis]

    for i in range(6):
        if listaInputs[0] > listaInputs[1]:
            listaInputs[0], listaInputs[1] = listaInputs[1], listaInputs[0]
        if listaInputs[1] > listaInputs[2]:
            listaInputs[1], listaInputs[2] = listaInputs[2], listaInputs[1]
        if listaInputs[2] > listaInputs[3]:
            listaInputs[2], listaInputs[3] = listaInputs[3], listaInputs[2]
        if listaInputs[3] > listaInputs[4]:
            listaInputs[3], listaInputs[4] = listaInputs[4], listaInputs[3]
        if listaInputs[4] > listaInputs[5]:
            listaInputs[4], listaInputs[5] = listaInputs[5], listaInputs[4]

    print(f"Valor ordenados: {listaInputs}")

#ordenarArray()

def primeiroValorNaoRepetido():
    valorUm = int(input("Digite o primeiro valor:"))
    valorDois = int(input("Digite o segundo valor:"))
    valorTres = int(input("Digite o terceiro valor:"))
    valorQuatro = int(input("Digite o quarto valor:"))
    valorCinco = int(input("Digite o quinto valor:"))
    valorSeis = int(input("Digite o sexto valor:"))

    listaInputs = [valorUm, valorDois, valorTres, valorQuatro, valorCinco, valorSeis]

    for valor in listaInputs:
        if listaInputs.count(valor) == 1:
            print(f"Valor não repetido: {valor}")
            return
        
#primeiroValorNaoRepetido()

