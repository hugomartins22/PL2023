def main():
    texto = input()
    lista = list(texto)
    nr_caracteres = len(texto)
    flag = True
    position = 0
    total = 0

    while position < nr_caracteres:
        if lista[position].isdigit() and flag:
            total += int(lista[position])

        if not lista[position].isdigit() and flag:
            if lista[position] == "=":
                print(total)
            if lista[position] == "O" or lista[position] == "o":
                if position+2 < nr_caracteres and lista[position+1] == "F" and lista[position+2] == "F":
                    flag = False

        if not lista[position].isdigit() and not flag:
            if lista[position] == "O" or lista[position] == "o":
                if position+1 < nr_caracteres and lista[position+1] == "N" and flag == False:
                    flag = True

        position += 1

if __name__ == '__main__':
    main()