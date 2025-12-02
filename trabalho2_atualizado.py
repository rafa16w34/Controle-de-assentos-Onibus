"""

Esse código foi feito por mim (Rafael Alves F.) e meu irmão (Gabriel Alves F.) e passamos muito tempo corrigindo erros, 
procurando novas funções e mudando a lógica do código para que tudo ficasse em equilíbrio.
O código a seguir é o que podemos garantir como funcional e para que se torne mais que isso, quero dizer, um pouco mais emocional
trago a frente um poema que achei na internet sobre uma viagem de ônibus:

“DENTRO DO ÔNIBUS”. (Daniel Costa)

Dentro do ônibus
Vejo todo tipo de gente
Uns dormindo, uns acordados
Uns perdidos e alguns crentes

O cobrador ali sentado
Viaja quase dormindo
O careca na minha frente
Olha pro lado me parecendo perdido

O ônibus mal cuidado
Segue em frente pegando no tranco
A gordinha do meu lado
Ocupa mais da metade do banco

Uma senhora segue em busca
Se um assento preferencial
O jovem malandro não se move
Enquanto finge ler um jornal

A garota vai apoiando
Sua cabeça na janela suja
Vejo uma mancha ensebada no vidro
Pelo neutrox que ela usa

Um ambulante entra suando
Vendendo tudo o que tem direito
Quando não compram ele apela
E bota tudo na metade do preço

Completamente distraído
Eu me assustei quando o coletivo freou
Eu não devia mas eu ri
De uma mulher que escorregou

Um pai furioso entrou com o filho
Que gritava e chorava
Não me importei por que em dois pontos
Em meu destino eu chegava.

"""

import numpy as np
import datetime as dt


#--------------------------------------------------------------------------------------------------------------------------------------------------

linhas : list[dict] = []#Dicionário das linhas

ARQUIVO_RESERVAS_FALHAS = "reservas_falharam.txt"#Define o nome do arquivo txt de reservas falhas

#------------------------------------------------------------------------------------------------------------------------------------------------

"""FUNÇÕES:"""
#------------------------------------------------------------------------------------------------------------------------------------------------

def criar_matriz_assentos():

    return np.zeros((5, 4), dtype=int) #Cria uma matriz 5x4 (0 = vazio | 1 = ocupado)

#-------------------------------------------------------------------------------------------------------------------------------------------------

def assento_numero_para_indices(n):#Serve para tranformar o número do assento digitado pelo usuário em uma posição na matriz
    
    if not (1 <= n <= 20):
        print("\nErro: Digite um valor entre 1 e 20.\n")
        return None
    
    indice = n - 1
    i = indice // 4  # de 0 a 4 (linhas)
    j = indice % 4   # de 0 a 3 (colunas)

    return i, j#Retorna as posições

#------------------------------------------------------------------------------------------------------------------------------------------------

def indices_para_assento_numero(i, j):#Tranforma o indice da matriz no "número do assento"

    return i * 4 + j + 1#Retorna os indices

#------------------------------------------------------------------------------------------------------------------------------------------------

def imprime_matriz(bus):#Imprime a matriz formatada (recebe os assentos de um ônibus escolhido)
    
    linhas, colunas = bus.shape
    print("\nMapa de assentos (ímpares = janela).\n")

    for i in range(linhas):
        linha = []
        for j in range(colunas):

            num = indices_para_assento_numero(i, j)#Número do assento

            if bus[i, j] == 0:
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

        print("\nERRO: Digite o horário no formato correto!(00:00)\n")
        return None
    
    hora, minuto = horario.split(':')

    try:

        hora = int(hora)
        minuto = int(minuto)
    
    except:

        print("\nERRO: O horário deve ser formado de inteiros!\n")
        return None
    
    if not (0 <= hora < 24 and 0 <= minuto < 60):

        print("ERRO: Horário fora do intervalo de 24hrs.")
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
    
    origem = input('\nDigite o nome da cidade de origem da linha:\n-> ')
    destino = input('Digite o nome da cidade de destino da linha:\n-> ')
    horario = input('Digite o horário de partida (00:00):\n-> ')
    
    
    horario_verificado = verificar_horario(horario)

    if (horario_verificado == None):
        return
    

    try:
        valor = int(input('\nDigite o valor em reais da passagem:\n-> R$'))

    except ValueError:
        print('\nERRO: Digite um número inteiro!\n')
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

    criar_30_onibus(linha)

    print("\nLinha cadastrada com sucesso!\n")

