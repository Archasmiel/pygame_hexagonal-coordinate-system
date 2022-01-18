import sys
from hexagonal_system.thaumcraft_aspects.aspects_io import *

# aer_connected = get_connected_aspects(aer)
# print([i.name for i in get_connected_aspects(herba)])
# print([i.name for i in get_connected_aspects(tenebrae)])
# print([i.name for i in get_connected_aspects(sensus)])
#
# combined1 = []
# combined2 = []
# combined3 = []


def get_connections_between(aspect1: Aspect, aspect2: Aspect, blank_hexes: int):
    for i1 in connections[blank_hexes - 1]:
        if i1[0] is aspect1 and i1[blank_hexes + 1] is aspect2:
            summ = 0
            res = []
            for ind, i2 in enumerate(i1):
                summ += i2.level
                res.append(i2.name)
            print(res, summ)
    print('\n\n\n', end='')


def extend_list(main: list, aux: list):
    res = []
    for i in main:
        res.append(i)
    for i in aux:
        res.append(i)
    return res


def read_connections(num: int) -> list:
    res = []
    f = open(f'connections{num}.txt', 'r')
    for temp in f:
        asps = [get_aspect_by_name(k) for k in temp.strip().split(' ')]
        res.append(asps)
    return res


def print_connections(num: int, arr: list):
    f = open(f'connections{num}.txt', 'w')
    for temp in arr:
        f.write(f'{"".join([i2.name + " " for i2 in temp])}\n')


def gen_connections_1empty() -> list:
    res = []
    for i in aspects:
        for j in aspects:
            i_c = get_connected_aspects(i, (True, True))
            j_c = get_connected_aspects(j, (True, True))
            for k in i_c:
                for l in j_c:
                    if k is l:
                        res.append([i, k, j])
    return res


def gen_connections_1empty_aspects(aspect1: Aspect, aspect2: Aspect) -> list:
    res = []
    i_c = get_connected_aspects(aspect1, (True, True))
    j_c = get_connected_aspects(aspect2, (True, True))
    for k in i_c:
        for l in j_c:
            if k is l:
                res.append([aspect1, k, aspect2])
    return res


def gen_connections_2empty() -> list:
    res = []
    for i in aspects:
        for j in aspects:
            i_c = get_connected_aspects(i, (True, True))
            for k in i_c:
                for m in connections_1empty:
                    if (m[0] is k) and (m[2] is j):
                        res.append(extend_list([i], m))
    return res


def gen_connections_2empty_aspects(aspect1: Aspect, aspect2: Aspect) -> list:
    res = []
    i_c = get_connected_aspects(aspect1, (True, True))
    for k in i_c:
        for m in connections_1empty:
            if (m[0] is k) and (m[2] is aspect2):
                res.append(extend_list([aspect1], m))
    return res


def gen_connections_3empty() -> list:
    res = []
    for i in aspects:
        for j in aspects:
            i_c = get_connected_aspects(i, (True, True))
            for k in i_c:
                for m in connections_2empty:
                    if (m[0] is k) and (m[3] is j):
                        res.append(extend_list([i], m))
    return res


def gen_connections_3empty_aspects(aspect1: Aspect, aspect2: Aspect) -> list:
    res = []
    i_c = get_connected_aspects(aspect1, (True, True))
    for k in i_c:
        for m in connections_2empty:
            if (m[0] is k) and (m[3] is aspect2):
                res.append(extend_list([aspect1], m))
    return res


def gen_connections_4empty() -> list:
    res = []
    for i in aspects:
        for j in aspects:
            i_c = get_connected_aspects(i, (True, True))
            for k in i_c:
                for m in connections_3empty:
                    if (m[0] is k) and (m[4] is j):
                        res.append(extend_list([i], m))
    return res


def gen_connections_4empty_aspects(aspect1: Aspect, aspect2: Aspect) -> list:
    res = []
    i_c = get_connected_aspects(aspect1, (True, True))
    for k in i_c:
        for m in connections_3empty:
            if (m[0] is k) and (m[4] is aspect2):
                res.append(extend_list([aspect1], m))
    return res


# ==================================================================
# print()
# connections_1empty = gen_connections_1empty()
# print_connections(1, connections_1empty)
# ----------------------------------------
connections_1empty = read_connections(1)
# print(sys.getsizeof(connections_1empty)/1024)
# print(len(connections_1empty))
# for i1 in connections_1empty:
#     print(''.join([i2.name + ' ' for i2 in i1]))

# ==================================================================
# print()
# connections_2empty = gen_connections_2empty()
# print_connections(2, connections_2empty)
# ----------------------------------------
connections_2empty = read_connections(2)
# print(sys.getsizeof(connections_2empty)/1024)
# print(len(connections_2empty))
# for i1 in connections_2empty:
#     print(''.join([i2.name + ' ' for i2 in i1]))

# ==================================================================
# print()
# connections_3empty = gen_connections_3empty()
# print_connections(3, connections_3empty)
# ----------------------------------------
connections_3empty = read_connections(3)
# print(sys.getsizeof(connections_3empty)/1024)
# print(len(connections_3empty))
# for i1 in connections_3empty:
#     print(''.join([i2.name + ' ' for i2 in i1]))

# ==================================================================
# print()
# connections_4empty = gen_connections_4empty()
# print_connections(4, connections_4empty)
# ----------------------------------------
connections_4empty = read_connections(4)
# print(sys.getsizeof(connections_4empty)/1024)
# print(len(connections_4empty))
# for i1 in connections_4empty:
#     print(''.join([i2.name + ' ' for i2 in i1]))

connections = [connections_1empty,
               connections_2empty,
               connections_3empty,
               connections_4empty]


asp1, asp2 = machina, praecantatio
get_connections_between(asp1, asp2, 4)

asp1, asp2 = machina, aqua
get_connections_between(asp1, asp2, 4)

asp1, asp2 = aqua, permutatio
get_connections_between(asp1, asp2, 4)

asp1, asp2 = auram, praecantatio
get_connections_between(asp1, asp2, 4)


# read_connections_1empty()


print(aspect_to_basic(exanimis, True))
print(aspect_to_basic(ira, True))

# print([i.name for i in get_connected_aspects(humanus, False, True)])

# for j in get_connected_aspects(sensus):
#     combined1.extend(get_connected_aspects(j))
# for j in get_connected_aspects(ordo):
#     combined2.extend(get_connected_aspects(j))
#
#
# print([i.name for i in get_connected_aspects(fames)])
# for i in aspects:
#     if (i in combined2) and (i in combined3):
#         print(i.name)
