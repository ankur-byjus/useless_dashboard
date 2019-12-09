import pickle
import xlrd

fileName = 'Data Pull_ MH, KL, Commerce_ 15 Nov 18-19_v1.2.xlsx'

workbook = xlrd.open_workbook(fileName,on_demand = True)

worksheet = workbook.sheet_by_index(0)
nRows = worksheet.nrows

chCount = {}

lbBr = {}
br = 0
lbGr = {}
gr = 0
lbSub = {}
sub = 0

for i in range(1,nRows):
	if worksheet.cell(i,8).value != 'None' and worksheet.cell(i,8).value != "":
		if worksheet.cell(i,6).value[2:] not in chCount:
			chCount[worksheet.cell(i,6).value[2:]] = 0
		chCount[worksheet.cell(i,6).value[2:]] += worksheet.cell(i,8).value

		if worksheet.cell(i,6).value[2:6] not in lbBr and len(worksheet.cell(i,6).value[2:6]) == 4:
			lbBr[worksheet.cell(i,6).value[2:6]] = br
			br += 1

		if worksheet.cell(i,6).value[6:8] not in lbGr and worksheet.cell(i,6).value[6:8] != "":
			lbGr[worksheet.cell(i,6).value[6:8]] = gr
			gr += 1

		if worksheet.cell(i,6).value[8:11] not in lbSub and worksheet.cell(i,6).value[8:11] != "":
			lbSub[worksheet.cell(i,6).value[8:11]] = sub
			sub += 1

chNum = {}

for i in chCount:
	if i[0:9] not in chNum and i[9:11] != "":
		chNum[i[0:9]] = []
	if i[9:11] != "" and i[9:11] not in chNum[i[0:9]] :
		chNum[i[0:9]].append(i[9:11])

xpPerCh = {}
for i in chCount:
 	if len(i) == 9 and i[0:9] in chNum:
 		xpPerCh[i] = chCount[i]/len(chNum[i[0:9]])

xFe = []
yFe = []

for i in xpPerCh:
	tempX = []
	tempY = []

	tempX.append(lbBr[i[0:4]])
	tempX.append(lbGr[i[4:6]])
	tempX.append(lbSub[i[6:9]])

	tempY.append(xpPerCh[i])

	xFe.append(tempX)
	yFe.append(tempY)

pickle_out = open("Pickle_files/midPerChX.pickle","wb")
pickle.dump(xFe,pickle_out)
pickle_out.close()

pickle_out = open("Pickle_files/midPerChY.pickle","wb")
pickle.dump(yFe,pickle_out)
pickle_out.close()

pickle_out = open("Pickle_files/midPerChLab.pickle","wb")
pickle.dump([lbBr,lbGr,lbSub],pickle_out)
pickle_out.close()

print(xFe)
print(yFe)
print(lbBr)