#------------------------------------------------------------------------------------------------------------------------------------------------

def listar_linhas():#Função para listar as linha mostrando os indices para o usuário

    if not linhas:
        print("\nNenhuma linha cadastrada.\n")
        return
    
    for indice_linha, linha in enumerate(linhas):

        print(f"Índice {indice_linha} | {linha['origem']} -> {linha['destino']} | Horário: {linha['horario']} | Valor: R$ {linha['valor']}")
        
        
        if linha['onibus']:

            for indice_onibus, onibus in enumerate(linha['onibus']):

                print(f"    Ônibus {indice_onibus} - Data: {onibus['data'].strftime('%d/%m/%Y')} - Assentos ocupados: {np.sum(onibus['assentos'])}/20")
    

#------------------------------------------------------------------------------------------------------------------------------------------------

def remover_linha():#Função para remover uma linha

    listar_linhas()

    try:
        indice = int(input("\nDigite o índice da linha a remover:\n-> "))

    except ValueError:
        print("\nERRO: digite um número inteiro.\n")
        return
    

    if 0 <= indice < len(linhas):#Se o indice estiver for realmente de uma linha..

        linhas.pop(indice)
        print("\nLinha removida com sucesso.\n")

    else:
        print("\nERRO: Índice inválido.\n")

#------------------------------------------------------------------------------------------------------------------------------------------------

def editar_linha():

    listar_linhas()

    try:
        indice = int(input("\nDigite o índice da linha a editar:\n-> "))

    except ValueError:
        print("\nERRO: digite um número inteiro.\n")
        return
    

    if not (0 <= indice < len(linhas)):
        print("\nERRO: Índice inválido.\n")
        return
    

    linha_escolhida = linhas[indice]


    opcao = int(input(f'\nDigite uma das opções para editar:\n1- Origem atual [{linha_escolhida['origem']}]\n2- Destino atual [{linha_escolhida['destino']}]\n3- Horário atual [{linha_escolhida['horario']}]\n4- Valor atual [R$ {linha_escolhida['valor']}]\n0- Voltar\n-> '))

    match(opcao):

        case 1:

            novo_origem = str(input('\nDigite o novo nome para a cidade de origem:\n-> '))
            linha_escolhida['origem'] = novo_origem


        case 2:
            novo_destino = str(input('\nDigite o novo nome para a cidade de destino:\n-> '))
            linha_escolhida['destino'] = novo_destino


        case 3:

            try:

                novo_horario = str(input('\nDigite o novo horário para a linha:\n-> '))
                verificar_horario(novo_horario)
                linha_escolhida['horario'] = novo_horario

            except ValueError as e:#Verifica se o horário está no formato aceito
                print("\nERRO: Horário inválido — mantido o original.\n")


        case 4:
            try:
                novo_valor = str(input('\nDigite o novo valor para a linha:\n-> '))
                linha_escolhida['valor'] = int(novo_valor)
            except ValueError:
                print("\nERRO: Valor inválido — mantido o original.\n")

        case 0:
            print('\nVoltando ao menu...\n')
            pass
        
        case _:
            print('\nERRO: Opção inválida!\n')

