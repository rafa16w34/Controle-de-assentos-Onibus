import datetime as dt
from pathlib import Path

# Dados principais
linhas = []  # cada item: {'origem':str, 'destino':str, 'horarios':[hh:mm,...], 'valor':float, 'onibus': { 'YYYY-MM-DD': [0/1 x20] } }

vendas = []  # lista de dicts: {'linha_idx':int, 'data': date, 'valor': float}
viagens = [] # lista de dicts: {'linha_idx':int, 'data': date, 'embarcados':int, 'capacidade':20}
falhas_arquivo = Path("reservas_falhas.txt")

# utilitários
def hoje():
    return dt.date.today()

def parse_hora(texto):
    try:
        h, m = texto.strip().split(":")
        h, m = int(h), int(m)
        if 0 <= h <= 23 and 0 <= m <= 59:
            return f"{h:02d}:{m:02d}"
    except Exception:
        pass
    return None

def parse_data_ddmmaaaa(texto):
    try:
        d = dt.datetime.strptime(texto.strip(), "%d/%m/%Y").date()
        return d
    except Exception:
        return None

def within_30_days(date_obj):
    delta = (date_obj - hoje()).days
    return 0 <= delta <= 30

def bus_exists_for_line_on_date(linha_idx, date_obj):
    key = date_obj.isoformat()
    return key in linhas[linha_idx]['onibus']

def create_bus_for_line_date(linha_idx, date_obj):
    key = date_obj.isoformat()
    if key not in linhas[linha_idx]['onibus']:
        linhas[linha_idx]['onibus'][key] = [0] * 20  # 20 assentos, 0 livre, 1 ocupado
    return linhas[linha_idx]['onibus'][key]

def imprimir_mapa_assentos(assentos):
    # exibe assentos 1..20, marcando L ou X, e indicando janelas (ímpares)
    linha_formatada = ""
    for i in range(20):
        status = "L" if assentos[i] == 0 else "X"
        num = i + 1
        janela = "(J)" if num % 2 == 1 else "   "
        linha_formatada += f"{num:02d}:{status}{janela}  "
        if (i + 1) % 5 == 0:
            linha_formatada += "\n"
    print(linha_formatada)

# CRUD linhas
def cadastroLinhas():
    origem = input("Cidade de origem: ").strip()
    destino = input("Cidade de destino: ").strip()
    horarios_texto = input("Horários de partida (separe por vírgula, ex: 07:30,13:00): ").strip()
    horarios = []
    for h in horarios_texto.split(","):
        hh = parse_hora(h)
        if hh:
            horarios.append(hh)
        else:
            print(f"Atenção: horário inválido ignorado -> {h.strip()}")
    if not horarios:
        print("É necessário informar pelo menos um horário válido.")
        return
    try:
        valor = float(input("Valor da passagem (R$): ").strip())
    except Exception:
        print("Valor inválido.")
        return
    linha = {
        'origem': origem,
        'destino': destino,
        'horarios': horarios,
        'valor': float(valor),
        'onibus': {}  # mapeia data iso -> lista de 20 assentos
    }
    linhas.append(linha)
    print("Linha cadastrada com sucesso.")

def listar_linhas_com_indices():
    if not linhas:
        print("Nenhuma linha cadastrada.")
        return
    for i, l in enumerate(linhas):
        print(f"{i} - {l['origem']} -> {l['destino']} | Horários: {', '.join(l['horarios'])} | R$ {l['valor']:.2f}")

def edit_linhas():
    if not linhas:
        print("Nenhuma linha cadastrada.")
        return
    listar_linhas_com_indices()
    try:
        idx = int(input("Escolha o índice da linha a editar: "))
    except Exception:
        print("Índice inválido.")
        return
    if idx < 0 or idx >= len(linhas):
        print("Índice fora do intervalo.")
        return
    l = linhas[idx]
    novo_origem = input(f"Origem (enter mantém '{l['origem']}'): ").strip()
    novo_destino = input(f"Destino (enter mantém '{l['destino']}'): ").strip()
    novos_hor = input(f"Horários (enter mantém '{', '.join(l['horarios'])}'). Para mudar, forneça separados por vírgula: ").strip()
    novo_valor = input(f"Valor (enter mantém R$ {l['valor']:.2f}): ").strip()
    if novo_origem:
        l['origem'] = novo_origem
    if novo_destino:
        l['destino'] = novo_destino
    if novos_hor:
        horarios_n = []
        for h in novos_hor.split(","):
            hh = parse_hora(h)
            if hh:
                horarios_n.append(hh)
            else:
                print(f"Horário inválido ignorado -> {h.strip()}")
        if horarios_n:
            l['horarios'] = horarios_n
    if novo_valor:
        try:
            l['valor'] = float(novo_valor)
        except Exception:
            print("Valor inválido, mantido o anterior.")
    print("Linha atualizada.")

