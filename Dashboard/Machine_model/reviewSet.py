import xlrd

from xlwt import Workbook

fileName = 'Tamil_nadu_data.xlsx'

wb = Workbook()

workbook = xlrd.open_workbook(fileName,on_demand = True)
worksheet = workbook.sheet_by_name('Sheet1')
nRows = worksheet.nrows

reviewPara = {'Needs Awareness':-2,'Needs Improvement':-1,'Meets Expectation':0,
                 'Exceeds Expectation':1,'Strongly Exceeds Expectation':2 }
ar1 = []
ar2 = []

actRedict = {}

def stringClear(data):
	dumAr = data.split(',')
	rewDict = {}

	for i in dumAr:
		dumAr2 = i.split('-')
		if len(dumAr2) == 1:
			if 'Qa' not in rewDict:
				rewDict['Qa'] = 0
			dumAr2[0] = dumAr2[0].strip()
			rewDict['Qa'] += reviewPara[dumAr2[0]]
		else:
			if dumAr2[0] not in rewDict:
				dumAr2[0] = dumAr2[0].strip()
				rewDict[dumAr2[0]] = 0
			dumAr2[0] = dumAr2[0].strip()
			dumAr2[1] = dumAr2[1].strip()
			rewDict[dumAr2[0]] += reviewPara[dumAr2[1]]

	return rewDict


empChar = {}

for i in range(1,nRows):
	if worksheet.cell(i,28).value != '':
		dummyDict = stringClear(worksheet.cell(i,28).value)

		if worksheet.cell(i,5).value not in empChar:
			empChar[worksheet.cell(i,5).value] = {worksheet.cell(i,6).value:{}}
		else:
			if worksheet.cell(i,6).value not in empChar[worksheet.cell(i,5).value]:
				empChar[worksheet.cell(i,5).value][worksheet.cell(i,6).value] = {}
		for j in dummyDict:
			if j not in empChar[worksheet.cell(i,5).value][worksheet.cell(i,6).value]:
				empChar[worksheet.cell(i,5).value][worksheet.cell(i,6).value][j] = dummyDict[j]
			else:
				empChar[worksheet.cell(i,5).value][worksheet.cell(i,6).value][j] += dummyDict[j]


for i in empChar:
	reAr = {}
	sheet = wb.add_sheet(i)
	sheet.write(0,0,'Activity name')
	ind = 1
	ind2 = 1
	for j in empChar[i]:
		sheet.write(ind,0,j)
		ind += 1

	ind3 = 1

	for j in empChar[i]:
		for k in empChar[i][j]:
			if k not in reAr:
				sheet.write(0,ind2,k)
				reAr[k] = ind2
				ind2 += 1
			sheet.write(ind3,reAr[k],empChar[i][j][k])
		ind3 += 1

wb.save('Sheets/Emp_character.xls')



	
