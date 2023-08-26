'''1.Faça um programa com uma função que necessite de três
argumentos e que forneça a soma desses três argumentos.'''

#função que soma os valores numéricos fornecidos
def soma (x, y, z):
    resultado = x + y + z
    print(f'A soma dos três números é igual a: {resultado}') 

x = int(input('Digite o primeiro valor para a soma: '))
y = int(input('Digite o segundo valor para a soma: '))
z = int(input('Digite o terceiro valor para a soma: '))

soma(x, y, z) #chamada da função
print('\n') #quebra de linha

'''2.Reverso do número. Faça uma função que retorne o reverso
de um número inteiro informado. Por exemplo: 127 -> 721.'''

#função que retorna o reverso do valor fornecido
def reverso_numero(x):
    resultado = int(str(x)[::-1])
    print(f'O reverso do número é: {resultado}')

x = int(input('Digite um número inteiro com 2 ou mais algarismos: '))

reverso_numero(x) #chamada da função
print('\n') #quebra de linha

'''3.Escreva um script que pergunta ao usuário se ele deseja
converter uma temperatura de graus Celsius para Fahrenheit ou
vice-versa. Para cada opção, crie uma função. Crie uma terceira,
que é um menu para o usuário escolher a opção desejada, onde esse
menu chama a função de conversão correta.'''

#função que converte a temperatura de Celsius para Fahrenheit
def conversao_celsius():
    C = float(input('Digite a temperatura em Celsius: '))    
    F = 9 * C / 5 + 32
    print(f'A temperatura em Fahrenheit é igual a: {F:.1f}ºF') #valor formatado com uma casa decimal

#função que converte a temperatura de Fahrenheit para Celsius
def conversao_fahrenheit():
    F = float(input('Digite a temperatura em graus Fahrenheit: '))    
    C = 5 / 9 * (F - 32)
    print(f'A temperatura em graus Celsius é igual a: {C:.1f}ºC') #valor formatado com uma casa decimal

#função que lê a resposta do usuário e converte a temperatura conforme a condição programada
def temp():
    opcao = int(input('Escolha:\n'
                  '1 para converter a temperatura de graus Celsius para Fahrenheit.\n' 
                  '2 para converter a temperatura de graus Fahrenheit para Celsius.\n' 
                  'Digite sua opção (1 ou 2): '))

    if (opcao == 1) or (opcao == 1):
        conversao_celsius()
    else:
        if (opcao == 2) or (opcao == 2):
            conversao_fahrenheit()

temp() #chamada da função
print('\n') #quebra de linha