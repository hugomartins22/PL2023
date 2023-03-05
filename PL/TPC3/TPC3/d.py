import json
import re

def main():

    auxiliar = dict()
    k = open("processos.txt", "r")
    f = open("novo.json", "w")
    num = 1

    for line in k:
        if num > 20:
            break

        x = re.split(r"::", line)
        year = re.findall(r"^[0-9]{4}", x[1])[0]

        if year in auxiliar:
            auxiliar[year].append((x[0], x[1], x[2], x[3], x[4], x[5]))
        else:
            auxiliar[year] = []
            auxiliar[year].append((x[0], x[1], x[2], x[3], x[4], x[5]))
        num += 1
    json.dump(auxiliar, f)
    k.close()
    f.close()

if __name__ == '__main__':
    main()