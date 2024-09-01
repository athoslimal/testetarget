def inverter_string(s):
    invertida = ""
    for i in range(len(s)-1, -1, -1):
        invertida += s[i]
    return invertida

string = input("Digite o dado que deseja inverter: ")
print(f"inverção: {inverter_string(string)}")
