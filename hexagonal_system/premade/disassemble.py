from hexagonal_system.premade.aspects import *

fi = open('in.txt', 'r')
fo = open('out.txt', 'w')
for i in fi:
    fo.write(f'aspects.append({i.split(" ")[0]})\n')

aer_connected = get_connected_aspects(aer)
print([i.name for i in get_connected_aspects(herba)])
print([i.name for i in get_connected_aspects(tenebrae)])
print([i.name for i in get_connected_aspects(sensus)])

combined1 = []
combined2 = []
combined3 = []
for j in get_connected_aspects(sensus):
    combined1.extend(get_connected_aspects(j))
for j in get_connected_aspects(ordo):
    combined2.extend(get_connected_aspects(j))


print([i.name for i in get_connected_aspects(fames)])
for i in aspects:
    if (i in combined2) and (i in combined3):
        print(i.name)
