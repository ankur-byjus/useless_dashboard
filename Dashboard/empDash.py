import dash
import dash_core_components as dcc
import dash_html_components as html 
import dash_daq as daq
import pandas as pd
import plotly.graph_objs as go

import flask

import pickle
from datetime import datetime
from itertools import combinations 

import midDataProc
import suggestionStat
import colorAr
import suggestionText

import random

server = flask.Flask(__name__)

external_stylesheets = ["https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css",
"https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js",
"https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,server = server, url_base_pathname='/dashboard/')
#app.config['suppress_callback_exceptions'] = True
server = app.server

ar = ['Anisha Sabu','Sunkari Sai Rakesh','Sujata Udapudi','Samyuktha Nethra Poojary','Deepa Manoj']

subDay = pickle.load(open('Machine_model/pickleFile/subDay.pickle','rb'))
grDay = pickle.load(open('Machine_model/pickleFile/grDict.pickle','rb'))

df_main = pd.read_excel(r'Machine_model/Tamil_nadu_data.xlsx')

df_grade = pd.read_excel(r'Machine_model/Sheets/Grade_totXp.xls')
df_subXp = pd.read_excel(r'Machine_model/Sheets/Sub_totXp.xls')

L1_mids = pickle.load(open('Machine_model/pickleFile/level1Mid.pickle','rb'))
L2_mids = pickle.load(open('Machine_model/pickleFile/level2Mid.pickle','rb'))
L3_mids = pickle.load(open('Machine_model/pickleFile/level3Mid.pickle','rb'))
L4_mids = pickle.load(open('Machine_model/pickleFile/level4Mid.pickle','rb'))

year = pickle.load(open('Pickle_files/yearD.pickle','rb'))
tyBoard = pickle.load(open('Pickle_files/tyBoardD.pickle','rb'))
grade = pickle.load(open('Pickle_files/grD.pickle','rb'))
subject = pickle.load(open('Pickle_files/sbD.pickle','rb'))
chapter = pickle.load(open('Pickle_files/chD.pickle','rb'))

yearFr = pickle.load(open('Pickle_files/yearFr.pickle','rb'))
tyBoardFr = pickle.load(open('Pickle_files/tyBoardFr.pickle','rb'))
grFr = pickle.load(open('Pickle_files/grFr.pickle','rb'))
sbFr = pickle.load(open('Pickle_files/sbFr.pickle','rb'))
chFr = pickle.load(open('Pickle_files/chFr.pickle','rb'))

Proj = pickle.load(open('Pickle_files/Proj.pickle','rb'))
cat = pickle.load(open('Pickle_files/cat.pickle','rb'))
acEle = pickle.load(open('Pickle_files/acEle.pickle','rb'))
acAct = pickle.load(open('Pickle_files/acAct.pickle','rb'))

ProjD = pickle.load(open('Pickle_files/ProjD.pickle','rb'))
catD = pickle.load(open('Pickle_files/catD.pickle','rb'))
acEleD = pickle.load(open('Pickle_files/acEleD.pickle','rb'))
acActD = pickle.load(open('Pickle_files/acActD.pickle','rb'))

ProjF = pickle.load(open('Pickle_files/ProjF.pickle','rb'))
catF = pickle.load(open('Pickle_files/catF.pickle','rb'))
acEleF = pickle.load(open('Pickle_files/acEleF.pickle','rb'))
acActF = pickle.load(open('Pickle_files/acActF.pickle','rb'))

TTBD_mid = pickle.load(open('Pickle_files/TTBD_mid.pickle','rb'))
TTBD_act = pickle.load(open('Pickle_files/TTBD_act.pickle','rb'))

yearAr = []
tyBoardAr = []
grAr = []
sbAr = []
chAr = []

ProjAr = []
catAr = []
acEleAr = []
acActAr = []

for i in year:
	if i not in yearAr:
		yearAr.append(i)

for i in tyBoard:
	if i not in tyBoardAr:
		tyBoardAr.append(i[2:6])

for i in grade:
	if i[6:8] not in grAr:
		grAr.append(i[6:8])

for i in subject:
	if i[8:11] not in sbAr:
		sbAr.append(i[8:11])

for i in chapter:
	if i[11:13] not in chAr:
		chAr.append(i[11:13])

for i in Proj:
	if i not in ProjAr:
		ProjAr.append(i)

for i in cat:
	if i not in catAr:
		catAr.append(i)

for i in acEle:
	if i not in acEleAr:
		acEleAr.append(i)

for i in acAct:
	if i not in acActAr:
		acActAr.append(i)

ProjMID = midDataProc.midData(L4_mids)

colorArray = colorAr.colorAr
colorLen = len(colorArray)

df = pd.read_excel(r'Machine_model/Sheets/Grade_sheet.xls')
grades = df.head()
gr = []

ind = 0
for i in grades:
	if ind != 0:
		gr.append(i)
	ind += 1

df_action = pd.read_excel(r'Machine_model/Sheets/Action_sheet.xls')
actions = df_action.head()
ac = []

ind = 0
for i in actions:
	if ind != 0:
		ac.append(i)
	ind += 1

df_element = pd.read_excel(r'Machine_model/Sheets/Element_sheet.xls')
elements = df_element.head()
ele = []

ind = 0
for i in elements:
	if ind != 0:
		ele.append(i)
	ind += 1

df_sub = pd.read_excel(r'Machine_model/Sheets/Subject_sheet.xls')
subs = df_sub.head()
sb = []

df_actMid = pd.read_excel(r'Machine_model/Sheets/actMid.xls')
mids = df_actMid['MIDS'].unique()

ind = 0
for i in subs:
	if ind != 0:
		sb.append(i)
	ind += 1

empName = df['Emp_name']

app.layout = html.Div(children=[
	html.Div(
		html.H1(
				children = 'Project-Analysis',
				style = {'textAlign':'center'}
				),
		className = 'jumbotron'
		),

	html.Div([

			html.Div([
				html.Label("Select Year"),
				dcc.Dropdown(
					id='yearId',
					options = [{'label':i, 'value':i} for i in yearAr],
					value='All'
					),
				], style={'width':'19%','float':'center','display':'inline-block','padding-left' : '70px'}),

			html.Div([
				html.Label("Select Board"),
				dcc.Dropdown(
					id='tyBoardId',
					options = [{'label':i, 'value':i} for i in tyBoardAr],
					value='All'
					),
				], style={'width':'19%','float':'center','display':'inline-block','padding-left' : '10px'}),

			html.Div([
				html.Label("Select Grade"),
				dcc.Dropdown(
					id='grId',
					options = [{'label':i, 'value':i} for i in grAr],
					value='All'
					),
				], style={'width':'19%','float':'center','display':'inline-block','padding-left' : '10px'}),

			html.Div([
				html.Label("Select Subject"),
				dcc.Dropdown(
					id='sbId',
					options = [{'label':i, 'value':i} for i in sbAr],
					value='All'
					),
				], style={'width':'19%','float':'center','display':'inline-block','padding-left' : '10px'}),

			html.Div([
				html.Label("Select Chapter"),
				dcc.Dropdown(
					id='chId',
					options = [{'label':i, 'value':i} for i in chAr],
					value='All'
					),
				], style={'width':'19%','float':'center','display':'inline-block','padding-left' : '10px'}),
	],style={'borderBottom': 'thin lightgrey solid',
	        	'backgroundColor': 'rgb(250, 250, 250)',
	        	'padding': '10px 5px'}),
	html.Div([

			html.Div([
				html.Label("Select Project"),
				dcc.Dropdown(
					id='ProjId',
					options = [{'label':i, 'value':i} for i in Proj],
					value='All'
					),
				], style={'width':'24%','float':'center','display':'inline-block','padding-left' : '70px'}),

			html.Div([
				html.Label("Select Category"),
				dcc.Dropdown(
					id='catId',
					options = [{'label':i, 'value':i} for i in cat],
					value='All'
					),
				], style={'width':'24%','float':'center','display':'inline-block','padding-left' : '10px'}),

			html.Div([
				html.Label("Select Element"),
				dcc.Dropdown(
					id='acEleId',
					options = [{'label':i, 'value':i} for i in acEle],
					value='All'
					),
				], style={'width':'24%','float':'center','display':'inline-block','padding-left' : '10px'}),

			html.Div([
				html.Label("Select Action"),
				dcc.Dropdown(
					id='acActId',
					options = [{'label':i, 'value':i} for i in acAct],
					value='All'
					),
				], style={'width':'24%','float':'center','display':'inline-block','padding-left' : '10px'}),

	],style={'borderBottom': 'thin lightgrey solid',
	        	'backgroundColor': 'rgb(250, 250, 250)',
	        	'padding': '10px 5px'}),
	html.Div([
		html.H1(
			children = 'Number of days left for completion',
			style = {'textAlign':'center'}
			),
		html.H3(
				id = 'ReqDays-graph',
				style = {'textAlign':'center'}
				),
		],className = 'well'),

	html.Div([
		html.Div([
			dcc.Graph(
				id = 'Fraction-graph'
				)
			],style={'width':'49%','display':'inline-block','padding':'0 20'}),

		html.Div([
			dcc.Graph(
				id = 'Fraction-graph-Ac'
				)
			],style={'width':'49%','float':'right','display':'inline-block','padding':'0 20'})
		],className = 'well'),

	html.Div([
		html.Div([
			dcc.Graph(
				id = 'Progress-graph',
				)
			],style={'width':'49%','display':'inline-block','padding':'0 20'}),

		html.Div([
			dcc.Graph(
				id = 'Progress-graph-Ac',
				)
			],style={'width':'49%','float':'right','display':'inline-block','padding':'0 20'})
	],className = 'well'),

	html.Div([
		html.Div([
			dcc.Graph(
				id = 'Progress-Slope-graph',
				)
			],style={'width':'49%','display':'inline-block','padding':'0 20'}),

		html.Div([
			dcc.Graph(
				id = 'Progress-Slope-graph-Ac',
				)
			],style={'width':'49%','float':'right','display':'inline-block','padding':'0 20'}),
	],className = 'well'),


    html.Div(
		html.H1(
				children = 'DWA-Predictions',
				style = {'textAlign':'center'}
				),
		className = 'jumbotron'
		),

    html.Div([
    	html.Div([
    		html.Label("Select employee"),
    		dcc.Dropdown(
				id='empNameMulti',
				options = [{'label':i, 'value':i} for i in empName],
				value='Select employee name',
				multi=True
				)
    		],style={'width':'49%','display':'inline-block'}),

    	html.Div([
    		html.Label("Select MID"),
    		dcc.Dropdown(
				id='actMidId',
				options = [{'label':i,'value':i} for i in mids],
				value='Select mid name'
				)
    		],style={'width':'49%','float':'right','display':'inline-block'})

    	],style={'borderBottom': 'thin lightgrey solid',
        	'backgroundColor': 'rgb(250, 250, 250)',
        	'padding': '10px 5px'}),

    html.Div([
    	html.Div([
    		dcc.Graph(
    			id = 'OutputTest',
    			)
    		],style={'width':'100%','display':'inline-block','padding':'0 20'})
    	],className = 'well'),

    html.Div([
    	html.Div([
    		html.Label("Select Employee"),
    		dcc.Dropdown(
				id='nameAr',
				options = [{'label':i,'value':i} for i in empName],
				value='Select employee name',
				multi=True
				)
    		],style={'width':'59%','float':'centre','display':'inline-block'}),

    	html.Div([
    		html.Label("Select MID"),
    		dcc.Dropdown(
				id='midValue',
				options = [{'label':i, 'value':i} for i in mids],
				value='Select mid name'
				)
    		],style={'width':'39%','float':'centre','display':'inline-block'}),
    	],style={'borderBottom': 'thin lightgrey solid',
        	'backgroundColor': 'rgb(250, 250, 250)',
        	'padding': '10px 5px'}),

    html.Div([
    	html.Div([
    		html.Label("Select Element"),
    		dcc.Dropdown(
    			id = 'SelEle',
    			options = [{'label':i, 'value':i} for i in ele],
				value='Select ele name'
				)  
    		],style={'width':'39%','float':'centre','display':'inline-block'}),

    	html.Div([
    		html.Label("Select Action"),
    		dcc.Dropdown(
    			id = 'SelAc',
    			options = [{'label':i, 'value':i} for i in ac],
				value='Select ac name'
				)  
    		],style={'width':'39%','float':'centre','display':'inline-block'}),
    	html.Div([
    		html.Label("Select Combination"),
    		dcc.Dropdown(
    			id = 'bestComb',
    			options = [{'label':i, 'value':i} for i in range(1,11)],
				value='1'
				)  
    		],style={'width':'9%','float':'centre','display':'inline-block'}),

    	html.Div([
    		html.Label("Select Top combinations"),
    		dcc.Dropdown(
    			id = 'topComb',
    			options = [{'label':i, 'value':i} for i in range(1,11)],
				value='1'
				)  
    		],style={'width':'9%','float':'centre','display':'inline-block'})

    	],style={'borderBottom': 'thin lightgrey solid',
        	'backgroundColor': 'rgb(250, 250, 250)',
        	'padding': '10px 5px'}),

    html.Div([
    	html.Div([
    		dcc.Graph(
    			id = 'OutputPredGraph'
    			)
    		],style={'width':'100%','display':'inline-block','padding':'0 20'})
    	],className = 'well'),

    html.Div([
    	html.Div([
    		html.Label("Select Mid"),
    		dcc.Dropdown(
				id='midSel',
				options = [{'label':i,'value':i} for i in mids],
				value='Select mid value',
				)
    		],style={'width':'29%','float':'centre','display':'inline-block'}),

    	html.Div(id = 'OutputSlider',
    		style={'width':'69%','float':'centre','display':'inline-block','padding-left': '10px','padding-bottom': '5px'}),
    	],style={'borderBottom': 'thin lightgrey solid',
        	'backgroundColor': 'rgb(250, 250, 250)',
        	'padding': '10px 5px'}),

     html.Div([
    	html.Div([
    		html.Label("Select Element"),
    		dcc.Dropdown(
    			id = 'SelElement',
    			options = [{'label':i, 'value':i} for i in ele],
				value='Select ele name'
				)  
    		],style={'width':'39%','float':'centre','display':'inline-block'}),

    	html.Div([
    		html.Label("Select Action"),
    		dcc.Dropdown(
    			id = 'SelAction',
    			options = [{'label':i, 'value':i} for i in ac],
				value='Select ac name'
				)  
    		],style={'width':'39%','float':'centre','display':'inline-block'}),
    	html.Div([
    		html.Label("Select Number of employees"),
    		dcc.Dropdown(
    			id = 'numEmps',
    			options = [{'label':i, 'value':i} for i in range(1,11)],
				value='1'
				)  
    		],style={'width':'9%','float':'centre','display':'inline-block'}),

    	html.Div([
    		html.Label("Select Days"),
    		dcc.Dropdown(
    			id = 'Days',
    			options = [{'label':i, 'value':i} for i in range(1,61)],
				value='1'
				)  
    		],style={'width':'9%','float':'centre','display':'inline-block'})

    	],style={'borderBottom': 'thin lightgrey solid',
        	'backgroundColor': 'rgb(250, 250, 250)',
        	'padding': '10px 5px'}),

     html.Div([
    	html.Div(
    		daq.Gauge(
        	id='OutputNum',
        	color="#FF687A",
        	size=300,
        	label="Effort required!!",
        	value=0,
    		),
    		style={'width':'100%','display':'inline-block','padding':'0 20'})
    	],className = 'well'),



    ],className = 'well')

@app.callback(
	dash.dependencies.Output('ReqDays-graph','children'),
	[dash.dependencies.Input('yearId','value'),
	dash.dependencies.Input('tyBoardId','value'),
	dash.dependencies.Input('grId','value'),
	dash.dependencies.Input('sbId','value'),
	dash.dependencies.Input('chId','value')]
	)

def reqDays(yearV,tyBoardV,grV,sbV,chV):

	finVal = 0

	def uniGraph(valDict,selVal):
		graphsAr = ""

		numVal = len(selVal)

		if numVal == 2:
			temp = 0
		elif numVal == 6:
			temp = 1
		elif numVal == 8:
			temp = 2
		elif numVal == 11:
			temp = 3
		else:
			temp = 4

		for i in valDict.keys():
			xpAr = []
			dateAr = []
			lenVal = len(list(selVal))
			if selVal == i[0:lenVal]:
				for j in valDict[i]:
					xpAr.append((valDict[i][j]/float(TTBD_mid[temp][selVal][0]))*100)
					dateAr.append(j)

				reqDays = xpAr[-1]-xpAr[0]
				reqDays = reqDays/len(xpAr)
				leftTask = (100-xpAr[-1])/reqDays
				graphsAr +=i +' - '+str(round(leftTask/100,2))+" "

		return graphsAr

	arrayPar = [yearV,tyBoardV,grV,sbV,chV]
	valPar = []

	for i in arrayPar:
		if i != 'All' and type(i) == str:
			valPar.append(i)

	if len(valPar) == 1:
		finVal = uniGraph(tyBoard,valPar[0])
	elif len(valPar) == 2:
		dumVal = "".join(valPar)
		finVal = uniGraph(grade,dumVal)
	elif len(valPar) == 3:
		dumVal = "".join(valPar)
		finVal = uniGraph(subject,dumVal) 
	elif len(valPar) == 4:
		dumVal = "".join(valPar)
		finVal = uniGraph(chapter,dumVal)
	elif len(valPar) == 5:
		dumVal = "".join(valPar)
		finVal = uniGraph(chapter,dumVal)

	return finVal


@app.callback(
	dash.dependencies.Output('Fraction-graph','figure'),
	[dash.dependencies.Input('yearId','value'),
	dash.dependencies.Input('tyBoardId','value'),
	dash.dependencies.Input('grId','value'),
	dash.dependencies.Input('sbId','value'),
	dash.dependencies.Input('chId','value')]
	)

def PiePlot(yearV,tyBoardV,grV,sbV,chV):
	finVal = []

	def uniGraph(valDict):
		graphsAr = []
		lables = []
		values = []
		for i in valDict.keys():
			lables.append(i)
			values.append(valDict[i])

		graphsAr.append(go.Pie(
				labels = lables,
				values = values,
				name = "Percentage Taken by Tasks",
				hole=.4, 
				hoverinfo="label+percent+name"
				))
		return graphsAr


	if yearV != 'All' and (tyBoardV == 'All' or type(tyBoardV) != str ) and (grV == 'All' or type(grV) != str) and (sbV == 'All' or type(sbV) != str) and (chV == 'All' or type(chV) != str) and type(yearV) == str:
		finVal = uniGraph(yearFr)
	elif yearV != 'All' and tyBoardV != 'All' and (grV == 'All' or type(grV) != str) and (sbV == 'All' or type(sbV) != str) and (chV == 'All' or type(chV) != str) and type(yearV) == str and type(tyBoardV) == str:
		finVal = uniGraph(tyBoardFr)
	elif yearV != 'All' and tyBoardV != 'All' and grV != 'All' and (sbV == 'All' or type(sbV) != str) and (chV == 'All' or type(chV) != str) and type(yearV) == str and type(tyBoardV) == str and type(grV) == str:
		finVal = uniGraph(grFr) 
	elif yearV != 'All' and tyBoardV != 'All' and grV != 'All' and sbV != 'All' and (chV == 'All' or type(chV) != str) and type(yearV) == str and type(tyBoardV) == str and type(grV) == str and type(sbV) == str:
		finVal = uniGraph(sbFr)
	elif yearV != 'All' and tyBoardV != 'All' and grV != 'All' and sbV != 'All' and chV != 'All' and type(yearV) == str and type(tyBoardV) == str and type(grV) == str and type(sbV) == str and type(chV) == str:
		finVal = uniGraph(chFr)

	return {
	'data' : finVal,
	'layout' : go.Layout(
		title_text = f'Fraction of task done in a project',
		annotations=[dict(text='Proj-status',x=0.18, y=0.5, font_size=20, showarrow=False)]
		),
	}

@app.callback(
	dash.dependencies.Output('Fraction-graph-Ac','figure'),
	[dash.dependencies.Input('ProjId','value'),
	dash.dependencies.Input('catId','value'),
	dash.dependencies.Input('acEleId','value'),
	dash.dependencies.Input('acActId','value')]
	)

def PiePlotAc(ProjV,catV,acEleV,acActV):
	finVal = []

	def uniGraph(valDict):
		graphsAr = []
		lables = []
		values = []
		for i in valDict.keys():
			lables.append(i)
			values.append(valDict[i])

		graphsAr.append(go.Pie(
				labels = lables,
				values = values,
				name = "Percentage Taken by Tasks",
				hole=.4, 
				hoverinfo="label+percent+name"
				))
		return graphsAr

	if ProjV != 'All' and (catV == 'All' or type(catV) != str) and (acEleV == 'All'or type(acEleV) != str) and (acActV == 'All' or type(acActV) != str) and type(ProjV) == str :
		finVal = uniGraph(ProjF)
	elif ProjV != 'All' and catV != 'All' and (acEleV == 'All'or type(acEleV) != str) and (acActV == 'All' or type(acActV) != str) and type(ProjV) == str and type(catV) == str:
		finVal = uniGraph(catF)
	elif ProjV != 'All' and catV != 'All' and acEleV != 'All' and (acActV == 'All' or type(acActV) != str) and type(ProjV) == str and type(catV) == str and type(acEleV) == str:
		finVal = uniGraph(acEleF) 
	elif ProjV != 'All' and catV != 'All' and acEleV != 'All' and acActV != 'All' and type(ProjV) == str and type(catV) == str and type(acEleV) == str and type(acActV) == str:
		finVal = uniGraph(acActF)

	return {
	'data' : finVal,
	'layout' : go.Layout(
		title_text = f'Fraction of task done in a project',
		annotations=[dict(text='Proj-status',x=0.18, y=0.5, font_size=20, showarrow=False)]
		),
	}

@app.callback(
	dash.dependencies.Output('Progress-graph','figure'),
	[dash.dependencies.Input('yearId','value'),
	dash.dependencies.Input('tyBoardId','value'),
	dash.dependencies.Input('grId','value'),
	dash.dependencies.Input('sbId','value'),
	dash.dependencies.Input('chId','value')]
	)

def ScatterPlot(yearV,tyBoardV,grV,sbV,chV):
	finVal = []

	def uniGraph(valDict,selVal):
		graphsAr = []

		numVal = len(selVal)

		if numVal == 2:
			temp = 0
		elif numVal == 6:
			temp = 1
		elif numVal == 8:
			temp = 2
		elif numVal == 11:
			temp = 3
		else:
			temp = 4

		for i in valDict.keys():
			xpAr = []
			dateAr = []
			lenVal = len(list(selVal))
			if selVal == i[0:lenVal]:
				for j in valDict[i]:
					xpAr.append((valDict[i][j]/float(TTBD_mid[temp][selVal][0]))*100)
					dateAr.append(j)

				reqDays = 0
				for k in range(len(xpAr)):
					if k+1 >= len(xpAr):
						break
					reqDays += xpAr[k+1]-xpAr[k]
				reqDays = reqDays/len(xpAr)
				leftTask = (100-xpAr[-1])/reqDays

				graphsAr.append(go.Scatter(
					x = dateAr,
					y = xpAr,
					text = i,
					mode = 'lines+markers',
					opacity = 0.7,
					marker = {
						'size': 10,
                		'line': {'width': 0.5, 'color': 'white'}
					},
					name = i
					))
		return graphsAr

	arrayPar = [yearV,tyBoardV,grV,sbV,chV]
	valPar = []

	for i in arrayPar:
		if i != 'All' and type(i) == str:
			valPar.append(i)

	if len(valPar) == 1:
		finVal = uniGraph(tyBoard,valPar[0])
	elif len(valPar) == 2:
		dumVal = "".join(valPar)
		finVal = uniGraph(grade,dumVal)
	elif len(valPar) == 3:
		dumVal = "".join(valPar)
		finVal = uniGraph(subject,dumVal) 
	elif len(valPar) == 4:
		dumVal = "".join(valPar)
		finVal = uniGraph(chapter,dumVal)
	elif len(valPar) == 5:
		dumVal = "".join(valPar)
		finVal = uniGraph(chapter,dumVal)

	return {
	'data' : finVal,
	'layout' : go.Layout(
		title = f'Progress vs Dates(Mid)',
		xaxis = {
			'title' : 'Dates'
		},
		yaxis = {
			'title' : 'Progress'
		},
		hovermode = 'closest'
		),
	}

@app.callback(
	dash.dependencies.Output('Progress-graph-Ac','figure'),
	[dash.dependencies.Input('ProjId','value'),
	dash.dependencies.Input('catId','value'),
	dash.dependencies.Input('acEleId','value'),
	dash.dependencies.Input('acActId','value')]
	)

def ScatterPlotAc(projV,catV,acEleV,acActV):
	finVal = []
	dumVal = 0

	def uniGraph(valDict,selVal):
		graphsAr = []

		numVal = len(selVal.split('_'))

		if numVal == 1:
			temp = 0
		elif numVal == 2:
			temp = 1
		elif numVal == 3:
			temp = 2
		else:
			temp = 3

		for i in valDict.keys():
			xpAr = []
			dateAr = []

			if selVal in i:
				for j in valDict[i]:
					xpAr.append(valDict[i][j])
					dateAr.append(j)

				graphsAr.append(go.Scatter(
					x = dateAr,
					y = xpAr,
					text = i,
					mode = 'lines+markers',
					opacity = 0.7,
					marker = {
						'size': 10,
                		'line': {'width': 0.5, 'color': 'white'}
					},
					name = i
					))
		return graphsAr

	arrayPar = [projV,catV,acEleV,acActV]
	valPar = []

	for i in arrayPar:
		if i != 'All' and type(i) == str:
			valPar.append(i)

	if len(valPar) == 1:
		finVal = uniGraph(catD,valPar[0])
	elif len(valPar) == 2:
		dumVal = "_".join(valPar)
		finVal = uniGraph(acEleD,dumVal)
	elif len(valPar) == 3:
		dumVal = "_".join(valPar)
		finVal = uniGraph(acActD,dumVal) 
	elif len(valPar) == 4:
		dumVal = "_".join(valPar)
		finVal = uniGraph(acActD,dumVal)

	return {
	'data' : finVal,
	'layout' : go.Layout(
		title = f'Progress vs Dates(Activity)',
		xaxis = {
			'title' : 'Dates'
		},
		yaxis = {
			'title' : 'Xps'
		},
		hovermode = 'closest'
		),
	}

@app.callback(
	dash.dependencies.Output('Progress-Slope-graph','figure'),
	[dash.dependencies.Input('yearId','value'),
	dash.dependencies.Input('tyBoardId','value'),
	dash.dependencies.Input('grId','value'),
	dash.dependencies.Input('sbId','value'),
	dash.dependencies.Input('chId','value')]
	)

def ScatterPlotSlope(yearV,tyBoardV,grV,sbV,chV):
	finVal = []

	def uniGraph(valDict,selVal):
		graphsAr = []
		for i in valDict.keys():
			xpAr = []
			dateAr = []
			deltaXp = []
			deltaDays = []
			counter = 1
			lenVal = len(list(selVal))
			if selVal == i[0:lenVal]:
				for j in valDict[i]:
					xpAr.append(valDict[i][j])
					dateAr.append(j)

				for j in range(len(xpAr)):
					if j+1 == len(xpAr):
						break

					deltaXp.append(xpAr[j+1] - xpAr[j])
					deltaDays.append(str(counter)+' delta day')
					counter += 1

				graphsAr.append(go.Scatter(
					x = deltaDays,
					y = deltaXp,
					text = i,
					mode = 'lines+markers',
					opacity = 0.7,
					marker = {
						'size': 10,
                		'line': {'width': 0.5, 'color': 'white'}
					},
					name = i
					))
		return graphsAr

	arrayPar = [yearV,tyBoardV,grV,sbV,chV]
	valPar = []

	for i in arrayPar:
		if i != 'All' and type(i) == str:
			valPar.append(i)

	if len(valPar) == 1:
		finVal = uniGraph(tyBoard,valPar[0])
	elif len(valPar) == 2:
		dumVal = "".join(valPar)
		finVal = uniGraph(grade,dumVal)
	elif len(valPar) == 3:
		dumVal = "".join(valPar)
		finVal = uniGraph(subject,dumVal) 
	elif len(valPar) == 4:
		dumVal = "".join(valPar)
		finVal = uniGraph(chapter,dumVal)
	elif len(valPar) == 5:
		dumVal = "".join(valPar)
		finVal = uniGraph(chapter,dumVal)

	return {
	'data' : finVal,
	'layout' : go.Layout(
		title = f'Progress Slope vs Days(Mid)',
		xaxis = {
			'title' : 'Dates'
		},
		yaxis = {
			'title' : 'Rate'
		},
		hovermode = 'closest'
		),
	}

@app.callback(
	dash.dependencies.Output('Progress-Slope-graph-Ac','figure'),
	[dash.dependencies.Input('ProjId','value'),
	dash.dependencies.Input('catId','value'),
	dash.dependencies.Input('acEleId','value'),
	dash.dependencies.Input('acActId','value')]
	)

def ScatterPlotAc(projV,catV,acEleV,acActV):
	finVal = []

	def uniGraph(valDict,selVal):
		graphsAr = []
		for i in valDict.keys():
			xpAr = []
			dateAr = []
			deltaXp = []
			deltaDays = []
			counter = 1

			if selVal in i:
				for j in valDict[i]:
					xpAr.append(valDict[i][j])
					dateAr.append(j)

				for j in range(len(xpAr)):
					if j+1 == len(xpAr):
						break

					deltaXp.append(xpAr[j+1] - xpAr[j])
					deltaDays.append(str(counter)+' delta day')
					counter += 1

				graphsAr.append(go.Scatter(
					x = deltaDays,
					y = deltaXp,
					text = i,
					mode = 'lines+markers',
					opacity = 0.7,
					marker = {
						'size': 10,
                		'line': {'width': 0.5, 'color': 'white'}
					},
					name = i
					))
		return graphsAr

	arrayPar = [projV,catV,acEleV,acActV]
	valPar = []

	for i in arrayPar:
		if i != 'All' and type(i) == str:
			valPar.append(i)

	if len(valPar) == 1:
		finVal = uniGraph(catD,valPar[0])
	elif len(valPar) == 2:
		dumVal = "_".join(valPar)
		finVal = uniGraph(acEleD,dumVal)
	elif len(valPar) == 3:
		dumVal = "_".join(valPar)
		finVal = uniGraph(acActD,dumVal) 
	elif len(valPar) == 4:
		dumVal = "_".join(valPar)
		finVal = uniGraph(acActD,dumVal)

	return {
	'data' : finVal,
	'layout' : go.Layout(
		title = f'Progress Slope vs Days(Activity)',
		xaxis = {
			'title' : 'Dates'
		},
		yaxis = {
			'title' : 'Rate'
		},
		hovermode = 'closest'
		),
	}

@app.callback(
	dash.dependencies.Output('OutputTest','figure'),
    [dash.dependencies.Input('empNameMulti','value'),
    dash.dependencies.Input('actMidId','value'),
    ])

def outputTable(name,mid):
	tempOut = [[],[],[]]
	if name != 'Select employee name' and name != '' and mid != 'Select mid name' and mid != '':
		tempOut = suggestionStat.statGen(mid,name)
	if len(name) == 0 or mid == "":
		tempOut = [[],[],[]]


	return {
		'data' :[go.Bar(
			name ='Current days',
			x = tempOut[2],
			y = tempOut[1],
			marker_color = '#FF6F91'
			),
			go.Bar(
			name = 'Predicted days',
			x = tempOut[2],
			y = tempOut[0],
			marker_color = '#D65DB1'
			)
		],
		'layout' : go.Layout(
			title=f'Current v/s Predicted of mid {mid}',
			xaxis={
			'title' : 'Activity name'
			},
			yaxis={
			'title': 'Current/Predicted days'
			},
			hovermode='closest'
			),
	}


@app.callback(
	dash.dependencies.Output('OutputPredGraph','figure'),
    [dash.dependencies.Input('midValue','value'),
    dash.dependencies.Input('nameAr','value'),
    dash.dependencies.Input('SelEle','value'),
    dash.dependencies.Input('SelAc','value'),
    dash.dependencies.Input('bestComb','value'),
    dash.dependencies.Input('topComb','value')
    ])

def outputGraph(mid,name,selEle,selAc,comb,topComb):
	graphs = []
	tempOut = [[],[],[]]

	if name != 'Select employee name' and mid != 'Select mid name' and selEle != 'Select ele name' and selAc != 'Select ac name':
		tempOut = suggestionStat.suggStat(mid,name,comb,topComb,selEle,selAc)
	if len(name) == 0 or mid == "":
		tempOut = [[],[],[]]

	val1 = tempOut[0]
	val2 = tempOut[1]
	val3 = tempOut[2]

	ind = random.randint(0,100)
	for i in range(len(val1)):
		ind += 5
		graphs.append(go.Bar(
				name = val3[i],
				x = val1[i],
				y = val2[i],
				marker_color = colorArray[ind]
				))

	return {
	'data' : graphs,
	'layout' : go.Layout(
		title = f'Predicted days of top {topComb} employees in combination of {comb}',
		xaxis = {
			'title' : 'Employee combination'
		},
		yaxis = {
			'title' : 'Predicted days'
		},
		hovermode = 'closest'
		),
	}

@app.callback(dash.dependencies.Output('OutputSlider',component_property='children'),
    [dash.dependencies.Input('midSel','value'),
    dash.dependencies.Input('SelElement','value'),
    dash.dependencies.Input('SelAction','value'),
    dash.dependencies.Input('numEmps','value'),
    ])

def outputSlid(mid,selEle,selAc,emps):
	emps = int(emps)*4
	if mid != 'Select mid value' and selEle != 'Select ele name' and selAc != 'Select ac name':
		return dcc.Slider(
			id = 'sliderId',
			min = 0,
			max = emps,
			marks = {i:'{}'.format(i*0.25) for i in range(emps)},
			step = None,
			updatemode = 'drag'
			),

@app.callback(dash.dependencies.Output('OutputNum','value'),
    [dash.dependencies.Input('midSel','value'),
    dash.dependencies.Input('SelElement','value'),
    dash.dependencies.Input('SelAction','value'),
    dash.dependencies.Input('numEmps','value'),
    dash.dependencies.Input('Days','value'),
    #dash.dependencies.Input('sliderId','value')
    ])

def OutputNum(midSel,SelElement,SelAction,numEmps,days):
	retNum = 0
	numEmps = int(numEmps)
	days = int(days)
	if midSel != 'Select mid value' and SelElement != 'Select ele name' and SelAction != 'Select ac name':
		retNum = suggestionText.possSugg(midSel,SelElement,SelAction,numEmps,days,0.8)

	return retNum

@server.route('/')
def index():
	return flask.render_template('index.html')

@server.route('/next/')
def welcome():
	return flask.render_template('welcome.html')

@server.route('/dashboard-view')
def render_dashboard():
	return flask.redirect('/dashboard')

if __name__ == '__main__':
	server.run(debug=True)
