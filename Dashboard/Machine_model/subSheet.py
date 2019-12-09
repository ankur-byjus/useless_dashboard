import xlrd

from xlwt import Workbook

import userSheet

import pickle

fileName = 'Tamil_nadu_data.xlsx'

wb_1 = Workbook()
sheet_1 = wb_1.add_sheet('Sub_sheet')

workbook = xlrd.open_workbook(fileName,on_demand = True)
worksheet = workbook.sheet_by_name('Sheet1')
nRows = worksheet.nrows

subAr = []

for i in userSheet.midDict:
	if i[8:11] != '':
		if i[8:11] not in subAr:
			subAr.append(i[8:11])

userSub = {}

for i in range(1,nRows):
	if worksheet.cell(i,5).value not in userSub:
		userSub[worksheet.cell(i,5).value] = {}
		for j in subAr:
			userSub[worksheet.cell(i,5).value][j] = 0
	if worksheet.cell(i,9).value[8:11] != '':
		userSub[worksheet.cell(i,5).value][worksheet.cell(i,9).value[8:11]] += 1

sheet_1.write(0,0,'Emp_name')

ind_1 = 1
for i in subAr:
	sheet_1.write(0,ind_1,i)
	ind_1 += 1

ind_2 = 1
for i in userSub:
	ind_3 = 1
	sheet_1.write(ind_2,0,i)
	for j in userSub[i]:
		sheet_1.write(ind_2,ind_3,userSub[i][j])
		ind_3 += 1
	ind_2 += 1

wb_1.save("Sheets/Subject_sheet.xls")

pickle_out = open("pickleFile/userSub.pickle","wb")
pickle.dump(userSub,pickle_out)
pickle_out.close()



