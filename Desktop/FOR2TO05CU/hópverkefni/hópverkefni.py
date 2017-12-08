#Bergur Ingi Ólafsson
#Kristberg Rúnar
#Hópverkefni í forritun Haust-Önn 2017
#22.11.2017
vidskiptavinir = []
Nafn = []

with open("bilaleiga.txt", "w", encoding="utf-8") as skra:
    skra.close
nafn = input("Settu nafnið þitt hér/Put your name here -->> ")
heimilisfang = input("Heimilisfang/Address -->>")
þjoderni = input("Þjóðerni/Country -->> ")
if þjoderni == "Ísland" and þjoderni == "ísland":
    kennitala = int(input("Kennitala -->> "))
    if len(kennitala) != 10:
        okuskirteinisnumer = int(input("Ökuskirteinisnumer/Driver license Number -->> "))
        simanumer = int(input("Símanumer/Phonenumber -->> "))
        tolvupostur = input("Tölvupóstur/E-mail -->> ")
        athugasemd = input("Athugasemd/Comment -->> ")
elif þjoderni != "Ísland" and þjoderni == "ísland":
    okuskirteinisnumer = int(input("Ökuskirteinisnumer/Driver license Number -->> "))
    simanumer = int(input("Símanumer/Phonenumber -->> "))
    tolvupostur = input("Tölvupóstur/E-mail -->> ")
    athugasemd = input("Athugasemd/Comment -->> ")

Nafn.append(nafn)
Nafn.append(heimilisfang)
Nafn.append(þjoderni)
Nafn.append(kennitala)
Nafn.append(okuskirteinisnumer)
Nafn.append(simanumer)
Nafn.append(tolvupostur)
Nafn.append(athugasemd)
vidskiptavinir.append(Nafn)
print(vidskiptavinir)
print(Nafn)

with open("bilaleiga.txt", "r", encoding="utf-8") as skra:
    skra = skra.read()
    for x in skra:
        print(x)
    listi = eval(skra)
    for x in listi:
        print(x,end=", ")

class Vidskiptavinur:
    def __init__(self, nafn, heimilisfang, kennitala, þjoderni, okuskirteinisNumer, simanumer, tolvupostur, athugasemd):
        self.nafn = nafn
        self.heimilisfang = heimilisfang
        self.kennitala = kennitala
        self.þjoderni = þjoderni
        self.okuskirteinisNumer = okuskirteinisNumer
        self.simanumer = simanumer
        self.tolvupostur = tolvupostur
        self.athugasemd = athugasemd

class Bilar:
    def __init__(self,tegund,framleidandi,fardegafjoldi, skraningarnumer, argerd, gerdbils, athugasemd):
        self.tegund = tegund
        self.framleidandi = framleidandi
        self.fardegafjoldi = fardegafjoldi
        self.skraningarnumer = skraningarnumer
        self.argerd = argerd
        self.gerdbils = gerdbils
        self.athugasemd = athugasemd



class Pantanir:
    def __init__(self, AudkenniVidskiptavinar, DagsBillPantadur, athugasemdPnt):
        self.AudkenniVidskiptaevinar = AudkenniVidskiptavinar
        self.DagsBillPantadur = DagsBillPantadur
        self.athugasemdPnt = athugasemdPnt

