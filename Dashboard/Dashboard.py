import dash
import dash_core_components as dcc
import dash_html_components as html 
import dash_daq as daq
import pandas as pd
import plotly.graph_objs as go

import flask

import pickle

external_stylesheets = ["https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css",
"https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js",
"https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

year = pickle.load(open('Pickle_files/yearD.pickle','rb'))
tyBoard = pickle.load(open('Pickle_files/tyBoardD.pickle','rb'))
gr = pickle.load(open('Pickle_files/grD.pickle','rb'))
sb = pickle.load(open('Pickle_files/sbD.pickle','rb'))
ch = pickle.load(open('Pickle_files/chD.pickle','rb'))

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

for i in gr:
	if i[6:8] not in grAr:
		grAr.append(i[6:8])

for i in sb:
	if i[8:11] not in sbAr:
		sbAr.append(i[8:11])

for i in ch:
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
				dcc.Dropdown(
					id='yearId',
					options = [{'label':i, 'value':i} for i in yearAr],
					value='All'
					),
				], style={'width':'19%','float':'center','display':'inline-block','padding-left' : '70px'}),

			html.Div([
				dcc.Dropdown(
					id='tyBoardId',
					options = [{'label':i, 'value':i} for i in tyBoardAr],
					value='All'
					),
				], style={'width':'19%','float':'center','display':'inline-block','padding-left' : '10px'}),

			html.Div([
				dcc.Dropdown(
					id='grId',
					options = [{'label':i, 'value':i} for i in grAr],
					value='All'
					),
				], style={'width':'19%','float':'center','display':'inline-block','padding-left' : '10px'}),

			html.Div([
				dcc.Dropdown(
					id='sbId',
					options = [{'label':i, 'value':i} for i in sbAr],
					value='All'
					),
				], style={'width':'19%','float':'center','display':'inline-block','padding-left' : '10px'}),

			html.Div([
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
				dcc.Dropdown(
					id='ProjId',
					options = [{'label':i, 'value':i} for i in Proj],
					value='All'
					),
				], style={'width':'24%','float':'center','display':'inline-block','padding-left' : '70px'}),

			html.Div([
				dcc.Dropdown(
					id='catId',
					options = [{'label':i, 'value':i} for i in cat],
					value='All'
					),
				], style={'width':'24%','float':'center','display':'inline-block','padding-left' : '10px'}),

			html.Div([
				dcc.Dropdown(
					id='acEleId',
					options = [{'label':i, 'value':i} for i in acEle],
					value='All'
					),
				], style={'width':'24%','float':'center','display':'inline-block','padding-left' : '10px'}),

			html.Div([
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
		html.Div([
			dcc.Graph(
				id = 'Fraction-graph'
				)
			],style={'width':'49%','display':'inline-block','padding':'0 20'})
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


	],className = 'well')

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


	if yearV != 'All' and tyBoardV == 'All' and grV == 'All' and sbV == 'All' and chV == 'All' and type(yearV) == str and type(tyBoardV) == str and type(grV) == str and type(sbV) == str and type(chV) == str:
		finVal = uniGraph(yearFr)
	elif yearV != 'All' and tyBoardV != 'All' and grV == 'All' and sbV == 'All' and chV == 'All' and type(yearV) == str and type(tyBoardV) == str and type(grV) == str and type(sbV) == str and type(chV) == str:
		finVal = uniGraph(tyBoardFr)
	elif yearV != 'All' and tyBoardV != 'All' and grV != 'All' and sbV == 'All' and chV == 'All' and type(yearV) == str and type(tyBoardV) == str and type(grV) == str and type(sbV) == str and type(chV) == str:
		finVal = uniGraph(grFr) 
	elif yearV != 'All' and tyBoardV != 'All' and grV != 'All' and sbV != 'All' and chV == 'All' and type(yearV) == str and type(tyBoardV) == str and type(grV) == str and type(sbV) == str and type(chV) == str:
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
		for i in valDict.keys():
			xpAr = []
			dateAr = []
			lenVal = len(list(selVal))
			if selVal == i[0:lenVal]:
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


	if yearV != 'All' and tyBoardV == 'All' and grV == 'All' and sbV == 'All' and chV == 'All' and type(yearV) == str:
		finVal = uniGraph(tyBoard,yearV)
	elif yearV != 'All' and tyBoardV != 'All' and grV == 'All' and sbV == 'All' and chV == 'All' and type(yearV) == str and type(tyBoardV) == str:
		dumVal = yearV+tyBoardV
		finVal = uniGraph(gr,dumVal)
	elif yearV != 'All' and tyBoardV != 'All' and grV != 'All' and sbV == 'All' and chV == 'All' and type(yearV) == str and type(tyBoardV) == str and type(grV) == str:
		dumVal = yearV+tyBoardV+grV
		finVal = uniGraph(sb,dumVal) 
	elif yearV != 'All' and tyBoardV != 'All' and grV != 'All' and sbV != 'All' and chV == 'All' and type(yearV) == str and type(tyBoardV) == str and type(grV) == str and type(sbV) == str:
		dumVal = yearV+tyBoardV+grV+sbV
		finVal = uniGraph(ch,dumVal)
	elif yearV != 'All' and tyBoardV != 'All' and grV != 'All' and sbV != 'All' and chV != 'All' and type(yearV) == str and type(tyBoardV) == str and type(grV) == str and type(sbV) == str and type(chV) == str:
		dumVal = yearV+tyBoardV+grV+sbV+chV
		finVal = uniGraph(ch,dumVal)

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

	def uniGraph(valDict,selVal):
		graphsAr = []
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

	if projV != 'All' and catV == 'All' and acEleV == 'All' and acActV == 'All' and type(projV) == str:
		finVal = uniGraph(catD,projV)
	elif projV != 'All' and catV != 'All' and acEleV == 'All' and acActV == 'All' and type(projV) == str and type(catV) == str:
		dumVal = "_".join([projV,catV])
		finVal = uniGraph(acEleD,dumVal)
	elif projV != 'All' and catV != 'All' and acEleV != 'All' and acActV == 'All' and type(projV) == str and type(catV) == str and type(acEleV) == str:
		dumVal = "_".join([projV,catV,acEleV])
		finVal = uniGraph(acActD,dumVal) 
	elif projV != 'All' and catV != 'All' and acEleV != 'All' and acActV != 'All' and type(projV) == str and type(catV) == str and type(acEleV) == str and type(acActV) == str:
		dumVal = "_".join([projV,catV,acEleV,acActV])
		finVal = uniGraph(acActD,dumVal)

	return {
	'data' : finVal,
	'layout' : go.Layout(
		title = f'Progress vs Dates(Activity)',
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

	if yearV != 'All' and tyBoardV == 'All' and grV == 'All' and sbV == 'All' and chV == 'All' and type(yearV) == str:
		finVal = uniGraph(tyBoard,yearV)
	elif yearV != 'All' and tyBoardV != 'All' and grV == 'All' and sbV == 'All' and chV == 'All' and type(yearV) == str and type(tyBoardV) == str:
		dumVal = yearV+tyBoardV
		finVal = uniGraph(gr,dumVal)
	elif yearV != 'All' and tyBoardV != 'All' and grV != 'All' and sbV == 'All' and chV == 'All' and type(yearV) == str and type(tyBoardV) == str and type(grV) == str:
		dumVal = yearV+tyBoardV+grV
		finVal = uniGraph(sb,dumVal) 
	elif yearV != 'All' and tyBoardV != 'All' and grV != 'All' and sbV != 'All' and chV == 'All' and type(yearV) == str and type(tyBoardV) == str and type(grV) == str and type(sbV) == str:
		dumVal = yearV+tyBoardV+grV+sbV
		finVal = uniGraph(ch,dumVal)
	elif yearV != 'All' and tyBoardV != 'All' and grV != 'All' and sbV != 'All' and chV != 'All' and type(yearV) == str and type(tyBoardV) == str and type(grV) == str and type(sbV) == str and type(chV) == str:
		dumVal = yearV+tyBoardV+grV+sbV+chV
		finVal = uniGraph(ch,dumVal)

	return {
	'data' : finVal,
	'layout' : go.Layout(
		title = f'Progress Slope vs Days(Mid)',
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

	if projV != 'All' and catV == 'All' and acEleV == 'All' and acActV == 'All' and type(projV) == str:
		finVal = uniGraph(catD,projV)
	elif projV != 'All' and catV != 'All' and acEleV == 'All' and acActV == 'All' and type(projV) == str and type(catV) == str:
		dumVal = "_".join([projV,catV])
		finVal = uniGraph(acEleD,dumVal)
	elif projV != 'All' and catV != 'All' and acEleV != 'All' and acActV == 'All' and type(projV) == str and type(catV) == str and type(acEleV) == str:
		dumVal = "_".join([projV,catV,acEleV])
		finVal = uniGraph(acActD,dumVal) 
	elif projV != 'All' and catV != 'All' and acEleV != 'All' and acActV != 'All' and type(projV) == str and type(catV) == str and type(acEleV) == str and type(acActV) == str:
		dumVal = "_".join([projV,catV,acEleV,acActV])
		finVal = uniGraph(acActD,dumVal)

	return {
	'data' : finVal,
	'layout' : go.Layout(
		title = f'Progress Slope vs Days(Activity)',
		xaxis = {
			'title' : 'Dates'
		},
		yaxis = {
			'title' : 'Progress'
		},
		hovermode = 'closest'
		),
	}






if __name__ == '__main__':
	app.run_server(debug=True)