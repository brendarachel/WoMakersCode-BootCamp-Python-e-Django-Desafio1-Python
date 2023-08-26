#Listas, Tuplas e Dicionários

'''1.Faça um programa que peça as quatro notas de 10 alunos,
calcule e armazene numa lista a média de cada aluno, imprima
o número de alunos com média maior ou igual a 7.0.'''

medias = [] #criação da lista para armazenar as médias

#Estrutura de repetição para leitura das notas dos alunos
for i in range(1,11): #quantidade de aluno
    notas = []
    print(f'Notas do Aluno {i}: ')    
    for j in range(1,5): #quantidade de notas
        nota = float(input(f'Digite a nota {j}: '))
        notas.append(nota)

    #Cálculo das médias
    media = sum(notas) / len(notas)

    #Armazenamento das médias em uma lista
    medias.append(media)

    #Verificando alunos com média maior ou igual a 7.0
    alunos_aprovados = 0
    for media in medias:
        if media >= 7.0:
            alunos_aprovados += 1
       
print(f'Número de alunos com média maior ou igual a 7.0: {alunos_aprovados}')
print('\n') #quebra de linha

'''2.Programa nome ao contrário em maiúsculas. Faça um programa
que permita ao usuário digitar seu nome e em seguida mostre o nome
do usuário de trás para frente utilizando somente letras maiúsculas.
Dica: lembre-se que ao informar o nome do usuário pode digitar letras
maiúsculas ou minúsculas.'''
lista_nome = [] #criação da lista

nome = input('Digite seu nome: ') #leitura do nome
lista_nome.append(nome[::-1].upper()) #inclusão do nome na lista de forma invertida e em maiúsculas

print(lista_nome)

print('\n') #quebra de linha

'''3.Escreva um programa em Python que onde todos os valores em um
dicionário são emitidos. Se sim, imprima True. Caso contrário,
imprima False.'''

#criação do dicionário
dicionario = {
    'maçã': 'fruta', 
    'Harry Potter': 'filme', 
    'camisa': '', 
    'Idade': 48 }

print(dicionario)

#Estrutura para verificar se todos os valores foram emitidos ou não
valores_emitidos = all(valor for valor in dicionario.values())

if valores_emitidos:
    print('True')
else:
    print('False')        

print('\n') #quebra de linha

'''4.Utilizando listas faça um programa que faça cinco perguntas para
uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"

O programa deve, no final, emitir uma classificação sobre a participação
da pessoa no crime. Se a pessoa responder positivamente a 2 questões, ela
deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5
como "Assassino". Caso contrário, ele será classificado como "Inocente".'''

#criação de lista para armazenamento das perguntas
perguntas = [
    'Telefonou para a vítima? ', 
    'Esteve no local do crime? ', 
    'Mora perto da vítima? ', 
    'Devia para a vítima? ', 
    'Já trabalhou com a vítima? '
]

#lista para armazenar as respostas
respostas = []

#Leitura das respostas e armazenamento em lista
for pergunta in perguntas:
    resposta = input(pergunta + 'Responda s/n: ').lower()
    respostas.append(resposta)

#Contagem das respostas positivas
respostas_positivas = respostas.count('s')

#Estrutura para classificação da pessoa conforme suas respostas
if respostas_positivas == 2:
    print('Suspeita')
elif (respostas_positivas == 3) or (respostas_positivas == 4):
    print('Cúmplice')
elif respostas_positivas == 5:
    print('Assassino')
else:
    print('Inocente')

print('\n') #quebra de linha