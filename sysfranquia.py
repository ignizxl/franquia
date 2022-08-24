from time import sleep
from random import randint
from traceback import print_tb
add = []
contador = 0
produtos = [["0001", "Carregador", 10.00, 1000],
            ["0002", "Fone", 50.58, 124],
            ["0003", "Computador", 4560.00, 23]]
carrinho = []
while True:
    print("-"*50)
    print("{}".format("MENU DE OPÇÕES".center(50, "/")))
    print("-"*50)
    print("[1] Listar Produtos\n[2] Buscar Produto\n[3] Vizualizar Carrinho\n[4] Remover do Carrinho\n[5] Finalizar Pedido")
    op = int(input("Selecione um opção:"))

    if op == 1:
        print("*"*50)
        print("Produtos Disponíveis".center(50))
        print("-"*50)
        sleep(1)
        print(f'{"Cod.":16}{"Descrição":24}{"Valor Unt."}')
        print("-"*50)
        for produto in produtos:
            print(f'{produto[0]:17}{produto[1]:15}{produto[2]:18}')

    elif op == 2:
        print(f'{"-"*50}\n{"BUSCA".center(50)}\n{"-"*50}')
        cod = input("Codigo do Produto que Deseja Buscar: ")
        print(f'{"-"*50}\n{"Produtos Encontrados".center(50)}\n{"-"*50}')
        print(f'{"Cod.":16}{"Descrição":24}{"Valor Unt."}')
        print("."*50)
        for linha in produtos:
            if cod in linha:
                contador +=1
                print(f'{linha[0]:16}{linha[1]:15}{linha[2]:18}')
                basequant = linha[3]
                add.append(linha[:2])
            print("."*50)
        if contador >= 1:
            addcar = int(input("[1] Adicionar ao Carrinho\n[2] Sair\nSelecione a Opção: "))
            print("-"*50)
            
            if addcar == 1:
                while True:
                    quantidade = int(input("Digite a Quantidade Que deseja Adicionar: "))
                    if quantidade > basequant:
                        print("Quantidade Indisponivel no Estoque")
                        continue
                    else:
                        carrinho.append(add)
                        add = []
                        break

        else:
            print("Produto Não Encontrado".center(50))
            print("-"*50)
                
    elif op == 3:
        print(f'{"-"*50}\n{"CARRINHO".center(50)}\n{"-"*50}')
        print(f'{"Cod.":12}{"Descrição":15}{"Valor Unt.":12}{"Quantidade":10}')
        for item in carrinho:
            print(f'{item[0]:12}{item[1]:15}{item[2]:12}{item[3]:10}')
    elif op == 4:
        remove = input("Codigo do Produto a ser Excluido:\n")
        for linha in lista:
            if remove in linha:
                pass
    elif op == 5:
        print("~"*50)
        print(f'{"Forma de Pagamento".center(50)}')
        print("~"*50)
        print("[1] Pix\n[2] Cartão de Crédito\n[3] Débito\n[4] Boleto")
        while True:
            pag = int(input("Selecione Uma Forma: "))
            if pag == 1:
                chave_pix = "35252452"
                print(
                    f'Faça o Pagamento Para A compra ser processada\nChave Pix: {chave_pix}')
                while True:
                    verif = int(
                        input("Fez o Pagamento?\n[1] Sim | [2] Não\nDigite: "))
                    if verif == 1:
                        print("Pagamento Confirmado")
                        break
                    elif verif == 2:
                        print("Pagamento Cancelado")
                        break
                    else:
                        print("Digite uma Opção Válida")
                        continue
            elif pag == 2:
                while True:
                    band = int(input(
                        "Selecione a Bandeira:\n[1] Visa\n[2] MasterCard\n[3] Elo\nSelecione a Opção: "))
                    if band == 1:
                        band = "Visa"
                        break
                    elif band == 2:
                        band = "MasterCard"
                        break
                    elif band == 3:
                        band = "Elo"
                        break
                    else:
                        print("Opção Inválida")
                        continue
                num_card = input("Número do Cartão:\n")
                data = input("Data de Vencimento:\n")
                cvv = int(input("CVV:\n"))
                nome = input("Nome do Titular:\n")
                parc = int("Quantidade de Parcela:\n")
                print(
                    f'Olá! {nome}\nSua Compra foi efetuada com Sucesso!\nQuantidade de Parcela: {parc}\nDados do Cartão\n{band}\nCartão: {num_card}\nValidade: {data}')
            elif pag == 3:
                while True:
                    band = int(input(
                        "Selecione a Bandeira:\n[1] Visa\n[2] MasterCard\n[3] Elo\nSelecione a Opção: "))
                    if band == 1:
                        band = "Visa"
                        break
                    elif band == 2:
                        band = "MasterCard"
                        break
                    elif band == 3:
                        band = "Elo"
                        break
                    else:
                        print("Opção Inválida")
                        continue
                num_card = input("Número do Cartão:\n")
                data = input("Data de Vencimento:\n")
                cvv = int(input("CVV:\n"))
                nome = input("Nome do Titular:\n")
                print(
                    f'Olá! {nome}\nSua Compra foi efetuada com Sucesso!\nDados do Cartão\n{band}\nCartão: {num_card}\nValidade: {data}')
            elif pag == 4:
                boleto = randint(000000000000000000000, 999999999999999999999)
                print(f'Boleto Gerado\n{boleto}')
                while True:
                    conf = int(input("o Boleto Foi Pago?\n[1] Sim\n[2] Não\nSelecione Uma Opção: "))
                    if conf == 1:
                        print("Pagamento Recebido")
                        break
                    elif conf == 2:
                        print("Pagamento Cancelado")
                        continue
                    else:
                        print("Opção Inválida!")
                        continue
            else:
                print("Digite Uma Opção Válida!")
                continue
            break
        carrinho.close()
        os.remove("./projeto/carrinho.txt")
        break
    else:
        print("SELECIONE UMA OPÇÃO EXISTENTE")
        continue