def del_linhas():
    if not linhas:
        print("Nenhuma linha cadastrada.")
        return
    listar_linhas_com_indices()
    try:
        idx = int(input("Escolha o índice da linha a remover: "))
    except Exception:
        print("Índice inválido.")
        return
    if idx < 0 or idx >= len(linhas):
        print("Índice fora do intervalo.")
        return
    conf = input("Digite 'S' para confirmar exclusão: ").strip().upper()
    if conf == 'S':
        linhas.pop(idx)
        print("Linha removida.")
    else:
        print("Operação cancelada.")

def encontrar_viagem(linha_idx, data, horario):
    for v in viagens:
        if (
            v["linha_idx"] == linha_idx and
            v["data"] == data and
            v["horario"] == horario
        ):
            return v
    return None


# Consultas
def consultarHorarios():
    cidade = input("Digite a cidade de origem para ver horários: ").strip()
    encontrados = []
    for i, l in enumerate(linhas):
        if l['origem'].lower() == cidade.lower():
            encontrados.append((i, l))
    if not encontrados:
        print("Nenhuma linha encontrada para essa cidade de origem.")
        return
    for idx, l in encontrados:
        print(f"Linha {idx}: {l['origem']} -> {l['destino']} | Horários: {', '.join(l['horarios'])} | R$ {l['valor']:.2f}")

def escolher_linha_por_dest_horario_data():
    destino = input("Digite a cidade de destino: ").strip()
    horario = input("Digite o horário (hh:mm): ").strip()
    horario = parse_hora(horario)
    if not horario:
        print("Horário inválido.")
        return None, None, None
    data_str = input("Digite a data da partida (dd/mm/aaaa): ").strip()
    data_obj = parse_data_ddmmaaaa(data_str)
    if not data_obj:
        print("Data inválida.")
        return None, None, None
    if not within_30_days(data_obj):
        print("A data deve ser dentro dos próximos 30 dias a partir de hoje.")
        return None, None, None
    # procurar linhas que tenham esse destino e horário
    candidatos = []
    for i, l in enumerate(linhas):
        if (l['destino'].lower() == destino.lower()) and (horario in l['horarios']):
            candidatos.append((i, l))
    if not candidatos:
        print("Nenhuma linha encontrada com esse destino e horário.")
        return None, None, None
    # se mais de uma linha, listar e pedir escolha
    if len(candidatos) > 1:
        print("Foram encontradas várias linhas. Escolha o índice:")
        for idx, l in candidatos:
            print(f"{idx} - {l['origem']} -> {l['destino']} | Valor R$ {l['valor']:.2f}")
        try:
            escolha = int(input("Digite o índice da linha desejada: "))
        except Exception:
            print("Índice inválido.")
            return None, None, None
        if not any(escolha == idx for idx, _ in candidatos):
            print("Escolha inválida.")
            return None, None, None
        linha_idx = escolha
    else:
        linha_idx = candidatos[0][0]
    return linha_idx, horario, data_obj

def consultarAssentos():
    linha_idx, horario, data_obj = escolher_linha_por_dest_horario_data()
    if linha_idx is None:
        return
    # verificar se ônibus já partiu (se data == hoje e horário < agora)
    now = dt.datetime.now()
    partida_datetime = dt.datetime.combine(data_obj, dt.time(int(horario[:2]), int(horario[3:])))
    if partida_datetime < now:
        print("Ônibus já partiu. Não é possível vender passagem para essa partida.")
        return

    assentos = create_bus_for_line_date(linha_idx, data_obj)
    print("\nMapa de assentos (L = Livre, X = Ocupado) [ímpares = janela]:\n")
    imprimir_mapa_assentos(assentos)

    # perguntar se deseja reservar
    if sum(assentos) < len(assentos):
        resp = input("Deseja reservar algum assento agora? (S/N): ").strip().upper()
        if resp == 'S':
            marcar_assento_em_onibus(linha_idx, data_obj, horario)
    else:
        print("Ônibus lotado.")

