saldo=0
NUMERO_SAQUES_DIARIOS=3
LIMITE_VALOR_SAQUE=500

extrato=""
qtd_saques_efetuados=0

def inicializar_menu():
    print("+","+".center(39,"-"), end="+\n")
    print("|"+"Sistema bancário - Opções".center(40), end="|\n")
    print("+","+".center(39,"-"), end="+\n")
    print("|", "[1]-depósito", " ".center(26), end="|\n")
    print("|", "[2]-saque", " ".center(29), end="|\n")
    print("|", "[3]-extrato", " ".center(27), end="|\n")
    print("|", "[0]-sair", " ".center(30), end="|\n")
    print("+","+".center(39,"-"), end="+\n")


while True:
    
    inicializar_menu()

    opcoes_validas=["0","1","2","3"]

    opcao = input("digite um dos dígitos abaixo uma acessar uma das opções listadas: ")

    while opcao not in opcoes_validas:
        opcao=input("digite uma opção válida: ")

    #sair
    if opcao == "0":
        break
    
    #depositar
    elif opcao == "1":
        valor=input("digite o valor que deseja depositar: ")

        if valor.isdigit()==False:
            print("digite um valor válido")
        else:
            valor = float(valor)

            saldo+=valor
            extrato += f"depóstio: {valor:.2f}\n"
            print("valor depositado com sucesso...")
    
    #sacar
    elif opcao == "2":

        valor_saque=(input("digite o valor que deseja sacar: "))

        if valor_saque.isdigit()==False:
            print("falha na operação! digite um valor numérico")
        else:
            valor_saque=float(valor_saque)
            #verificar disponibilidade de saldo
            if valor_saque>saldo:
                print("saldo insuficiente")

            #verificar se valor excede limite unitário de saque
            elif valor_saque>500:
                print("valor inserido excede o limite de saque permitido")

            #verificar se saque excede limite de quantidades diárias
            elif qtd_saques_efetuados>=3:
                print("número de saques diários excedidos, tente novamente amanhã")
            else:
                qtd_saques_efetuados=qtd_saques_efetuados+1
                saldo-=valor_saque
                extrato+=f"saque: {valor_saque:.2f} \n"
                print("saque efetuado com sucesso")

    #extrato
    elif opcao == "3":
        print("exibindo extrato...")
        print("+","+".center(39,"-"), end="+\n")
        print("|"+"histórico de movimentações".center(40), end="|\n")
        print("+","+".center(39,"-"), end="+\n")
        
        print(extrato if extrato !="" else "não foram realizadas movimentações")

        print(f"saldo final: {saldo}")
        print(f"saques efetuados:{qtd_saques_efetuados}")