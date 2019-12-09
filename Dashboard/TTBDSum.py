import pickle
import xlrd

model = pickle.load(open("Pickle_files/modelTTBDMid.pickle","rb"))
modelAc = pickle.load(open("Pickle_files/modelTTBDAct.pickle","rb"))
labMid = pickle.load(open("Pickle_files/midPerChLab.pickle","rb"))
labActivity = pickle.load(open("Pickle_files/labActivity.pickle","rb"))

fileName = 'Tamil_nadu_data.xlsx'

workbook = xlrd.open_workbook(fileName,on_demand = True)

worksheet = workbook.sheet_by_index(0)
nRows = worksheet.nrows

yrDict = {}
brDict = {}
grDict = {}
subDict = {}
chDict = {}

projDict = {}
catDict = {}
eleDict = {}
actDict = {}


for i in range(1,nRows):
	if worksheet.cell(i,9).value[2:6] != "" and worksheet.cell(i,9).value[6:8] != "" and worksheet.cell(i,9).value[8:11] != "":
		if worksheet.cell(i,9).value[0:2] not in yrDict:
			yrDict[worksheet.cell(i,9).value[0:2]] = 0
		yrDict[worksheet.cell(i,9).value[0:2]] += model.predict([[labMid[0][worksheet.cell(i,9).value[2:6]],labMid[1][worksheet.cell(i,9).value[6:8]],labMid[2][worksheet.cell(i,9).value[8:11]]]])

		if worksheet.cell(i,9).value[0:6] not in brDict:
			brDict[worksheet.cell(i,9).value[0:6]] = 0
		brDict[worksheet.cell(i,9).value[0:6]] += model.predict([[labMid[0][worksheet.cell(i,9).value[2:6]],labMid[1][worksheet.cell(i,9).value[6:8]],labMid[2][worksheet.cell(i,9).value[8:11]]]])

		if worksheet.cell(i,9).value[0:8] not in grDict:
			grDict[worksheet.cell(i,9).value[0:8]] = 0
		grDict[worksheet.cell(i,9).value[0:8]] += model.predict([[labMid[0][worksheet.cell(i,9).value[2:6]],labMid[1][worksheet.cell(i,9).value[6:8]],labMid[2][worksheet.cell(i,9).value[8:11]]]])

		if worksheet.cell(i,9).value[0:11] not in subDict:
			subDict[worksheet.cell(i,9).value[0:11]] = 0
		subDict[worksheet.cell(i,9).value[0:11]] += model.predict([[labMid[0][worksheet.cell(i,9).value[2:6]],labMid[1][worksheet.cell(i,9).value[6:8]],labMid[2][worksheet.cell(i,9).value[8:11]]]])

		if worksheet.cell(i,9).value[0:13] not in chDict:
			chDict[worksheet.cell(i,9).value[0:13]] = 0
		chDict[worksheet.cell(i,9).value[0:13]] += model.predict([[labMid[0][worksheet.cell(i,9).value[2:6]],labMid[1][worksheet.cell(i,9).value[6:8]],labMid[2][worksheet.cell(i,9).value[8:11]]]])

	# actStr = worksheet.cell(i,6).value.split('_')

	# if actStr[0] not in projDict:
	# 	projDict[actStr[0]] = 0
	# projDict[actStr[0]] += modelAc.predict([[labActivity[0][actStr[1]],labActivity[1][actStr[2]],labActivity[2][actStr[3]]]])

	# tempAct = "_".join([actStr[0],actStr[1]])

	# if tempAct not in catDict:
	# 	catDict[tempAct] = 0
	# catDict[tempAct] += modelAc.predict([[labActivity[0][actStr[1]],labActivity[1][actStr[2]],labActivity[2][actStr[3]]]])

	# tempAct = "_".join([actStr[0],actStr[1],actStr[2]])

	# if tempAct not in eleDict:
	# 	eleDict[tempAct] = 0
	# eleDict[tempAct] += modelAc.predict([[labActivity[0][actStr[1]],labActivity[1][actStr[2]],labActivity[2][actStr[3]]]])

	# tempAct = "_".join([actStr[0],actStr[1],actStr[2],actStr[3]])

	# if tempAct not in actDict:
	# 	actDict[tempAct] = 0
	# actDict[tempAct] += modelAc.predict([[labActivity[0][actStr[1]],labActivity[1][actStr[2]],labActivity[2][actStr[3]]]])

pickle_out = open("Pickle_files/TTBD_mid.pickle","wb")
pickle.dump([yrDict,brDict,grDict,subDict,chDict],pickle_out)
pickle_out.close()

print([yrDict,brDict,grDict,subDict,chDict])

pickle_out = open("Pickle_files/TTBD_act.pickle","wb")
pickle.dump([projDict,catDict,eleDict,actDict],pickle_out)
pickle_out.close()



