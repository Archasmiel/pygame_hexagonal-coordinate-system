def get_connected_aspects(item):
    res = []
    for i in aspects:
        if (i.get_aspects()[0] is item) or (i.get_aspects()[1] is item):
            res.append(i)
    if item.first is not None:
        res.append(item.first)
    if item.second is not None:
        res.append(item.second)
    return res


class Aspect:
    """
        Aspect declaration class
    """

    def __init__(self, name: str, first=None, second=None):
        self.name = name
        self.first = first
        self.second = second
        self.basic = (first is None) and (second is None)

    def print_aspects(self):
        print(self.first.name, self.second.name)

    def get_aspects(self):
        return [self.first, self.second]

    def get_name(self):
        return self.name


# basic aspects
terra = Aspect("terra")
aqua = Aspect("aqua")
ignis = Aspect("ignis")
aer = Aspect("aer")
ordo = Aspect("ordo")
perditio = Aspect("perditio")

# 1-level aspect
victus = Aspect("victus", terra, aqua)
potentia = Aspect("potentia", ignis, ordo)
vacuos = Aspect("vacuos", aer, perditio)
motus = Aspect("motus", aer, ordo)
lux = Aspect("lux", ignis, aer)
gelum = Aspect("gelum", ignis, perditio)
vitreus = Aspect("vitreus", terra, ordo)
permutatio = Aspect("permutatio", ordo, perditio)
tempestus = Aspect("tempestus", aer, aqua)
venenum = Aspect("venenum", aqua, perditio)

# 2-nd level aspect
volatus = Aspect("volatus", motus, aer)
sano = Aspect("sano", victus, ordo)
mortuus = Aspect("motuus", victus, perditio)
herba = Aspect("herba", victus, terra)
praecantatio = Aspect("praecantatio", potentia, vacuos)
tenebrae = Aspect("tenebrae", vacuos, lux)
bestia = Aspect("bestia", motus, victus)
vinculum = Aspect("vinculum", motus, perditio)
fames = Aspect("fames", victus, vacuos)
iterAspect = Aspect("iter", motus, terra)
limus = Aspect("limus", victus, aqua)
metallum = Aspect("metallum", vitreus, terra)

# 3-rd level
vitium = Aspect("vitium", praecantatio, perditio)
superbia = Aspect("superbia", volatus, vacuos)
spiritus = Aspect("spiritus", victus, mortuus)
alienis = Aspect("alienis", vacuos, tenebrae)
arbor = Aspect("arbor", herba, aer)
auram = Aspect("auram", praecantatio, aer)
corpus = Aspect("corpus", bestia, mortuus)
exanimis = Aspect("exanimis", motus, mortuus)
gula = Aspect("gula", fames, vacuos)
infernus = Aspect("infernus", praecantatio, ignis)

# 4-th level
cognitio = Aspect("cognitio", spiritus, ignis)
desidia = Aspect("desidia", spiritus, vinculum)
exubitor = Aspect("exubitor", alienis, mortuus)
sensus = Aspect("sensus", spiritus, aer)
luxuria = Aspect("luxuria", corpus, fames)

# 5-th level
invidia = Aspect("invidia", fames, sensus)
humanus = Aspect("humanus", bestia, cognitio)

# 6-th level
perfodio = Aspect("perfodio", humanus, terra)
messis = Aspect("messis", herba, humanus)
instrumentum = Aspect("instrumentum", humanus, ordo)
lucrum = Aspect("lucrum", humanus, fames)

# 7-th level
tutamen = Aspect("tutamen", instrumentum, terra)
pannus = Aspect("pannus", instrumentum, bestia)
meto = Aspect("meto", messis, instrumentum)
machina = Aspect("machina", instrumentum, motus)
telum = Aspect("telum", instrumentum, ignis)
fabrico = Aspect("fabrico", humanus, instrumentum)

# 8-th level
ira = Aspect("ira", telum, ignis)

# Aspect list
aspects = [terra, aqua, ignis, aer, ordo, perditio, victus, potentia, vacuos, motus, lux, gelum, vitreus, permutatio,
           tempestus, venenum, volatus, sano, mortuus, herba, praecantatio, tenebrae, bestia, vinculum, fames,
           iterAspect, limus, metallum, vitium, superbia, spiritus, alienis, arbor, auram, corpus, exanimis, gula,
           infernus, cognitio, desidia, exubitor, sensus, luxuria, invidia, humanus, perfodio, messis, instrumentum,
           lucrum, tutamen, pannus, meto, machina, telum, fabrico, ira]
