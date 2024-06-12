import re

def formatar_cpf(cpf):

    cpf_modificado=""
    for numero in cpf:
        if numero.isdigit()==True:
            cpf_modificado+=numero

    return cpf_modificado

def verificar_cpf(cpf):

    qtd_caractere_numerico=0

    for caractere in cpf:
        if caractere.isdigit()==True:
            qtd_caractere_numerico+=1

        if (caractere.isdigit()==False) and (caractere!="." and caractere!="-"):
            return False
    
    if qtd_caractere_numerico<11 or qtd_caractere_numerico>11:
        return False

def formatar_endereço(endereço):

    num_virgulas=0
    endereço_formatado=""

    #substituir virgulas por " -" e adicionar / entre cidade e estado
    for letra in endereço:
        if letra!=",":
            endereço_formatado+=letra
        else:
            num_virgulas+=1
            if num_virgulas==1:
                endereço_formatado+=","
            elif num_virgulas>1 and num_virgulas<4:
                endereço_formatado+=" -"
            else:
                endereço_formatado+="/"
                break
           
    #adicionar estado em maiúsculo
    estados_br={"Acre":"AC", "Alagoas":"AL", "Amapá":"AP", "Amazonas":"AM", "Bahia":"BA", "Ceará":"CE", "Distrito Federal":"DF", "Espírito Santo":"ES", "Goiás":"GO", "Maranhão":"MA", "Mato Grosso":"MT", "Mato Grosso Do Sul":"MS", "Minas Gerais":"MG", "Pará":"PA", "Paraíba":"PB", "Paraná":"PR", "Pernambuco":"PE", "Piauí":"PI", "Roraima":"RR", "Rondônia":"RO", "Rio de Janeiro":"RJ", "Rio Grande Do Norte":"RN", "Rio Grande Do Sul":"RS", "Santa Catarina":"SC", "São Paulo":"SP", "Sergipe":"SE", "Tocantins":"TO"}

    estado = endereço[len(endereço_formatado)-1:len(endereço)].title()

    if estado in estados_br:
        endereço_formatado+=estados_br[estado]
    else:
        tam=len(endereço)
        endereço_formatado+=endereço[-2:tam].upper()
    
    return endereço_formatado
    #formato = logradouro, numero - bairro - cidade/estado_sigla

def verificar_data(data):
    formato_1=re.compile(r'^\d{2}/\d{2}/\d{4}$') #dd/mm/aaaa
    formato_2=re.compile(r'^\d{2} de [a-zA-Z]+ de \d{4}$') #dd de mês de aaaa

    if formato_1.match(data) or formato_2.match(data):
        return True
    else:
        return False

def verificar_endereço(endereço):
    formato=re.compile(r'^[\w\s]+\, [\w\s]+\, \d{2,5}\, [\w\s]+\, [\w\s]+$')

    if formato.match(endereço):
        return True
    else:
        return False
    

def formatar_data(data):

    data=data.title()
    data_formatada=""

    meses = {"Janeiro": "01", "Fevereiro": "02", "Março": "03", "Abril": "04",
    "Maio": "05", "Junho": "06", "Julho": "07", "Agosto": "08", "Setembro": "09",
    "Outubro": "10", "Novembro": "11", "Dezembro": "12"}

    #adiciona apenas números na data formatada
    qtd_num=0
    for letra in data:
        if letra.isdigit():
            data_formatada+=letra
        else:
            #converter mes por extenso em numero
            for mes, num in meses.items():
                if data.find(mes)!=-1:
                    qtd_num+=1
                    mes_fornecido=num
            if qtd_num==1:
                data_formatada+=mes_fornecido
        #adiciona / entre dia, mes e ano
        if len(data_formatada)==2 or len(data_formatada)==5:
            data_formatada+="/"

    #verificar se dia é equivalente a qdt de dias do mês
    return data_formatada    

def menu_usuário():
    print("+","+".center(39,"-"), end="+\n")
    print("|"+"Sistema bancário - menu inicial".center(40), end="|\n")
    print("+","+".center(39,"-"), end="+\n")
    print("|", "[1]-entrar", " ".center(28), end="|\n")
    print("|", "[2]-criar novo usuário", " ".center(16), end="|\n")
    print("|", "[3]-criar nova conta", " ".center(18), end="|\n")
    print("|", "[0]-sair", " ".center(30), end="|\n")
    print("+","+".center(39,"-"), end="+\n")

def criar_usuario(user_number, nome, data, cpf, endereco):
    global usuarios
    usuario={f"usuario_{user_number}": {"nome": nome, "data_nascimento": data, "cpf": cpf, "endereco": endereco}}
    usuarios.append(usuario)

def criar_conta(num_usuario, cpf, senha):
    global contas
    conta={"agencia": "0001", "conta": num_usuario, "cpf":cpf, "senha":senha}
    contas.append(conta)

def menu_bancario():
    print("+","+".center(39,"-"), end="+\n")
    print("|"+"Sistema bancário - Opções".center(40), end="|\n")
    print("+","+".center(39,"-"), end="+\n")
    print("|", "[1]-depósito", " ".center(26), end="|\n")
    print("|", "[2]-saque", " ".center(29), end="|\n")
    print("|", "[3]-extrato", " ".center(27), end="|\n")
    print("|", "[0]-sair", " ".center(30), end="|\n")
    print("+","+".center(39,"-"), end="+\n")

def deposito (saldo_disponivel, valor, extrato_atual, /):
    
    if valor.isdigit()==False:
        print("digite um valor válido")
    else:
        valor = float(valor)

        saldo_disponivel+=valor
        extrato_atual+=f"depóstio: {valor:.2f}\n"
        print("valor depositado com sucesso...")
    
    return saldo_disponivel, extrato_atual


