import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__)

# Create some sample data
df = pd.DataFrame({
    'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 'Bananas'],
    'Amount': [4, 1, 2, 2, 4, 5],
    'City': ['SF', 'SF', 'SF', 'NYC', 'MTL', 'NYC']
})

# Define the layout of the app
app.layout = html.Div([
    html.H1('Dash Demo Dashboard'),
    
    html.Div([
        html.H3('Interactive Graph'),
        dcc.Dropdown(
            id='city-dropdown',
            options=[{'label': i, 'value': i} for i in df['City'].unique()],
            value='SF'
        ),
        dcc.Graph(id='bar-chart')
    ]),
    
    html.Div([
        html.H3('Static Graph'),
        dcc.Graph(
            figure=px.scatter(df, x='Fruit', y='Amount', color='City', title='Fruit Amounts by City')
        )
    ]),
    
    html.Div([
        html.H3('Interactive Components'),
        dcc.Slider(
            id='slider-demo',
            min=0,
            max=10,
            step=1,
            value=5,
        ),
        html.Div(id='slider-output')
    ])
])

# Define callback to update bar chart
@app.callback(
    Output('bar-chart', 'figure'),
    Input('city-dropdown', 'value')
)
def update_bar_chart(selected_city):
    filtered_df = df[df['City'] == selected_city]
    fig = px.bar(filtered_df, x='Fruit', y='Amount', title=f'Fruit Amounts in {selected_city}')
    return fig

# Define callback to update slider output
@app.callback(
    Output('slider-output', 'children'),
    Input('slider-demo', 'value')
)
def update_slider_output(value):
    return f'You have selected: {value}'

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)