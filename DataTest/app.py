# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

colors = {
    'background': '#ffffff',
    'text': '#000000'
}
# Bubblesort Charts
df1 = pd.read_csv('bubblesort.csv')
fig1 = px.scatter(df1, x="Test_No", y="Unsorted_size_100",
                 labels={
                     "Test_No": "Test Number",
                     "Unsorted_size_100": "Time Taken To Sort (in microseconds) ",
                 },
                title="Bubble Sort<br>Unsorted Dataset of Size 100")
fig2 = px.scatter(df1, x="Test_No", y="Unsorted_size_1000",
                 labels={
                     "Test_No": "Test Number ",
                     "Unsorted_size_1000": "Time Taken To Sort (in microseconds) ",
                 },
                title="Bubble Sort<br>Unsorted Dataset of Size 1000")
fig3 = px.scatter(df1, x="Test_No", y="Unsorted_size_10000",
                 labels={
                     "Test_No": "Test Number ",
                     "Unsorted_size_10000": "Time Taken To Sort (in microseconds) ",
                 },
                title="Bubble Sort<br>Unsorted Dataset of Size 10000")
fig4 = px.scatter(df1, x="Test_No", y="Sorted_size_100",
                 labels={
                     "Test_No": "Test Number ",
                     "Sorted_size_100": "Time Taken To Sort (in microseconds) ",
                 },
                title="Bubble Sort<br>Sorted Dataset of Size 100")
fig5 = px.scatter(df1, x="Test_No", y="Sorted_size_1000",
                 labels={
                     "Test_No": "Test Number ",
                     "Sorted_size_1000": "Time Taken To Sort (in microseconds) ",
                 },
                title="Bubble Sort<br>Sorted Dataset of Size 1000")
fig6 = px.scatter(df1, x="Test_No", y="Sorted_size_10000",
                 labels={
                     "Test_No": "Test Number ",
                     "Sorted_size_10000": "Time Taken To Sort (in microseconds) ",
                 },
                title="Bubble Sort<br>Sorted Dataset of Size 10000")
#Mergesort Charts
df2 = pd.read_csv('mergesort.csv')
fig7 = px.scatter(df2, x="Test_No", y="Unsorted_size_100",
                 labels={
                     "Test_No": "Test Number ",
                     "Unsorted_size_100": "Time Taken To Sort (in microseconds) ",
                 },
                title="Merge Sort<br>Unsorted Dataset of Size 100")
fig8 = px.scatter(df2, x="Test_No", y="Unsorted_size_1000",
                 labels={
                     "Test_No": "Test Number ",
                     "Unsorted_size_1000": "Time Taken To Sort (in microseconds) ",
                 },
                title="Merge Sort<br>Unsorted Dataset of Size 1000")
fig9 = px.scatter(df2, x="Test_No", y="Unsorted_size_10000",
                 labels={
                     "Test_No": "Test Number ",
                     "Unsorted_size_10000": "Time Taken To Sort (in microseconds) ",
                 },
                title="Merge Sort<br>Unsorted Dataset of Size 10000")
fig10 = px.scatter(df2, x="Test_No", y="Sorted_size_100",
                 labels={
                     "Test_No": "Test Number ",
                     "Sorted_size_100": "Time Taken To Sort (in microseconds) ",
                 },
                title="Merge Sort<br>Sorted Dataset of Size 100")
fig11 = px.scatter(df2, x="Test_No", y="Sorted_size_1000",
                 labels={
                     "Test_No": "Test Number ",
                     "Sorted_size_1000": "Time Taken To Sort (in microseconds) ",
                 },
                title="Merge Sort<br>Sorted Dataset of Size 1000")
fig12 = px.scatter(df2, x="Test_No", y="Sorted_size_10000",
                 labels={
                     "Test_No": "Test Number ",
                     "Sorted_size_10000": "Time Taken To Sort (in microseconds) ",
                 },
                title="Merge Sort<br>Sorted Dataset of Size 10000")
