L = float(input('Largura da parede: '))
A = float(input('Altura da parede '))
ar = L * A
T = ar / 2
print(' Sua par5ede tem dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m2 \n Para pintar essa parede, você precisará de {:.2f}L de tinta'.format(L, A, ar, T))