import pickle
import numpy as np

X = pickle.load(open('pickleFile/X.pickle','rb'))
Y = pickle.load(open('pickleFile/Y.pickle','rb'))

X = np.matrix(X)
Y = np.matrix(Y)

print(X)

X_T = X.T

X_N = []
Y_N = []

for i in range(1,len(X_T)):
    X_max = X_T[i].max()
    X_max = str(X_max)
    X_max = X_max.split('.')
    X_max = X_max[0]

    normNum = 1

    for j in X_max:
        normNum *= 10

    X_N.append(normNum)

    for j in range(len(X_T[i])):
        X_T[i][j] = (X_T[i][j]/normNum)

X = X_T.T

m = len(X)
Y_max = Y.max()

def norm(matVal):
    m = len(Y)
    
    Y_max_1 = str(Y_max)
    Y_max_1 = Y_max_1.split('.')
    Y_max_1 = Y_max_1[0]

    normNum = 1

    for i in Y_max_1:
        normNum *= 10

    Y_N.append(normNum)

    for i in range(m):
        Y[i][0] = (Y[i][0]/normNum)

    return Y,Y_N

Y_dum = norm(Y)
normY = Y_dum[1]
Y = Y_dum[0]

#print(np.matmul((np.linalg.inv(np.matmul(X.T,X))),X.T))
#print(X.shape,Y.shape)

Theta = np.matmul(np.matmul((np.linalg.inv(np.matmul(X.T,X))),X.T),Y)

print(Theta)

#alpha = 0.000050

predictedVal = np.matmul(X,Theta)

print((np.sum(np.square(X*Theta - Y))))
J = (1/(2*m))*np.sum(np.square(X*Theta - Y))

Y_P = X*Theta

for i in range(len(Y)):
	print(Y[i][0]*normY[0],Y_P[i][0]*normY[0])

pickle_out = open("pickleFile/Theta.pickle","wb")
pickle.dump(Theta,pickle_out)
pickle_out.close()

pickle_out = open("pickleFile/X_N.pickle","wb")
pickle.dump(X_N,pickle_out)
pickle_out.close()

pickle_out = open("pickleFile/Y_N.pickle","wb")
pickle.dump(Y_N,pickle_out)
pickle_out.close()