#Quicksort Charts
df3 = pd.read_csv('quicksort.csv')
fig13 = px.scatter(df3, x="Test_No", y="Unsorted_size_100",
                 labels={
                     "Test_No": "Test Number ",
                     "Unsorted_size_100": "Time Taken To Sort (in microseconds) ",
                 },
                title="Quick Sort<br>Unsorted Dataset of Size 100")
fig14 = px.scatter(df3, x="Test_No", y="Unsorted_size_1000",
                 labels={
                     "Test_No": "Test Number ",
                     "Unsorted_size_1000": "Time Taken To Sort (in microseconds) ",
                 },
                title="Quick Sort<br>Unsorted Dataset of Size 1000")
fig15 = px.scatter(df3, x="Test_No", y="Unsorted_size_10000",
                 labels={
                     "Test_No": "Test Number ",
                     "Unsorted_size_10000": "Time Taken To Sort (in microseconds) ",
                 },
                title="Quick Sort<br>Unsorted Dataset of Size 10000")
fig16 = px.scatter(df3, x="Test_No", y="Sorted_size_100",
                 labels={
                     "Test_No": "Test Number ",
                     "Sorted_size_100": "Time Taken To Sort (in microseconds) ",
                 },
                title="Quick Sort<br>Sorted Dataset of Size 100")
fig17 = px.scatter(df3, x="Test_No", y="Sorted_size_1000",
                 labels={
                     "Test_No": "Test Number ",
                     "Sorted_size_1000": "Time Taken To Sort (in microseconds) ",
                 },
                title="Quick Sort<br>Sorted Dataset of Size 1000")
fig18 = px.scatter(df3, x="Test_No", y="Sorted_size_10000",
                 labels={
                     "Test_No": "Test Number ",
                     "Sorted_size_10000": "Time Taken To Sort (in microseconds) ",
                 },
                title="Quick Sort<br>Sorted Dataset of Size 10000")
#Selectionsort Charts
df4 = pd.read_csv('selectionsort.csv')
fig19 = px.scatter(df4, x="Test_No", y="Unsorted_size_100",
                 labels={
                     "Test_No": "Test Number ",
                     "Unsorted_size_100": "Time Taken To Sort (in microseconds) ",
                 },
                title="Selection Sort<br>Unsorted Dataset of Size 100")
fig20 = px.scatter(df4, x="Test_No", y="Unsorted_size_1000",
                 labels={
                     "Test_No": "Test Number ",
                     "Unsorted_size_1000": "Time Taken To Sort (in microseconds) ",
                 },
                title="Selection Sort<br>Unsorted Dataset of Size 1000")
fig21 = px.scatter(df4, x="Test_No", y="Unsorted_size_10000",
                 labels={
                     "Test_No": "Test Number ",
                     "Unsorted_size_10000": "Time Taken To Sort (in microseconds) ",
                 },
                title="Selection Sort<br>Unsorted Dataset of Size 10000")
fig22 = px.scatter(df4, x="Test_No", y="Sorted_size_100",
                 labels={
                     "Test_No": "Test Number ",
                     "Sorted_size_100": "Time Taken To Sort (in microseconds) ",
                 },
                title="Selection Sort<br>Sorted Dataset of Size 100")
fig23 = px.scatter(df4, x="Test_No", y="Sorted_size_1000",
                 labels={
                     "Test_No": "Test Number ",
                     "Sorted_size_1000": "Time Taken To Sort (in microseconds) ",
                 },
                title="Selection Sort<br>Sorted Dataset of Size 1000")
fig24 = px.scatter(df4, x="Test_No", y="Sorted_size_10000",
                 labels={
                     "Test_No": "Test Number ",
                     "Sorted_size_10000": "Time Taken To Sort (in microseconds) ",
                 },
                title="Selection Sort<br>Sorted Dataset of Size 10000")
