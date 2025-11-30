import numpy as np
import datetime as dt
from typing import List

#--------------------------------------------------------------------------------------------------------------------------------------------------

linhas : list[dict] = []#Dicionário das linhas

ARQUIVO_RESERVAS_FALHAS = "reservas_falharam.txt"#Define o nome do arquivo txt de reservas falhas

#------------------------------------------------------------------------------------------------------------------------------------------------






#--------------------------------------------------------------------------------------------------------------------------------------------------
"""FUNÇÕES:"""
#------------------------------------------------------------------------------------------------------------------------------------------------

def criar_matriz_assentos():

    return np.zeros((5, 4), dtype=int) #Cria uma matriz 5x4 (0 = vazio | 1 = ocupado)

#-------------------------------------------------------------------------------------------------------------------------------------------------

def assento_numero_para_indices(n):#Serve para tranformar o número do assento digitado pelo usuário em uma posição na matriz
    
    if not (1 <= n <= 20):
        print("\nErro: Digite um valor entre 1 e 20.\n")
        return None
    
    idx = n - 1
    i = idx // 4  # 0..4
    j = idx % 4   # 0..3

    return i, j

#------------------------------------------------------------------------------------------------------------------------------------------------

def indices_para_assento_numero(i, j):#Tranforma o indice da matriz no "número do assento"

    return i * 4 + j + 1

#------------------------------------------------------------------------------------------------------------------------------------------------

def imprime_matriz(mat):#Imprime a matriz formatada
    
    linhas, colunas = mat.shape
    print("\nMapa de assentos (ímpares = janela).\n")

    for i in range(linhas):
        linha = []
        for j in range(colunas):

            num = indices_para_assento_numero(i, j)#Número do assento

            if mat[i, j] == 0:
                assento = "V" #Assento vazio
            else:
                assento = "O" #Assento ocupado

            linha.append(f"[{num}:{assento}]") 

        print("  ".join(linha))# imprime com pequeno espaçamento para simular corredor ;)


#------------------------------------------------------------------------------------------------------------------------------------------------

def verificar_data(data_str):#Verifica se a data foi digitada corretamente, caso sim retorna em formato datetime, caso não exibe uma mensagem de erro
    
    try:

        dia, mes, ano = data_str.split('/')
        data_dt = dt.date(int(ano), int(mes), int(dia))
        return data_dt
    
    except Exception:

        print("\nERRO: Digite a data no formato correto! (dd/mm/aaaa)\n")
        return None
    
#------------------------------------------------------------------------------------------------------------------------------------------------

def verificar_horario(horario):#Verifica se o horário foi digitada corretamente, caso sim retorna as horas e minutos, caso não exibe uma mensagem de erro
    
    if horario.find(':') != 2:

        print("\nERRO: Digite o horário no formato correto!(HH:MM)\n")
        return None
    
    hora, minuto = horario.split(':')

    try:

        hora = int(hora)
        minuto = int(minuto)
    
    except:

        print("\nERRO: O horário deve ser formado de inteiros!\n")
        return None
    
    if not (0 <= hora < 24 and 0 <= minuto < 60):

        print("Horário fora do intervalo.")
        return None
    
    return hora, minuto

#------------------------------------------------------------------------------------------------------------------------------------------------

def dentro_de_30_dias(data_viagem):#Função para verificar se o ônibus estará dentro dos pŕoximos 30 dias

    hoje = dt.date.today()#Usa a função de datetime para saber o dia de hoje

    diferenca = (data_viagem - hoje).days#Calcula a diferença da data da viagem e a data atual

    return 0 <= diferenca <= 30

#------------------------------------------------------------------------------------------------------------------------------------------------

def onibus_ja_partiu(data_viagem, horario_str):#Verifica se o ônibus já partiu, com base na data atual

    
    hora, minuto = verificar_horario(horario_str)

    dt_viagem = dt.datetime.combine(data_viagem, dt.time(hour=hora, minute=minuto))

    return dt.datetime.now() >= dt_viagem

