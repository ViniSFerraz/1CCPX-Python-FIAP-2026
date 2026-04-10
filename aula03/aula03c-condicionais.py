#OPERADORES DE ATRIBUIÇÃO

num = 15
print(num)

num *= 2
print(num)

#OPERADORES RELACIONAIS

print() #pular linha
print(6 >= 6)

idade = 20
print(idade == 20)

maior_idade = idade >= 18
print(maior_idade)

#OPERADORES LOGICOS
#LOGICA E (and)
print()

verifica_email = True
verifica_senha = True

login = verifica_email and verifica_senha
print(login)

if login:
    print("Acesso liberado!")
else:
    print("Acesso negado")

print()
#NOTAS...

nota_final = 12

if nota_final > 0 and nota_final < 10:
    if nota_final < 4:
        print("Reprovado")
    elif nota_final < 6:
        print("Reprovado")
    else:
        print("Aprovado")

else:
    print("Nota invalida")
print("FIM")

