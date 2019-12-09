import xlrd
import pickle

fileName = 'Data Pull_ MH, KL, Commerce_ 15 Nov 18-19_v1.2.xlsx'

workbook = xlrd.open_workbook(fileName,on_demand = True)

featureAct = {}
featureMid = {}

cAr = []
eAr = []
aAr = []

mGr = []
mSub = []
mCh = []

actFeAr = []
midFeAr = []

yAc = []
yMid = []

cDi = {}
eDi = {}
aDi = {}

mGrDi = {}
mSubDi = {}
mChDi = {}

def lab(ar,di):
    ind = 0

    for i in ar:
        if i not in di:
            di[i] = ind
            ind += 1
    return di

for k in range(3):

    worksheet = workbook.sheet_by_index(k)
    nRows = worksheet.nrows

    for i in range(1,nRows):
        if worksheet.cell(i,6).value != 'None' and worksheet.cell(i,2).value != "":
            dumAr = []

            temp = worksheet.cell(i,2).value.split("_")

            if temp[1] not in cAr:
                cAr.append(temp[1])
 
            if temp[2] not in eAr:
                eAr.append(temp[2])

            if temp[3] not in aAr:
                aAr.append(temp[3])

            tempStr = "_".join([temp[1],temp[2],temp[3]])

            if tempStr not in featureAct:
                featureAct[tempStr] = 0
            featureAct[tempStr] += worksheet.cell(i,9).value
            
            tempM = "".join([worksheet.cell(i,6).value[6:8],worksheet.cell(i,6).value[8:11],worksheet.cell(i,6).value[11:13]])

            if worksheet.cell(i,6).value[6:8] not in mGr:
                mGr.append(worksheet.cell(i,6).value[6:8])

            if worksheet.cell(i,6).value[8:11] not in mSub:
                mSub.append(worksheet.cell(i,6).value[8:11])

            if worksheet.cell(i,6).value[11:13] not in mCh:
                mCh.append(worksheet.cell(i,6).value[11:13])

            if tempM not in featureMid:
                featureMid[tempM] = 0
            featureMid[tempM] += worksheet.cell(i,9).value

    cDi = lab(cAr,cDi)
    eDi = lab(eAr,eDi)
    aDi = lab(aAr,aDi)

    mGrDi = lab(mGr,mGrDi)
    mSubDi = lab(mSub,mSubDi)
    mChDi = lab(mCh,mChDi)

    for i in featureAct:
        temp = i.split("_")

        dumAr = []

        dumAr.append(cDi[temp[0]])
        dumAr.append(eDi[temp[1]])
        dumAr.append(aDi[temp[2]])

        yAc.append([featureAct[i]])

        actFeAr.append(dumAr)

    for i in featureMid:
        midFeAr.append([mGrDi[i[0:2]],mSubDi[i[2:5]],mChDi[i[5:7]]])
        yMid.append(featureMid[i])

print(actFeAr,yAc)

pickle_out = open("Pickle_files/activityAr.pickle","wb")
pickle.dump(actFeAr,pickle_out)
pickle_out.close()

pickle_out = open("Pickle_files/activityY.pickle","wb")
pickle.dump(yAc,pickle_out)
pickle_out.close()

pickle_out = open("Pickle_files/midAr.pickle","wb")
pickle.dump(midFeAr,pickle_out)
pickle_out.close()

pickle_out = open("Pickle_files/midY.pickle","wb")
pickle.dump(yMid,pickle_out)
pickle_out.close()

pickle_out = open("Pickle_files/labActivity.pickle","wb")
pickle.dump([cDi,eDi,aDi],pickle_out)
pickle_out.close()

pickle_out = open("Pickle_files/labActivity.pickle","wb")
pickle.dump([cDi,eDi,aDi],pickle_out)
pickle_out.close()

pickle_out = open("Pickle_files/labMid.pickle","wb")
pickle.dump([mGrDi,mSubDi,mChDi],pickle_out)
pickle_out.close()
