import numpy as np
import datetime as dt
from pathlib import Path

data_atual = dt.datetime.now()

linhas = {'Cidade de origem':[],'Cidade de destino':[],'Horário de partida':[],'Valor da passagem':[], 'Ônibus': [] }#Dicionário da linha

onibus = {'Data da partida': [], 'Assentos Disponíveis':[]}#Dicionário do ônibus

viagem = []
vendas = [] 

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
# Editar linhas:

def edit_linhas():
    # Verifica se existe linha cadastrada
    if len(linhas['Cidade de origem']) == 0:
        print("\nNenhuma linha encontrada!")
        return

    print("\nLinhas Cadastradas:\n")
    for i in range(len(linhas['Cidade de origem'])):
        print(f"{i} - {linhas['Cidade de origem'][i]}|{linhas['Cidade de destino'][i]}|Partida:{linhas['Horário de partida'][i]}|Valor: R${linhas['Valor da passagem'][i]}")
    
    try:
        idx = int(input("\nDigite o número da linha que deseja editar:\n-> "))
    except ValueError: 
        print("\nErro: Digite um número inteiro!\n")
        return
    
    if idx < 0 or idx >= len(linhas['Cidade de origem']):
        print("\nErro: Linha inexistente!\n")
        return
    # Pergunta novos valores (Enter mantém o mesmo)
    print("\nQual campo deseja DELETAR?\n")
    print("1 - Cidade de origem;\n2 - Cidade de destino;\n3 - Horário de partida;\n4 - Valor da passagem;\n5 - Ônibus (remove apenas 1 ônibus)\n")

    cidade_origem_edit = input(f"Nova cidade de origem (atual: {linhas['Cidade de origem'][idx]}): ")
    cidade_destino_edit = input(f"Nova cidade de destino (atual: {linhas['Cidade de destino'][idx]}): ")

    horario_edit = input(f"Novo horário (atual: {linhas['Horário de partida'][idx]}) [00:00]: ")

    valor_edit = input(f"Novo valor da passagem (atual: R$ {linhas['Valor da passagem'][idx]}): ")

    if cidade_origem_edit.strip():
        linhas['Cidade de origem'][idx] = cidade_origem_edit
    if cidade_destino_edit.strip():
        linhas['Cidade de destino'][idx] = cidade_destino_edit
    if horario_edit.strip():
        if ":" in horario_edit:
            hora, minuto = horario_edit.split(':')
            if hora.isdigit() and minuto.isdigit() and 0 < int(hora) < 24 and 0 < int(minuto) < 60:
                linhas['Horário de partida'][idx] = horario_edit
            else:
                    print("\nHorário inválido. Mantido o original.\n")
        else:
            print("\nFormato inválido. Mantido o original.\n")
    if valor_edit.strip():
        try:
            linhas['Valor da passagem'][idx] = int(valor_edit)
        except ValueError:
            print("\nValor inválido. Mantido o original.\n")
    
    print("\nLinha atualizada com sucesso!\n")

