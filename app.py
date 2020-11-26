# import pandas
import pandas as pd

# load data
abalone_p ="abalone.data.csv"
df = pd.read_csv(abalone_p, sep=',', decimal='.', header=None,
names=['Sex', 'Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings'])

# import dash
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output
import plotly.graph_objects as go

# Initialise the app
app = dash.Dash(__name__)

# Define the app
app.layout = html.Div()


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

  
    children=[
        html.Div(className='row',  # Define the row element
                 children=[
                     html.Div(className='four columns div-user-controls',
                              children = [
                                  html.H2('Abalone Dashboard'),
                                  html.P('''Visualising the abalone dataset with Plotly - Dash'''),
                                  html.P('''Pick x and y columns from the dropdown below.''')
                              ]
                             ),

                     # Define the right element
                          # Define the right element
                     html.Div(className='eight columns div-for-charts bg-grey',
                              children = [
                                  dcc.Graph(id='scatterplot',
                                            config={'displayModeBar': False},
                                            animate=True,
                                            figure=px.scatter(df,
                                                              x='Diameter',
                                                              y='Rings',
                                                              color='Sex',
                                                              template='plotly_dark').update_layout(
                                                {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                                 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
                                           )
                              ]
                             )

                 ]
                )
    ]



             