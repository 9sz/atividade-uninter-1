print('Bem vindo à lojinha do Matheus!')
unidadeproduto = int(input('Qual a quantidade?'))
valorproduto = int(input('Qual o valor do produto?'))

# O valor inicial é definido multiplicando o valor com a unidade.
valorinicialproduto = valorproduto * unidadeproduto

desconto = 0
# Por padrão, o desconto será zero, vou aplicar os descontos se as regras acontecerem.

if unidadeproduto >= 5 <= 19:
    desconto = valorinicialproduto * (3/100)

if unidadeproduto >= 20 <= 99:
    desconto = valorinicialproduto * (6/100)

if unidadeproduto >= 100:
    desconto = valorinicialproduto * (10/100)

else:
    print('Está abaixo de 4 unidades!')

valorfinal = valorinicialproduto - desconto

print('O valor total sem desconto é: {} R$'.format(valorinicialproduto))
print('O valor final após o desconto é: {} R$'.format(valorfinal))
# Vou aplicar uma regra para saber se houve desconto
if valorfinal < valorinicialproduto:
    print('O desconto foi aplicado com sucesso.')
elif valorfinal == valorinicialproduto:
    print('Não houve desconto.')

