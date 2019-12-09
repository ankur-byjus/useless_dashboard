import xlrd
import pickle
import pandas as pd

df = pd.read_excel(r'Machine_model/Sheets/actMid.xls')

fileName = 'Machine_model/Sheets/actMid.xls'

workbook = xlrd.open_workbook(fileName,on_demand = True)
worksheet = workbook.sheet_by_index(0)
nRows = worksheet.nrows

userSub = pickle.load(open('Machine_model/pickleFile/userSub.pickle','rb'))
userGr = pickle.load(open('Machine_model/pickleFile/userScore.pickle','rb'))
userElement = pickle.load(open('Machine_model/pickleFile/userElement.pickle','rb'))
userAction = pickle.load(open('Machine_model/pickleFile/userAction.pickle','rb'))

def actFe(mid,nameAr,eleName,acName):
	X_test = []
	X_actu = []
	tempActivity = []
	workFolks = []

	for i in range(1,nRows):
		tempEA = worksheet.cell(i,1).value.split('_')
		if eleName == tempEA[-2] and acName == tempEA[-1] and worksheet.cell(i,0).value == mid:
			#print(tempEA[-2],tempEA[-1],worksheet.cell(i,0).value,i)
			tempAr = [1]
			tempAr1 = [1]
			workFolks.append(worksheet.cell(i,10).value)
			for j in range(3,10):
				if j != 5:
					tempAr.append(worksheet.cell(i,j).value)
					tempAr1.append(worksheet.cell(i,j).value)
			tempActivity.append(worksheet.cell(i,1).value)

			dumStr =worksheet.cell(i,2).value.replace('[','')
			dumStr = dumStr.replace(']','')
			dumStr = dumStr.replace("'",'')
			dumStr = dumStr.split(",")

			dumGr = worksheet.cell(i,0).value[6:8]
			dumSub = worksheet.cell(i,0).value[8:11]

			# actName = dff.iat[i,1].split('_')

			# eleName = actName[-2]
			# acName = actName[-1]

			dumSubFe = 0
			dumGrFe = 0
			dumEle = 0
			dumAc = 0

			for j in dumStr:
				j = j.strip()
				if dumSub != '':
					dumSubFe += userSub[j][dumSub]
				if dumGr != '':
					dumGrFe +=  userGr[j][dumGr]
				dumEle += userElement[j][eleName]
				dumAc += userAction[j][acName]

			tempAr1.append(dumSubFe)
			tempAr1.append(dumGrFe)
			tempAr1.append(dumEle)
			tempAr1.append(dumAc)

			X_actu.append(tempAr1)

			dumSubFe = 0
			dumGrFe = 0
			dumEle = 0
			dumAc = 0

			for j in nameAr:
				j = j.strip()
				if dumSub != '':
					dumSubFe += userSub[j][dumSub]
				if dumGr != '':
					dumGrFe +=  userGr[j][dumGr]
				dumEle += userElement[j][eleName]
				dumAc += userAction[j][acName]

			tempAr[-2] = len(nameAr)
			tempAr.append(dumSubFe)
			tempAr.append(dumGrFe)
			tempAr.append(dumEle)
			tempAr.append(dumAc)

			X_test.append(tempAr)

	return X_test,X_actu,tempActivity,workFolks

def actFeSug(mid,nameAr):
	X_test = []
	X_actu = []
	tempActivity = []

	dff = df[df['MIDS'] == mid]

	s = dff.shape

	for i in range(s[0]):
		tempAr = [1]
		tempAr1 = [1]
		for j in range(3,10):
			if j != 5:
				tempAr.append(dff.iat[i,j])
				tempAr1.append(dff.iat[i,j])
		tempActivity.append(dff.iat[i,1])

		dumStr = dff.iat[i,2].replace('[','')
		dumStr = dumStr.replace(']','')
		dumStr = dumStr.replace("'",'')
		dumStr = dumStr.split(",")

		dumGr = dff.iat[i,0][6:8]
		dumSub = dff.iat[i,0][8:11]

		actName = dff.iat[i,1].split('_')

		eleName = actName[-2]
		acName = actName[-1]

		dumSubFe = 0
		dumGrFe = 0
		dumEle = 0
		dumAc = 0

		for j in dumStr:
			j = j.strip()
			if dumSub != '':
				dumSubFe += userSub[j][dumSub]
			if dumGr != '':
				dumGrFe +=  userGr[j][dumGr]
			dumEle += userElement[j][eleName]
			dumAc += userAction[j][acName]

		tempAr1.append(dumSubFe)
		tempAr1.append(dumGrFe)
		tempAr1.append(dumEle)
		tempAr1.append(dumAc)

		X_actu.append(tempAr1)

		dumSubFe = 0
		dumGrFe = 0
		dumEle = 0
		dumAc = 0

		for j in nameAr:
			j = j.strip()
			if dumSub != '':
				dumSubFe += userSub[j][dumSub]
			if dumGr != '':
				dumGrFe +=  userGr[j][dumGr]
			dumEle += userElement[j][eleName]
			dumAc += userAction[j][acName]

		tempAr[-2] = -(len(nameAr))
		tempAr.append(dumSubFe)
		tempAr.append(dumGrFe)
		tempAr.append(dumEle)
		tempAr.append(dumAc)

		X_test.append(tempAr)

	return X_test,X_actu,tempActivity

#actFe('19SBTN06MAT',['Sujata Udapudi'])




