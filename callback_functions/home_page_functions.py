import pandas as pd
import datetime as dt
import dash_bootstrap_components as dbc
from dash import Input, Output
from callback_functions.main_app_class import main_app
from dash.exceptions import PreventUpdate
import plotly.graph_objects as go


# creating a mock dataframe to create dashoard
row_index = [1,2,3,4]

columns_labels = ['Progress','Wave','Milestone Name','Milestone Date','Target Design Threshold','Field Mapping Threshold','Rule Build Threshold','Threshold to meet']

data = [ 
        ['Current','NA','Mock 1',dt.datetime(2024,2,11),87.93,89.65,85.34,90,], 
        ['Future','NA','Mock 2',dt.datetime(2024,4,12),97.64,89.65,85.34,95,], 
        ['Future','NA','Dress Rehearsal',dt.datetime(2024,6,13),77.64,89.65,85.34,100,], 
        ['Future','NA','Go live',dt.datetime(2024,4,14),57.64,89.65,85.34,100,] 
    ]

mock_data = pd.DataFrame(data,row_index,columns_labels)

@main_app.app.callback(
    Output('gauge_chart_1', 'figure'),
    Output('gauge_chart_2', 'figure'),
    Output('gauge_chart_3', 'figure'),
    Output('number_chart', 'figure'),
    Input('url1', 'pathname')
)
def update_output(pathname):
    if pathname != main_app.environment_details ["home_page_link"]:
        raise PreventUpdate
    
    gauge1 = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = 54,
    domain = {'x': [0, 1], 'y': [0, 1]},
    gauge={'axis': {'range': [None, 100]}},
    title = {'text': "Target Design % Complete"}))
    
    gauge1.update_layout(margin=dict(b=1,r=8,l=8,t=45))

    gauge2 = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = 84,
    domain = {'x': [0, 1], 'y': [0, 1]},
    gauge={'axis': {'range': [None, 100]}},
    title = {'text': "Field Mapping % Complete"}))
    
    gauge2.update_layout(margin=dict(b=1,r=8,l=8,t=45))

    gauge3 = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = 64,
    domain = {'x': [0, 1], 'y': [0, 1]},
    gauge={'axis': {'range': [None, 100]}},
    title = {'text': "Rule Build % Complete"}))
    
    gauge3.update_layout(margin=dict(b=1,r=8,l=8,t=45))
    
    numberchart = go.Figure(go.Indicator(
    mode = "number",
    value = 55,
    title = {'text': "Number of Objects"},
    domain = {'x': [0, 1], 'y': [0, 1]})) 
    
    numberchart.update_layout(margin=dict(b=1,r=8,l=8,t=45))

    
    return gauge1, gauge2, gauge3, numberchart
 


