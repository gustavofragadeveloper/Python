KM = float(input('Informe a quilometragem rodada: '))
D = int(input('informe quantos dias ficou alugado: '))
resultado =  (D * 60) + (KM * 0.15)
print('O valor a ser pago será: R${:.2f}'.format(resultado))