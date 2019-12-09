import pandas as pd
import pickle

# L1_mids = pickle.load(open('Machine_model/pickleFile/level1Mid.pickle','rb'))
# L2_mids = pickle.load(open('Machine_model/pickleFile/level2Mid.pickle','rb'))
# L3_mids = pickle.load(open('Machine_model/pickleFile/level3Mid.pickle','rb'))
# L4_mids = pickle.load(open('Machine_model/pickleFile/level4Mid.pickle','rb'))


# df_actMid = pd.read_excel(r'Machine_model/Sheets/actMid.xls')
# mids = L1_mids.keys()

# df = pd.read_excel(r'Machine_model/Sheets/Action_sheet.xls')
# grades = df.head()

def dataFetch(dataFrame,i):

	dff = dataFrame[dataFrame['MIDS'] == i]

	Y1 = dff['Days']*dff['Xp']
	Y2 = dff['Days']
	X = dff['Activity_name']

	return Y1,Y2,X

def dataMem(dataFrame,i):

	dff = dataFrame[dataFrame['MIDS'] == i]


	Y1 = dff['Partial memeber']
	Y2 = dff['Actual memeber']
	X = dff['Activity_name']

	return Y1,Y2,X

def dataQt(dataFrame,i):

	dff = dataFrame[dataFrame['MIDS'] == i]


	Y1 = dff['Quantity']
	Y2 = dff['Target']
	X = dff['Activity_name']

	return Y1,Y2,X

def dataAction(dataFrame,i):

	dff = dataFrame[dataFrame['Emp_name'] == i]
	s = dff.shape
	Y = []
	if i != 'Select employee name':
		for j in range(1,s[1]):
			Y.append(dff.iat[0,j])

	return Y

def dataActivity(dataFrame,i):
	dff = dataFrame[dataFrame['MID'] == i]
	actAr = dff['Activity Name'].unique()
	dateAr = dff['Date']
	xpAr = dff['Filled Xp']

	return dff,actAr,dateAr,xpAr

def midData(midDict):
	mid = []
	midXp = []

	for i in midDict:
		mid.append(i)
		midXp.append(midDict[i])

	return mid,midXp

#print(midData(L1_mids))