def saque (*, valor, saldo_disponivel, qtd_saques, extrato_atual):
    
    if valor.isdigit()==False:
        print("falha na operação! digite um valor numérico")
    else: 
        valor=float(valor)
        #verificar disponibilidade de saldo
        if valor>saldo_disponivel:
            print("saldo insuficiente")

        #verificar se valor excede limite unitário de saque
        elif valor>LIMITE_VALOR_SAQUE:
            print("valor inserido excede o limite de saque permitido")

        #verificar se saque excede limite de quantidades diárias
        elif qtd_saques>=NUMERO_SAQUES_DIARIOS:
            print("número de saques diários excedidos, tente novamente amanhã")

        else:
            qtd_saques=qtd_saques+1
            saldo_disponivel-=valor
            extrato_atual+=f"saque: {valor:.2f} \n"
            print("saque efetuado com sucesso")
        
        return saldo_disponivel, extrato_atual, qtd_saques


def extrato (saldo_disponivel, /, *, extrato):

    print("exibindo extrato...")
    print("+","+".center(39,"-"), end="+\n")
    print("|"+"histórico de movimentações".center(40), end="|\n")
    print("+","+".center(39,"-"), end="+\n")
    
    if extrato=="":
        print("não foram realizadas movimentações")
    
    return extrato, saldo_disponivel

#regra de negócio
NUMERO_SAQUES_DIARIOS=3
LIMITE_VALOR_SAQUE=500

#variáveis de controle de conta/usuário:
user_number=0
numero_conta=0
usuarios=[]
contas=[]

#variáveis de controle de op bancárias:
#atributos do usuário
saldo=0
extrato_atual=""
qtd_saques_efetuados=0

def sistema_bancario(saldo, extrato_atual, qtd_saques_efetuados):

    while True:

        menu_bancario()

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
            saldo, extrato_atual = deposito(saldo, valor, extrato_atual)
            print(f"saldo atual {saldo}")
            
        #sacar
        elif opcao == "2":

            valor_saque=(input("digite o valor que deseja sacar: "))
            saldo, extrato_atual, qtd_saques_efetuados = saque(valor=valor_saque, saldo_disponivel=saldo, qtd_saques=qtd_saques_efetuados, extrato_atual=extrato_atual)
            print(f"saldo atual: {saldo}")

        #extrato
        elif opcao == "3":
                
            extrato_atual, saldo = extrato(saldo, extrato=extrato_atual)
            print(extrato_atual)

            print(f"saldo final: {saldo}")
            print(f"saques efetuados:{qtd_saques_efetuados}")


while True:

    menu_usuário()

    opçoes_usuario=["0","1","2","3"]
    op_user_escolhida = input("digite uma opção: ")

    while op_user_escolhida not in opçoes_usuario:
        op_user_escolhida = input("digite uma opção válida: ")

    if op_user_escolhida=="1":

        if len(contas)==0:
            print("base de usuários inexistente")
            continue

        user_name = input("digite o seu cpf: ")
        user_name = formatar_cpf(user_name)
        user_login = input("digite sua senha: ")

        for conta in contas:
            if conta["cpf"]==user_name and conta["senha"]==user_login:
                print("login efetuado com sucesso")
                sistema_bancario(saldo, extrato_atual, qtd_saques_efetuados)
            else:
                print("usuario e/ou senha incorretos")

    elif op_user_escolhida =="2":

        user_number+=1

        nome = input("digite seu nome: ")

        data_nascimento = input("digite sua data de nascimento no formato (dd/mm/aaaa) ou (dd de mes de aaaa): ")

        while verificar_data(data_nascimento)==False:
            print("formato de entrada inválido")
            data_nascimento = input("digite sua data de nascimento em um formato válido: ")
            
        data_nascimento=formatar_data(data_nascimento)

        cpf=input("digite seu cpf: ")

        #verificar se cpf digitado é formado por caracteres numéricos válidos
        while verificar_cpf(cpf)==False:
            print("cpf inválido ou com número incorreto de digitos")
            cpf=input("digite um cpf válido: ")

        #eleminar caracteres não numéricos do cpf digitado
        cpf=formatar_cpf(cpf)

        #verificar se usuario possui cpf exclusivo
        for usuario in usuarios:
            for id_usuario, info_usuario in usuario.items():
                while info_usuario.get("cpf")==cpf:
                    cpf=input("cpf já cadastrado, digite um cpf válido: ")
                    cpf=formatar_cpf(cpf)

        endereço = input("digite seu endereço no formato: rua, bairro, numero, cidade, estado: ")
        
        while verificar_endereço(endereço)==False:
            print("formato de endereço inválido")
            endereço = input("digite o endereço no formato específicado: ")
        
        endereço=formatar_endereço(endereço)

        #não pode haver dois usuários com mesmo cpf

        criar_usuario(user_number, nome, data_nascimento, cpf, endereço)

        for usuario in usuarios:
            print(usuario)

    elif op_user_escolhida=="3":

        if len(usuarios)==0:
            print("base de usuários inexistente")
            continue

        numero_conta+=1
        cpf_conta=input("informe o cpf do usuário: ")
        cpf_conta=formatar_cpf(cpf_conta)

        for usuario in usuarios:
            for user_id, user_info in usuario.items():
                user_found=user_info.get("cpf", "não encontrado")
                if user_found==cpf_conta:
                    senha=input("digite sua senha: ")
                    criar_conta(numero_conta, cpf_conta, senha)
                    print("conta criada com sucesso")
                elif user_found!=cpf_conta:
                    print("usuário inexistente, é necessário um usuário pré cadastrado para criar uma conta")
                    continue
            
        for conta in contas:
            print(conta)

    elif op_user_escolhida=="0":
        break

