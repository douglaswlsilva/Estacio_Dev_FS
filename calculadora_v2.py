# Declarar variaveis
saida = ''

# Declarar funções
def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return a / b

def calculadora(num1, num2, operacao):
    if operacao == '+' or operacao == 'adicao':
        return adicao(num1, num2)
    elif operacao == '-' or operacao == 'subtracao':
        return subtracao(num1, num2)
    elif operacao == '*' or operacao == 'multiplicacao':
        return multiplicacao(num1, num2)
    elif operacao == '/' or operacao == 'divisao':
        return divisao(num1, num2)
    else:
        return "Operação inválida"

# Inicio do Loop
while saida.lower() != 'n':
    # Solicita dados do calculo
    num1 = float(input('Digite o primeiro valor: '))
    num2 = float(input('Digite o segundo valor: '))
    operacao = input('Digite a operação desejada (+, -, *, /) ou o nome da operação sem acentos: ')

    # Chama calculadora
    resultado = calculadora(num1, num2, operacao)
    print('Resultado da operação:', resultado)

    # Confirmação de uso
    saida = input('Deseja continuar? (S/N): ')