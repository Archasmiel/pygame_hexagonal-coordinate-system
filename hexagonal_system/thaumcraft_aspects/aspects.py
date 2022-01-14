class Aspect:
    """
        Aspect declaration class
    """

    def __init__(self, name: str, first, second, level):
        self.name = name
        self.first = first
        self.second = second
        self.basic = (first is None) and (second is None)
        self.level = level

    # def print_aspects(self):
    #     print(self.first.name, self.second.name)
    #
    # def get_aspects(self):
    #     return [self.first, self.second]
    #
    # def get_name(self):
    #     return self.name


# basic aspects
terra = Aspect("terra", None, None, level=0)
aqua = Aspect("aqua", None, None, level=0)
ignis = Aspect("ignis", None, None, level=0)
aer = Aspect("aer", None, None, level=0)
ordo = Aspect("ordo", None, None, level=0)
perditio = Aspect("perditio", None, None, level=0)

# 1-level aspect
victus = Aspect("victus", terra, aqua, level=1)
potentia = Aspect("potentia", ignis, ordo, level=1)
vacuos = Aspect("vacuos", aer, perditio, level=1)
motus = Aspect("motus", aer, ordo, level=1)
lux = Aspect("lux", ignis, aer, level=1)
gelum = Aspect("gelum", ignis, perditio, level=1)
vitreus = Aspect("vitreus", terra, ordo, level=1)
permutatio = Aspect("permutatio", ordo, perditio, level=1)
tempestus = Aspect("tempestus", aer, aqua, level=1)
venenum = Aspect("venenum", aqua, perditio, level=1)

# 2-nd level aspect
volatus = Aspect("volatus", motus, aer, level=2)
sano = Aspect("sano", victus, ordo, level=2)
mortuus = Aspect("motuus", victus, perditio, level=2)
herba = Aspect("herba", victus, terra, level=2)
praecantatio = Aspect("praecantatio", potentia, vacuos, level=2)
tenebrae = Aspect("tenebrae", vacuos, lux, level=2)
bestia = Aspect("bestia", motus, victus, level=2)
vinculum = Aspect("vinculum", motus, perditio, level=2)
fames = Aspect("fames", victus, vacuos, level=2)
iterAspect = Aspect("iter", motus, terra, level=2)
limus = Aspect("limus", victus, aqua, level=2)
metallum = Aspect("metallum", vitreus, terra, level=2)

# 3-rd level
vitium = Aspect("vitium", praecantatio, perditio, level=3)
superbia = Aspect("superbia", volatus, vacuos, level=3)
spiritus = Aspect("spiritus", victus, mortuus, level=3)
alienis = Aspect("alienis", vacuos, tenebrae, level=3)
arbor = Aspect("arbor", herba, aer, level=3)
auram = Aspect("auram", praecantatio, aer, level=3)
corpus = Aspect("corpus", bestia, mortuus, level=3)
exanimis = Aspect("exanimis", motus, mortuus, level=3)
gula = Aspect("gula", fames, vacuos, level=3)
infernus = Aspect("infernus", praecantatio, ignis, level=3)

# 4-th level
cognitio = Aspect("cognitio", spiritus, ignis, level=4)
desidia = Aspect("desidia", spiritus, vinculum, level=4)
exubitor = Aspect("exubitor", alienis, mortuus, level=4)
sensus = Aspect("sensus", spiritus, aer, level=4)
luxuria = Aspect("luxuria", corpus, fames, level=4)

# 5-th level
invidia = Aspect("invidia", fames, sensus, level=5)
humanus = Aspect("humanus", bestia, cognitio, level=5)

# 6-th level
perfodio = Aspect("perfodio", humanus, terra, level=6)
messis = Aspect("messis", herba, humanus, level=6)
instrumentum = Aspect("instrumentum", humanus, ordo, level=6)
lucrum = Aspect("lucrum", humanus, fames, level=6)

# 7-th level
tutamen = Aspect("tutamen", instrumentum, terra, level=7)
pannus = Aspect("pannus", instrumentum, bestia, level=7)
meto = Aspect("meto", messis, instrumentum, level=7)
machina = Aspect("machina", instrumentum, motus, level=7)
telum = Aspect("telum", instrumentum, ignis, level=7)
fabrico = Aspect("fabrico", humanus, instrumentum, level=7)

# 8-th level
ira = Aspect("ira", telum, ignis, level=8)

