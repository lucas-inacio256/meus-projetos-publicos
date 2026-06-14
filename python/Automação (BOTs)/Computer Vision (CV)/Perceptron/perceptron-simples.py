import numpy as np

numEpocas = 100000
q = 6

peso = np.array([113, 122, 107, 98, 115, 120])
pH = np.array([6.8, 4.7, 5.2, 3.6, 2.9, 4.2])

bias = 1
x = np.vstack((peso, pH))
y = np.array([-1, 1, -1, -1, 1, 1])

eta = 0.1

w = np.zeros([1, 3])

e = np.zeros(6)

def funcAtivacao(value):
    if value < 0.0:
        return -1
    else:
        return  1

for i in range(numEpocas):
    for t in range(q):
        xb = np.hstack((bias, x[:,t]))

        v = np.dot(w, xb)

        yr = funcAtivacao(v)

        e[t] = y[t] - yr

        w = w + eta * e[t] * xb

print('Vetor de erros (e) = ' + str(e))
