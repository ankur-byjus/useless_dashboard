from itertools import combinations
import pickle
import suggestionStat
import suggestions

import numpy as np

empNames = pickle.load(open('Machine_model/pickleFile/userElement.pickle','rb'))
X_N = pickle.load(open('Machine_model/pickleFile/X_N.pickle','rb'))
Y_N = pickle.load(open('Machine_model/pickleFile/Y_N.pickle','rb'))
Theta = pickle.load(open('Machine_model/pickleFile/Theta.pickle','rb'))

empAr = []

for i in empNames:
	empAr.append(i)

def possSugg(mid,eleName,acName,numEmp,days,partialMem):
	dayDict = {}
	for i in empAr:
		X_test,_,_ = suggestionStat.statGen2(mid,[i],eleName,acName)
		dayDict[i] = X_test
	sortedDays = sorted(dayDict.items(), key=lambda kv: kv[1], reverse=False)

	bestEmp = []
	for i in range(numEmp):
		bestEmp.append(sortedDays[i][0])

	finX,_,_,workFolks = suggestions.actFe(mid,bestEmp,eleName,acName)
	finX = np.matrix(finX)
	finX = suggestionStat.norm(finX)
	finX = np.array(finX)
	finX[0][5] = partialMem

	tempVal1 = 0

	for i in range(len(finX[0])):
		if i != 2:
			tempVal1 += (finX[0][i]*Theta[i][0])*Y_N[0]

	if tempVal1 <= days:
		return 0
	else:
		reqXpWq = (days-tempVal1)/(Theta[2][0]*Y_N[0])
		result = ((reqXpWq*X_N[1])*(workFolks[0]+(days*numEmp)))-((finX[0][2]*X_N[1])*workFolks[0])
		result = result/(days*numEmp)
	result = np.array(result)
	return result[0][0]

#possSugg('19SBTN','Management','Strategy/Planning',2,16,1.064329203)


