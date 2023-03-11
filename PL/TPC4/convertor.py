import json
import re

def main():

    #campo normal = 1
    #campo lista = 2
    #campo lista tamanho variavel = 3
    #campo media = 4
    # campo sum = 5

    final = []
    k = open("alunos.csv", "r")
    f = open("alunos.json", "w")
    aux = []
    i = 0

    fields = k.readline()
    functions = fields.split("::")

    if functions[0]:
        field = re.split(",(?![^{]*\})", functions[0])
        for x in field:
            if re.match(r"^\w+$", x):
                aux.append((1, x))
                i += 1

            if re.search(r"\{[\d]\}$", x):
                value = re.findall(r"[\d]", x)[0]
                aux.append((2, x, value))
                i += 1

            if re.search(r"\{[\d]+,[\d]+\}$", x):
                value1 = re.findall(r"[\d]", x)[0]
                value2 = re.findall(r"[\d]", x)[1]
                aux.append((3, x, value1, value2))
                i += 1



    if len(functions) > 1:
        aux2 = functions[1].split(",")
        for func in aux2:
            if func == "media":
                aux.append((4, func))
                i += 1

            if func == "sum":
                aux.append((5, func))
                i += 1


    for x in aux:
        print(x)



    linha = k.readline()
    while linha:
        dicionario = dict()
        valores = linha.split(",")
        t = 0
        i = 0
        while i < len(valores):
            if aux[t][0] == 1:
                dicionario[aux[t][1]] = valores[i]

            if aux[t][0] == 2:
                dicionario[aux[t][1]] = []
                x = 0
                while x < int(aux[t][2]):
                    dicionario[aux[t][1]].append(valores[i])
                    x += 1
                    i += 1
                    if x == int(aux[t][2]):
                        i -= 1

            if aux[t][0] == 3:
                dicionario[aux[t][1]] = []
                x = 0
                while x < int(aux[t][3]):
                    if valores[i] != "":
                        dicionario[aux[t][1]].append(valores[i])
                        x += 1
                        i += 1
                        if x == int(aux[t][3]):
                            i -= 1
                    else:
                        x += 1
                        i += 1
                        if x == int(aux[t][3]):
                            i -= 1

            if aux[t][0] == 4:
                soma = 0
                nr = 0
                while valores[i] != "":
                    nr += 1
                    soma += int(valores[i])
                    i += 1
                    if i == len(valores):
                        break
                dicionario[aux[t][1]] = soma/nr
                break

            if aux[t][0] == 5:
                soma = 0
                while valores[i] != "":
                    soma += int(valores[i])
                    i += 1
                    if i == len(valores):
                        break
                dicionario[aux[t][1]] = soma
                break

            i += 1
            t += 1
        final.append(dicionario)
        linha = k.readline()

    json.dump(final, f)
    k.close()
    f.close()

if __name__ == '__main__':
    main()