import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
 
import random
import string 

external_stylesheets =[dbc.themes.BOOTSTRAP]
res = {}
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

				html.Div('Input URL'),
				dbc.Textarea(id='ip', placeholder='Enter Input'),
				html.Hr(),
				html.Button(id='submit_btn', children = 'Submit', n_clicks = 0),

				html.Div(id='showtext')
			])

def get_data(key,val):
	res = {}
	res[key]=val
	return res

@app.callback(Output('showtext','children'),
			[Input('submit_btn','n_clicks')], [State('ip','value')])
def get_text(n_clicks, value):
	if n_clicks and value:
		if not res:
			chars = "".join([random.choice(string.digits[:26]) for i in range(15)])
			res[chars] = value
			return html.P(chars)
		else:
			try:
				return html.P(res[value])
			except Exception as e:
				chars = "".join([random.choice(string.digits[:26]) for i in range(15)])
				res[chars] = value
				return html.P(chars)
			
		

if __name__ == '__main__':
    app.run_server(debug=True, port=8051)