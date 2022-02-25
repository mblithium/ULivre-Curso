meuCartao = int(input("Digite o número do cartão de crédito: "))

cartaoLido = 1
encontreiMeuCartaoNaLista = False

while cartaoLido != 0 and not encontreiMeuCartaoNaLista:
  cartaoLido = int(input("Digite o número do próximo cartão de crédito: "))
  if cartaoLido == meuCartao:
    encontreiMeuCartaoNaLista = True

if encontreiMeuCartaoNaLista:
  print("Eba! Meu cartão está lá!")
else:
  print("Xii, meu cartão não está lá...")
