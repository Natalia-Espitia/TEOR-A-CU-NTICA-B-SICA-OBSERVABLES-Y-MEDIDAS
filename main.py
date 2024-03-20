import numpy as np

def probab_pos(v, p):

    norma = np.linalg.norm(v) ** 2
    c = (abs(v[p])) ** 2

    return c / norma

print(probab_pos([-3 - 1j, -2j, 1j, 2], 2))

def probabilidad_transitar(v, k):

    nv = np.linalg.norm(v)
    nk = np.linalg.norm(k)
    i = 0
    while i < len(v):
        v[i] = v[i] / nv
        k[i] = k[i] / nk
        i += 1

    prod_in = 0
    i = 0
    while i < len(v):
        prod_in += np.conj(k[i]) * v[i]
        i += 1
    prod_v = nv * nk
    prob = prod_in / prod_v

    return prob

print(probabilidad_transitar([np.sqrt(2) / 2, np.sqrt(2) / 2, 0], [0, -np.sqrt(2) / 2, np.sqrt(2) / 2]))

def ampl_transicion(v1, v2):

    norma_v1 = np.linalg.norm(v1)
    norma_v2 = np.linalg.norm(v2)
    i = 0

    while i < len(v1):
        v1[i] = v1[i] / norma_v1
        i += 1

    i = 0
    while i < len(v2):
        v2[i] = v2[i] / norma_v2
        i += 1

    i = 0
    while i < len(v1):
        v1[i] = np.conj(v1[i])
        i += 1

    prod_in = 0
    i = 0
    while i < len(v1):
        prod_in += v1[i] * v2[i]
        i += 1

    return np.abs(prod_in) ** 2

print(ampl_transicion(np.array([1+2j, -3j, 4+1j]), np.array([5j, 2-1j, 3+4j])))


