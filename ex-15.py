'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se
 que são descontados 11% para o Imposto de Renda,
  8% para o INSS 
  e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.'''

qtporhr = float(input("\n\nDigite quanto você ganha por hora trabalhada: " ))
qntshrs = float(input("\n\nDigite quantas horas você trabalhou nesse mês: "))

qtporhr = qtporhr * qntshrs

print(f"\n Salário bruto: {qtporhr} R$")

ir = (qtporhr * 0.11)

print(f"\nValor pago ao Inposto de Renda: {ir} R$")

inss = (qtporhr * 0.08)

print(f"\nValor pago ao INSS de renda: {inss} R$")

sindicato = (qtporhr * 0.05 )

print(f"\nValor pago ao Sindícato: {sindicato} R$")

desontosalario = ir + inss + sindicato

salarioliquido = (qtporhr - desontosalario)

print(f"\nSalário liquído: {salarioliquido} R$\n")