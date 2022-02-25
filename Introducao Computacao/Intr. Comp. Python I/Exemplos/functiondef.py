def soma (x, y):
    return x + y

def complexo (x, y):
    x = soma(x, y)
    y = y + x
    return x * y

print(f"Resultado: {soma(5, 12)}")

print(complexo(5, 8))