#------------------------------------------------------------------------------------------------------------------------------------------------

def cadastroLinhas():#Função que cria as linhas
    
    origem = input('\nDigite o nome da cidade de origem da linha:\n-> ').strip()
    destino = input('Digite o nome da cidade de destino da linha:\n-> ').strip()
    horario = input('Digite o horário de partida (HH:MM):\n-> ').strip()
    
    
    horario_verificado = verificar_horario(horario)

    if (horario_verificado == None):
        return
    

    try:
        valor = int(input('Digite o valor em reais da passagem (inteiro):\n-> R$').strip())

    except ValueError:
        print('\nErro: Digite um número inteiro!\n')
        return

    linha = {#Dicionário da linha preenchido
        "origem": origem,#cidade de origem
        "destino": destino,#cidade de destino
        "horario": f"{horario[:2]}:{horario[3:]}",#horário de partida
        "valor": valor,#valor da passagem
        "onibus": [],#ônibus
        "vendas": []  # histórico de vendas desta linha
    }

    linhas.append(linha)#adiciona esse dicionário a lista de dicionário de linhas

    print("\nLinha cadastrada com sucesso! Agora você pode adicionar ônibus (datas) a esta linha.\n")

#------------------------------------------------------------------------------------------------------------------------------------------------

def listar_linhas():#Função para listar as linha mostrando os indices para o usuário
    if not linhas:
        print("\nNenhuma linha cadastrada.\n")
        return
    for idx, l in enumerate(linhas):
        print(f"Índice {idx} | {l['origem']} -> {l['destino']} | Horário: {l['horario']} | Valor: R$ {l['valor']}")
        if l['onibus']:
            for b_i, b in enumerate(l['onibus']):
                print(f"    Ônibus {b_i} - Data: {b['data'].strftime('%d/%m/%Y')} - Assentos ocupados: {np.sum(b['assentos'])}/20")
    print()

#------------------------------------------------------------------------------------------------------------------------------------------------

def remover_linha():#Função para remover uma linha

    listar_linhas()

    try:
        indice = int(input("Digite o índice da linha a remover:\n-> "))

    except ValueError:
        print("Erro: digite um número inteiro.")
        return
    

    if 0 <= indice < len(linhas):
        linhas.pop(indice)
        print("Linha removida.")
    else:
        print("Índice inválido.")

#------------------------------------------------------------------------------------------------------------------------------------------------

def editar_linha():

    listar_linhas()

    try:
        indice = int(input("Digite o índice da linha a editar:\n-> "))

    except ValueError:
        print("Erro: digite um número inteiro.")
        return
    

    if not (0 <= indice < len(linhas)):
        print("Índice inválido.")
        return
    

    l = linhas[indice]

    #Criar um switch case para ficar mais organizado
    print("Deixe em branco para manter o valor atual.")
    novo_origem = input(f"Origem atual [{l['origem']}]:\n-> ").strip()
    novo_destino = input(f"Destino atual [{l['destino']}]:\n-> ").strip()
    novo_horario = input(f"Horário atual [{l['horario']}]:\n-> ").strip()
    novo_valor = input(f"Valor atual [R$ {l['valor']}]:\n-> ").strip()

    if novo_origem:
        l['origem'] = novo_origem


    if novo_destino:
        l['destino'] = novo_destino


    if novo_horario:
        try:
            verificar_horario(novo_horario)
            l['horario'] = novo_horario
        except ValueError as e:
            print("Horário inválido — mantido o original.")


    if novo_valor:
        try:
            l['valor'] = int(novo_valor)
        except ValueError:
            print("Valor inválido — mantido o original.")

    
    print("Linha editada.")

#------------------------------------------------------------------------------------------------------------------------------------------------

