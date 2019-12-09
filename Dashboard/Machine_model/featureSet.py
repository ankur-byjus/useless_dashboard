import xlrd

from xlwt import Workbook

fileName = 'Tamil_nadu_data.xlsx'

wb = Workbook()
sheet = wb.add_sheet('Fe_sheet')

workbook = xlrd.open_workbook(fileName,on_demand = True)
worksheet = workbook.sheet_by_name('Sheet1')
nRows = worksheet.nrows

empAr = []

for i in range(1,nRows):
	if worksheet.cell(i,5).value not in empAr:
		empAr.append(worksheet.cell(i,5).value)

actQt = {}
actXp = {}
actDay = {}
actEmpName = {}
actDate = {}
actEmpDate = {}
totalEmp = {}

uniAct = []

totProjXp = 0

for i in range(1,nRows):

	if ':'.join([worksheet.cell(i,6).value,worksheet.cell(i,9).value]) not in uniAct:
		uniAct.append(':'.join([worksheet.cell(i,6).value,worksheet.cell(i,9).value]))


	if ':'.join([worksheet.cell(i,6).value,worksheet.cell(i,9).value]) not in actQt:
		actQt[':'.join([worksheet.cell(i,6).value,worksheet.cell(i,9).value])] = 0
		actXp[':'.join([worksheet.cell(i,6).value,worksheet.cell(i,9).value])] = 0
		actDay[':'.join([worksheet.cell(i,6).value,worksheet.cell(i,9).value])] = []
	actQt[':'.join([worksheet.cell(i,6).value,worksheet.cell(i,9).value])] += worksheet.cell(i,8).value
	actXp[':'.join([worksheet.cell(i,6).value,worksheet.cell(i,9).value])] += worksheet.cell(i,10).value 

	totProjXp += worksheet.cell(i,10).value

	if worksheet.cell(i,3).value not in actDay[':'.join([worksheet.cell(i,6).value,worksheet.cell(i,9).value])]:
		actDay[':'.join([worksheet.cell(i,6).value,worksheet.cell(i,9).value])].append(worksheet.cell(i,3).value)

	if ':'.join([worksheet.cell(i,6).value,worksheet.cell(i,9).value]) not in actEmpName:
		actEmpName[':'.join([worksheet.cell(i,6).value,worksheet.cell(i,9).value])] = []
	if worksheet.cell(i,5).value not in actEmpName[':'.join([worksheet.cell(i,6).value,worksheet.cell(i,9).value])]:
		actEmpName[':'.join([worksheet.cell(i,6).value,worksheet.cell(i,9).value])].append(worksheet.cell(i,5).value)

	if worksheet.cell(i,3).value not in actDate:
		actDate[worksheet.cell(i,3).value] = {worksheet.cell(i,5).value:worksheet.cell(i,10).value}
	else:
		if worksheet.cell(i,5).value in actDate[worksheet.cell(i,3).value]:
			actDate[worksheet.cell(i,3).value][worksheet.cell(i,5).value] += worksheet.cell(i,10).value
		else:
			actDate[worksheet.cell(i,3).value][worksheet.cell(i,5).value] = worksheet.cell(i,10).value

	if worksheet.cell(i,3).value not in actEmpDate:
		actEmpDate[worksheet.cell(i,3).value] = {':'.join([worksheet.cell(i,6).value,worksheet.cell(i,9).value]):{worksheet.cell(i,5).value:worksheet.cell(i,10).value}}
	else:
		if ':'.join([worksheet.cell(i,6).value,worksheet.cell(i,9).value]) in actEmpDate[worksheet.cell(i,3).value]:
			if worksheet.cell(i,5).value in actEmpDate[worksheet.cell(i,3).value][':'.join([worksheet.cell(i,6).value,worksheet.cell(i,9).value])]:
				actEmpDate[worksheet.cell(i,3).value][':'.join([worksheet.cell(i,6).value,worksheet.cell(i,9).value])][worksheet.cell(i,5).value] += worksheet.cell(i,10).value
			else:
				actEmpDate[worksheet.cell(i,3).value][':'.join([worksheet.cell(i,6).value,worksheet.cell(i,9).value])][worksheet.cell(i,5).value] = worksheet.cell(i,10).value
				#print(worksheet.cell(i,6).value,worksheet.cell(i,5).value,worksheet.cell(i,10).value)
		else:
			actEmpDate[worksheet.cell(i,3).value][':'.join([worksheet.cell(i,6).value,worksheet.cell(i,9).value])] = {worksheet.cell(i,5).value:worksheet.cell(i,10).value}

	if ':'.join([worksheet.cell(i,6).value,worksheet.cell(i,9).value]) not in totalEmp:
		totalEmp[':'.join([worksheet.cell(i,6).value,worksheet.cell(i,9).value])] = {worksheet.cell(i,3).value:[worksheet.cell(i,5).value]}
	else:
		if worksheet.cell(i,3).value in totalEmp[':'.join([worksheet.cell(i,6).value,worksheet.cell(i,9).value])]:
			if worksheet.cell(i,5).value not in totalEmp[':'.join([worksheet.cell(i,6).value,worksheet.cell(i,9).value])][worksheet.cell(i,3).value]:
				totalEmp[':'.join([worksheet.cell(i,6).value,worksheet.cell(i,9).value])][worksheet.cell(i,3).value].append(worksheet.cell(i,5).value)
		else:
			totalEmp[':'.join([worksheet.cell(i,6).value,worksheet.cell(i,9).value])][worksheet.cell(i,3).value] = [worksheet.cell(i,5).value]
	
totEmp = {}

for i in totalEmp:
	totEmp[i] = 0

	for j in totalEmp[i]:
		totEmp[i] += 1*len(totalEmp[i][j])


partialMember = {}

for i in actEmpDate:
	for j in actEmpDate[i]:
		if j not in partialMember:
			partialMember[j] = 0
		for k in actEmpDate[i][j]:
			if actDate[i][k] != 0:
				partialMember[j] += actEmpDate[i][j][k]/actDate[i][k]

sheet.write(0,0,'MIDS')
sheet.write(0,1,'Activity_name')
sheet.write(0,2,'Emp_name')
sheet.write(0,3,'Quantity')
sheet.write(0,4,'Xp')
sheet.write(0,5,'Days')
sheet.write(0,6,'Actual memeber')
sheet.write(0,7,'Target')
sheet.write(0,8,'Partial memeber')
sheet.write(0,9,'Project fraction')
sheet.write(0,10,'Working folks')

ind = 1

for i in uniAct:
	tempAr = i.split(':')
	if totEmp[i] != 0 and len(actDay[i]) != 0 and actXp[i] != 0 and totProjXp != 0:
		sheet.write(ind,0,tempAr[1])
		sheet.write(ind,1,tempAr[0])
		sheet.write(ind,2,str(actEmpName[i]))
		sheet.write(ind,3,actQt[i]/totEmp[i])
		sheet.write(ind,4,actXp[i]/totEmp[i])
		sheet.write(ind,5,len(actDay[i]))
		sheet.write(ind,6,(actXp[i]/len(actDay[i]))*0.1)
		sheet.write(ind,7,round((actQt[i]/actXp[i])*10,0))
		sheet.write(ind,8,partialMember[i]/len(actDay[i]))
		sheet.write(ind,9,actXp[i]/totProjXp)
		sheet.write(ind,10,totEmp[i])
		ind += 1

wb.save('Sheets/actMid.xls')