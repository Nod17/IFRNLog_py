# IFRNLog_py
Analisar registros (logs) de auditoria de servidores e serviços de rede é uma atividade inerente ao profissional que atua na operação de serviços de TI.
Essa análise, na maioria das vezes, é impossível de ser realizada com qualidade sem o auxílio de ferramentas (programas) feitos sob medida para filtrar
e identificar anormalidades. É nesse contexto que o projeto LOG-PY se aplica, pois consiste em desenvolver uma ferramenta para LER, PROCESSAR e MOSTRAR
informações relativas aos acessos realizados à servidores WEB.   O projeto pode ser desenvolvido individualmente ou em equipe com dois integrantes.
Independente da formação da equipe, todos os alunos devem enviar a atividade.

O escopo da FASE 1:
Leitura e preparação dos dados:
O objetivo dessa etapa é realizar a leitura do arquivo de log (local ou remoto) no padrão APACHE, identificar o padrão e salvar em um outro arquivo em
melhor formato para análise/processamento

ENTRADA: Arquivo de log bruto
SAÍDA: Arquivo .CSV com todos os campos organizados

Exemplo de saída (arquivo.csv):

Host,Os,Method,Access,Code,Bytes
83.149.9.216,Mac,GET,Manhã,200,203023
100.149.9.216,Windows,GET,Manhã,200,171717
81.149.10.216,Linux,POST,Tarde,200,26185
19.149.9.26,Outro,OPTIONS,Noite,200,7697

Requisitos de codificação:
a) Modularização de código (funções)
b) Tratamento de exceções

O escopo da FASE 2:

Processamento e apresentação dos dados:
O objetivo dessa etapa é realizar o processamento do arquivo do pré-processado (Arquivo .CSV) e apresentar os dados para avaliação do analista de redes:

ENTRADA: Arquivo .CSV
SAÍDA: Estatísticas conforme listado abaixo


Estatísticas: a) Quantidade de solicitações por método de acesso (GET, POST, PUT, DELETE)
b) Quantidade de solicitações com sucesso (HTTP 200 e 301) e com erro (Demais códigos HTTP)
c) TOP 10 hosts (IPs) que mais transferiram dados (bytes)
d) Participação dos sistemas operacionais (Windows, Linux, Mac, Outros)
e) Horários com maior número de acesso (Manhã, Tarde ou Noite)


Requisitos de codificação:
a) Modularização de código (funções)
b) Tratamento de exceções


Desafio extra de exibição de dados(20 pontos):
a) Gráficos de barras
b) Gráfico de linhas
c) Gráfico de pizza
