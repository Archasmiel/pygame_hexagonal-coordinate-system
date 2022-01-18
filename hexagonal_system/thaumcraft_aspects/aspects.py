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

    def get_aspects(self):
        return [self.first, self.second]


# no aspect
current_level = -1
aspect_none = Aspect("noneobj", None, None, level=current_level)

# basic aspects
current_level = 0
terra = Aspect("terra", None, None, level=current_level)
aqua = Aspect("aqua", None, None, level=current_level)
ignis = Aspect("ignis", None, None, level=current_level)
aer = Aspect("aer", None, None, level=current_level)
ordo = Aspect("ordo", None, None, level=current_level)
perditio = Aspect("perditio", None, None, level=current_level)

# 1-level aspect
current_level = 1
victus = Aspect("victus", terra, aqua, level=current_level)
potentia = Aspect("potentia", ignis, ordo, level=current_level)
vacuos = Aspect("vacuos", aer, perditio, level=current_level)
motus = Aspect("motus", aer, ordo, level=current_level)
lux = Aspect("lux", ignis, aer, level=current_level)
gelum = Aspect("gelum", ignis, perditio, level=current_level)
vitreus = Aspect("vitreus", terra, ordo, level=current_level)
permutatio = Aspect("permutatio", ordo, perditio, level=current_level)
tempestus = Aspect("tempestus", aer, aqua, level=current_level)
venenum = Aspect("venenum", aqua, perditio, level=current_level)

# 2-nd level aspect
current_level = 2
volatus = Aspect("volatus", motus, aer, level=current_level)
sano = Aspect("sano", victus, ordo, level=current_level)
mortuus = Aspect("mortuus", victus, perditio, level=current_level)
herba = Aspect("herba", victus, terra, level=current_level)
praecantatio = Aspect("praecantatio", potentia, vacuos, level=current_level)
tenebrae = Aspect("tenebrae", vacuos, lux, level=current_level)
bestia = Aspect("bestia", motus, victus, level=current_level)
vinculum = Aspect("vinculum", motus, perditio, level=current_level)
fames = Aspect("fames", victus, vacuos, level=current_level)
iterAspect = Aspect("iter", motus, terra, level=current_level)
limus = Aspect("limus", victus, aqua, level=current_level)
metallum = Aspect("metallum", vitreus, terra, level=current_level)

# 3-rd level
current_level = 3
vitium = Aspect("vitium", praecantatio, perditio, level=current_level)
superbia = Aspect("superbia", volatus, vacuos, level=current_level)
spiritus = Aspect("spiritus", victus, mortuus, level=current_level)
alienis = Aspect("alienis", vacuos, tenebrae, level=current_level)
arbor = Aspect("arbor", herba, aer, level=current_level)
auram = Aspect("auram", praecantatio, aer, level=current_level)
corpus = Aspect("corpus", bestia, mortuus, level=current_level)
exanimis = Aspect("exanimis", motus, mortuus, level=current_level)
gula = Aspect("gula", fames, vacuos, level=current_level)
infernus = Aspect("infernus", praecantatio, ignis, level=current_level)

# 4-th level
current_level = 4
cognitio = Aspect("cognitio", spiritus, ignis, level=current_level)
desidia = Aspect("desidia", spiritus, vinculum, level=current_level)
exubitor = Aspect("exubitor", alienis, mortuus, level=current_level)
sensus = Aspect("sensus", spiritus, aer, level=current_level)
luxuria = Aspect("luxuria", corpus, fames, level=current_level)

# 5-th level
current_level = 5
invidia = Aspect("invidia", fames, sensus, level=current_level)
humanus = Aspect("humanus", bestia, cognitio, level=current_level)

# 6-th level
current_level = 6
perfodio = Aspect("perfodio", humanus, terra, level=current_level)
messis = Aspect("messis", herba, humanus, level=current_level)
instrumentum = Aspect("instrumentum", humanus, ordo, level=current_level)
lucrum = Aspect("lucrum", humanus, fames, level=current_level)

# 7-th level
current_level = 7
tutamen = Aspect("tutamen", instrumentum, terra, level=current_level)
pannus = Aspect("pannus", instrumentum, bestia, level=current_level)
meto = Aspect("meto", messis, instrumentum, level=current_level)
machina = Aspect("machina", instrumentum, motus, level=current_level)
telum = Aspect("telum", instrumentum, ignis, level=current_level)
fabrico = Aspect("fabrico", humanus, instrumentum, level=current_level)

# 8-th level
current_level = 8
ira = Aspect("ira", telum, ignis, level=current_level)

# all aspects list
aspects = [terra, aqua, ignis, aer, ordo, perditio,
           victus, potentia, vacuos, motus, lux, gelum, vitreus, permutatio, tempestus, venenum,
           volatus, sano, mortuus, herba, praecantatio, tenebrae, bestia, vinculum, fames, iterAspect, limus, metallum,
           vitium, superbia, spiritus, alienis, arbor, auram, corpus, exanimis, gula, infernus,
           cognitio, desidia, exubitor, sensus, luxuria,
           invidia, humanus,
           perfodio, messis, instrumentum, lucrum,
           tutamen, pannus, meto, machina, telum, fabrico,
           ira]

basic = [terra, aqua, ignis, aer, ordo, perditio]
