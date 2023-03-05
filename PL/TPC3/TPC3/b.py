import re
from collections import defaultdict

dicionario=dict()

def aux():
    a=open("processos.txt")
    for k in a:
        if k.strip():
            x=re.split(r"::",k)

            year = re.findall(r"^[0-9]{4}",x[1])[0]

            if year in dicionario :
                dicionario[year].append((x[0],x[1],x[2],x[3],x[4],x[5]))
            else :
                dicionario[year] =[]
                dicionario[year].append((x[0],x[1],x[2],x[3],x[4],x[5]))


def namepopular(anobaixo, anocima):
    contanomes = dict()
    contaapelidos = dict()
    for key in dicionario:
        if (int(key) >= anobaixo and int(key) <= anocima):
            for posicao in dicionario[key]:

                cont = 2
                while cont < 5:
                    if posicao[cont] != "":
                        nome = re.findall(r"(?i:^[a-z]+)", posicao[cont])[0]
                        if nome in contanomes:
                            contanomes[nome] += 1
                        else:
                            contanomes[nome] = 1

                        a = re.findall(r"(?i:[a-z]+$)", posicao[cont])
                        aux = re.sub(r"\(|\)", "", posicao[cont])
                        b = re.findall(r"( ou)", aux)

                        if a != []:
                            apelido = a[0]
                            if apelido in contaapelidos:
                                contaapelidos[apelido] += 1
                            else:
                                contaapelidos[apelido] = 1
                        if b != []:
                            aqui = re.split(r" ou", aux)

                            for i in aqui:
                                last = re.findall(r"(?i:[a-z]+$)", i)

                                for la in last:
                                    if la in contaapelidos:
                                        contaapelidos[la] += 1
                                    else:
                                        contaapelidos[la] = 1

                    cont += 1;

    sorted_items = sorted(contanomes.items(), key=lambda x: x[1], reverse=True)
    top_items = sorted_items[:5]

    sit = sorted(contaapelidos.items(), key=lambda x: x[1], reverse=True)
    sunames = sit[:5]

    return (top_items, sunames)


def nomesmaispopulares():
    min = 1600
    while (min < 2000):
        print("########################################################")
        print(f"Os nomes mais populares no seculo {(min + 99 - 1) // 100 + 1} ")
        a = namepopular(min, min + 99)

        for i in a[0]:
            print(f"Nome : {i[0]} , Frequência :{i[1]}")

        print("------------------------------------------------")
        print(f"Os Apelidos mais populares no seculo {(min + 99 - 1) // 100 + 1} ")

        for i in a[1]:
            print(f"Apelido : {i[0]} , Frequência :{i[1]}")

        min += 100
        print("########################################################")



def main():

    aux()
    nomesmaispopulares()





if __name__ == '__main__':
    main()