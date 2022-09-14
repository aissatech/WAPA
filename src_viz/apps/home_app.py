# -*- coding: utf-8 -*-
import sys
import dash_apps_wapa
sys.path.insert(0, '/srv/wapa/src_viz')
from dash_apps_wapa import *


### DASH APP TEST IN LOCAL ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### 
home_app = Dash(__name__, server = app_wapa, url_base_pathname= webtype + "/", external_stylesheets=external_stylesheets, external_scripts=external_scripts)
home_app.config['suppress_callback_exceptions']=True

title = "Home"
home_app.title = title+title_addenda
home_app.layout = html.Div([
    navbar,

    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.H2(html.B('Wikipedia Administrative Pages Analytics'), style={'textAlign':'center', 'font-weight':'bold'}),
    html.Div(
    dcc.Markdown('''
    Providing data, visualizations and tools to work towards a better maintenance and inclusion in administration pages across Wikipedia language editions.'''.replace('  ', '')), style={'textAlign':'center'},),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    footbar,

], className="container")