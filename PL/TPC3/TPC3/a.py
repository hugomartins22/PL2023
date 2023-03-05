import re

def main():
    file = open("processos.txt", "r")

    freq_process_ano = {}
    i=0

    for line in file:
        data = re.findall(r"[0-9]+-[0-9]+-[0-9]+",line)
        if data:
            ano = re.findall("\d{4}",data[0])
        if ano:
            freq_process_ano[int(ano[0])] = freq_process_ano.get(int(ano[0]), 0) + 1

    file.close()


if __name__ == '__main__':
    main()