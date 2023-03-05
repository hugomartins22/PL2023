import re

def main():
    file = open("processos.txt", "r")

    freq_parentesco = {}

    for line in file:
        parentesco = re.findall(r"Irmao|Sobrinho|Pai|Mãe|Sogra|Irma|Avo|Tio",line)

        for p in parentesco:
            freq_parentesco[p] = freq_parentesco.get(p,0)+1

    file.close()


if __name__ == '__main__':
    main()