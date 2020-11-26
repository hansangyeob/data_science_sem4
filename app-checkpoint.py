# import pandas
import pandas as pd

# load data and preprocess
df = pd.read_csv('USA_cars_datasets.csv')
df_subset = df[['color']]
df_subset = pd.get_dummies(df_subset)
df_subset['brand'] = df['brand']
df_subset = df_subset.groupby('brand').sum()

# list to choose from
color_list = list(df_subset.columns)
brand_list = list(df_subset.index)


# import dash
import dash
import dash_html_components as html
import dash_core_components as dcccd
import plotly.express as px
from dash.dependencies import Input, Output
import plotly.graph_objects as go

# Initialise the app
app = dash.Dash(__name__)


# Callback for interactive scatterplot
@app.callback(Output('stackedbar', 'figure'),
              [Input('selector1', 'value'), Input('selector2', 'value')])
def update_plot(selector1, selector2):
    ''' Draw traces of the feature 'value' based one the currently selected stocks '''
    # STEP 1
    trace = []  
    brands = []
    
    # STEP 2
    # Draw and append traces for each list
    
    print(selector1)
    if type(selector1) == list:
        for brand in selector1:
            print(brand)
            brands.append(brand)
    else:
        brands.append(selector1)
        
    df_selected_brand = df_subset.loc[brands,:]  
    
    if type(selector2) == list:
        for color in selector2:    
            trace.append(go.Bar(name=color,x=brands,y=list(df_selected_brand.loc[:,color])))
    else:
        trace.append(go.Bar(name=str(selector2),x=brands,y=list(df_selected_brand.loc[:,selector2])))
        
    
    # STEP 3
    traces = [trace]
    data = [val for sublist in traces for val in sublist]
    # Define Figure
    # STEP 4
    figure = {'data': data,
              'layout': go.Layout(
                  template='plotly_dark',
                  paper_bgcolor='rgba(0, 0, 0, 0)',
                  plot_bgcolor='rgba(0, 0, 0, 0)',
                  autosize=True,
                  barmode='stack',
                  title={'text': 'Car color by brand', 'font': {'color': 'white'}, 'x': 0.5},
              ),
              }
    return figure


# Define the app
app.layout = html.Div(
    children=[
        html.Div(className='row',  # Define the row element
                 children=[
                     # Define the left element
                     html.Div(className='four columns div-user-controls',
                              children = [
                                  html.H2('Cars Dashboard'),
                                  html.P('''Visualising the car colors by brand'''),
                                  html.P('''Pick brand and color from the dropdown below. You can select multiple'''),
                                  # Adding option to select columns
                                  html.Div(className='div-for-dropdown',
                                           children=[
                                               dcc.Dropdown(id='selector1',
                                                            options=[
                                                                {"label": i, "value": i}
                                                                for i in brand_list
                                                            ],
                                                            multi=True,
                                                            placeholder="Select car brands",
                                                            value='bmw',
                                                           )
                                           ]
                                          ),
                                  html.Div(className='div-for-dropdown',
                                           children=[
                                               dcc.Dropdown(id='selector2',
                                                            options=[
                                                                {"label": i, "value": i}
                                                                for i in color_list
                                                            ],
                                                            multi=True,
                                                            placeholder="Select car colors",
                                                            value='color_blue',
                                                           )
                                           ]
                                          ),
                              ]
                             ),
                     # Define the right element
                     html.Div(className='eight columns div-for-charts bg-grey',
                              children = [
                                  dcc.Graph(id='stackedbar',
                                            config={'displayModeBar': False},
                                            animate=True,
                                           )
                              ]
                             )
                 ]
                )
    ]
)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_ui=True, dev_tools_props_check=True)


