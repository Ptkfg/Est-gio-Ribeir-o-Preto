# Est-gio-Ribeir-o-Preto
indice = 13
soma = 0 
k = 0

while k < indice:
    k = k + 1
    soma = soma + 1

print(soma)

numero_desejado = int(input("Informe um numero: "))

def fibonacci(n):
    a, b = 0, 1

    if n == a or n == b:
        return True
    
    while b < n:
        a, b = b, a + b

    if b == n:
        return True
    else:
        return False
    
    
if fibonacci(numero_desejado):
    print(numero_desejado, 'pertence a sequencia de Fibonacci')
else:
    print(numero_desejado, 'nao pertence a sequencia de Fibonacci')
