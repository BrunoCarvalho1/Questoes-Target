string_original = input("Digite a string que deseja inverter: ")

string_invertida = ""

for i in range(len(string_original) - 1, -1, -1):
    string_invertida += string_original[i]

print(f"String original: {string_original}")
print(f"String invertida: {string_invertida}")