def marcar_assento_em_onibus(linha_idx, data_obj, horario_str=None):
    # Se horario_str não for fornecido, pedir
    if horario_str is None:
        entrada = input("Digite o horário (hh:mm) da viagem: ").strip()
        horario_str = parse_hora(entrada)
        if not horario_str:
            print("Horário inválido.")
            return

    # Parse de horas e minutos
    hora = int(horario_str[:2])
    minuto = int(horario_str[3:])

    # Criar/obter assentos do ônibus
    assentos = create_bus_for_line_date(linha_idx, data_obj)

    # Número do assento
    try:
        num = int(input("Digite o número do assento desejado (1-20): "))
    except:
        print("Número inválido.")
        return

    if not (1 <= num <= 20):
        print("Assento inválido.")
        return

    idx = num - 1

    # Verificar se a viagem já partiu
    partida_datetime = dt.datetime.combine(data_obj, dt.time(hora, minuto))
    if partida_datetime < dt.datetime.now():
        print("Não é possível reservar: ônibus já partiu.")
        return

    # Verificar se assento está ocupado
    if assentos[idx] == 1:
        print("Assento já ocupado.")
        return

    # Marca assento
    assentos[idx] = 1

    # Registrar venda simples
    valor = linhas[linha_idx]['valor']
    vendas.append({
        'linha_idx': linha_idx,
        'data': data_obj,
        'valor': valor
    })

    # ➤ CORREÇÃO: evitar duplicação de viagens
    viagem = encontrar_viagem(linha_idx, data_obj, horario_str)

    if viagem is None:
        viagem = {
            "linha_idx": linha_idx,
            "data": data_obj,
            "horario": horario_str,
            "vendidos": 0,
            "valor_unitario": valor
        }
        viagens.append(viagem)

    # Atualiza ocupação real
    viagem["vendidos"] += 1

    print(f"Reserva realizada: Linha {linha_idx}, Data {data_obj.strftime('%d/%m/%Y')}, "
          f"Horário {horario_str}, Assento {num} | Valor R$ {valor:.2f}")

# função para criar ônibus manualmente (opção 5)
def criar_outro_onibus():
    listar_linhas_com_indices()
    try:
        idx = int(input("Escolha o índice da linha para criar ônibus em uma data: "))
    except Exception:
        print("Índice inválido.")
        return
    if idx < 0 or idx >= len(linhas):
        print("Índice fora do intervalo.")
        return
    data_str = input("Data da partida (dd/mm/aaaa): ").strip()
    data_obj = parse_data_ddmmaaaa(data_str)
    if not data_obj:
        print("Data inválida.")
        return
    if not within_30_days(data_obj):
        print("A data deve estar dentro dos próximos 30 dias.")
        return
    create_bus_for_line_date(idx, data_obj)
    print("Ônibus criado para a data informada.")

# Relatórios
def total_arrecadado_linha():
    mes_atual = hoje().month
    ano_atual = hoje().year
    totais = {}
    for v in vendas:
        data = v['data']
        if isinstance(data, dt.date):
            d = data
        else:
            # se houver strings, tentar parse
            d = dt.date.fromisoformat(str(data))
        if d.month == mes_atual and d.year == ano_atual:
            idx = v['linha_idx']
            totais[idx] = totais.get(idx, 0.0) + float(v['valor'])
    return totais

def ocupacao_media():
    # estrutura temporária: {linha_idx: {weekday: [ocupações%...]}}
    temp = {}
    for reg in viagens:
        d = reg['data'] if isinstance(reg['data'], dt.date) else dt.date.fromisoformat(str(reg['data']))
        weekday = d.weekday() # 0..6
        idx = reg['linha_idx']
        ocup = (reg['embarcados'] / reg['capacidade']) * 100
        if idx not in temp:
            temp[idx] = {i: [] for i in range(7)}
        temp[idx][weekday].append(ocup)
    resultado = {}
    for idx, dias in temp.items():
        resultado[idx] = {}
        for wd in range(7):
            lista = dias.get(wd, [])
            resultado[idx][wd] = round(sum(lista) / len(lista), 2) if lista else 0.0
    return resultado

