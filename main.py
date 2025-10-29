from collections import defaultdict

"""
Resolução de problemas utilizando if, elif, else, try, excpet, for e while. 
"""

### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.
def exercicio01():
    quantidade = int(input("Digite a quantidade de vendas: "))
    preco = float(input("Digite o valor de vendas:R$ "))
    if quantidade > 0 and preco > 0:
        print(f"\nA quantidade de vendas de '{quantidade}' e o valor de vendas R$ '{preco}' são Dados válidos!")
    else:
        print(f"\n A quantidade e valor de vendas não podem ser negativos. Dados inválidos.")
    

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'
def exercicio02():
    
    temperatura_input = int(input("Digite a temperatura do sensor IoT: "))
    if temperatura_input < 18:
        print("A temperatura do sensor é 'Baixa'.")
    elif temperatura_input >= 18 and temperatura_input <= 26:
        print("A temperatura do sensor é 'Normal'")
    elif temperatura_input > 26:
        print("A temperatura do sensor é 'Alta'")
    else:
        print("Por favor, digite o valor da temperatura novamente.")
    

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
def exercicio03():
    log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
    if log['level'] == 'ERROR':
        print(log['message'])


### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.
def exercicio04():
    # Valida idade do usuário
    try:
        idade_input = input("Por favor, digite sua idade: ").strip()
        if not idade_input:
            print("Erro: A idade não pode estar em branco.")
        else:
            idade_num = int(idade_input)

            if 18 <= idade_num <= 65:
                print(f"ACESSO CONCEDIDO: A idade {idade_num} é válido para o acesso.")
            else:
                print(f"ACESSO NEGADO: A idade {idade_num} está fora da faixa permitida")
    except ValueError:
        print(f"Erro: A entrada '{idade_num}' não é um número válido")

    # Valida e-mail do usuário
    try:
        email_input = input("Por favor, digite seu e-mail: ").strip()
        if not email_input:
            print("Erro: O e-mail não pode estar em branco;")
        if email_input.count('@') !=1:
                print("Erro: O e-mail deve conter um '@'")
        else:
            nome_usuario, dominio = email_input.split('@')
            
            if not nome_usuario or not dominio:
                print("Erro: O nome de usuário e domínio não podem ser vazios.")
            elif '.' not in dominio or dominio.startswith('.') or dominio.endswith('.'):
                print("Erro: O domínio do e-mail parece estar incompleto.")
            else: 
                print(f"ACESSO CONCEDIDO: Seu e-mail {nome_usuario, dominio} é válido.")
    except:
        print(f"Erro: A entrada '{email_input}' não é um e-mail válido")
    

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.
def exercicio05():
  transacao = {'valor': 12000, 'hora': 20}
  if transacao ['valor'] > 10_000 or transacao['hora'] < 9 or transacao['hora'] > 18:
      print("Erro: Transação suspeita")
  else:
      print("Transação bem sucedida.")


### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.
def exercicio06():
    # Texto original
    texto_original = "Aqui está um texto para ver quantas palavras tem nele."

    # Divide em uma lista de palavras
    lista_palavras = texto_original.split()

    # Conta quantas palavras tem o texto
    lista_palavras = len(lista_palavras)

    print(f"O texto original '{texto_original}'\ntem: {lista_palavras} palavras.")
    

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
def exercicio07():

    # Lista de números
    numeros = [10, 20, 30, 40, 50]
    minimo = min(numeros)
    maximo = max(numeros)
    normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

    print(normalizados)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando
def exercicio08():
    usuarios = [
        {"nome":"Alice", "email": "alice@email.com"},
        {"nome":"Bob", "email": ""},
        {"nome":"Carol", "email": "carol@email.com"},
    ]
    usuarios_validos = [usuario for usuario in usuarios if usuario["email"]]
    print(usuarios_validos)


### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.
def exercicio09():
    # Define a sequência de números de 1 a 10
    numeros = range(1,11)
    # Para cada x em numeros, se x for par, adiciona x a nova lista
    pares = [x for x in numeros if x % 2 == 0]
    print(pares)



### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
# vendas = [
#     {"categoria": "eletrônicos", "valor": 1200},
#     {"categoria": "livros", "valor": 200},
#     {"categoria": "eletrônicos", "valor": 800}
# ]
def exercicio10():
    vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
    ]

    total_por_categoria = {}
    for venda in vendas:
        categoria = venda["categoria"]
        valor = venda["valor"]
        if categoria in total_por_categoria:
            total_por_categoria[categoria] += valor
        else:
            total_por_categoria[categoria] = valor

    print(total_por_categoria)


### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
def exercicio11():
    dados = []
    while True:
        print("#=====================================#")
        print("Digite 'sair' para encerrar o programa")
        print("#=====================================#")

        entrada = input("Digite o valor desejado: ")
        if entrada == "sair":
            print("Encerrando programa...")
            break 
        print(f"O valor {entrada} foi adicionado aos dados")


### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
def exercicio12():
    while True:
        numero = int(input("Digite um número de 1 a 10: "))
        if numero == 5:
            print(f"O número '{numero}' foi digitado. Pode entrar!")
            break
        else:
            print(f"O número '{numero}' está incorreto. Tente novamente.")
    

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.
def exercicio13():
    pagina_atual = 1
    pagina_total = 5
    while pagina_atual <= pagina_total:
        print(f"Processando {pagina_atual} de {pagina_total}...")
        pagina_atual += 1
    print("Todas as páginas foram processadas")


### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
def exercicio14():
    tentativa = 1
    tentativa_maxima = 10
    while tentativa <= tentativa_maxima:
        print(f"'{tentativa}' de '{tentativa_maxima}'")
        tentativa += 1
        if tentativa == 10:
            print("Você chegou ao limite de tentativas.")
            break


### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.
# itens = [1, 2, 3, "parar", 4, 5]
def exercicio15():
    itens = [1, 2, 3, "parar", 4, 5]

    item = 0
    while item < len(itens):
        if itens[item] == "parar":
            print("Parada encontrada, encerrando o processamento.")
            break
        # Processa o item
        print(f"Processando item: {itens[item]}")
        item += 1

# Programa principal
if __name__ =="__main__":
    exercicio01()
    exercicio02()
    exercicio03()
    exercicio04()
    exercicio05()
    exercicio06()
    exercicio07()
    exercicio08()
    exercicio09()
    exercicio10()
    exercicio11()
    exercicio12()
    exercicio13()
    exercicio14()
    exercicio15()