def del_linhas():
    # Verifica se existe linha cadastrada
    if len(linhas['Cidade de origem']) == 0:
        print("\nNenhuma linha encontrada!")
        return

    print("\nLinhas Cadastradas:\n")
    for i in range(len(linhas['Cidade de origem'])):
        print(f"{i} - {linhas['Cidade de origem'][i]}|{linhas['Cidade de destino'][i]}|Partida:{linhas['Horário de partida'][i]}|Valor: R${linhas['Valor da passagem'][i]}")
    
    try:
        idx2 = int(input("\nDigite o número da linha que deseja editar:\n-> "))
    except ValueError: 
        print("\nErro: Digite um número inteiro!\n")
        return
    
    if idx2 < 0 or idx2 >= len(linhas['Cidade de origem']):
        print("\nErro: Linha inexistente!\n")
        return
    # Pergunta valores a serem deletados (Enter mantém o mesmo)
    print("\nQual campo deseja DELETAR?\n")
    print("1 - Cidade de origem;\n2 - Cidade de destino;\n3 - Horário de partida;\n4 - Valor da passagem;\n5 - Ônibus (remove apenas 1 ônibus)\n")

    try:
        opc = int(input("Opção: "))
        # Deletar campo escolhido
        match opc:
            case 1:
                linhas['Cidade de origem'][idx2] = None
            case 2:
                linhas['Cidade de destino'][idx2] = None
            case 3:
                linhas['Horário de partida'][idx2] = None
            case 4:
                linhas['Valor da passagem'][idx2] = None
            case 5:
                linhas['Ônibus'][idx2] = None
            case _:
                print("\nErro: Opção inválida!\n")
                return
    except ValueError:
        print("\nErro: Digite um número inteiro!\n")
        return

    print("\nCampo deletado com sucesso!\n")
    
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
        # Registrando a venda:
            valor = linhas['Valor da passagem'][onibus_escolhido]
            hoje = dt.date.today().isoformat()
            vendas.append({"Linha" : onibus_escolhido, "Data" : hoje, "Valor" : valor}) 

        #Registrando a viagem:
            capacidade = onibus.size
            embarcados = np.sum(onibus)

            viagem.append({"Linha:": onibus_escolhido, "Data": hoje, "Embarcados": int(embarcados), "Capacidade" : capacidade})

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

    onibus = []

    for i in range(5):
        for j in range(4):
            status = "L" if assentos[i][j] == 0 else "X"
            onibus.append(f"[{i},{j}] - {status}")


    return onibus

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
# Total arrecadado por linha
def total_arrecadado_linha(vendas):
    # Obtém mês e ano atuais para filtrar apenas os registros do mês corrente
    mes_atual = dt.date.today().month
    ano_atual = dt.date.today().year

    totais = {} # dicionário onde chave = linha e valor = total em dinheiro
    # Percorre todas as vendas registradas
    for v in vendas:
        # A data está no formato YYYY-MM-DD, então dividimos
        ano, mes, _ = map(int, v["Data"].split("-"))
        # Verifica se a venda ocorreu no ano e mês atuais
        if ano == ano_atual and mes == mes_atual:
            linha = v["Linha"]
            # Soma o valor ao total da linha correspondente
            totais[linha] = totais.get(linha, 0) + v["Valor"] # totais.get(linha, 0) retorna 0 caso a linha ainda não exista no dicionário
    return totais

#Calcular a ocupação percentual média de cada linha em cada dia da semana (matriz 7 dias)
def ocupacao_media():
    matriz = {} # estrutura: {linha: {dia: [ocupações]}}

    # Processa cada registro de viagem
    for v in viagem:
        # Converte string "YYYY-MM-DD" para data real do Python
        data = dt.date.fromisoformat(v["Data"])
        # weekday() -> segunda=0, ..., domingo=6
        dia = data.weekday()  # segunda=0 ... domingo=6
        linha = v["Linha"]
        # Calcula ocupação percentual da viagem
        ocupacao = (v["Embarcados"] / v["Capacidade"]) * 100

        # Se a linha ainda não existe, cria estrutura com 7 listas (uma para cada dia)
        if linha not in matriz:
            matriz[linha] = {d: [] for d in range(7)}
        # Adiciona o valor de ocupação no respectivo dia da semana
        matriz[linha][dia].append(ocupacao)

    # cálculo das médias
    resultado = {}
    for linha, dias in matriz.items():
        # Para cada linha, cria um dicionário com a média por dia
        resultado[linha] = {}
        for dia, ocups in dias.items():
            if ocups:  # há valores na lista
                media = round(sum(ocups) / len(ocups), 2)
            else:      # lista vazia → média = 0
                media = 0

            resultado[linha][dia] = media

    return resultado


