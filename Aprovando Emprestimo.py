Valcasa = int (input('Qual o valor da casa desejada?'))

Salario = int (input('Qual o salario do comprador?'))

Anos = float (input('Em quantos anos o comprador planeja pagar?'))
Parcelas = Valcasa /(Anos * 12)
minimo = Salario * 30/100
print('As parcelas de uma casa de R$ {:.2f} Reais, serao de R${:.2f} Reais'.format(Valcasa, Parcelas))

if Parcelas >= minimo:
    print('Emprestimo negado')
else:
    print('Emprestimo aprovado!')
