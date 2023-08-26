#Tomada de Decisão e Estruturas de Repetição

#1.Faça um programa que peça dois números e imprima o maior deles.

#Leitura dos valores
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

#Estrutura de decisão
if numero1 > numero2:
    print(f'O maior número é o {numero1}')
else:
    print(f'O maior número é o {numero2}')

print('\n') #quebra de linha

'''2.Faça um programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-vespertino ou N-noturno.
Imprima a mensagem "Bom dia!", "Boa tarde!" ou "Boa noite!" ou
"Valor Inválido!", conforme o caso.'''

#Leitura do valor
turno = input('Em que turno você estuda? Digite M (matutino), V (vespertino) ou N (noturno): ')

#Estrutura de decisão conforme valor inserido
if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('Valor Inválido!')

print('\n') #quebra de linha

'''3.Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue 
pedindo até que o usuário informe um valor válido.'''

#Leitura da nota
nota = int(input('Digite uma nota entre zero e dez: '))

#Estrutura de repetição conforme valor informado
while (nota < 0) or (nota > 10):
    nota = int(input('Valor Inválido! Digite novamente uma nota entre zero e dez: '))
print('Nota inserida com sucesso!')

print('\n') #quebra de linha
