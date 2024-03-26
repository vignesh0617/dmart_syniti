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


def create_gauge_chart(title : str, actual_value :int , total_value : int) -> go.Figure:

    gauge_color = "darkblue"

    percentage = (actual_value / total_value) * 100
    
    gauge_chart = go.Figure(
        go.Indicator(
        mode = "gauge",
        value = actual_value,
        # delta = {
        #             "increasing.symbol" : "" , 
        #             "reference": actual_value - actual_value/ total_value * 100 , 
        #             "suffix" : "%" , 
        #             "increasing.color" : "black", 
        #             "valueformat" : ".2f",
        #             "font" :{
        #                 "size" : 20
        #             }
        #         },
        domain = {'x': [0, 1], 'y': [0, 1]},
        gauge = {
            'axis': {
                'range': [None, total_value],
                'dtick' : total_value,
                "tickmode" :"array",
                "tickvals" : [0,actual_value,total_value],
                "ticktext" : [0,actual_value,total_value]
                },
            "threshold" : {
                    "value" : total_value,
                    "line.color" : gauge_color,
                    "line.width" : 2,
                    "thickness" : 1,
                },
            'bar': {
                    'color': gauge_color,
                    "thickness" : 1,
                    },
        
            'steps': [
                {'range': [0, total_value], 'color': 'gray'}],
            }
        )
    )
    
    gauge_chart.add_annotation(
                    x= 0.5, y=0.2,
                    text=f"{percentage:.2f}%",
                    showarrow=False,
                    font={'size': 15}
                )
    
    gauge_chart.update_layout(
        margin=dict(b=1,l=25,r=45,t=70),
        title = {"x" : 0.06 , "y" : 0.9 , "text" : title , "font.size" : 13}
    )
    
    return gauge_chart


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

    gauge1 = create_gauge_chart("Target Design % Complete", 1557, 2218) 
    gauge2 = create_gauge_chart("Field Mapping % Complete", 1435, 2335) 
    gauge3 = create_gauge_chart("Rule Build % Complete", 1314, 2335)
    gauge1 = create_gauge_chart("Target Design % Complete", 1557, 2218) 
    gauge2 = create_gauge_chart("Field Mapping % Complete", 1435, 2335) 
    gauge3 = create_gauge_chart("Rule Build % Complete", 1314, 2335)

    numberchart = go.Figure(go.Indicator(
    mode = "number",
    value = 55,
    title = {
        'text': "Number of Objects",
        'font.size' : 15,
        },
    domain = {'x': [0, 1], 'y': [0, 1]})) 
    
    numberchart.update_layout(
        margin=dict(b=1,l=25,r=45,t=70),
        title = {"x" : 0.06 , "y" : 0.9 , "text" : title , "font.size" : 13}
    )

    
    return gauge1, gauge2, gauge3, numberchart
 


