'''from math import trunc
num = float(input('Digite um número: '))
numero_inteiro = trunc(num)
print(f'A porção inteira de {num} é {numero_inteiro}')'''

num = float(input('Digite um número: '))
print('A porção inteira de {} é {:.0f}'.format(num, num))