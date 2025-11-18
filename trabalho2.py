import numpy as np
import datetime as dt

data_atual = dt.datetime.now()

hora_atual = data_atual.hour
minuto_atual = data_atual.minute

linhas = {'Cidade de origem':[],'Cidade de destino':[],'Horário de partida':[],'Valor da passagem':[], 'Ônibus': [] }#Dicionário da linha

onibus = {'Data da partida': [], 'Assentos Disponíveis':[]}#Dicionário do ônibus






def cadastroLinhas():# Preenche a linha com os dados que o usuario fornece

    linhas['Cidade de origem'].append(str(input('\nDigite o nome da cidade de origem da linha:\n-> ')))
    linhas['Cidade de destino'].append(str(input('\nDigite o nome da cidade de destino da linha:\n-> ')))
    linhas['Horário de partida'].append((f'{hora_atual}:{minuto_atual}'))
    
    try:

        linhas['Valor da passagem'].append(int(input('\nDigite o valor em reais da passagem:\n-> R$')))

    except(ValueError):

        print('\nErro: Digite um número inteiro!\n')
        pass

    linhas['Ônibus'].append((gerar_onibus()))
    
    










def gerar_onibus():#Função que cria o ônibus

    assentos = np.zeros((5, 4), dtype=int)
    
    return assentos









def escolher_onibus():

    print('\nÔnibus existentes:\n')

    try:

        for i in range(len(linhas['Ônibus'])):

            print(f'Ônibus {i} | {linhas["Cidade de origem"]} - {linhas["Cidade de destino"]}|\n')

        onibus_escolhido = int(input('\nDigite o número do ônibus:\n-> '))

        return(onibus_escolhido)

    except(ValueError):
        print('\nErro: Digite um número inteiro!\n')




def preencher_onibus():

        onibus_escolhido = escolher_onibus()
    
        onibus = linhas['Ônibus'][onibus_escolhido]
        
        print(onibus)

        i = int(input(f"Digite qual assento você gostaria de ocupar (x): "))
        j = int(input(f"Digite qual assento você gostaria de ocupar (y): "))

        if(i< 5) and (j<4):

            if onibus[i][j] != 1:

                onibus[i][j] = 1

            else:
                print('\nErro: Esse assento já está ocupado.\n')
        else:

            print('\nErro: Esse assento não existe!\n')

  















def consultarAssentos():

    onibus_escolhido = escolher_onibus()

    assentos = linhas['Ônibus'][onibus_escolhido]

    onibus['Assentos Disponíveis'] = [None]

    for i, j in np.ndindex(assentos.shape):

        if (assentos[i][j] == 0) and (assentos[i][j] != None):
            onibus['Assentos Disponíveis'].append(f'[{i},{j}]')


    return(onibus['Assentos Disponíveis'])




def consultarHorarios():

    horarios_cidade = []

    print('\nCidades existentes:\n')

    for i in range(len(linhas['Cidade de origem'])):

        if linhas['Cidade de origem'][i] != linhas['Cidade de origem'][i-1]:

            print(f'Cidade {i} | {linhas["Cidade de origem"][i]} |\n')

    try:

        cidade_escolhida = int(input('\nDigite o número da cidade:\n-> '))
        cidade_escolhida = linhas['Cidade de origem'][cidade_escolhida]
            
    except(ValueError):
        print('\nErro: Digite um número inteiro!\n')


    for i in range(len(linhas['Cidade de origem'])):

        if linhas['Cidade de origem'][i] == cidade_escolhida:

            horarios_cidade.append(linhas['Horário de partida'][i])


    print(f'\nHorários de partida do ônibus: {horarios_cidade}')

    



def gerarRelatorios():
    '''
 Permitir a geração dos relatórios (na tela ou em arquivo texto, escolha do usuário):
o Total arrecadado com venda de passagens no mês corrente para cada linha.
o Ocupação percentual média de cada linha em cada dia da semana (uma matriz).

 Além de receber as reservas pelo teclado, permitir ler as reservas de um arquivo texto
no seguinte formato:
o CIDADE, HORÁRIO(hh:mm), DATA(dd/mm/aaaa), ASSENTO
o Uma reserva por linha.
    '''
    pass

sair = 0 #Varíavel que controla o loop do while do menu

onibus_criado = False #Variável usada por mim somente para testar as funções, uma outra implementação deve ser desenvolvida para o menu

while sair == 0 :

    try:
        print("\nSistema da Rodoviária:")
        print("1 - Cadastrar ou editar linhas ")
        print("2 - Consultar horários disponíveis para uma cidade")
        print("3 - Consultar os assentos disponíveis no ônibus")
        print('4 - Marcar um assento de um ônibus')
        print("0 - Sair")

        opcao = int(input("Opção: "))

        match(opcao):
            case 1:

                #Permite inserir, remover ou alterar alguma linha.

                try:

                    opcao_linhas = int(input('\nDigite uma das opções abaixo:\n1- Criar linha\n2- Remover linha\n3- Editar linha\n-> '))
                    
                    match(opcao_linhas):
                        
                        case 1:
                            cadastroLinhas()

                        case 2:
                            print('\nEm breve..\n')

                        case 3:
                            print('\nEm breve..\n')

                        case _:
                            print('\nErro: Digite um dos valores exibidos no menu!\n')

                except(ValueError):
                    print('\nErro: Digite um número inteiro!\n')
               
            
            case 2:

                if (linhas['Ônibus']):

                    #Consultar horários disponíveis para uma cidade
                    consultarHorarios()

                else:
                    print('\nErro: Nenhuma linha foi criada para que se possa verificar!\n')
                
            case 3:

                if (linhas['Ônibus']):

                    lista_assentos = consultarAssentos()
                    
                    print('\nAssentos disponíveis:\n')

                    for i in range(len(lista_assentos)):
                        print(f'{lista_assentos[i]}\n')

                else:
                    print('\nErro: Nenhuma linha foi criada para que se possa verificar!\n')
                
            case 4: #Marcar um assento
                    
                if (linhas['Ônibus']):

                    preencher_onibus()

                    confirmacao = str(input('\nDigite qualquer tecla para retornar ao menu.\n'))

                else:
                    print('\nErro: Nenhuma linha foi criada para que se possa verificar!\n')

            case 0:

                sair = 1
                print('\nFinalizando programa...\n')
            
            case _:
                print("\nErro: Digite uma das opções exibidas no menu!\n")
        
    except (ValueError):
        print("=====" * 10)
        print("\nErro: Opção inválida, digite um número inteiro!\n")
        print("=====" * 10)