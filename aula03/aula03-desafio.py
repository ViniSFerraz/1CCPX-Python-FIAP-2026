idade = int(input("Qual a sua idade?"))

if idade < 16:
    print("Você não pode votar!")
elif idade < 18 or idade > 70:
    print("O seu voto é opcional!")
else:
    print("O seu voto é obrigatório!")