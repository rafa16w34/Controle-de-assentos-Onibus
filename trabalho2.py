import numpy as np
import datetime as dt

data_atual = dt.datetime.now()

linhas = {'Cidade de origem':[],'Cidade de destino':[],'Horário de partida':[],'Valor da passagem':[], 'Ônibus': [] }#Dicionário da linha

onibus = {'Data da partida': [], 'Assentos Disponíveis':[]}#Dicionário do ônibus

#############################################################################################################################################################

#Funções:

#Criar uma linha com as informações fornecidadas:

def cadastroLinhas():# Preenche a linha com os dados que o usuario fornece

    cidade_origem_digitada = str(input('\nDigite o nome da cidade de origem da linha:\n-> '))

    cidade_destino_digitada = str(input('\nDigite o nome da cidade de destino da linha:\n-> '))

    hora_digitada = str(input('\nDigite a hora que ele irá sair: \nFormato: ( 00:00 )\n-> '))

    if (hora_digitada.find(':') == 2):

        hora_digitada = hora_digitada.split(':')

        hora_atual = int(hora_digitada[0])
        minuto_atual = int(hora_digitada[1])

        if (hora_atual < 24) and (hora_atual >= 0) and (minuto_atual < 59) and (minuto_atual >= 0):

            linhas['Cidade de origem'].append(cidade_origem_digitada)
            linhas['Cidade de destino'].append(cidade_destino_digitada)

            linhas['Horário de partida'].append((f'{hora_atual}:{minuto_atual}'))
            
            try:

                linhas['Valor da passagem'].append(int(input('\nDigite o valor em reais da passagem:\n-> R$')))

            except(ValueError):

                print('\nErro: Digite um número inteiro!\n')
                pass

            linhas['Ônibus'].append((gerar_onibus()))

        else:

            pass

    else:

        print('\nErro: Digite uma data no formato correto!\n')
        pass
    
#####################################################################################################################################################

#Gera um ônibus vazio:

def gerar_onibus():#Função que cria o ônibus

    assentos = np.zeros((5, 4), dtype=int)
    
    return assentos

###################################################################################################################################################

#Criar outro ônibus para uma linha já existente:


def DuplicarLinhas(linha_escolhida):#Duplica as informações da linha da qual se quer duplicar o onibus, mantendo as informações mas criando mais um ônibus vazio

    linhas['Cidade de origem'].append(linhas['Cidade de origem'][linha_escolhida])
    linhas['Cidade de destino'].append(linhas['Cidade de destino'][linha_escolhida])
    linhas['Horário de partida'].append(linhas['Horário de partida'][linha_escolhida])
    
    try:

        linhas['Valor da passagem'].append(linhas['Valor da passagem'][linha_escolhida])

    except(ValueError):

        print('\nErro: Digite um número inteiro!\n')
        pass

    linhas['Ônibus'].append((gerar_onibus()))



def criar_outro_onibus():#Função que cria mais um ônibus para linha

    
    print('\nEscolha entre as linhas existentes aquela que você gostaria de adicionar um ônibus:\n')

    try:

        for i in range(len(linhas['Cidade de origem'])):

            print(f'Linha {i} | {linhas["Cidade de origem"][i]} - {linhas["Cidade de destino"][i]}|\n')

        linha_escolhida = int(input('\nDigite o número da linha :\n-> '))

    except(ValueError):
        print('\nErro: Digite um número inteiro!\n')
        pass

    DuplicarLinhas(linha_escolhida)

    return 

###########################################################################################################################################################

#Marcar um assento:


def escolher_onibus():#Escolher um do ônibus para fazer a viagem

    print('\nÔnibus existentes:\n')

    try:

        for i in range(len(linhas['Ônibus'])):

            print(f'Ônibus {i} | {linhas["Cidade de origem"][i]} - {linhas["Cidade de destino"][i]}|\n')

        onibus_escolhido = int(input('\nDigite o número do ônibus:\n-> '))

        return(onibus_escolhido)

    except(ValueError):
        print('\nErro: Digite um número inteiro!\n')




def preencher_onibus():#Escolher qual será seu assento

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

    print(f'\nO valor será de : R$ {linhas["Valor da passagem"][onibus_escolhido]:.2f}\n')

    print('\nCompra realizada com sucesso!\n')

#####################################################################################################################################

#Consulta os assentos do Ônibus
  
def consultarAssentos():

    onibus_escolhido = escolher_onibus()

    assentos = linhas['Ônibus'][onibus_escolhido]

    onibus['Assentos Disponíveis'] = [None]

    for i, j in np.ndindex(assentos.shape):

        if (assentos[i][j] == 0) and (assentos[i][j] != None):
            onibus['Assentos Disponíveis'].append(f'[{i},{j}]')


    return(onibus['Assentos Disponíveis'])

############################################################################################################################################

#Consulta os horários disponíveis em uma cidade

def consultarHorarios():

    horarios_cidade = []
    cidade_exibida = []

    print('\nCidades existentes:\n')

    for i in range(len(linhas['Cidade de origem'])):

        if (len(linhas['Cidade de origem'])) > 1:

            if ((linhas['Cidade de origem'][i]) not in cidade_exibida):

                print(f'Cidade {i} | {linhas["Cidade de origem"][i]} |\n')  #Ele pode digitar um número i de uma das cidades repetidas
                
                cidade_exibida.append(linhas['Cidade de origem'][i])        #Posso usar essa lista para contornar esse erro

        else:

            print(f'Cidade {i} | {linhas["Cidade de origem"][i]} |\n')

    try:

        cidade_escolhida = int(input('\nDigite o número da cidade:\n-> '))
        cidade_escolhida = linhas['Cidade de origem'][cidade_escolhida]
            
    except(ValueError):
        print('\nErro: Digite um número inteiro!\n')
        pass


    for i in range(len(linhas['Cidade de origem'])):

        if linhas['Cidade de origem'][i] == cidade_escolhida:

            horarios_cidade.append(linhas['Horário de partida'][i])


    print(f'\nHorários de partida do ônibus: {horarios_cidade}')

#####################################################################################################################################################



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

#########################################################################################################################################################

# Menu principal

sair = 0 #Varíavel que controla o loop do while do menu

while sair == 0 :

    try:
        print("\nSistema da Rodoviária:")
        print("1 - Cadastrar ou editar linhas;")
        print("2 - Consultar horários disponíveis para uma cidade;")
        print("3 - Consultar os assentos disponíveis no ônibus;")
        print('4 - Marcar um assento de um ônibus;')
        print('5 - Criar outro ônibus para uma linha já existente;')
        print("0 - Sair.")

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

                    confirmacao = str(input('\nDigite a tecla "Enter" para retornar ao menu.\n'))

                else:
                    print('\nErro: Nenhuma linha foi criada para que se possa verificar!\n')

            case 5:#Cria outro ônibus para uma linha já existente

                if (linhas['Ônibus']):

                    criar_outro_onibus()

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