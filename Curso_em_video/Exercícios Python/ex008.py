n = float(input('Digite um valor: '))
km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000
print('O valor {} em metros corresponde a \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(n, km, hm, dam, dm, cm, mm))