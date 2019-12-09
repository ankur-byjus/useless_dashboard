import xlrd
import pickle

from xlwt import Workbook

fileName = 'Tamil_nadu_data.xlsx'

workbook = xlrd.open_workbook(fileName,on_demand = True)
worksheet = workbook.sheet_by_name('Sheet1')
nRows = worksheet.nrows

year = {}
tyBoard = {}
gr = {}
sb = {}
ch = {}

Proj = {}
cat = {}
acEle = {}
acAct = {}

ProjF = {}
catF = {}
acEleF = {}
acActF = {}

yearD = {}
tyBoardD = {}
grD = {}
sbD = {}
chD = {}

ProjD = {}
catD = {}
acEleD = {}
acActD = {}

Dates = []

for i in range(1,nRows):
	if worksheet.cell(i,9).value[0:2] not in year:
		year[worksheet.cell(i,9).value[0:2]] = 0
	year[worksheet.cell(i,9).value[0:2]] += worksheet.cell(i,10).value

	if worksheet.cell(i,9).value[0:6] not in tyBoard:
		tyBoard[worksheet.cell(i,9).value[0:6]] = 0
	tyBoard[worksheet.cell(i,9).value[0:6]] += worksheet.cell(i,10).value

	if worksheet.cell(i,9).value[6:8] != "":
		if worksheet.cell(i,9).value[0:8] not in gr:
			gr[worksheet.cell(i,9).value[0:8]] = 0
		gr[worksheet.cell(i,9).value[0:8]] += worksheet.cell(i,10).value

	if 	worksheet.cell(i,9).value[8:11] != "":
		if worksheet.cell(i,9).value[0:11] not in sb:
			sb[worksheet.cell(i,9).value[0:11]] = 0
		sb[worksheet.cell(i,9).value[0:11]] += worksheet.cell(i,10).value

	if 	worksheet.cell(i,9).value[11:13] != "":
		if worksheet.cell(i,9).value[0:13] not in ch:
			ch[worksheet.cell(i,9).value[0:13]] = 0
		ch[worksheet.cell(i,9).value[0:13]] += worksheet.cell(i,10).value

	actAr = worksheet.cell(i,6).value.split('_')

	if actAr[0] not in Proj:
		Proj[actAr[0]] = 0
	Proj[actAr[0]] += worksheet.cell(i,10).value

	if actAr[1] not in cat:
		cat[actAr[1]] = 0
	cat[actAr[1]] += worksheet.cell(i,10).value

	if actAr[2] not in acEle:
		acEle[actAr[2]] = 0
	acEle[actAr[2]] += worksheet.cell(i,10).value

	if actAr[3] not in acAct:
		acAct[actAr[3]] = 0
	acAct[actAr[3]] += worksheet.cell(i,10).value

	if worksheet.cell(i,9).value[0:2] not in yearD:
		yearD[worksheet.cell(i,9).value[0:2]] = {worksheet.cell(i,3).value:0}
	else:
		if worksheet.cell(i,3).value in yearD[worksheet.cell(i,9).value[0:2]]:
			yearD[worksheet.cell(i,9).value[0:2]][worksheet.cell(i,3).value] += worksheet.cell(i,10).value
		else:
			yearD[worksheet.cell(i,9).value[0:2]][worksheet.cell(i,3).value] = worksheet.cell(i,10).value

	if worksheet.cell(i,9).value[0:6] not in tyBoardD:
		tyBoardD[worksheet.cell(i,9).value[0:6]] = {worksheet.cell(i,3).value:0}
	else:
		if worksheet.cell(i,3).value in tyBoardD[worksheet.cell(i,9).value[0:6]]:
			tyBoardD[worksheet.cell(i,9).value[0:6]][worksheet.cell(i,3).value] += worksheet.cell(i,10).value
		else:
			tyBoardD[worksheet.cell(i,9).value[0:6]][worksheet.cell(i,3).value] = worksheet.cell(i,10).value

	if worksheet.cell(i,9).value[6:8] != "":
		if worksheet.cell(i,9).value[0:8] not in grD:
			grD[worksheet.cell(i,9).value[0:8]] = {worksheet.cell(i,3).value:0}
		else:
			if worksheet.cell(i,3).value in grD[worksheet.cell(i,9).value[0:8]]:
				grD[worksheet.cell(i,9).value[0:8]][worksheet.cell(i,3).value] += worksheet.cell(i,10).value
			else:
				grD[worksheet.cell(i,9).value[0:8]][worksheet.cell(i,3).value] = worksheet.cell(i,10).value

	if 	worksheet.cell(i,9).value[8:11] != "":
		if worksheet.cell(i,9).value[0:11] not in sbD:
			sbD[worksheet.cell(i,9).value[0:11]] = {worksheet.cell(i,3).value:0}
		else:
			if worksheet.cell(i,3).value in sbD[worksheet.cell(i,9).value[0:11]]:
				sbD[worksheet.cell(i,9).value[0:11]][worksheet.cell(i,3).value] += worksheet.cell(i,10).value
			else:
				sbD[worksheet.cell(i,9).value[0:11]][worksheet.cell(i,3).value] = worksheet.cell(i,10).value

	if 	worksheet.cell(i,9).value[11:13] != "":
		if worksheet.cell(i,9).value[0:13] not in chD:
			chD[worksheet.cell(i,9).value[0:13]] = {worksheet.cell(i,3).value:0}
		else:
			if worksheet.cell(i,3).value in chD[worksheet.cell(i,9).value[0:13]]:
				chD[worksheet.cell(i,9).value[0:13]][worksheet.cell(i,3).value] += worksheet.cell(i,10).value
			else:
				chD[worksheet.cell(i,9).value[0:13]][worksheet.cell(i,3).value] = worksheet.cell(i,10).value

	if actAr[0] not in ProjD:
		ProjD[actAr[0]] = {worksheet.cell(i,3).value:0}
		ProjF[actAr[0]] = 0
	else:
		if worksheet.cell(i,3).value in ProjD[actAr[0]]:
			ProjD[actAr[0]][worksheet.cell(i,3).value] += worksheet.cell(i,10).value
		else:
			ProjD[actAr[0]][worksheet.cell(i,3).value] = worksheet.cell(i,10).value

	ProjF[actAr[0]] += worksheet.cell(i,10).value

	if "_".join([actAr[0],actAr[1]]) not in catD:
		catD["_".join([actAr[0],actAr[1]])] = {worksheet.cell(i,3).value:0}
		catF["_".join([actAr[0],actAr[1]])] = 0
	else:
		if worksheet.cell(i,3).value in catD["_".join([actAr[0],actAr[1]])]:
			catD["_".join([actAr[0],actAr[1]])][worksheet.cell(i,3).value] += worksheet.cell(i,10).value
		else:
			catD["_".join([actAr[0],actAr[1]])][worksheet.cell(i,3).value] = worksheet.cell(i,10).value

	catF["_".join([actAr[0],actAr[1]])] += worksheet.cell(i,10).value

	if "_".join([actAr[0],actAr[1],actAr[2]]) not in acEleD:
		acEleD["_".join([actAr[0],actAr[1],actAr[2]])] = {worksheet.cell(i,3).value:0}
		acEleF["_".join([actAr[0],actAr[1],actAr[2]])] = 0
	else:
		if worksheet.cell(i,3).value in acEleD["_".join([actAr[0],actAr[1],actAr[2]])]:
			acEleD["_".join([actAr[0],actAr[1],actAr[2]])][worksheet.cell(i,3).value] += worksheet.cell(i,10).value
		else:
			acEleD["_".join([actAr[0],actAr[1],actAr[2]])][worksheet.cell(i,3).value] = worksheet.cell(i,10).value

	acEleF["_".join([actAr[0],actAr[1],actAr[2]])] += worksheet.cell(i,10).value

	if "_".join([actAr[0],actAr[1],actAr[2],actAr[3]]) not in acActD:
		acActD["_".join([actAr[0],actAr[1],actAr[2],actAr[3]])] = {worksheet.cell(i,3).value:0}
		acActF["_".join([actAr[0],actAr[1],actAr[2],actAr[3]])] = 0
	else:
		if worksheet.cell(i,3).value in acActD["_".join([actAr[0],actAr[1],actAr[2],actAr[3]])]:
			acActD["_".join([actAr[0],actAr[1],actAr[2],actAr[3]])][worksheet.cell(i,3).value] += worksheet.cell(i,10).value
		else:
			acActD["_".join([actAr[0],actAr[1],actAr[2],actAr[3]])][worksheet.cell(i,3).value] = worksheet.cell(i,10).value

	acActF["_".join([actAr[0],actAr[1],actAr[2],actAr[3]])] += worksheet.cell(i,10).value


	if worksheet.cell(i,3).value not in Dates:
		if type(worksheet.cell(i,3).value) == str:
			Dates.append(worksheet.cell(i,3).value)

