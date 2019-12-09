import pickle
import numpy as np

from itertools import combinations

import suggestions

X_N = pickle.load(open('Machine_model/pickleFile/X_N.pickle','rb'))
Y_N = pickle.load(open('Machine_model/pickleFile/Y_N.pickle','rb'))
Theta = pickle.load(open('Machine_model/pickleFile/Theta.pickle','rb'))

def norm(X):
	X_T = X.T

	for i in range(1,len(X_T)):
		for j in range(len(X_T[i])):
			X_T[i][j] = X_T[i][j]/X_N[i-1] 

	X_T = X_T.T

	return X_T

def statGen(mid,nameAr):
	xAr = suggestions.actFeSug(mid,nameAr)

	X_test = np.matrix(xAr[0])
	X_actu = np.matrix(xAr[1])

	X_test = norm(X_test)
	X_actu = norm(X_actu)

	X_temp1 = np.array(np.matmul(X_test,Theta)*Y_N[0])
	X_temp2 = np.array(np.matmul(X_actu,Theta)*Y_N[0])

	x1 = []
	x2 = []

	for i in range(len(X_temp1)):
		x1.append(X_temp1[i][0])
		x2.append(X_temp2[i][0])

	return x1,x2,xAr[2]

	# print(np.matmul(X_test,Theta)*Y_N[0])
	# print(np.matmul(X_actu,Theta)*Y_N[0])

#print(statGen('19SBTN06MAT',['Sujata Udapudi']))

def statGen2(mid,nameAr,eleName,acName):
	xAr = suggestions.actFe(mid,nameAr,eleName,acName)

	X_test = np.matrix(xAr[0])
	X_actu = np.matrix(xAr[1])

	X_test = norm(X_test)
	X_actu = norm(X_actu)

	X_temp1 = np.array(np.matmul(X_test,Theta)*Y_N[0])
	X_temp2 = np.array(np.matmul(X_actu,Theta)*Y_N[0])

	x1 = []
	x2 = []

	for i in range(len(X_temp1)):
		x1.append(X_temp1[i][0])
		x2.append(X_temp2[i][0])

	return x1,x2,xAr[2]

def suggStat(mid,nameAr,numBest,topVals,eleName,acName):
	numBest = int(numBest)
	topVals = int(topVals)

	if numBest > len(nameAr):
		numBest = len(nameAr)
	CombAr = list(combinations(nameAr, numBest))

	empD = {}

	for i in CombAr:
		dumAr = []
		retVal,_,actName = statGen2(mid,i,eleName,acName)
		lenAct = len(retVal)
		tempStr = '-'.join(i)
		if tempStr not in empD:
			empD[tempStr] = retVal

	finalAr = []

	for i in range(lenAct):
		tempDict = {}
		for j in empD:
			tempDict[j] = empD[j][i]
		finalAr.append(tempDict)

	if topVals > len(nameAr):
		topVals = len(nameAr)

	resAr = []
	for i in finalAr:
		falseAr = []
		i = sorted(i.items(), key=lambda kv: kv[1], reverse=False)
		resAr.append(i[:topVals])

	xFin = []
	yFin = []
	for i in resAr:
		xVal = []
		yVal = []
		for j in i:
			xVal.append(j[0])
			yVal.append(j[1])
		xFin.append(xVal)
		yFin.append(yVal)

		
	return xFin,yFin,actName


#ar = ['Anisha Sabu','Sunkari Sai Rakesh','Sujata Udapudi','Samyuktha Nethra Poojary','Deepa Manoj']
#print(suggStat('19SBTN06MAT',ar,2,2))


