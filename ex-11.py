'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.'''

num1 = int(input("\n Digite um número inteiro: "))
num2 = int(input("\n Digite outro número inteiro: "))
num3 = float(input("\n Digite um número real(flutuante): "))

dobro1 = num1 * 2
triplo = num1 * 3
metade2 = num2 / 2
elevado3 = pow(num3, 3)

vezes = dobro1 * metade2
soma = triplo + num3

print(f"\n O produto do dobro do primeiro número com metade do segundo número é: {vezes:.2f} ")
print(f"\n A soma do triplo do primeiro número com o terceiro número é: {soma:.2f} ")
print(f"\n O terceiro número elevado ao cubo é: {elevado3:.2f} ")
