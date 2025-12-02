# Trabalho 2 de Programação Python: Controle de assentos de Ônibus

# Autores: 
* Rafael Alves Faria
* Gabriel Alves Faria
# Orientador: 
* Guido

# 1) Sobre o Projeto:
  O projeto aqui apresentado é uma simulação de um sistema de uma empresa de um todoviária de ônibus, onde o usuário pode:
  * Definir a linha de percusso do ônibus, ou seja, sua origem e destino;
  * Seu horário de partida;
  * O preço da passagem por assento;
  * O assento que vai ocupar, de um a vinte sendo os lugares com janelas os números impares;
  * Gerar dos relatórios na tela do prompt ou em arquivo de texto, contendo o total arrecadado com venda de passagens no mês corrente para cada linha e a ocupação percentual média de cada linha em cada dia da semana, em forma de matriz;
  * Receber e gravar em um arquivo texto todas as reservas que não puderam ser realizadas, juntamente com o motivo (ex.: ônibus cheio, ônibus já partiu, assento ocupado).

# 2) Como Iniciar/Terminar o Projeto:
O projeto inicializa com o usuário escolhendo a opção de criar uma linha de ônibus na opção um do menu principal e no menu da mesma, onde é possivel editar ou apagar a linha já existente. O projeto se finaliza quando o usuário escolher a opção zero, que ira encerrar no prompt.

# 3) Opções Oferecidas:
* 1 - Cadastrar, editar ou excluir linhas;
Permite criar novas linhas de ônibus informando cidade de origem, cidade de destino, horário da viagem e valor da passagem após cadastrada, além de também ser possível editar esses dados.
* 2 - Consultar horários disponíveis para uma cidade
O usuário informa uma cidade, e o sistema lista todas as linhas que partem ou chegam nela, exibindo horários e preços.
* 3 - Consultar os assentos disponíveis no ônibus:
Exibe o mapa de assentos do ônibus (5 x 4), marcando: "L" para assento livre e "X" para ocupado. O usuário escolhe a linha e o ônibus desejado.
* 4 - Marcar (reservar) um assento de um ônibus:
Permite reservar um assento informando a linha, a data / horário e o número do assento (1 a 20). O sistema verifica disponibilidade e registra a reserva.
* 5 - Criar outro ônibus (adicionar data) para uma linha já existente. Caso uma linha precise operar em mais de uma data, o sistema permite criar um novo ônibus associando: data da viagem, nova matriz de assentos vazia e armazenamento de reservas futuras
* 6 - Ler reservas de arquivo (formato especificado). Permite carregar um arquivo texto contendo várias reservas.
O sistema:
tenta realizar cada reserva;
rejeita reservas inválidas;
salva em outro arquivo os erros e motivos (por exemplo: assento ocupado, linha inexistente, data inválida, etc.).
* 7 - Gerar relatórios: Gera relatórios como:
total arrecadado por linha;
ocupação média (%) dos ônibus;
quantidade de assentos ocupados por viagem.
* 8 - Listar todas as linhas e ônibus cadastrados: Mostra um resumo com todas as linhas existentes e suas datas de operação, cada uma com seus respectivos ônibus cadastrados.
* 0 - Sair: Encerra o programa.

# 4) Principais Telas:
O projeto apresenta uma tela primitiva no prompt personalizada pelos strings do python.
* Menu inicial;
* Menu da opção um de criar, editar e deletar;
* Definir onibus;
* Escolher assento;
* Consultar assentos disponiveis ou ocupados ou reservados;
* Gerar relatório no prompt ou em um arquivo .txt;
* Mostrar arquivo de reseva de assentos;

# 5) REQUISITOS:
* Python 3.8+;
* Instalar numpy;

# 6) Conclusão:
Esse trabalho acrescentou muito para os autores do projeto a aplicar na prática tudo o que aprenderam ao longo do semestre, pois foi necessario usar funções, listas, dicionários e gerenciamento de arquivos em python, além de entender como uma preparação para diversos projetos de softwares futuros ou aprimorar este projeto para criar interface gráfica como o Kivy, criar API em Flask/FastAPI ou Adicionar JSON ou um banco de dados real.   
