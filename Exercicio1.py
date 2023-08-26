#Conceitos Básicos de Python

'''1.Faça um programa que peça um número e então mostre a mensagem:
-> O número informado foi [número].'''

numero = int(input('Digite um número: ')) #Leitura do número

print(f'O número informado foi {numero}') #Impressão do número informado
print('\n') #quebra de linha

#2.Faça um programa que peça dois números e imprima a soma.

#Leitura dos números
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

#Cálculo e resultado da soma
soma = numero1 + numero2
print(f'A soma dos números é {soma}')
print('\n') #quebra de linha

'''3.Faça um programa que peça a temperatura em graus Celsius, transforme e 
mostre em graus Fahrenheit.'''

#Leitura da temperatura em Celsius
temp_celsius = float(input('Digite a temperatura em graus Celsius: '))

#Conversão da temperatura em Celsius para Fahrenheit
temp_fahrenheit = 9 * temp_celsius / 5 + 32 #fórmula para transformar Celsius em Fahrenheit
print(f'A temperatura em graus Fahrenheit é igual a {temp_fahrenheit:.1f}ºF') #graus Fahrenheit formatado com uma casa decimal
print('\n') #quebra de linha

'''4.Faça um programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês. Calcule e mostre o total do seu
salário no referido mês.'''

#Leitura dos valores
ganho_hora = float(input('Digite quanto você recebe por hora trabalhada: '))
horas_trabalhadas = float(input('Digite quantas horas você trabalhou esse mês: '))

salario = ganho_hora * horas_trabalhadas #cálculo do salário
print(f'O salário do mês é igual a R${salario:.2f}') #salario formatado com duas casas decimais
print('\n') #quebra de linha