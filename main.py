import numpy as np
# 1. El sistema debe calcular la probabilidad de encontrarlo en una posición en particular.
def probab_pos(v, p):

    norma = np.linalg.norm(v) ** 2
    c = (abs(v[p])) ** 2

    return c / norma

print(probab_pos([-3 - 1j, -2j, 1j, 2], 2))
# 2. El sistema si se le da otro vector Ket debe buscar la probabilidad de transitar del primer vector al segundo.
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
# 1. Amplitud de transición. El sistema puede recibir dos vectores y calcular la probabilidad de transitar de el uno al otro después de hacer la observación
def amplitud_transicion(v1, v2):

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

print(amplitud_transicion(np.array([1, 2j, -3j]), np.array([0, 1+1j, 3-4j])))
# 2. Ahora con una matriz que describa un observable y un vector ket, el sistema revisa que la matriz sea hermitiana, y si lo es, calcula la media y la varianza del observable en el estado dado.
def hermitiana_media_varianza(m,v):

    def b(v):
        for i in range(len(v)):
            v[i] = v[i].conjugate()
        return v

    def accion(v, m):
        ans = [0] * len(m)
        for i in range(len(m)):
            aux = 0
            for j in range(len(m[i])):
                aux += m[i][j] * v[j]
            ans[i] = aux
        return ans

    def prod_inter(v1, v2):
        ans = 0
        for i in range(len(v1)):
            v1[i] = v1[i].conjugate()
            ans += v1[i] * v2[i]
        return ans

    def prod_mat(m1, m2):
            ans = [[0 for j in range(len(m2[0]))] for i in range(len(m1))]
            for i in range(len(m1)):
                for j in range(len(m2[0])):
                    aux = 0
                    for k in range(len(m2)):
                        aux = m1[i][k] * m2[k][j]
                    ans[i][j] = aux
            return ans
    b_v=b(v)
    ax_v=accion(v,m)
    media=prod_inter(ax_v,b_v)
    matri=[[media * -1 for i in range(len(m[0]))] for j in range(len(m))]
    for i in range(len(m)):
        for j in range(len(m)):
            matri[i][j] += m[i][j]
    matriz=prod_mat(matri,matri)
    var=prod_inter(accion(v,matriz),b_v)
    return media,var

m = [[1, 2+1j, 3], [2-1j, 4, 5+2j], [3, 5-2j, 6]]
v = [1, 2, 3]
media, varianza = hermitiana_media_varianza(m, v)

print("La media es:", media)
print("La varianza es:", varianza)
# 3. El sistema calcula los valores propios del observable y la probabilidad de que el sistema transite a alguno de los vectores propios después de la observación.

# 4. Se considera la dinámica del sistema. Ahora con una serie de matrices Un el sistema calcula el estado final a partir de un estado inicial.
# Ejercicio 4.3.1
# Ejercicio 4.3.2
# Ejercicio 4.4.1
def mat_unitaria(matrix):
    return True

def multmatrices(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

def ejercicio_4_4_1(u1, u):
    if mat_unitaria(u1) and mat_unitaria(u):
        answer = multmatrices(u1, u)
        if mat_unitaria(answer):
            return True
    return False

u1 = np.array([[0, 1], [1, 0]])
u = np.array([[np.sqrt(2)/2, np.sqrt(2)/2], [np.sqrt(2)/2, -np.sqrt(2)/2]])
resultado = ejercicio_4_4_1(u1, u)

if resultado:
    print("Las matrices y su producto son unitarios.")
else:
    print("Al menos una de las matrices o su producto no es unitario.")
# Ejercicio 4.4.2


