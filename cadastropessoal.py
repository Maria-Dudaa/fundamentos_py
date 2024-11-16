# Cadastro de informações pessoais

# Solicita o nome completo
nome = input("Digite seu nome completo: ")

# Solicita a idade e converte para inteiro
idade = int(input("Digite sua idade: "))

# Pergunta se é estudante e armazena a resposta
estudante = input("Você é estudante? (sim/não): ").strip().lower()

# Converte a resposta para 'Sim' ou 'Não'
if estudante == 'sim':
    estudante = 'Sim'
    # Exibe as informações incluindo a resposta sobre ser estudante
    print(f"\nMeu nome é {nome}, tenho {idade} anos e sou estudante: {estudante}")
else:
    # Exibe as informações sem a parte de ser estudante
    print(f"\nMeu nome é {nome}, tenho {idade} anos.")
