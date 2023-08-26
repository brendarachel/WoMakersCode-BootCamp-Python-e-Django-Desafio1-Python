'''1.Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira e calcule quanto poderia comprar de cada moeda estrangeira.
Considere os valores de conversão abaixo:
Dólar Americano: R$4,91
Peso Argentino: R$0,02
Dólar Australiano: R$3,18
Dólar Canadense: R$3,64
Franco Suíço: R$0,42
Euro: R$5,36
Libra esterlina: R$6,21'''

#Leitura do valor em Real na carteira
carteira = float(input('Digite o valor em Real que você possui na carteira: '))

#Conversão do valor em Real para cada moeda estrangeira
dolar_americano = carteira / 4.91
peso_argentino = carteira / 0.02
dolar_australiano = carteira / 3.18
dolar_canadense = carteira / 3.64
franco_suico = carteira / 0.42
euro = carteira / 5.36
libra_esterlina = carteira / 6.21

#Impressão dos resultados (valores formatados com duas casas decimais)
print('Com o valor disponível, você poderia comprar:')
print(f'Dólar Americano: US${dolar_americano:.2f}.')
print(f'Peso Argentino: ${peso_argentino:.2f}.')
print(f'Dólar Australiano: A${dolar_australiano:.2f}.')
print(f'Dólar Canadense: C${dolar_canadense:.2f}.')
print(f'Franco Suíço: Fr{franco_suico:.2f}.')
print(f'Euro: €{euro:.2f}.')
print(f'Libra Esterlina: £{libra_esterlina:.2f}.')
print('\n') #quebra de linha

'''2.Escreva um programa que pergunte a quantidade de km
percorridos por um carro alugado e a quantidade de dias
pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$80,00 por dia e R$0,20 por
km rodado.'''

#função que calcula os km percorridos x a quantidade de dias de aluguel
def calculo(km, dias):
    preco_km = km * 0.20
    preco_dias = dias * 80

    preco_total = preco_km + preco_dias
    print(f'O valor total a ser pago é R${preco_total:.2f}') #valor total formatada com duas casas decimais
    
km = float(input('Quantos km foram percorridos? '))
dias = int(input('Por quantos dias o carro foi alugado? '))

calculo(km, dias) #chamada da função
print('\n') #quebra de linha

'''3.Faça um algoritmo que leia o salário de um funcionário
e mostre seu novo salário.
    Se o salário for até R$1000,00 o funcionário terá 20%
    de aumento.
    Entre R$1001,00 até R$2800,00 o funcionário terá 10% de
    aumento.
    Acima de R$2801,00 o funcionário terá 5% de aumento.'''

#Leitura do salário
salario = float(input("Digite o salário do funcionário: "))

#Condições para o cálculo da porcentagem correta para cada faixa salarial
if salario <= 1000:
    novo_salario = salario + (salario * 0.2)
    print(f'O novo salário é de R${novo_salario:.2f}')
elif (salario >= 1001) and (salario <= 2800):
    novo_salario = salario + (salario * 0.1)
    print(f'O novo salário é de R${novo_salario:.2f}')
else:
    novo_salario = salario + (salario * 0.05)
    print(f'O novo salário é de R${novo_salario:.2f}') 

print('\n') #quebra de linha

'''4.Crie um programa que tenha a função leiaInt(), que vai
funcionar de forma semelhante à função input() do Python, só
que fazendo a validação para aceitar apenas um valor numérico.
    Ex:
    n = leiaInt('Digite um n')'''

#função que aceita apenas um valor numérico inteiro
def leiaInt():
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
            print(f'Você digitou o valor {n}')
            break
        except ValueError:
            print('Erro! Digite apenas números inteiros.')

leiaInt() #chamada da função
print('\n') #quebra de linha