def gerarRelatorios_em_tela():
    print("===== RELATÓRIO =====")
    totais = total_arrecadado_linha()
    print("\n1) Total arrecadado por linha no mês atual:")
    if not totais:
        print("  Nenhuma venda no mês corrente.")
    else:
        for idx, val in totais.items():
            print(f"  Linha {idx}: {linhas[idx]['origem']} -> {linhas[idx]['destino']} | R$ {val:.2f}")
    print("\n2) Ocupação média (%) por dia da semana:")
    ocup = ocupacao_media()
    dias = ["Seg","Ter","Qua","Qui","Sex","Sáb","Dom"]
    if not ocup:
        print("  Nenhuma viagem registrada.")
    else:
        for idx, dados in ocup.items():
            print(f"\nLinha {idx}: {linhas[idx]['origem']} -> {linhas[idx]['destino']}")
            for d in range(7):
                print(f"  {dias[d]}: {dados.get(d,0.0):.2f}%")

def gerarRelatorios_em_arquivo():
    totais = total_arrecadado_linha()
    ocup = ocupacao_media()
    texto = "===== RELATÓRIO =====\n\n1) Total arrecadado por linha no mês atual:\n"
    if not totais:
        texto += "  Nenhuma venda no mês corrente.\n"
    else:
        for idx, val in totais.items():
            texto += f"  Linha {idx}: {linhas[idx]['origem']} -> {linhas[idx]['destino']} | R$ {val:.2f}\n"
    texto += "\n2) Ocupação média (%) por dia da semana:\n"
    dias = ["Seg","Ter","Qua","Qui","Sex","Sáb","Dom"]
    if not ocup:
        texto += "  Nenhuma viagem registrada.\n"
    else:
        for idx, dados in ocup.items():
            texto += f"\nLinha {idx}: {linhas[idx]['origem']} -> {linhas[idx]['destino']}\n"
            for d in range(7):
                texto += f"  {dias[d]}: {dados.get(d,0.0):.2f}%\n"
    Path("Relatorio.txt").write_text(texto, encoding="utf-8")
    print("Relatório salvo em Relatorio.txt")

# Ler reservas de arquivo
# Formato: CIDADE, HORÁRIO(hh:mm), DATA(dd/mm/aaaa), ASSENTO
# ASSENTO pode ser "N" (número 1..20) ou formato "N" (1..20). Uma reserva por linha.
def ler_reservas_arquivo(nome):
    falhas = []
    caminho = Path(nome)
    if not caminho.exists():
        print("Arquivo não encontrado.")
        return
    with caminho.open("r", encoding="utf-8") as f:
        for linha in f:
            linha_original = linha.rstrip("\n")
            parts = linha.strip().split(",")
            if len(parts) != 4:
                falhas.append((linha_original, "Formato inválido"))
                continue
            cidade, horario, data_str, assento_str = [p.strip() for p in parts]
            hora = parse_hora(horario)
            data_obj = parse_data_ddmmaaaa(data_str)
            if not hora or not data_obj:
                falhas.append((linha_original, "Data ou horário inválido"))
                continue
            if not within_30_days(data_obj):
                falhas.append((linha_original, "Data fora do período de 30 dias"))
                continue
            # encontrar linha que tenha destino igual à cidade e esse horário (assumimos que 'CIDADE' no arquivo é destino)
            linha_encontrada = None
            for i, l in enumerate(linhas):
                if l['destino'].lower() == cidade.lower() and hora in l['horarios']:
                    linha_encontrada = i
                    break
            if linha_encontrada is None:
                falhas.append((linha_original, "Linha não encontrada para cidade/horário"))
                continue
            # verificar horário já passado
            partida_dt = dt.datetime.combine(data_obj, dt.time(int(hora[:2]), int(hora[3:])))
            if partida_dt < dt.datetime.now():
                falhas.append((linha_original, "Ônibus já partiu"))
                continue
            # parse do assento
            try:
                num_assento = int(assento_str)
            except Exception:
                falhas.append((linha_original, "Assento inválido"))
                continue
            if not (1 <= num_assento <= 20):
                falhas.append((linha_original, "Assento fora do intervalo 1-20"))
                continue
            # criar ônibus se necessário e tentar reservar
            assentos = create_bus_for_line_date(linha_encontrada, data_obj)
            idx = num_assento - 1
            if assentos[idx] == 1:
                falhas.append((linha_original, "Assento ocupado"))
                continue
            # tudo ok: reservar
            assentos[idx] = 1
            valor = linhas[linha_encontrada]['valor']
            vendas.append({'linha_idx': linha_encontrada, 'data': data_obj, 'valor': valor})
            embarcados = sum(assentos)
            viagens.append({'linha_idx': linha_encontrada, 'data': data_obj, 'embarcados': embarcados, 'capacidade': 20})
    # gravar falhas
    if falhas:
        with falhas_arquivo.open("a", encoding="utf-8") as out:
            for linha, motivo in falhas:
                out.write(f"{linha} -> {motivo}\n")
        print(f"{len(falhas)} reserva(s) falharam. Detalhes gravados em {falhas_arquivo}")
    else:
        print("Todas as reservas do arquivo processadas com sucesso.")