def criar_onibus_para_linha():#Função que adiciona um ônibus a uma linha já existente
    
    listar_linhas()

    try:
        indice = int(input("Digite o índice da linha para adicionar um ônibus:\n-> "))
    except ValueError:
        print("Erro: digite um número inteiro.")
        return
    

    if not (0 <= indice < len(linhas)):
        print("Erro: Digite um ínndice válido.")
        return
    

    data_str = input("Digite a data da viagem (dd/mm/aaaa):\n-> ").strip()


    data_viagem = verificar_data(data_str)

    if (data_viagem != None):
        
        return
    

    if not dentro_de_30_dias(data_viagem):

        print("Erro: a data deve ser dentro dos próximos 30 dias (e não no passado).")
        return
    

    # cria ônibus com matriz vazia
    onibus = {"data": data_viagem, "assentos": criar_matriz_assentos(), "vendas_onibus": []}#Dicionário do ônibus

    linhas[indice]['onibus'].append(onibus)#Adiciona o novo ônibus no dicionário da linha
    
    print("Ônibus criado com sucesso para a data", data_viagem.strftime("%d/%m/%Y"))

#------------------------------------------------------------------------------------------------------------------------------------------------

def escolher_linha_onibus():#Para o usário escolher uma linha e um ônibus da mesma


    cidade = input("\nDigite a cidade de destino para consulta:\n-> ").strip()#Pede aonde o usuário quer ir

    candidatos = [(i, l) for i, l in enumerate(linhas) if l['destino'].lower() == cidade.lower()]#Lista as linhas que têm esse destino

    if not candidatos:#Se não houver linhas com esse destino não retorna nada
        print("Nenhuma linha encontrada para essa cidade.")
        return None, None
    

    
    print("\nLinhas encontradas:")#Printa as linhas e horários e o indice para que o usuário possa escolher

    for i, l in candidatos:
        print(f"{i} - {l['origem']} -> {l['destino']} | Horário: {l['horario']} | Valor: R$ {l['valor']}")

    try:
        indice_linha = int(input("\nEscolha o índice da linha (entre os listados):\n-> "))

    except ValueError:
        print("Erro: digite um número inteiro.")
        return None, None
    

    if not (0 <= indice_linha < len(linhas)) or (linhas[indice_linha]['destino'].lower() != cidade.lower()):#trata caso o indice não exista ou se a cidade de destino for diferente
        print("Índice inválido para a cidade informada.")
        return None, None
    

    
    linha_escolhida = linhas[indice_linha]# Agora o usuário escolhe data dentre ônibus disponíveis

    if not linha_escolhida['onibus']:#Se a linha não tiver ônibus, irá retornar nada
        print("Essa linha não tem ônibus cadastrados (datas).")
        return None, None
    

    print("\nÔnibus (índice) e datas disponíveis para essa linha:")#Mostra os ônibus e seus índices

    for i, o in enumerate(l['onibus']):
        print(f"{i} - Data: {o['data'].strftime('%d/%m/%Y')} - Assentos ocupados: {np.sum(o['assentos'])}/20")
    
    
    try:
        indice_onibus = int(input("\nEscolha o índice do ônibus (data):\n-> "))#Usuário digita qual ônibus ele quer

    except ValueError:
        print("Erro: digite um número inteiro.")
        return None, None
    

    if not (0 <= indice_onibus < len(l['onibus'])):#Se o índice não existir
        print("Índice de ônibus inválido.")
        return None, None
    

    return indice_linha, indice_onibus

#------------------------------------------------------------------------------------------------------------------------------------------------

def consultarHorarios():#Função para o usuário consultar os horários disponíveis para uma cidade

    cidade_escolhida = input("\nDigite a cidade para listar horários disponíveis (origem ou destino):\n-> ").strip()
    horarios = []

    for i in linhas:

        if i['origem'].lower() == cidade_escolhida.lower() or i['destino'].lower() == cidade_escolhida.lower():
            horarios.append((i['origem'], i['destino'], i['horario']))

    if not horarios:
        print("Nenhum horário encontrado para essa cidade.")

    else:
        print("\nHorários encontrados para cidade", cidade_escolhida)

        for origem, destino, horario in horarios:
            print(f"{origem} -> {destino} | Horário: {horario}")

    