#------------------------------------------------------------------------------------------------------------------------------------------------
def criar_30_onibus(linha):#Função que adiciona os 30 ônibus iniciais
    

    data_viagem = dt.date.today()  # data inicial

    for i in range(30):

        nova_data = data_viagem + dt.timedelta(days=i)  # soma i dias

        onibus = {"data": nova_data, "assentos": criar_matriz_assentos(), "vendas_onibus": []}#Dicionário do ônibus

        linha['onibus'].append(onibus)#Adiciona o novo ônibus no dicionário da linha
    
    print(f"\nOs 30 ônibus foram criados com sucesso para os próximos 30 dias\n")

#------------------------------------------------------------------------------------------------------------------------------------------------

def criar_onibus_para_linha():#Função que adiciona um ônibus a uma linha já existente
    
    listar_linhas()

    try:
        indice = int(input("\nDigite o índice da linha para adicionar um ônibus:\n-> "))
    except ValueError:
        print("\nERRO: Digite um número inteiro.\n")
        return
    

    if not (0 <= indice < len(linhas)):
        print("\nERRO: Digite um ínndice válido.\n")
        return
    

    data_str = input("\nDigite a data da viagem (dd/mm/aaaa):\n-> ")

    data_viagem = verificar_data(data_str)

    if (data_viagem == None):
        
        return
    

    if not dentro_de_30_dias(data_viagem):

        print("\nERRO:A data deve ser dentro dos próximos 30 dias (e não no passado).\n")#Nossos ônibus não tem capacitores de fluxo..
        return
    

    # cria ônibus com matriz vazia
    onibus = {"data": data_viagem, "assentos": criar_matriz_assentos(), "vendas_onibus": []}#Dicionário do ônibus

    linhas[indice]['onibus'].append(onibus)#Adiciona o novo ônibus no dicionário da linha
    
    print(f"\nÔnibus criado com sucesso para a data {data_viagem.strftime("%d/%m/%Y")}\n")

#------------------------------------------------------------------------------------------------------------------------------------------------

def escolher_linha_onibus():#Para o usário escolher uma linha e um ônibus da mesma


    cidade = input("\nDigite a cidade de destino para consulta:\n-> ")#Pede aonde o usuário quer ir

    candidatos = [(i, l) for i, l in enumerate(linhas) if l['destino'].lower() == cidade.lower()]#Lista as linhas que têm esse destino

    if not candidatos:#Se não houver linhas com esse destino não retorna nada
        print("\nERRO: Nenhuma linha encontrada para essa cidade.\n")
        return None, None
    

    
    print("\nLinhas encontradas:")#Printa as linhas e horários e o indice para que o usuário possa escolher

    for i, l in candidatos:
        print(f"{i} - {l['origem']} -> {l['destino']} | Horário: {l['horario']} | Valor: R$ {l['valor']}")

    try:
        indice_linha = int(input("\nEscolha o índice da linha (entre os listados):\n-> "))

    except ValueError:
        print("\nERRO: digite um número inteiro.\n")
        return None, None
    

    if not (0 <= indice_linha < len(linhas)) or (linhas[indice_linha]['destino'].lower() != cidade.lower()):#trata caso o indice não exista ou se a cidade de destino for diferente
        print("\nERRO: Índice inválido para a cidade informada.\n")
        return None, None
    

    
    linha_escolhida = linhas[indice_linha]# Agora o usuário escolhe data dentre ônibus disponíveis

    if not (linha_escolhida['onibus']):#Se a linha não tiver ônibus, irá retornar nada
        print("\nERRO: Essa linha não tem ônibus cadastrados .\n")
        return None, None
    

    print("\nÔnibus (índice) e datas disponíveis para essa linha:")#Mostra os ônibus e seus índices

    for i, o in enumerate(linha_escolhida['onibus']):
        print(f"{i} - Data: {o['data'].strftime('%d/%m/%Y')} - Assentos ocupados: {np.sum(o['assentos'])}/20")
    
    
    try:
        indice_onibus = int(input("\nEscolha o índice do ônibus:\n-> "))#Usuário digita qual ônibus ele quer

    except ValueError:
        print("\nERRO: digite um número inteiro.\n")
        return None, None
    

    if not (0 <= indice_onibus < len(linha_escolhida['onibus'])):#Se o índice não existir
        print("\nERRO: Índice de ônibus inválido.\n")
        return None, None
    

    return indice_linha, indice_onibus

