from hexagonal_system.thaumcraft_aspects.aspects import *


aspects = [terra, aqua, ignis, aer, ordo, perditio,
           victus, potentia, vacuos, motus, lux, gelum, vitreus, permutatio, tempestus, venenum,
           volatus, sano, mortuus, herba, praecantatio, tenebrae, bestia, vinculum, fames, iterAspect, limus, metallum,
           vitium, superbia, spiritus, alienis, arbor, auram, corpus, exanimis, gula, infernus,
           cognitio, desidia, exubitor, sensus, luxuria,
           invidia, humanus,
           perfodio, messis, instrumentum, lucrum,
           tutamen, pannus, meto, machina, telum, fabrico,
           ira]


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