Dates = sorted(Dates)

def finCalc(finDict):
	netDict = {}
	
	for i in finDict:
		dumVal = 0
		if i not in netDict:
			netDict[i] = {}
		for j in Dates:
			if j in finDict[i]:
				dumVal += finDict[i][j]
				netDict[i][j] = dumVal
			else:
				netDict[i][j] = dumVal

	return  netDict

def fracCalc(dictVal):
	tempDict = {}
	tot = 0

	for i in dictVal:
		tot += dictVal[i]

	for i in dictVal:
		if i not in tempDict:
			tempDict[i] = (dictVal[i]/tot)*100

	return  tempDict

pickle_out = open("Pickle_files/year.pickle","wb")
pickle.dump(year,pickle_out)
pickle_out.close()

pickle_out = open("Pickle_files/tyBoard.pickle","wb")
pickle.dump(tyBoard,pickle_out)
pickle_out.close()

pickle_out = open("Pickle_files/gr.pickle","wb")
pickle.dump(gr,pickle_out)
pickle_out.close()

pickle_out = open("Pickle_files/sb.pickle","wb")
pickle.dump(sb,pickle_out)
pickle_out.close()

pickle_out = open("Pickle_files/ch.pickle","wb")
pickle.dump(ch,pickle_out)
pickle_out.close()