#------------------------------------------------------------------------------------------------------------------------------------------------

def consultarHorarios():#Função para o usuário consultar os horários disponíveis para uma cidade

    cidade_escolhida = input("\nDigite o nome de uma cidade cadastrada (origem ou destino):\n-> ")
    horarios = []#Lista usada só para salvar os dados que serão exibidos

    for i in linhas:

        if (i['origem'].lower() == cidade_escolhida.lower()) or (i['destino'].lower() == cidade_escolhida.lower()):#verifica se o nome digitado está cadastrado
            horarios.append((i['origem'], i['destino'], i['horario']))

    if not horarios:#Se a lista ficar vazia....

        print("\nERRO: Nenhum horário encontrado para essa cidade.\n")

    else:#Senão printa os horários encontrados
        print(f"\nHorários encontrados para cidade {cidade_escolhida}:\n")

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

        print("\nERRO:Data fora do intervalo de 30 dias.\n")
        return
    
    
    imprime_matriz(onibus_escolhido['assentos'])# Imprime a matriz formatada


#------------------------------------------------------------------------------------------------------------------------------------------------

def preencher_onibus():#Permite o usário escolher um assento

    indice_linha, indice_onibus = escolher_linha_onibus()

    if (indice_linha is None) or (indice_onibus is None):#Se ele retornar None é porque algum erro aconteceu na função escolher_linha_onibus
        return
        

    linha_escolhida = linhas[indice_linha]
    onibus_escolhido = linha_escolhida['onibus'][indice_onibus]


    
    if not dentro_de_30_dias(onibus_escolhido['data']):#Verifica se a data corresponde para os 30 dias

        print("\nERRO: Não é possível reservar data para mais 30 dias.\n")
        return
    

    
    if onibus_ja_partiu(onibus_escolhido['data'], linha_escolhida['horario']):#Verifica se o ônibus já partiu

        print("\nERRO: Não é possível reservar: ônibus já partiu.\n")
        return
    


    imprime_matriz(onibus_escolhido['assentos'])#Imprime a matriz dos assentos do ônibus
    
    try:#Usuário pode digitar qual assento (1-20) quer reservar
        numero_assento = int(input("\nDigite o número do assento desejado (1-20):\n-> "))

    except ValueError:
        print("\nERRO: Digite um número inteiro.\n")
        return
    

    
    i, j = assento_numero_para_indices(numero_assento)#Tranforma o número em posição da matriz
    
    if (i == None) and (j == None):#Caso seja vazio é porque algo deu errado na função
        
        return
    

    if onibus_escolhido['assentos'][i, j] == 1:#VErifica se o assento já não foi reservado

        print("\nERRO: Assento já ocupado.\n")
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

    print(f"\nCompra realizada com sucesso! Valor: R$ {linha_escolhida['valor']:.2f} - Assento {numero_assento}\n")

#------------------------------------------------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------------------------------------------------------------
"""ARQUIVOS .TXT :"""
#------------------------------------------------------------------------------------------------------------------------------------------------

# ------------------------------
# Relatórios :
# ------------------------------


def _escrever_ou_imprimir(texto, destino, nome_arquivo):#Função para definir se o relatório será printado no terminal ou em um arquivo txt

    if destino == 'tela':
        print(texto)

    elif destino == 'arquivo':

        if not nome_arquivo:
            print("Erro: nome do arquivo não fornecido para gravação.")
            return
        
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            f.write(texto + '\n')
    else:
        print("Destino inválido. Use 'tela' ou 'arquivo'.")