#------------------------------------------------------------------------------------------------------------------------------------------------

def consultarAssentos():#Função que mostra quais os assentos estão disponíveis ou não


    indice_linha, indice_onibus = escolher_linha_onibus()

    if indice_linha is None:
        return
    

    linha_escolhida = linhas[indice_linha]
    onibus_escolhido = linha_escolhida['onibus'][indice_onibus]

    
    if not dentro_de_30_dias(onibus_escolhido['data']):# verificar data dentro de 30 dias
        print("Data fora do intervalo de 30 dias.")
        return
    
    
    imprime_matriz(onibus_escolhido['assentos'])# Imprime a matriz formatada

    
    if np.sum(onibus_escolhido['assentos']) < 20:#verifica se existem assentos disponíveis

        resp = input("Deseja reservar algum assento? (s/n)\n-> ").strip().lower()

        if resp == 's':
            preencher_onibus(indice_linha, indice_onibus)

    else:#Caso não tenha mais assentos
        print("Ônibus cheio.")

#------------------------------------------------------------------------------------------------------------------------------------------------

def preencher_onibus(indice_linha, indice_onibus):#Permite o usário escolher um assento

    if indice_linha is None or indice_onibus is None:

        indice_linha, indice_onibus = escolher_linha_onibus()

        if indice_linha is None:#Se ele retornar None é porque algum erro aconteceu na função escolher_linha_onibus
            return
        

    linha_escolhida = linhas[indice_linha]
    onibus_escolhido = linha_escolhida['onibus'][indice_onibus]


    
    if not dentro_de_30_dias(onibus_escolhido['data']):#Verifica se a data corresponde para os 30 dias

        print("Erro: Não é possível reservar data para mais 30 dias.")
        return
    

    
    if onibus_ja_partiu(onibus_escolhido['data'], linha_escolhida['horario']):#Verifica se o ônibus já partiu

        print("Não é possível reservar: ônibus já partiu.")
        return
    


    imprime_matriz(onibus_escolhido['assentos'])#Imprime a matriz dos assentos do ônibus
    
    try:#Usuário pode digitar qual assento (1-20) quer reservar
        numero_assento = int(input("Digite o número do assento desejado (1-20):\n-> "))

    except ValueError:
        print("Erro: digite um número inteiro.")
        return
    

    
    i, j = assento_numero_para_indices(numero_assento)#Tranforma o número em posição da matriz
    
    if (i == None) and (j == None):#Caso seja vazio é porque algo deu errado na função
        
        return
    

    if onibus_escolhido['assentos'][i, j] == 1:#VErifica se o assento já não foi reservado

        print("Erro: assento já ocupado.")
        return
    

    onibus_escolhido['assentos'][i, j] = 1#Marca o assento escolhido pelo usuário


    venda = {# registra venda no relatório
        
        "data_venda": dt.datetime.now(),
        "preco": linha_escolhida['valor'],
        "data_viagem": onibus_escolhido['data'],
        "assento": numero_assento,
        "linha_origem": linha_escolhida['origem'],
        "linha_destino": linha_escolhida['destino']
    }


    linha_escolhida['vendas'].append(venda)
    onibus_escolhido['vendas_onibus'].append(venda)

    print(f"\nCompra realizada! Valor: R$ {linha_escolhida['valor']:.2f} - Assento {numero_assento}\n")

#------------------------------------------------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------------------------------------------------------------
"""ARQUIVOS .TXT :"""
#------------------------------------------------------------------------------------------------------------------------------------------------

# Arquivo de reservas (leitura)

