import xlrd

from xlwt import Workbook

fileName = 'Tamil_nadu_data.xlsx'

wb = Workbook()
sheet = wb.add_sheet('Grade_xp')

wb1 = Workbook()
sheet1 = wb1.add_sheet('Sub_xp')

workbook = xlrd.open_workbook(fileName,on_demand = True)
worksheet = workbook.sheet_by_name('Sheet1')
nRows = worksheet.nrows

gradeDict = {}
subDict = {}

for i in range(1,nRows):
	if worksheet.cell(i,9).value[6:8] != '':
		if worksheet.cell(i,9).value[6:8] not in gradeDict:
			gradeDict[worksheet.cell(i,9).value[6:8]] = worksheet.cell(i,10).value
		else:
			gradeDict[worksheet.cell(i,9).value[6:8]] += worksheet.cell(i,10).value

	if worksheet.cell(i,9).value[8:11] != '':
		if worksheet.cell(i,9).value[8:11] not in subDict:
			subDict[worksheet.cell(i,9).value[8:11]] = worksheet.cell(i,10).value
		else:
			subDict[worksheet.cell(i,9).value[8:11]] += worksheet.cell(i,10).value

sheet.write(0,0,'Grade')
sheet.write(0,1,'Tot_Xp')

sheet1.write(0,0,'Subject')
sheet1.write(0,1,'Tot_Xp')

ind = 1
for i in gradeDict:
	sheet.write(ind,0,i)
	sheet.write(ind,1,gradeDict[i])
	ind += 1

ind = 1
for i in subDict:
	sheet1.write(ind,0,i)
	sheet1.write(ind,1,subDict[i])
	ind += 1

wb.save("Sheets/Grade_totXp.xls")
wb1.save("Sheets/Sub_totXp.xls")


