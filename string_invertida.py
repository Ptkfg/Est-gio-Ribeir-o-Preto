string = input("Digite uma palavra ou frase: ")

#string vazia
string_invertida = ""

for i in range(len(string) - 1, -1, -1):
    string_invertida += string[i]

print("String invertida:", string_invertida)