def processar_arquivo_reservas(nome_arquivo: str):
    """
    Cada linha do arquivo:
    CIDADE, HORARIO(hh:mm), DATA(dd/mm/aaaa), ASSENTO
    Exemplo: Belo Horizonte, 08:30, 12/12/2025, 5
    """
    falhas = []
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            linhas_arquivo = [ln.strip() for ln in f if ln.strip()]
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return
    for linha_txt in linhas_arquivo:
        parts = [p.strip() for p in linha_txt.split(',')]
        if len(parts) != 4:
            falhas.append((linha_txt, "Formato inválido"))
            continue
        cidade, horario_str, data_str, assento_str = parts
        # localizar linha que tenha destino = cidade e horario = horario_str
        candidatos = [ (li, l) for li, l in enumerate(linhas) 
                       if l['destino'].lower() == cidade.lower() and l['horario'] == horario_str ]
        if not candidatos:
            falhas.append((linha_txt, "Linha inexistente (cidade/horário não correspondem)"))
            continue
        # pegar data
        try:
            data_viagem = verificar_data(data_str)
        except ValueError:
            falhas.append((linha_txt, "Data inválida"))
            continue
        # encontrar ônibus com essa data
        li, l = candidatos[0]  # se várias linhas iguais, pega a primeira
        idx_onibus = None
        for bi, b in enumerate(l['onibus']):
            if b['data'] == data_viagem:
                idx_onibus = bi
                break
        if idx_onibus is None:
            falhas.append((linha_txt, "Ônibus nessa data não encontrado"))
            continue
        # validar assento numérico
        try:
            num_assento = int(assento_str)
        except ValueError:
            falhas.append((linha_txt, "Assento inválido"))
            continue
        # validar data <=30 dias e não partiu e assento livre
        b = l['onibus'][idx_onibus]
        if not dentro_de_30_dias(b['data']):
            falhas.append((linha_txt, "Data fora do intervalo de 30 dias"))
            continue
        if onibus_ja_partiu(b['data'], l['horario']):
            falhas.append((linha_txt, "Ônibus já partiu"))
            continue
        try:
            i, j = assento_numero_para_indices(num_assento)
        except ValueError:
            falhas.append((linha_txt, "Assento fora de 1-20"))
            continue
        if b['assentos'][i, j] == 1:
            falhas.append((linha_txt, "Assento ocupado"))
            continue
        # tudo ok: reservar
        b['assentos'][i, j] = 1
        venda = {
            "data_venda": dt.datetime.now(),
            "preco": l['valor'],
            "data_viagem": b['data'],
            "assento": num_assento,
            "linha_origem": l['origem'],
            "linha_destino": l['destino']
        }
        l['vendas'].append(venda)
        b['vendas_onibus'].append(venda)
    # gravar falhas em arquivo
    if falhas:
        with open(ARQUIVO_RESERVAS_FALHAS, 'a', encoding='utf-8') as f:
            for txt, motivo in falhas:
                f.write(f"{txt} -> Motivo: {motivo}\n")
        print(f"{len(falhas)} reserva(s) não puderam ser realizadas. Detalhes gravados em {ARQUIVO_RESERVAS_FALHAS}")
    else:
        print("Todas as reservas do arquivo foram processadas com sucesso.")

#------------------------------------------------------------------------------------------------------------------------------------------------

# Relatórios

def relatorio_total_arrecadado_mes_corrente():
    hoje = dt.date.today()
    mes = hoje.month
    ano = hoje.year
    print(f"\nTotal arrecadado no mês corrente ({mes}/{ano}):\n")
    for idx, l in enumerate(linhas):
        total = 0
        for v in l['vendas']:
            if v['data_venda'].year == ano and v['data_venda'].month == mes:
                total += v['preco']
        print(f"Linha {idx}: {l['origem']} -> {l['destino']} | Total: R$ {total:.2f}")
    print()

