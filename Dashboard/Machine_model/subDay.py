import xlrd
import pickle

fileName = 'Tamil_nadu_data.xlsx'

workbook = xlrd.open_workbook(fileName,on_demand = True)
worksheet = workbook.sheet_by_name('Sheet1')
nRows = worksheet.nrows

subDict = {}
grDict = {}

for i in range(1,nRows):
	if worksheet.cell(i,9).value[8:11] != '':
		if worksheet.cell(i,9).value[8:11] not in subDict:
			subDict[worksheet.cell(i,9).value[8:11]] = {worksheet.cell(i,3).value:worksheet.cell(i,10).value}
		else:
			if worksheet.cell(i,3).value in  subDict[worksheet.cell(i,9).value[8:11]]:
				subDict[worksheet.cell(i,9).value[8:11]][worksheet.cell(i,3).value] += worksheet.cell(i,10).value
			else:
				subDict[worksheet.cell(i,9).value[8:11]][worksheet.cell(i,3).value] = worksheet.cell(i,10).value

	if worksheet.cell(i,9).value[6:8] != '':
		if worksheet.cell(i,9).value[6:8] not in grDict:
			grDict[worksheet.cell(i,9).value[6:8]] = {str(worksheet.cell(i,3).value):worksheet.cell(i,10).value}
		else:
			if str(worksheet.cell(i,3).value) in  grDict[worksheet.cell(i,9).value[6:8]]:
				grDict[worksheet.cell(i,9).value[6:8]][str(worksheet.cell(i,3).value)] += worksheet.cell(i,10).value
			else:
				grDict[worksheet.cell(i,9).value[6:8]][str(worksheet.cell(i,3).value)] = worksheet.cell(i,10).value

pickle_out = open("pickleFile/subDay.pickle","wb")
pickle.dump(subDict,pickle_out)
pickle_out.close()

pickle_out = open("pickleFile/grDict.pickle","wb")
pickle.dump(grDict,pickle_out)
pickle_out.close()

print(grDict)