# Menu principal

sair = 0 #Varíavel que controla o loop do while do menu

while sair == 0 :

    try:
        print("\nSistema da Rodoviária:")
        print("1 - Cadastrar ou editar linhas;")
        print("2 - Consultar horários por cidade de origem")
        print("3 - Consultar assentos (destino, horário, data)")
        print("4 - Marcar assento (direto)")
        print("5 - Criar outro ônibus para uma linha em data")
        print("6 - Ler reservas de arquivo")
        print("7 - Gerar relatório")
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
                            del_linhas()

                        case 3:
                            edit_linhas()

                        case _:
                            print('\nErro: Digite um dos valores exibidos no menu!\n')

                except(ValueError):
                    print('\nErro: Digite um número inteiro!\n')
            
            case 2:

                if linhas:

                    #Consultar horários disponíveis para uma cidade
                    consultarHorarios()

                else:
                    print('\nErro: Nenhuma linha foi criada para que se possa verificar!\n')
                
            case 3:

                if linhas:

                    consultarAssentos()

                else:
                    print('\nErro: Nenhuma linha foi criada para que se possa verificar!\n')
                    
                
            case 4:
                listar_linhas_com_indices()
                try:
                    idx = int(input("Escolha índice da linha: "))
                except:
                    print("Índice inválido.")
                    continue
                if idx < 0 or idx >= len(linhas):
                    print("Índice fora do intervalo.")
                    continue

                data_str = input("Data da partida (dd/mm/aaaa): ").strip()
                data_obj = parse_data_ddmmaaaa(data_str)
                if not data_obj or not within_30_days(data_obj):
                    print("Data inválida ou fora do período de 30 dias.")
                    continue

                horario = parse_hora(input("Horário (hh:mm): "))
                if not horario:
                    print("Horário inválido.")
                    continue

                marcar_assento_em_onibus(idx, data_obj, horario)


            case 5:#Cria outro ônibus para uma linha já existente

                if (linhas['Ônibus']):

                    criar_outro_onibus()

                else:
                    print('\nErro: Nenhuma linha foi criada para que se possa verificar!\n')
            
            case 6:
                nome = input("Nome do arquivo de reservas: ").strip()
                ler_reservas_arquivo(nome)

            case 7:
                print("\n1 - Mostrar relatório na tela")
                print("2 - Salvar relatório em arquivo")
                escolha = input("Escolha: ").strip()
                if escolha == "1":
                    gerarRelatorios_em_tela()
                elif escolha == "2":
                    gerarRelatorios_em_arquivo()
                else:
                    print("Opção inválida")
                
            case 0:

                sair = 1
                print('\nFinalizando programa...\n')
            
            case _:
                print("\nErro: Digite uma das opções exibidas no menu!\n")
        
    except (ValueError):
        print("=====" * 10)
        print("\nErro: Opção inválida, digite um número inteiro!\n")
        print("=====" * 10)
