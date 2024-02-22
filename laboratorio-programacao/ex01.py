
contador_clientes_femininos_7_dias = 0
clientes = []
km_total = 0 
while True:
    nome = str(input("Informe o nome do cliente (ou 'SAIR' para encerrar):"))
    if nome.upper() == 'SAIR':
        break

    sexo = str(input('Informe seu sexo (F- Feminino, M- Masculino): '))
    placa = str(input('Informe a placa do carro alugado: '))
    km_contratados = int(input('Informe a quantidade de quilômetros contratados: '))
    dias = int(input('Informe a quantidade de dias contratados: '))

    
    total = (dias * 70) + (km_contratados * 0.10)
    clientes.append((nome, placa, total))

    km_total += km_contratados

    if sexo == 'f' and dias > 7:
        contador_clientes_femininos_7_dias += 1

print('\n--- Relatório de Contratações ---')
for clientes in clientes:
    print(f'Cliente: {clientes[0]}, Placa do carro: {clientes[1]}, Valor Total a Pagar: {clientes[2]:.2f}')

if len(clientes) > 0:
    media_km = km_total / len(clientes)
    print(f'\nMédia de quilômetros contratados pelos clientes: {media_km:.2f}')

if contador_clientes_femininos_7_dias > 0: 
    print(f'\nNúmero de clientes femininos com aluguéis acima de 7 dias: {contador_clientes_femininos_7_dias}')
