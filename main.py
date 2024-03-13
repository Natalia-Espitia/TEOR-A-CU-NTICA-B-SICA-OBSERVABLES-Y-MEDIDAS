import numpy as np

def probab_pos(v, p):
    norma = np.linalg.norm(v) ** 2
    c = (abs(v[p])) ** 2
    return c / norma

def probab_transitar(v, k):
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

print(probab_pos([-3 - 1j, -2j, 1j, 2], 2))
print(probab_transitar([1, 2, 3, 4, 2], [9, 1, 8, 7, 6]))

def transicion(v1,v2):

    norma_v1=np.linalg.norm(v1)
    for i in range(len(v1)):
        v1[i]=v1[i]/norma_v1
        return v1
    norma_v2= np.linalg.norm(v2)
    for i in range(len(v2)):
        v2[i] = v2[i] / norma_v2
        return v2


    for i in range(len(v1)):
        v1[i] = v1[i].conjugate()
        interno=np.inner(v1,v2)
    return interno

print(transicion([1,2,3],[4,5,6]))

