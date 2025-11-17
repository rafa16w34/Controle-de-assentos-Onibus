'''
 SISTEMA DE UMA EMPRESA DE TRANSPORTE DE PASSAGEIROS.
 Faça um programa para controlar os assentos disponíveis nos ônibus de uma empresa
de transporte rodoviário de passageiros.

Cada linha tem um conjunto de horários diários de partida de ônibus.
Cada ônibus suporta até 20 passageiros: assentos de 1 até 20, onde os ímpares são nas janelas.

 Os dados de cada linha são:
o Cidade de origem
o Cidade de destino
o Horário de partida (hora:minuto)
o Valor da passagem

 Cada linha tem ônibus partindo todos os dias. Portanto, as informações de cada ônibus
são:
o Data da partida (dia/mês/ano)
o Assentos disponíveis

 O sistema deve permitir:
o Cadastro de linhas: inserir, remover e alterar.
o Consultar todos os horários disponíveis para uma determinada cidade.
o Consultar os assentos disponíveis no ônibus, informando a cidade de destino, horário e data. A data deve ser inferior a 30 dias, contados a partir da data atual.
o Após uma consulta de assento disponível, o sistema deve perguntar se algum assento vai ser reservado (caso existam ainda assentos disponíveis).
o Nenhuma passagem pode ser comercializada para ônibus que já partiram (consultar o relógio do sistema).

 Permitir a geração dos relatórios (na tela ou em arquivo texto, escolha do usuário):
o Total arrecadado com venda de passagens no mês corrente para cada linha.
o Ocupação percentual média de cada linha em cada dia da semana (uma matriz).

 Além de receber as reservas pelo teclado, permitir ler as reservas de um arquivo texto
no seguinte formato:
o CIDADE, HORÁRIO(hh:mm), DATA(dd/mm/aaaa), ASSENTO
o Uma reserva por linha.

 Gravar em um arquivo texto todas as reservas que não puderam ser realizadas, juntamente com o motivo (ex.: ônibus cheio, ônibus já partiu, assento ocupado).
'''
linhas = dict


def gerar_onibus():
    onibus = []
    for i in range(20):
        linha = []
        for j in range(20):
            onibus.append(linha)

    return onibus


def preencher_onibus():
    '''
    As informações de cada ônibus são:
o Data da partida (dia/mês/ano)
o Assentos disponíveis
    '''
    pass


def cadastroLinhas():
    '''
Cada linha tem um conjunto de horários diários de partida de ônibus.
 Os dados de cada linha são:
o Cidade de origem
o Cidade de destino
o Horário de partida (hora:minuto)
o Valor da passagem
    '''
    pass


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


while True:
    try:
        print("Sistema da Rodoviária:\n 1 - Cadastro de linhas: (inserir, remover e alterar).")
        print("\n2 - Consultar todos os horários disponíveis para uma determinada cidade.")
        print("\n3 - Consultar os assentos disponíveis no ônibus, informando a cidade de destino, horário e data. A data deve ser inferior a 30 dias, contados a partir da data atual.\nApós uma consulta de assento disponível, o sistema deve perguntar se algum assento vai ser reservado (caso existam ainda assentos disponíveis).")
        print("geração dos relatórios (na tela ou em arquivo texto, escolha do usuário): \no Total arrecadado com venda de passagens no mês corrente para cada linha. \no Ocupação percentual média de cada linha em cada dia da semana (uma matriz).\n Além de receber as reservas pelo teclado, permitir ler as reservas de um arquivo textono seguinte formato:\no CIDADE, HORÁRIO(hh:mm), DATA(dd/mm/aaaa), ASSENTO\no Uma reserva por linha.\n Gravar em um arquivo texto todas as reservas que não puderam ser realizadas, juntamente com o motivo (ex.: ônibus cheio, ônibus já partiu, assento ocupado).")
        print("0 - Sair")

        opsao = input(int("Opção: "))
        match(opsao):
            case 1:
            
            case 2:
            
            case 3:
            
            case 0:
            
            case _:
                print("Opção inválida")
        
    except ValueError:
        print("=====" * 10)
        print("Opção inválida!")
        print("=====" * 10)