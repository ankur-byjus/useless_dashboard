import xlrd

import pickle

from xlwt import Workbook

userSub = pickle.load(open('pickleFile/userSub.pickle','rb'))
userGr = pickle.load(open('pickleFile/userScore.pickle','rb'))
userElement = pickle.load(open('pickleFile/userElement.pickle','rb'))
userAction = pickle.load(open('pickleFile/userAction.pickle','rb'))

fileName = 'Sheets/actMid.xls'

wb = Workbook()

workbook = xlrd.open_workbook(fileName,on_demand = True)
worksheet = workbook.sheet_by_index(0)
nRows = worksheet.nrows

arY = []
arX = []

for i in range(1,nRows):
	try:
		
		dumX = [1]
		for j in range(3,10):
			if j != 5:
				dumX.append(worksheet.cell(i,j).value)

		dumStr = worksheet.cell(i,2).value.replace('[','')
		dumStr = dumStr.replace(']','')
		dumStr = dumStr.replace("'",'')
		dumStr = dumStr.split(",")

		dumGr = worksheet.cell(i,0).value[6:8]
		dumSub = worksheet.cell(i,0).value[8:11]

		actName = worksheet.cell(i,1).value.split('_')

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

		dumX.append(dumSubFe)
		dumX.append(dumGrFe)
		dumX.append(dumEle)
		dumX.append(dumAc)

		arX.append(dumX)
		arY.append([worksheet.cell(i,5).value])
	except Exception as e:
		print(e)

pickle_out = open("pickleFile/Y.pickle","wb")
pickle.dump(arY,pickle_out)
pickle_out.close()

pickle_out = open("pickleFile/X.pickle","wb")
pickle.dump(arX,pickle_out)
pickle_out.close()