import numpy as np
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html

# Create data
def gaussian(x,mu,sig):
    return  np.exp(-0.5*np.power((x-mu)/sig, 2))

xLinGs = np.linspace(-1.0,1,1000)
xLogGs = np.logspace(0,4,10000)
xGs = np.concatenate((xLinGs,xLogGs))
yGs = gaussian(xGs,0,0.25) + gaussian(xGs,10,2.5) + \
    gaussian(xGs,100,25) + gaussian(xGs,1000,250) + \
    gaussian(xGs,10000,2500)

# Create figure
fig = go.Figure()
fig.add_trace(
    go.Scatter(x=xGs, y=yGs, name='Linear', xaxis='x1', line_color='red')
)
fig.add_trace(
    go.Scatter(x=xGs, y=yGs, name='Log', xaxis='x2', line_color='blue')
)
domFrac = 1.0/3.0 # distance from 0 to 1 same as 10 to 100
fig.update_layout(
    title_text='Simple Symmetrical Log (symlog) Example',
    xaxis={
        'domain':[0,domFrac],
        'range':[-1.0,0.999] # prevent an additional '1' on x-axis
    },
    xaxis2={
        'domain':[domFrac,1],
        'range':[0,4],
        'title':'Time',
        'type':'log',
        'dtick':'D1'
    },
    yaxis={
        'title':'Amplitude'
    }
)

# Create app
app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

# Run app
app.run_server(debug=True)