#------------------------------------------------------------------------------------------------------------------------------

def relatorio_total_mes(destino, nome_arquivo): #Função que faz o relatorio do mes
    
    hoje = dt.date.today()
    mes = hoje.month
    ano = hoje.year

    linhas_text = []

    cabecalho = f"Relatório - Total arrecadado no mês: ({mes}/{ano}):"

    linhas_text.append(cabecalho)

    for indice, linha in enumerate(linhas):

        total = 0

        for i in linha.get('vendas', []):

            if (i['data_venda'].year == ano) and (i['data_venda'].month == mes):

                total += i['preco']

        linhas_text.append(f"Linha {indice}: {linha['origem']} -> {linha['destino']} | Total: R$ {total:.2f}")

    texto = '\n'.join(linhas_text) + '\n'

    _escrever_ou_imprimir(texto, destino, nome_arquivo)#Chama a função de printar no terminal ou no arquivo

    return texto

#-------------------------------------------------------------------------------------------------------------------------------

def relatorio_media_dia(destino, nome_arquivo):


    """
    Gera relatório de ocupação percentual média por linha por dia da semana.
    Produz uma 'matriz' textual onde cada linha corresponde a uma linha de ônibus,
    e as 7 colunas correspondem a segunda..domingo (0..6).
    """


    cabecalho = "Relatório - Ocupação percentual média por linha por dia da semana (Seg..Dom):"
    linhas_text = [cabecalho]
    
    for indice, linha in enumerate(linhas):

        # listas por dia
        dias = [[] for _ in range(7)]


        for bus in linha.get('onibus', []):

            weekday = bus['data'].weekday()  # segunda=0 .. domingo=6
            ocup = (np.sum(bus['assentos']) / 20) * 100
            dias[weekday].append(ocup)


        # calc médias
        medias = []

        for lst in dias:

            medias.append((sum(lst) / len(lst)) if lst else 0.0)


        # montar linha textual formatada (7 colunas)
        medias_fmt = " | ".join(f"{m:5.1f}%" for m in medias)
        linhas_text.append(f"Linha {indice}: {linha['origem']} -> {linha['destino']}  ||  {medias_fmt}")

    texto = '\n'.join(linhas_text) + '\n'
    _escrever_ou_imprimir(texto, destino, nome_arquivo)
    return texto

#------------------------------------------------------------------------------------------------------------------------------------

def gerarRelatorios():


    """
    Menu de relatórios: pergunta qual relatório e se será exibido na tela ou gravado em arquivo.
    """


    print("\nRelatórios disponíveis:")
    print("1 - Total arrecadado no mês corrente por linha;")
    print("2 - Ocupação percentual média por linha por dia da semana;")
    print('3 - Arquivo com as reservas;')
    
    try:
        opcao = int(input("Escolha uma das opções:\n-> "))

    except ValueError:
        print("ERRO: digite um inteiro.")
        return

    if (opcao != 3):

        # escolher onde será printado
        print("\nDeseja imprimir na tela ou gravar em arquivo?")
        print("1 - Tela")
        print("2 - Arquivo (append)")
        
        try:
            opcao_print = int(input("Escolha uma das opções:\n-> "))

        except ValueError:
            print("ERRO: digite um inteiro.")
            return


        match(opcao_print):

            case 1:
                destino = 'tela'

            case 2:
                destino = 'arquivo'

            case _:
                print('\nOpção inválida!\n')
                return

        nome_arquivo = None

        if destino == 'arquivo':

            nome_arquivo = input("Digite o nome do arquivo para gravar (ex: relatorio.txt):\n-> ").strip()

            # cabeçalho no arquivo
            with open(nome_arquivo, 'a', encoding='utf-8') as f:
                f.write(f"--- Relatório gerado em {dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ---\n")


    match(opcao):
        case 1:
            relatorio_total_mes(destino=destino, nome_arquivo=nome_arquivo)
        case 2:
            relatorio_media_dia(destino=destino, nome_arquivo=nome_arquivo)
        
        case 3:
            gerar_arquivo_reservas("reservas_geradas.txt")
        case _:
            print("Opção inválida.")

