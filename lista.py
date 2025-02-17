# Lista original
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Remover duplicados mantendo a ordem original
numeros_sem_duplicados = []
for num in numeros:
    if num not in numeros_sem_duplicados:
        numeros_sem_duplicados.append(num)

# Calcular a soma dos números após a remoção dos duplicados
soma = sum(numeros_sem_duplicados)

print("Lista sem duplicados:", numeros_sem_duplicados)
print("Soma dos números após a remoção dos duplicados:", soma)
