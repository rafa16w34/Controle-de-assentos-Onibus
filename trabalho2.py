import numpy as np
import datetime as dt

data_atual = dt.datetime.now()

hora_atual = data_atual.hour
minuto_atual = data_atual.minute

linhas = {'Cidade de origem':'','Cidade de destino':'','Horário de partida':'','Valor da passagem':0 }

onibus = {'Data da partida': [], 'Assentos Disponíveis':[]}

def gerar_onibus():

    assentos = np.zeros((5, 4), dtype=int)
    

    return assentos


def preencher_onibus(onibus):

    print(onibus)

    i = int(input(f"Digite qual assento você gostaria de ocupar: "))
    j = int(input(f"Digite qual assento você gostaria de ocupar: "))

    if(i< 5) and (j<4):

        if onibus[i][j] != 1:

            onibus[i][j] = 1

        else:
            print('\nErro: Esse assento já está ocupado.\n')
    else:

        print('\nErro: Esse assento não existe!\n')




def cadastroLinhas():
    '''
    Cada linha tem um conjunto de horários diários de partida de ônibus.
     Os dados de cada linha são:
    o Cidade de origem
    o Cidade de destino
    o Horário de partida (hora:minuto)
    o Valor da passagem
    '''
    
    linhas['Cidade de origem'] = str(input('\nDigite o nome da cidade de origem da linha:\n-> '))
    linhas['Cidade de destino'] = str(input('\nDigite o nome da cidade de destino da linha:\n-> '))
    linhas['Horário de partida'] = (f'{hora_atual}:{minuto_atual}')
    
    try:

        linhas['Valor da passagem'] = int(input('\nDigite o valor em reais da passagem:\n-> R$'))

    except(ValueError):
        print('\nErro: Digite um número inteiro!\n')
        pass

    print(linhas)

def consultarHorarios():
    pass


def consultarAssentos():
    '''
o Consultar os assentos disponíveis no ônibus, informando a cidade de destino, horário e data. A data deve ser inferior a 30 dias, contados a partir da data atual.
o Após uma consulta de assento disponível, o sistema deve perguntar se algum assento vai ser reservado (caso existam ainda assentos disponíveis).
    '''
    pass


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
assentos_onibus = gerar_onibus()

while sair == 0 :

    try:
        print("\nSistema da Rodoviária:\n1 - Cadastrar ou editar linhas ")
        print("2 - Consultar horários disponíveis para uma cidade")
        print("3 - Consultar os assentos disponíveis no ônibus")
        print("0 - Sair")

        opcao = int(input("Opção: "))

        match(opcao):
            case 1:

                #Permite inserir, remover ou alterar alguma linha.

                cadastroLinhas()
            
            case 2:

                #Consultar horários disponíveis para uma cidade

                print('\nEm breve..\n')
            
            case 3:
            
                #Consultar os assentos disponíveis no ônibus, informando a cidade de destino, horário e data.
                #A data deve ser inferior a 30 dias, contados a partir da data atual.
                #Após uma consulta de assento disponível, o sistema deve perguntar se algum assento vai ser reservado (caso existam ainda assentos disponíveis).

                print('\nAssentos disponíveis no ônibus escolhido:\n')
                
                print('\n0- Disponível\n1- Ocupado\n')

                preencher_onibus(assentos_onibus)

                confirmacao = str(input('\nDigite qualquer tecla para retornar ao menu.\n'))

            case 0:

                sair = 1
                print('\nFinalizando programa...\n')
            
            case _:
                print("\nErro: Digite uma das opções exibidas no menu!\n")
        
    except (ValueError):
        print("=====" * 10)
        print("\nErro: Opção inválida, digite um número inteiro!\n")
        print("=====" * 10)



'''geração dos relatórios (na tela ou em arquivo texto, escolha do usuário): 
o Total arrecadado com venda de passagens no mês corrente para cada linha. 
o Ocupação percentual média de cada linha em cada dia da semana (uma matriz).


 Além de receber as reservas pelo teclado, permitir ler as reservas de um arquivo textono seguinte formato:
o CIDADE, HORÁRIO(hh:mm), DATA(dd/mm/aaaa), ASSENTO
o Uma reserva por linha.
 Gravar em um arquivo texto todas as reservas que não puderam ser realizadas, juntamente com o motivo 
(ex.: ônibus cheio, ônibus já partiu, assento ocupado).'''