# ------------------------------
# Processamento de arquivo de reservas (com gravação de falhas)
# ------------------------------

def gerar_arquivo_reservas(nome_arquivo):#Cria um arquivo txt com as reservas, para que possa ser lido depois
    """
    Gera um arquivo contendo TODAS AS RESERVAS já realizadas no sistema,
    no formato aceito por processar_arquivo_reservas():

        CIDADE, HORARIO, DATA, ASSENTO
    """

    linhas_txt = []

    for linha in linhas:

        destino = linha["destino"]
        horario = linha["horario"]

        # percorre todos os ônibus da linha
        for bus in linha["onibus"]:

            # percorre todas as vendas deste ônibus
            for venda in bus.get("vendas_onibus", []):
                
                data_str = venda["data_viagem"].strftime("%d/%m/%Y")
                assento = venda["assento"]

                # monta a linha no formato correto
                linha_formatada = f"{destino}, {horario}, {data_str}, {assento}"

                linhas_txt.append(linha_formatada)

    # grava no arquivo
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        for linha_info in linhas_txt:
            f.write(linha_info + "\n")

    print(f"\nArquivo '{nome_arquivo}' criado com sucesso com {len(linhas_txt)} reserva(s)!\n")



#--------------------------------------------------------------------------------------------------------------------
def processar_arquivo_reservas():#Ler arquivo das reservas txt


    """
    Lê arquivo com linhas:
    CIDADE, HORARIO(hh:mm), DATA(dd/mm/aaaa), ASSENTO
    Tenta aplicar cada reserva. Se falhar, registra a linha no arquivo ARQUIVO_RESERVAS_FALHAS com o motivo.
    """


    falhas = []

    try:
        with open("reservas_geradas.txt", 'r', encoding='utf-8') as f:
            linhas_arquivo = [ln.strip() for ln in f if ln.strip()]

    except FileNotFoundError:
        
        gerar_arquivo_reservas("reservas_geradas.txt")
        return

    for linha_txt in linhas_arquivo:

        partes = [p.strip() for p in linha_txt.split(',')]

        if len(partes) != 4:

            falhas.append((linha_txt, "Formato inválido (esperado 4 campos)"))
            continue

        cidade, horario_str, data_str, assento_str = partes

        # encontrar linhas com destino igual à cidade e horário igual
        candidatos = [(li, l) for li, l in enumerate(linhas)
                      
                      if l['destino'].lower() == cidade.lower() and l['horario'] == horario_str]
        
        if not candidatos:
            falhas.append((linha_txt, "Linha inexistente (cidade/horário não correspondem)"))
            continue

        # verifica data
        try:
            data_viagem = verificar_data(data_str)

        except ValueError:
            falhas.append((linha_txt, "Data inválida"))
            continue

        # pega primeira linha candidata (poderia haver múltiplas; ajuste se quiser lógica diferente)
        li, l = candidatos[0]

        # procura ônibus com essa data
        idx_onibus = None
        for bi, b in enumerate(l.get('onibus', [])):
            if b['data'] == data_viagem:
                idx_onibus = bi
                break
        if idx_onibus is None:
            falhas.append((linha_txt, "Ônibus nessa data não encontrado"))
            continue

        # valida assento
        try:
            num_assento = int(assento_str)
        except ValueError:
            falhas.append((linha_txt, "Assento inválido (não é inteiro)"))
            continue
        try:
            i, j = assento_numero_para_indices(num_assento)
        except ValueError:
            falhas.append((linha_txt, "Assento fora do intervalo 1-20"))
            continue

        b = l['onibus'][idx_onibus]

        # valida intervalo 30 dias
        if not dentro_de_30_dias(b['data']):
            falhas.append((linha_txt, "Data fora do intervalo de 30 dias"))
            continue


        # valida se já partiu
        if onibus_ja_partiu(b['data'], l['horario']):
            falhas.append((linha_txt, "Ônibus já partiu"))
            continue


        # valida assento ocupado
        if b['assentos'][i, j] == 1:
            falhas.append((linha_txt, "Assento ocupado"))
            continue

        # tudo OK -> reservar
        b['assentos'][i, j] = 1
        venda = {
            "data_venda": dt.datetime.now(),
            "preco": l['valor'],
            "data_viagem": b['data'],
            "assento": num_assento,
            "linha_origem": l['origem'],
            "linha_destino": l['destino']
        }
        l.setdefault('vendas', []).append(venda)
        b.setdefault('vendas_onibus', []).append(venda)

    # gravar falhas em arquivo padrão
    if falhas:
        with open(ARQUIVO_RESERVAS_FALHAS, 'a', encoding='utf-8') as f:
            f.write(f"--- Processamento em {dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Arquivo: 'reservas_geradas.txt' ---\n")
            for txt, motivo in falhas:
                f.write(f"{txt} -> Motivo: {motivo}\n")
            f.write("\n")
        print(f"{len(falhas)} reserva(s) NÃO puderam ser realizadas. Detalhes gravados em {ARQUIVO_RESERVAS_FALHAS}")
    else:
        print("Todas as reservas do arquivo foram processadas com sucesso.")