# Insertionsort
df5 = pd.read_csv('insertionsort.csv')
fig25 = px.scatter(df5, x="Test_No", y="Unsorted_size_100",
                 labels={
                     "Test_No": "Test Number ",
                     "Unsorted_size_100": "Time Taken To Sort (in microseconds) ",
                 },
                title="Insertion Sort<br>Unsorted Dataset of Size 100")
fig26 = px.scatter(df5, x="Test_No", y="Unsorted_size_1000",
                 labels={
                     "Test_No": "Test Number ",
                     "Unsorted_size_1000": "Time Taken To Sort (in microseconds) ",
                 },
                title="Insertion Sort<br>Unsorted Dataset of Size 1000")
fig27 = px.scatter(df5, x="Test_No", y="Unsorted_size_10000",
                 labels={
                     "Test_No": "Test Number ",
                     "Unsorted_size_10000": "Time Taken To Sort (in microseconds) ",
                 },
                title="Insertion Sort<br>Unsorted Dataset of Size 10000")
fig28 = px.scatter(df5, x="Test_No", y="Sorted_size_100",
                 labels={
                     "Test_No": "Test Number ",
                     "Sorted_size_100": "Time Taken To Sort (in microseconds) ",
                 },
                title="Insertion Sort<br>Sorted Dataset of Size 100")
fig29 = px.scatter(df5, x="Test_No", y="Sorted_size_1000",
                 labels={
                     "Test_No": "Test Number ",
                     "Sorted_size_1000": "Time Taken To Sort (in microseconds) ",
                 },
                title="Insertion Sort<br>Sorted Dataset of Size 1000")
fig30 = px.scatter(df5, x="Test_No", y="Sorted_size_10000",
                 labels={
                     "Test_No": "Test Number ",
                     "Sorted_size_10000": "Time Taken To Sort (in microseconds) ",
                 },
                title="Insertion Sort<br>Sorted Dataset of Size 10000")
#Overall Sorted Dataset
df6 = pd.read_csv('SortedSize100.csv')
fig31 = px.line(df6, x="Test_No", y=[" Bubble"," Insertion"," Merge"," Quick"," Selection"],
                 labels={
                     "Test_No": "Test Number ",
                     " Bubble": "Bubble Sort",
                     " Insertion": "Insertion Sort",
                     " Merge": "Merge Sort",
                     " Quick": "Quick Sort",
                     " Selection": "Selection Sort",
                     "value": "Sorting Time ",
                     "variable": "Algorithm "
                 },
                title="Testing Algorithms on Dataset of 100 intergers")
