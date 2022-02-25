soma = 0

print("Digite uma sequência de valores e use o valor 0 para terminar de adicionar valores para somar.")

valor = 1
while (valor != 0):
    valor = int(input('Digite um valor a ser somado: '))
    soma = soma + valor
print(f"A soma dos valores digitados é: ", soma)