#------------------------------------------------------------------------------------------------------------------------------------------------

"""MENU PRINCIPAL:"""

print('\nSeja bem vindo ao sistema de controle de rodoviária!\nCriado por: Gabriel e Rafael Alves Faria\n')

sair = 0

while sair == 0:
    try:
        print("\nSistema da Rodoviária:")
        print("1 - Cadastrar ou editar linhas;")
        print("2 - Consultar horários disponíveis para uma cidade;")
        print("3 - Consultar os assentos disponíveis no ônibus;")
        print("4 - Marcar (reservar) um assento de um ônibus;")
        print("5 - Criar outro ônibus para uma linha já existente;")
        print("6 - Ler ou gerar arquivos de reservas;")
        print("7 - Gerar relatórios;")
        print("0 - Sair.")
        opcao = int(input("\nOpção:\n-> "))


        match (opcao):
            
            case 1:#Criar, remover ou editar uma linha

                print("\nDigite uma das opções abaixo:\n1 - Criar linha\n2 - Remover linha\n3 - Editar linha\n0 - voltar")
                
                try:
                    opcao_linha = int(input("\nOpção:\n-> "))
                
                except ValueError:
                    print("\nErro: digite um inteiro.\n")
                    continue

                match opcao_linha:

                    case 1:#Cria uma linha
                        cadastroLinhas()

                    case 2:#Remove uma linha
                        remover_linha()
                    
                    case 3:#Edita linha
                        editar_linha()

                    case 0:
                        pass

                    case _:#Default
                        print("\nErro: Opção inválida.\n")
            
            
            case 2:#Consulta os horários disponíveis 
                consultarHorarios()
            
            case 3:#Consulta os assentos disponíveis em um ônibus
                consultarAssentos()
            
            case 4:#Reserva um assento em um ônibus
                preencher_onibus()
            
            case 5:#Cria um ônibus para uma linha já existente
                criar_onibus_para_linha()
            
            case 6:#Le um arquivo txt com as reservas ou cria um se ele não existir
                processar_arquivo_reservas()
            
            case 7:
                gerarRelatorios()

            case 0:#Para finalizar o programa
                print("\nFinalizando o programa...\n")
                sair = 1
                break

            case _:#Default
                print("\nErro: Opção inválida.\n")


    except ValueError:#Tratar erro
        print("\nErro: opção inválida. Digite um número inteiro.\n")

