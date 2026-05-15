temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

maior = 0
sala = 0

for i in range(len(temperaturas)):

    soma = 0
    critico = 0

    for j in range(len(temperaturas[i])):

        soma = soma + temperaturas[i][j]

        if temperaturas[i][j] >= 33:
            critico = critico + 1

    media = soma / len(temperaturas[i])

    print(f"Sala {i + 1}")
    print(f"Média: {media}")
    print(f"Registros críticos: {critico}")
    print()

    if critico > maior:
        maior = critico
        sala = i + 1

print(f"Sala com maior risco: Sala {sala}")