fig31.update_layout(
    xaxis_title="Test Number",
    yaxis_title="Time Taken To Sort (in microseconds)",
    legend_title="Sorting Algorithms",
    title={
        'text': "Algorithms Tested on Dataset of 100 intergers",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
df7 = pd.read_csv('SortedSize1000.csv')
fig32 = px.line(df7, x="Test_No", y=[" Bubble"," Insertion"," Merge"," Quick"," Selection"],
                 labels={
                     "Test_No": "Test Number ",
                     " Bubble": "Bubble Sort",
                     " Insertion": "Insertion Sort",
                     " Merge": "Merge Sort",
                     " Quick": "Quick Sort",
                     " Selection": "Selection Sort",
                     "value": "Sorting Time ",
                     "variable": "Algorithm "
                 },
                title="Testing Algorithms on Dataset of 1000 intergers")
fig32.update_layout(
    xaxis_title="Test Number",
    yaxis_title="Time Taken To Sort (in microseconds)",
    legend_title="Sorting Algorithms",
    title={
        'text': "Testing Algorithms on Dataset of 1000 intergers",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
df8 = pd.read_csv('SortedSize10000.csv')
fig33 = px.line(df8, x="Test_No", y=[" Bubble"," Insertion"," Merge"," Quick"," Selection"],
                 labels={
                     "Test_No": "Test Number ",
                     " Bubble": "Bubble Sort",
                     " Insertion": "Insertion Sort",
                     " Merge": "Merge Sort",
                     " Quick": "Quick Sort",
                     " Selection": "Selection Sort",
                     "value": "Sorting Time ",
                     "variable": "Algorithm "
                 },
                title="Testing Algorithms on Dataset of 10000 intergers")
fig33.update_layout(
    xaxis_title="Test Number",
    yaxis_title="Time Taken To Sort (in microseconds)",
    legend_title="Sorting Algorithms",
    title={
        'text': "Testing Algorithms on Dataset of 10000 intergers",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
#Overall Unsorted Dataset
df9 = pd.read_csv('UnsortedSize100.csv')
fig34 = px.line(df9, x="Test_No", y=[" Bubble"," Insertion"," Merge"," Quick"," Selection"],
                 labels={
                     "Test_No": "Test Number ",
                     " Bubble": "Bubble Sort",
                     " Insertion": "Insertion Sort",
                     " Merge": "Merge Sort",
                     " Quick": "Quick Sort",
                     " Selection": "Selection Sort",
                     "value": "Sorting Time ",
                     "variable": "Algorithm "
                 },
                title="Testing Algorithms on Dataset of 100 intergers")
fig34.update_layout(
    xaxis_title="Test Number",
    yaxis_title="Time Taken To Sort (in microseconds)",
    legend_title="Sorting Algorithms",
    title={
        'text': "Algorithms Tested on Dataset of 100 intergers",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
df10 = pd.read_csv('UnsortedSize1000.csv')
fig35 = px.line(df10, x="Test_No", y=[" Bubble"," Insertion"," Merge"," Quick"," Selection"],
                 labels={
                     "Test_No": "Test Number ",
                     " Bubble": "Bubble Sort",
                     " Insertion": "Insertion Sort",
                     " Merge": "Merge Sort",
                     " Quick": "Quick Sort",
                     " Selection": "Selection Sort",
                     "value": "Sorting Time ",
                     "variable": "Algorithm "
                 },
                title="Testing Algorithms on Dataset of 1000 intergers")
fig35.update_layout(
    xaxis_title="Test Number",
    yaxis_title="Time Taken To Sort (in microseconds)",
    legend_title="Sorting Algorithms",
    title={
        'text': "Algorithms Tested on Dataset of 1000 intergers",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
df11 = pd.read_csv('UnsortedSize10000.csv')
fig36 = px.line(df11, x="Test_No", y=[" Bubble"," Insertion"," Merge"," Quick"," Selection"],
                 labels={
                     "Test_No": "Test Number ",
                     " Bubble": "Bubble Sort",
                     " Insertion": "Insertion Sort",
                     " Merge": "Merge Sort",
                     " Quick": "Quick Sort",
                     " Selection": "Selection Sort",
                     "value": "Sorting Time ",
                     "variable": "Algorithm "
                 },
                title="Testing Algorithms on Dataset of 10000 intergers")
fig36.update_layout(
    xaxis_title="Test Number",
    yaxis_title="Time Taken To Sort (in microseconds)",
    legend_title="Sorting Algorithms",
    title={
        'text': "Algorithms Tested on Dataset of 10000 intergers",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
#Navigation Bar for web app
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Test sorting algorithms based on the size and nature (sorted or unsorted) of the dataset.", href="#"))
    ],
    brand="Data Test",
    brand_href="#",
    color="dark",
    dark=True,
)
#Footer Navigation Bar for web app
fnavbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Developed by Aditya Pujara", href="#"))
    ],
    brand_href="#",
    color="primary",
    dark=True,
)
#app layout
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.Div(navbar),
    dcc.Tabs(        
        children = [
            dcc.Tab(label='Bubble Sort', 
                children=[
                    dcc.Tabs(children=[
                        dcc.Tab(label = 'Unsorted Dataset', children=[
                            dcc.Graph(
                                figure = fig1
                            ),
                            dcc.Graph(
                                figure = fig2
                            ),
                            dcc.Graph(
                                figure = fig3
                            )
                        ]),
                        dcc.Tab(label = 'Sorted Dataset', children=[
                            dcc.Graph(
                                figure = fig4
                            ),
                            dcc.Graph(
                                figure = fig5
                            ),
                            dcc.Graph(
                                figure = fig6
                            )
                        ]),
                    ])
                ]),
            dcc.Tab(label='Merge Sort', 
                children=[
                    dcc.Tabs(children=[
                        dcc.Tab(label = 'Unsorted Dataset', children=[
                            dcc.Graph(
                                figure = fig7
                            ),
                            dcc.Graph(
                                figure = fig8
                            ),
                            dcc.Graph(
                                figure = fig9
                            )
                        ]),
                        dcc.Tab(label = 'Sorted Dataset', children=[
                            dcc.Graph(
                                figure = fig10
                            ),
                            dcc.Graph(
                                figure = fig11
                            ),
                            dcc.Graph(
                                figure = fig12
                            )
                        ]),
                    ])
                ]),
            dcc.Tab(label='Quick Sort', 
                children=[
                    dcc.Tabs(children=[
                        dcc.Tab(label = 'Unsorted Dataset', children=[
                            dcc.Graph(
                                figure = fig13
                            ),
                            dcc.Graph(
                                figure = fig14
                            ),
                            dcc.Graph(
                                figure = fig15
                            )
                        ]),
                        dcc.Tab(label = 'Sorted Dataset', children=[
                            dcc.Graph(
                                figure = fig16
                            ),
                            dcc.Graph(
                                figure = fig17
                            ),
                            dcc.Graph(
                                figure = fig18
                            )
                        ]),
                    ])
                ]),
            dcc.Tab(label='Selection Sort', 
                children=[
                    dcc.Tabs(children=[
                        dcc.Tab(label = 'Unsorted Dataset', children=[
                            dcc.Graph(
                                figure = fig19
                            ),
                            dcc.Graph(
                                figure = fig20
                            ),
                            dcc.Graph(
                                figure = fig21
                            )
                        ]),
                        dcc.Tab(label = 'Sorted Dataset', children=[
                            dcc.Graph(
                                figure = fig22
                            ),
                            dcc.Graph(
                                figure = fig23
                            ),
                            dcc.Graph(
                                figure = fig24
                            )
                        ]),
                    ])
                ]),
            dcc.Tab(label='Insertion Sort', 
                children=[
                    dcc.Tabs(children=[
                        dcc.Tab(label = 'Unsorted Dataset', children=[
                            dcc.Graph(
                                figure = fig25
                            ),
                            dcc.Graph(
                                figure = fig26
                            ),
                            dcc.Graph(
                                figure = fig27
                            )
                        ]),
                        dcc.Tab(label = 'Sorted Dataset', children=[
                            dcc.Graph(
                                figure = fig28
                            ),
                            dcc.Graph(
                                figure = fig29
                            ),
                            dcc.Graph(
                                figure = fig30
                            )
                        ]),
                    ])
                ]),
            dcc.Tab(label='Comparison by Nature (Sorted/Unsorted)', 
                children=[
                    dcc.Tabs(children=[
                        dcc.Tab(label = 'Unsorted Dataset', children=[
                            dcc.Graph(
                                figure = fig34
                            ),
                            dcc.Graph(
                                figure = fig35
                            ),
                            dcc.Graph(
                                figure = fig36
                            )
                        ]),
                        dcc.Tab(label = 'Sorted Dataset', children=[
                            dcc.Graph(
                                figure = fig31
                            ),
                            dcc.Graph(
                                figure = fig32
                            ),
                            dcc.Graph(
                                figure = fig33
                            )
                        ]),
                    ])
                ]),
    ]),
    html.Div(fnavbar)
])

def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Tab content 1')
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Tab content 2')
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H3('Tab content 3')
        ])
    elif tab == 'tab-4':
        return html.Div([
            html.H3('Tab content 4')
        ])


if __name__ == '__main__':
    app.run_server(debug=True)