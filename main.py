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
    