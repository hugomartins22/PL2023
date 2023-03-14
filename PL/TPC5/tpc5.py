import re

def main():

    while True:
        saldo = 0
        print("Para iniciar uma chamada, pff prima -> LEVANTAR")
        comando = input()
        if comando == "LEVANTAR":
            print("Introduza moedas.")
            moedas = input()
            arr_moedas = re.findall(r"\b[0-9]+[ec]\b", moedas)

            moedas_inv = []
            for moeda in arr_moedas:
                if moeda == "1c" or moeda == "2c" or moeda == "5c" or moeda == "10c" or moeda == "20c" or moeda == "50c":
                    quantia = re.search(r"[0-9]+", moeda)[0]
                    saldo += int(quantia)/100
                elif moeda == "1e" or moeda == "2e":
                    quantia = re.search(r"[0-9]+", moeda)[0]
                    saldo += int(quantia)
                else:
                    quantia = re.search(r"[0-9]+", moeda)[0]
                    moedas_inv.append(quantia)

            if len(moedas_inv) == 0:
                if saldo >= 1:
                    euros = re.search(r"^[0-9]+", str(saldo))[0]
                    centimos = re.search(r"[0-9]+$", str(saldo))[0]
                    print("Saldo = " + euros + "e" + centimos + "c")
                elif saldo > 0 and saldo < 1:
                    centimos = re.search(r"[0-9]+$",str(saldo))[0]
                    print("Saldo = 0" + "e" + centimos + "c")
                else:
                    print("Saldo = 0 !")

            else:
                for mi in moedas_inv:
                    print(mi+"- Moeda inválida;")
                euros = re.search(r"^[0-9]+", str(saldo))[0]
                centimos = re.search(r"[0-9]+$", str(saldo))[0]
                print("Saldo = " + euros + "e" + centimos + "c")

            while True:
                print("Marque o número de telefone pff")
                nr_telefone = input()
                numero = re.search(r"\d+", nr_telefone)[0]

                if len(numero) < 9:
                    if numero[0:2] == "00":
                        if saldo > 1.5:
                            saldo -= 1.5
                            print("Chamada em execução. Se pretender deslidar , pff prima -> POUSAR")
                            p = input()
                            if p == "POUSAR":
                                euros = re.search(r"^[0-9]+", str(saldo))[0]
                                centimos = re.search(r"[0-9]+$", str(saldo))[0]
                                print("Troco= "+ euros+"e"+centimos+"c"+ "; Volte sempre!")
                                break
                    else:
                        print("Número Inválido!")
                        print("Insira um número válido!")
                elif len(numero) > 9:
                    print("Número Inválido!")
                    print("Insira um número válido!")

                else:
                    if numero[0:3] == "601" or numero[0:3] == "641":
                        print("A sua chamada foi bloqueada !")

                    if numero[0] == "2":
                        if saldo > 0.25:
                            saldo -= 0.25
                            print("Chamada em execução. Se pretender deslidar , pff prima -> POUSAR")
                            p = input()
                            if p == "POUSAR":
                                euros = re.search(r"^[0-9]+", str(saldo))[0]
                                centimos = re.search(r"[0-9]+$", str(saldo))[0]
                                print("Troco= "+ euros+"e"+centimos+"c"+ "; Volte sempre!")
                                break

                    if numero[0:3] == "800":
                        print("Chamada em execução. Se pretender deslidar , pff prima -> POUSAR")
                        p = input()
                        if p == "POUSAR":
                            print("volte sempre!")
                            break

                    if numero[0:3] == "808":
                        if saldo > 0.1:
                            saldo -= 0.1
                            print("Chamada em execução. Se pretender deslidar , pff prima -> POUSAR")
                            p = input()
                            if p == "POUSAR":
                                euros = re.search(r"^[0-9]+", str(saldo))[0]
                                centimos = re.search(r"[0-9]+$", str(saldo))[0]
                                print("Troco= "+ euros+"e"+centimos+"c"+ "; Volte sempre!")
                                break




        else:
            print("Talvez queira levantar o telefone primeiro? Pff prima -> LEVANTAR")

if __name__ == '__main__':
    main()