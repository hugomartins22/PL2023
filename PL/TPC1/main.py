from turtle import pd

from prettytable import PrettyTable


mydictionar = dict()

def getage(val):
    return int(val[0])

def getvol(val):
    return int(val[2])

def parser():
    row =0
    flag=0
    #MP=MASCULINO PORTADOR DE DOENÇA
    mydictionar["MP"] = []
    mydictionar["FP"]=[]
    mydictionar["MI"] = []
    mydictionar["FI"] = []
    f = open("files/myheart.csv", "r")
    for i in f :
        flag=0
        if row ==0:
            row+=1
        else:
            row+=1
            k=i.split(",")
            if (int (k[0])<=0 or int (k[0])>=120 or int (k[2])==0 or int(k[3])==0 or int(k[4])==0 ):
                flag=1
            for aux in k:
                if not aux :
                 flag =1



            if (flag==0):
                tuple = (k[0],k[2],k[3],k[4])
                if (k[1] == "M" and k[5].strip("\n") =="0"):
                    mydictionar["MI"].append( tuple)
                if (k[1] == "M" and  k[5].strip("\n") == "1"):
                    mydictionar["MP"].append( tuple)
                if (k[1] == "F" and k[5].strip("\n") =="0"):
                    mydictionar["FI"].append( tuple)
                if (k[1] == "F" and  k[5].strip("\n") == "1"):
                    mydictionar['FP'].append( tuple)
    f.close();
#2time---------------------------------------------



def sexdist():
    masc = len(mydictionar["MP"])
    masc+= len(mydictionar["MI"])

    fem = len(mydictionar["FP"])
    fem += len(mydictionar["FI"])

    mp = len(mydictionar["MP"])
    mi = len(mydictionar["MI"])
    fp = len(mydictionar["FP"])
    fi = len(mydictionar["FI"])

    table = [[' ', 'Masculino', 'Feminino','TOTAL'], ["Portador ", mp, fp,mp+fp], ["Não Portador ",mi, fi,mi+fi],["TOTAL ",masc, fem,""]]
    tab = PrettyTable(table[0])
    tab.add_rows(table[1:])

    print(tab)

def ageinInterval(value,min,max):
    if (getage(value)>=min and getage(value)<=max) :
        return  True

    return False


def getpositives(min,max):
    count = 0
    for i in mydictionar["FP"]:
        if ageinInterval((i), min, max):
            count += 1
    for i in mydictionar["MP"]:
        if ageinInterval((i), min, max):
            count += 1
    return count
def getnegatives(min,max):
    count=0
    for i in mydictionar["FI"]:
        if ageinInterval((i),min,max):
            count+=1
    for i in mydictionar["MI"]:
        if ageinInterval((i),min,max):
            count+=1
    return count


def distidades():
 positotal=0
 negtotal = 0
 min=25

 table = [[' ', 'Portador', 'Não Portador']]

 while (min < 80):
        positotal+=getpositives(min, min + 4)
        negtotal += getnegatives(min, min + 4)
        table.append([f"[{min},{min + 4}]", getpositives(min, min + 4 ),getnegatives(min, min + 4 )])

        min += 5
 table.append(["TOTAL",positotal,negtotal])
 tab = PrettyTable(table[0])
 tab.add_rows(table[1:])
 print(tab)


def colesterolininterval(value,min,max):
    if (getvol(value)>=min and getvol(value)<=max) :
        return  True

    return False

def getpositivesbycolesterol(min,max):
    count = 0
    for i in mydictionar["FP"]:
        if colesterolininterval((i), min, max):
            count += 1
    for i in mydictionar["MP"]:
        if colesterolininterval((i), min, max):
            count += 1
    return count

def getnegativesbycolesterol(min,max):
    count=0
    for i in mydictionar["FI"]:
        if colesterolininterval((i),min,max):
            count+=1
    for i in mydictionar["MI"]:
        if colesterolininterval((i),min,max):
            count+=1
    return count
def distbycolesterol():
 min=0
 pos=0
 neg=0

 table = [[' ', 'Portador', 'Não Portador']]

 while (min < 620):
     pos += getpositives(min, min + 9)
     neg += getnegatives(min, min + 9)
     ## if  not (getpositivesbycolesterol(min, min + 9 )==0 and getnegativesbycolesterol(min, min + 9 )==0 ):
     table.append([f"[{min},{min + 9}]", getpositivesbycolesterol(min, min + 9 ),getnegativesbycolesterol(min, min + 9 )])

     min += 10
 table.append(["TOTAL", pos, neg])
 tab = PrettyTable(table[0])
 tab.add_rows(table[1:])
 print(tab)

if __name__ == '__main__':
    opcao =1
    parser()
    while (opcao!=4):
        print("-------------------TPC1-A96075--------------------------------")
        print("| 1-> Obter a distribuição da doença por sexo                |")
        print("| 2-> Obter a distribuição da doença por idade               |")
        print("| 3-> Obter a distribuição da doença por níveis de coleterol |")
        print("| 4->Sair                                                    |")

        print("|------------------------------------------------------------|")
        print("|Nota:Foram discartados os Registos invalidos nomeadamente   |")
        print("|os que possuem colesterol , tensão ou batimento a 0         |")
        print("--------------------------------------------------------------")
        opcao = input("Insira a opção que pretende realizar :\n")
        if (opcao =="1") :
            sexdist()
        elif (opcao == "2"):

            distidades()
        elif(opcao=="3"):

            distbycolesterol()
        else :
            break



