from traceback import print_tb


tempoDeJogo = int(input("Quanto tempo temos já jogado? "))

if tempoDeJogo <= 90:
    print("Ainda tem jogo pela frente")
else:
    print("Putz, tá acabando o jogo.")