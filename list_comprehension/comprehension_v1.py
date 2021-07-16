dobros = [i*2 for i in range(10)]

print('Dobro: ', dobros)


dobro_dos_pares = [i * 2 for i in range(10) if i % 2 == 0]

print('Dobro dos pares: ', dobro_dos_pares)


generator = (i ** 2 for i in range(10) if i % 2 == 0)

# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))

for numero in generator:
    print(numero)

# Podemos usar o f para nomear as chaves
dicionario = {i: i * 2 for i in range(10) if i % 2 == 0}
print('Dicionario com comprehension: ', dicionario)

for numero, dobro in dicionario.items():
    print(f'{numero} x 2 = {dobro}')