pickle_out = open("Pickle_files/Proj.pickle","wb")
pickle.dump(Proj,pickle_out)
pickle_out.close()

pickle_out = open("Pickle_files/cat.pickle","wb")
pickle.dump(cat,pickle_out)
pickle_out.close()

pickle_out = open("Pickle_files/acEle.pickle","wb")
pickle.dump(acEle,pickle_out)
pickle_out.close()

pickle_out = open("Pickle_files/acAct.pickle","wb")
pickle.dump(acAct,pickle_out)
pickle_out.close()



pickle_out = open("Pickle_files/yearFr.pickle","wb")
pickle.dump(fracCalc(year),pickle_out)
pickle_out.close()

pickle_out = open("Pickle_files/tyBoardFr.pickle","wb")
pickle.dump(fracCalc(tyBoard),pickle_out)
pickle_out.close()

pickle_out = open("Pickle_files/grFr.pickle","wb")
pickle.dump(fracCalc(gr),pickle_out)
pickle_out.close()

pickle_out = open("Pickle_files/sbFr.pickle","wb")
pickle.dump(fracCalc(sb),pickle_out)
pickle_out.close()

pickle_out = open("Pickle_files/chFr.pickle","wb")
pickle.dump(fracCalc(ch),pickle_out)
pickle_out.close()


pickle_out = open("Pickle_files/yearD.pickle","wb")
pickle.dump(finCalc(yearD),pickle_out)
pickle_out.close()

pickle_out = open("Pickle_files/tyBoardD.pickle","wb")
pickle.dump(finCalc(tyBoardD),pickle_out)
pickle_out.close()

pickle_out = open("Pickle_files/grD.pickle","wb")
pickle.dump(finCalc(grD),pickle_out)
pickle_out.close()

pickle_out = open("Pickle_files/sbD.pickle","wb")
pickle.dump(finCalc(sbD),pickle_out)
pickle_out.close()

pickle_out = open("Pickle_files/chD.pickle","wb")
pickle.dump(finCalc(chD),pickle_out)
pickle_out.close()

pickle_out = open("Pickle_files/ProjD.pickle","wb")
pickle.dump(finCalc(ProjD),pickle_out)
pickle_out.close()

pickle_out = open("Pickle_files/catD.pickle","wb")
pickle.dump(finCalc(catD),pickle_out)
pickle_out.close()

pickle_out = open("Pickle_files/acEleD.pickle","wb")
pickle.dump(finCalc(acEleD),pickle_out)
pickle_out.close()

pickle_out = open("Pickle_files/acActD.pickle","wb")
pickle.dump(finCalc(acActD),pickle_out)
pickle_out.close()


pickle_out = open("Pickle_files/ProjF.pickle","wb")
pickle.dump(fracCalc(ProjF),pickle_out)
pickle_out.close()

pickle_out = open("Pickle_files/catF.pickle","wb")
pickle.dump(fracCalc(catF),pickle_out)
pickle_out.close()

pickle_out = open("Pickle_files/acEleF.pickle","wb")
pickle.dump(fracCalc(acEleF),pickle_out)
pickle_out.close()

pickle_out = open("Pickle_files/acActF.pickle","wb")
pickle.dump(fracCalc(acActF),pickle_out)
pickle_out.close()

