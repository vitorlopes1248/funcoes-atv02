# Crie uma função chamada verificar_paridade que receba um número inteiro como argumento e retorne uma mensagem indicando se o número é par ou ímpar.

num = int(input("Digite um numero:"))
def verificar_paridade(num):
    if num %2 == 0:
        return "numero par"
    else:
        return "numero impar"
    
mani=verificar_paridade(num)
print(mani)