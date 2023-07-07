# Método 1 da interpolação

nome = 'Alan Lucena'
idade = 43
profissao = 'Developer'
linguagem = 'Python'

print("Olá, me chamo %s. EU tenho %d anos de idade, trabalho com %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

# Método 2 da interpolação

print("Olá, me chamo {}. EU tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

# Método 2 da interpolação

print("Olá, me chamo {}. EU tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

# Formatação duas casas
PI = 3.14159

print(f'Valor de PI: {PI:.2F}')

# Formatação duas casas com espaço
PI = 3.14159

print(f'Valor de PI: {PI:10.2F}')


profissao = "Progamador"
linguagem = "Python"

dados = {"nome": "Alan Lucena", "idade": 28}

print("Nome: %S Idade: %d" % (nome, idade))
print("Nome: {} Idade:".format(nome, idade))
print("Nome: {1} Idade: {0)".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}" .format(idade, nome))
print("Nome: {nome} Idade: {idade}" .format( nome=nome, idade=idade))
print("Nome: {nome} Idade: {idade}" .format(age= idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")





