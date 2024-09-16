def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def encontrar_primos(inicio, fim):
    primos = []
    for num in range(inicio, fim + 1):
        if eh_primo(num):
            primos.append(num)
    return primos

# Solicita ao usuário o intervalo
inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

# Encontra e imprime os números primos no intervalo
primos = encontrar_primos(inicio, fim)
print("Números primos no intervalo de", inicio, "a", fim, ":")
print(primos)