# Gerar Relatorio na tela
def gerarRelatorios():
    print("\n===== RELATÓRIO =====")

    print("\n1) Total arrecadado por linha no mês atual:")
    # Chama a função que calcula o total arrecadado
    totais = total_arrecadado_linha(vendas)
    for linha, valor in totais.items():
        print(f"Linha {linha}: R$ {valor:.2f}")

    print("\n2) Ocupação média (%) por dia da semana:")
    # Chama a função que calcula ocupações
    matriz = ocupacao_media()
    dias = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"] # Estética
    # Imprime matriz por linha
    for linha, valores in matriz.items():
        print(f"\nLinha {linha}:")
        for d in range(7):
            print(f"  {dias[d]}: {valores[d]:.2f}%")
'''
 Função: Ler um arquivo de reservas e:
 - marcar assentos no ônibus
 - registrar vendas
 - atualizar estatísticas de viagens
'''
def ler_reservas_arquivo(nome):
    with open(nome, "r", encoding="utf-8") as f:
        for linha in f:
            cidade, horario, data_str, assento = linha.strip().split(",")
            # Remove espaços excedentes
            cidade = cidade.strip()
            horario = horario.strip()
            # Converte data para objeto date
            data = dt.datetime.strptime(data_str.strip(), "%d/%m/%Y").date()
            # Assento no formato "x-y"
            x, y = map(int, assento.strip().split("-"))

            # Encontrar a linha correspondente, ou seja, procura a linha correspondente dentro do cadastro
            for i in range(len(linhas["Cidade de origem"])):
                if (linhas["Cidade de origem"][i] == cidade
                   and linhas["Horário de partida"][i] == horario):

                    # Marca o assento como ocupado (1)
                    linhas["Ônibus"][i][x][y] = 1

                    # registrar venda
                    valor = linhas["Valor da passagem"][i]
                    vendas.append({"Linha": i, "Data": data, "Valor": valor})

                    # registrar viagem
                    capacidade = 20
                    embarcados = np.sum(linhas["Ônibus"][i])
                    # Registra estatística de viagem
                    viagem.append({"Linha": i, "Data": data, "Embarcados": embarcados, "Capacidade": capacidade})
                    break


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
        print("6 - Gerar Relatório;")
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
                            del_linhas()
                            print('\nEm breve..\n')

                        case 3:
                            edit_linhas()
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
            
            case 6:
                try:
                    opcao2 = int(input("Deseja gerar relatório:\n1 - Em arquivo .txt\n2 - Na tela\n-> "))

                    totais = total_arrecadado_linha(vendas)
                    ocupacao = ocupacao_media()

                    if opcao2 == 1:
                        relatorio = Path("Relatorio.txt")

                        texto = "===== RELATÓRIO =====\n\n"

                        texto += "1) Total arrecadado por linha no mês:\n"
                        for linha, valor in totais.items():
                            texto += f"   Linha {linha}: R$ {valor:.2f}\n"

                        texto += "\n2) Ocupação média por dia da semana (%):\n"
                        dias = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]

                        for linha, dados in ocupacao.items():
                            texto += f"\n   Linha {linha}:\n"
                            for d in range(7):
                                texto += f"      {dias[d]}: {dados[d]:.2f}%\n"

                        relatorio.write_text(texto, encoding="utf-8")
                        print("\nRelatório salvo em Relatorio.txt!\n")

                    elif opcao2 == 2:
                        gerarRelatorios()

                    else:
                        print("\nErro: Opção inválida!\n")

                except ValueError:
                    print("\nErro: Digite um número inteiro!\n")

                
            case 0:

                sair = 1
                print('\nFinalizando programa...\n')
            
            case _:
                print("\nErro: Digite uma das opções exibidas no menu!\n")
        
    except (ValueError):
        print("=====" * 10)
        print("\nErro: Opção inválida, digite um número inteiro!\n")
        print("=====" * 10)
