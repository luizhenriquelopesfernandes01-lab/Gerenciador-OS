#variaveis de valores de cada serviço
tela = 250.00
bateria = 120.00
conector = 80.00
software = 60.00

# Variaveis do encerramento do dia
quantidade_os = 0
faturamento = 0
maior_os = 0
trocas_tela = 0
urgencias = 0
clientes = []
while True:
    menu = int(input("MENU:\n1-ABRIR OS\n2-ENCERRAR O DIA\n0-SAIR\n:")) #o \n serve para "quebrar" a linha, para não ficar em linha continua.

    if menu != 1 and menu != 2 and menu != 0:
        print("Selecione uma opção valida")
    elif menu == 1:
        print("Abrindo OS...")
        nome = str(input("NOME COMPLETO:"))
        modelo =(input("MODELO DO APARELHO:"))
        telefone= int(input("TELEFONE PARA CONTATO:"))
        while True: # laço de repetição para validar a opção de serviço
            servico = int(input("Qual opção de serviço deseja:\n1-TELA:250.00\n2-BATERIA:120.00\n3-CONECTOR:80.00\n4-SOFTWARE:60.00\n:"))
            if servico != 1 and servico != 2 and servico != 3 and servico != 4:
                print("Selecione uma opção valida")
            elif servico == 1:
                servico = tela
                trocas_tela = trocas_tela + 1
                print("Ordem de serviço cadastrada")
                break
            elif servico == 2:
                servico = bateria
                print("Ordem de serviço cadastrada")
                break #break para sair do loop caso a opção seja válida
            elif servico == 3:
                servico = conector
                print("Ordem de serviço cadastrada")
                break
            elif servico == 4:
                servico = software
                print("Ordem de serviço cadastrada")
                break
        
        while True:     
            urgencia = str(input("O ATENDIMENTO IRÁ NECESSITAR DE URGENCIA:(S/N):")) 
            if urgencia == "S" or urgencia == "s":
                if servico != software:
                    taxa = servico * 0.30
                    total = servico * 1.30
                    print(f"VALOR DA TAXA DE URGÊNCIA: R${taxa:.2f}") # O ":.2f" serve para limitar o valor a duas casas decimais
                    print(f"VALOR TOTAL DO SERVIÇO COM TAXA DE URGÊNCIA: R${total:.2f}")
                    servico = total
                else:
                    print(f"O SERVIÇO SOLICITADO NÂO TEM TAXA DE URGENCIA\n O VALOR DO SERVIÇO SERA DE R$:{servico:.2f}")
                break
            elif urgencia == "N" or urgencia == "n":
                print(f"O VALOR DO SERVIÇO SERA DE: R${servico:.2f}")
                break  
   
# 1 Informar parcelas e valores
        while True:
            parcelas = int(input("Informe a quantidade de parcelas (1 a 6): "))
            if parcelas < 1 or parcelas > 6:
                print("Selecione uma quantidade de parcelas válida.")
            else:
                break
        if parcelas == 1:
            valor_final = servico * 0.95
            print("Voce recebeu um desconto de 5% no valor do serviço, o valor final é de R$"+str(valor_final))
        elif parcelas == 2 or parcelas == 3:
            valor_final = servico
        else:
            valor_final = servico * 1.10

        valor_parcela = valor_final / parcelas
        
        print("\n===== DADOS DA OS =====")
        print("Cliente:", nome)
        print("Modelo:", modelo)
        print("Telefone:", telefone)
        print(f"Valor total da OS: R${valor_final:.2f}")
        print(f"Quantidade de parcelas:,{parcelas}")
        print(f"Valor de cada parcela: R${valor_parcela:.2f}")

        # o resumo do dia
        quantidade_os = quantidade_os + 1
        faturamento = faturamento + valor_final
        clientes = clientes + [nome]

        if quantidade_os == 1:
            maior_os = valor_final

        elif valor_final > maior_os:
            maior_os = valor_final

        if (urgencia == "S" or urgencia == "s") and servico != software:
            urgencias = urgencias + 1

        print("==OS registrada com sucesso!==")

    elif menu == 2:
        print("\n===== RESUMO DO DIA =====")

        if quantidade_os == 0:
            print("Nenhuma OS foi registrada.")

        else:
            media = faturamento / quantidade_os
            print("Quantidade de OS:", quantidade_os)
            print(f"Faturamento total: R${faturamento:.2f}")
            print(f"Valor medio por OS: R${media:.2f}")
            print(f"Maior OS: R${maior_os:.2f}")
            print("Trocas de tela:", trocas_tela)
            print("OS com urgencia:", urgencias)
            print("\nClientes atendidos:")
            for cliente in clientes:
                print(cliente)
        print("Encerrando o dia...")
        break
    elif menu == 0:
        print("Saindo...")
        break