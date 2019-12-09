import xlrd

import pickle

from xlwt import Workbook

fileName = 'Tamil_nadu_data.xlsx'

wb_2 = Workbook()
sheet_2 = wb_2.add_sheet('Act_sheet')

wb_3 = Workbook()
sheet_3 = wb_3.add_sheet('Ele_sheet')

workbook = xlrd.open_workbook(fileName,on_demand = True)
worksheet = workbook.sheet_by_name('Sheet1')
nRows = worksheet.nrows

actDict = {}

for i in range(1,nRows):
	if worksheet.cell(i,6).value not in actDict:
		actDict[worksheet.cell(i,6).value] = 1

actionAr = []
elementAr = []

for i in actDict:
	dumAr = i.split('_')
	if dumAr[-1] not in actionAr:
		actionAr.append(dumAr[-1])

	if dumAr[-2] not in elementAr:
		elementAr.append(dumAr[-2])

#print(actionAr)
#print(elementAr)

sheet_2.write(0,0,'Emp_name')
sheet_3.write(0,0,'Emp_name')

ind = 1

for i in actionAr:
	sheet_2.write(0,ind,i)
	ind += 1

ind = 1

for i in elementAr:
	sheet_3.write(0,ind,i)
	ind += 1

userAction = {}
userElement = {}

for i in range(1,nRows):
	if worksheet.cell(i,5).value not in userAction:
		userAction[worksheet.cell(i,5).value] = {}
		userElement[worksheet.cell(i,5).value] = {}

		for j in actionAr:
			userAction[worksheet.cell(i,5).value][j] = 0

		for j in elementAr:
			userElement[worksheet.cell(i,5).value][j] = 0

	dumVal = worksheet.cell(i,6).value.split('_')

	userAction[worksheet.cell(i,5).value][dumVal[-1]] += 1
	userElement[worksheet.cell(i,5).value][dumVal[-2]] += 1

ind_2 = 1

for i in userAction:
	ind_3 = 1
	sheet_2.write(ind_2,0,i)
	for j in userAction[i]:
		sheet_2.write(ind_2,ind_3,userAction[i][j])
		ind_3 += 1
	ind_2 += 1

ind_2 = 1
for i in userElement:
	ind_3 = 1
	sheet_3.write(ind_2,0,i)
	for j in userElement[i]:
		sheet_3.write(ind_2,ind_3,userElement[i][j])
		ind_3 += 1
	ind_2 += 1

#print(userElement)

wb_2.save("Sheets/Action_sheet.xls")
wb_3.save("Sheets/Element_sheet.xls")

pickle_out = open("pickleFile/userElement.pickle","wb")
pickle.dump(userElement,pickle_out)
pickle_out.close()

pickle_out = open("pickleFile/userAction.pickle","wb")
pickle.dump(userAction,pickle_out)
pickle_out.close()