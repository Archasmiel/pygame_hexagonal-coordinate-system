fi = open('in.txt', 'r')
fo = open('out.txt', 'w')
for i in fi:
    fo.write(f'aspects.append({i.split(" ")[0]})\n')
