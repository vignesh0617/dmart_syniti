from dash import html, dcc
from components.navbar import get_navbar
from callback_functions.main_app_class import main_app
import dash_bootstrap_components as dbc
from callback_functions.home_page_functions import mock_data
from callback_functions.custom_helpers import create_dash_table_from_data_frame

# ids = get_request_id_for_user()

def rule1(number:int):
    if number > 90 :
        return "flag_1 bi bi-circle-fill"
    
    if number > 70 :
        return "flag_2 bi bi-exclamation-triangle-fill"
    
    return "flag_3 bi bi-diamond-fill"

rule_col_numbers = [4] 

rules = {
    4 : rule1
}

milestone_reporting_contents = html.Div(
    children=[
        html.H3("Milestone Reporting"),
        create_dash_table_from_data_frame(
            data_frame_original=mock_data,
            table_id= main_app.environment_details['milestone_reporting_table_id'],
            key_col_number=0,
            generate_srno=False,
            create_simmple_table = True,
            rules = rules,
            rule_col_number=rule_col_numbers,
            rule_container_className="flag_container"),

            html.Div(children = [
                dcc.Graph(id='gauge_chart_1'),
                dcc.Graph(id='gauge_chart_2'),
                dcc.Graph(id='gauge_chart_3'), 
                dcc.Graph(id='number_chart'),
            ],className='chart_container')
        ],
    className="milestone_reporting_container"
)

tabs = dbc.Tabs(
    [
        dbc.Tab("Executive summary contents", label="Executive Summar"),
        dbc.Tab(milestone_reporting_contents, label="Milestone Reporting"),
    ]
)

layout = html.Div( 
    children=[
        html.Div(className="app_bg"),

        html.Div(children=[
            get_navbar(active_link=main_app.environment_details["home_page_link"]),
        ],className='cm_nav_bar_container'),
        
        html.Div(children=[
            tabs
        ], className="cm_body_container")
],className="cm_main_container")