def relatorio_ocupacao_media_por_dia_da_semana():
    """
    Para cada linha, calcula ocupação percentual média por dia da semana (0=segunda,...6=domingo).
    Ocupação = (assentos ocupados)/(20) *100
    Calculamos média considerando todos os ônibus existentes (datas) daquela linha (incluindo passadas).
    """
    print("\nOcupação percentual média por linha (linhas) por dia da semana (0=segunda ... 6=domingo):\n")
    for idx, l in enumerate(linhas):
        # criar vetor de listas para cada dia da semana
        dias = [[] for _ in range(7)]
        for b in l['onibus']:
            weekday = b['data'].weekday()  # 0..6 (segunda..domingo)
            ocup = (np.sum(b['assentos']) / 20) * 100
            dias[weekday].append(ocup)
        # calcular médias
        medias = []
        for lista in dias:
            if lista:
                medias.append(sum(lista)/len(lista))
            else:
                medias.append(0.0)
        # imprimir
        medias_str = ", ".join([f"{m:.1f}%" for m in medias])
        print(f"Linha {idx}: {l['origem']} -> {l['destino']} | Médias por dia: [{medias_str}]")
    print()

def gerarRelatorios():
    print("\nRelatórios disponíveis:")
    print("1 - Total arrecadado no mês corrente por linha")
    print("2 - Ocupação percentual média por linha por dia da semana")
    try:
        opc = int(input("Escolha (1/2):\n-> "))
    except ValueError:
        print("Erro: digite um inteiro.")
        return
    if opc == 1:
        relatorio_total_arrecadado_mes_corrente()
    elif opc == 2:
        relatorio_ocupacao_media_por_dia_da_semana()
    else:
        print("Opção inválida.")

#------------------------------------------------------------------------------------------------------------------------------------------------

"""MENU:"""

def menu_principal():

    sair = 0

    while sair == 0:


        try:
            print("\nSistema da Rodoviária:")
            print("1 - Cadastrar ou editar linhas;")
            print("2 - Consultar horários disponíveis para uma cidade;")
            print("3 - Consultar os assentos disponíveis no ônibus;")
            print("4 - Marcar (reservar) um assento de um ônibus;")
            print("5 - Criar outro ônibus (adicionar data) para uma linha já existente;")
            print("6 - Ler reservas de arquivo (formato especificado);")
            print("7 - Gerar relatórios;")
            #print("8 - Listar todas as linhas e ônibus cadastrados;") TESTE
            print("0 - Sair.")
            opcao = int(input("Opção: "))


            match (opcao):
                
                case 1:#Criar, remover ou editar uma linha

                    print("\n1 - Criar linha\n2 - Remover linha\n3 - Editar linha\n-> ")
                    
                    try:
                        opcao_linha = int(input("Opção: "))
                    
                    except ValueError:
                        print("Erro: digite um inteiro.")
                        continue

                    match opcao_linha:

                        case 1:#Cria uma linha
                            cadastroLinhas()

                        case 2:#Remove uma linha
                            remover_linha()
                        
                        case 3:#Edita linha
                            editar_linha()

                        case _:#Default
                            print("Opção inválida.")
                
                
                case 2:#Consulta os horários disponíveis 
                    consultarHorarios()
                
                case 3:#Consulta os assentos disponíveis em um ônibus
                    consultarAssentos()
                
                case 4:#Reserva um assento em um ônibus
                    preencher_onibus()
                
                case 5:#Cria um ônibus para uma linha já existente
                    criar_onibus_para_linha()
                
                case 6:
                    nome_arquivo = input("Digite o caminho do arquivo de reservas:\n-> ").strip()
                    processar_arquivo_reservas(nome_arquivo)
                
                case 7:
                    gerarRelatorios()
                
                
                #TESTE
                #case 8:
                #    listar_linhas_com_indices()


                case 0:#Para finalizar o programa
                    print("Finalizando o programa...")
                    sair = 1
                    break

                case _:#Default
                    print("Opção inválida.")


        except ValueError:#Tratar erro
            print("Erro: opção inválida. Digite um número inteiro.")

