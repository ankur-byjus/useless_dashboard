import xlrd

import pickle

from xlwt import Workbook

fileName = 'Tamil_nadu_data.xlsx'

wb = Workbook()
sheet = wb.add_sheet('Grade_sheet')

workbook = xlrd.open_workbook(fileName,on_demand = True)
worksheet = workbook.sheet_by_name('Sheet1')
nRows = worksheet.nrows

midDict = {}

for i in range(1,nRows):
	if worksheet.cell(i,9).value not in midDict:
		midDict[worksheet.cell(i,9).value] = 1
	else:
		midDict[worksheet.cell(i,9).value] += 1

L_1_mids = {}

for i in midDict.keys():
	if i[0:8] not in L_1_mids:
		L_1_mids[i[0:8]] = []

for i in midDict.keys():
	if i[0:8] != i:
		L_1_mids[i[0:8]].append(i)

userDict = {}

for i in range(1,nRows):
	if worksheet.cell(i,5).value not in userDict:
		userDict[worksheet.cell(i,5).value] = []
	else:
		if worksheet.cell(i,9).value[6:8] not in userDict[worksheet.cell(i,5).value] and worksheet.cell(i,9).value[6:8] != '' :
			userDict[worksheet.cell(i,5).value].append(worksheet.cell(i,9).value[6:8])

gradeAr = []

for i in range(1,nRows):
	if worksheet.cell(i,9).value[6:8] not in gradeAr and  worksheet.cell(i,9).value[6:8] != '':
		gradeAr.append( worksheet.cell(i,9).value[6:8])

sheet.write(0,0,'Emp_name')

ind = 1
for i in gradeAr:
	sheet.write(0,ind,i)
	ind += 1

userScore = {}

for i in range(1,nRows):
	if worksheet.cell(i,5).value not in userScore:
		userScore[worksheet.cell(i,5).value] = {}
		for j in gradeAr:
			userScore[worksheet.cell(i,5).value][j] = 0
	if worksheet.cell(i,9).value[6:8] != '':
		userScore[worksheet.cell(i,5).value][worksheet.cell(i,9).value[6:8]] += 1

ind = 1
for i in userScore:
	sheet.write(ind,0,i)
	indG = 1
	for j in userScore[i]:
		sheet.write(ind,indG,userScore[i][j])
		indG += 1

	ind += 1

wb.save("Sheets/Grade_sheet.xls")

pickle_out = open("pickleFile/userScore.pickle","wb")
pickle.dump(userScore,pickle_out)
pickle_out.close()

for i in L_1_mids:
	if len(L_1_mids[i]) == 0:
		projMid = i

for i in L_1_mids:
	if i != projMid:
		L_1_mids[projMid].append(i)

pickle_out = open("pickleFile/L_1_mids.pickle","wb")
pickle.dump(L_1_mids,pickle_out)
pickle_out.close()




