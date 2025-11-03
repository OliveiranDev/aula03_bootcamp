"""
Programa que valida entrada de usuário através de um banco de dados.
Retorna se o nome do usuário é válido em três tentativas, valida o salário
e calcula o bônus de 5%.
"""
# Banco de dados simulado
banco_de_dados = [
    {"nome": "Maria de Oliveira", "cargo": "Gerente de TI", "salario": 10_000},
    {"nome": "Joao Alves", "cargo": "Analista Junior", "salario": 3_500},
    {"nome": "Pedro Camargo", "cargo": "Analista Senior", "salario": 7_000},
    {"nome": "Jose de Souza", "cargo": "Secretario", "salario": 2_700},
    {"nome": "Sebastiana Pontes", "cargo": "Financeiro", "salario": 4_200}
]
print("\n" + "=" * 40)
print(" ----------SIMULADOR DE BÔNUS----------")
print("\n" + "=" * 40)

TENTATIVAS_MAXIMAS = 3
usuario_encontrado = None
salario_encontrado = False

# Loop de tentativas
for tentativa in range(TENTATIVAS_MAXIMAS):
    print("-" * 20)

    # valida nome do usuário
    nome_input = input("Por favor, digite seu nome completo: ").strip().lower()
    
    # Loop de busca
    for usuario_db in banco_de_dados:
        if not nome_input:
            print("O campo não pode estar em branco. Por favor, digite um nome.")
        if nome_input == usuario_db["nome"].lower():
            print(f"Bem-vendo(a), {usuario_db['nome'].title()}!")
            usuario_encontrado = usuario_db
            break

    # Termina o loop de tentativas    
    if usuario_encontrado:
          break
    # Se loop terminou e não encontra nome do usuário
    else:
        print(f"Nome '{nome_input}' não foi encontrado.")
        print(f"Você tem '{TENTATIVAS_MAXIMAS - 1 - tentativa}' de '{TENTATIVAS_MAXIMAS}'")

# Valida se usuário foi ou encontrado ou não
if not usuario_encontrado:
    print("\nNúmero máximo de tentativas excedido. Acesso negado.")
else:
    print("\nValidação de nome concluída com sucesso.")


    # Valida salário do usuário
    salario_validado = False
    for tentativa_salario in range(TENTATIVAS_MAXIMAS):
        try:
            salario_input = input("Por favor, digite o seu salário: R$ ")

            if not salario_input:
                print("Erro:O campo não pode estar em branco.")
                continue

            salario_limpo = salario_input.strip().replace("R$", "").replace(".", "").replace(",", ".")

            # Converter entrada do usuário para float
            salario_num = float(salario_limpo)

            # Busca o salario do usuário encontrado
            salario_correto = usuario_encontrado["salario"]

            # Condição se o salario digitado é o mesmo do usuário
            if salario_num == salario_correto:
                print(f"SUCESSO! Salário R$ {salario_num:,.2f} confirmado.")
                salario_validado = True 
                break
            else:
                print(f"Erro: O salário R$ {salario_num:.2f} está incorreto.")
        except ValueError:
            print(f"Erro: A entrada '{salario_input}' não é um número válido.")
        
        print(f"Você tem {TENTATIVAS_MAXIMAS - 1 - tentativa_salario} tentativa(s) restantes.")

# Valida se salario foi ou encontrado ou não
if not salario_validado:
    print("\nNúmero máximo de tentativas excedido. Acesso negado.")
else:
    print("\nSalário validado com sucesso!")

    # Resumo dos dados 
    salario_final = usuario_encontrado["salario"]
    cargo = usuario_encontrado["cargo"]
    nome = usuario_encontrado["nome"].title()

    # Calcular o valor do bônus
    bonus = salario_final * 0.05 # 5% de bônus
    total_receber = salario_final + bonus

    print("\n" + "=" * 40)
    print(" ----------RESUMO DE BÔNUS----------")
    print("\n" + "=" * 40)
    print(f"Colaborador(a): {nome}")
    print(f"Cargo: {cargo}")
    print(f"Salário base: R$ {salario_final:,.2f}")
    print(f"Bônus: (5%): R$ {bonus:,.2f}")
    print(f"Total a Receber: R$ {total_receber:,.2f}")
    print("\n" + "=" * 40)        
