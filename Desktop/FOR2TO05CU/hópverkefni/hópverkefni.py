#Bergur Ingi Ólafsson
#Kristberg Rúnar
#Hópverkefni í forritun Haust-Önn 2017
#22.11.2017

class Bilar:
    def __init__(self, skraningarnumer, argerd, gerdbils, athugasemd):
        self.skraningarnumer = skraningarnumer
        self.argerd = argerd
        self.gerdbils = gerdbils
        self.athugasemd = athugasemd

class Pantanir:
    def __init__(self, AudkenniVidskiptavinar, DagsBillPantadur, athugasemdPnt):
        self.AudkenniVidskiptaevinar = AudkenniVidskiptavinar
        self.DagsBillPantadur = DagsBillPantadur
        self.athugasemdPnt = athugasemdPnt