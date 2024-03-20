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

