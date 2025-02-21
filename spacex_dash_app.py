# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Clean column names to remove any extra spaces or hidden characters
spacex_df.columns = spacex_df.columns.str.strip()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    
    # TASK 1: Add a dropdown list to enable Launch Site selection
    dcc.Dropdown(
        id='site-dropdown',
        options=[
            {'label': 'All Sites', 'value': 'ALL'},
            {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
            {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
            {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
            {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'}  # Add more as needed
        ],
        value='ALL',  # Default to 'ALL'
        placeholder='Select a Launch Site here',
        searchable=True
    ),
    html.Br(),

    # Pie chart for showing success count
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P("Payload range (Kg):"),
    # TASK 3: Add a slider to select payload range
    dcc.RangeSlider(
        id='payload-slider',
        min=0,
        max=10000,
        step=1000,
        marks={i: str(i) for i in range(0, 10001, 2000)},
        value=[min_payload, max_payload]
    ),

    # Scatter chart for payload vs. mission outcome
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])

# TASK 2: Callback for rendering the pie chart
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(entered_site):
    # Clean column names to remove any extra spaces or hidden characters
    spacex_df.columns = spacex_df.columns.str.strip()
    
    if entered_site == 'ALL':
        # For All Sites, group by class and calculate the total count of successes (1) and failures (0)
        fig = px.pie(
            spacex_df,
            names='class',  # Class 1 = success, Class 0 = failure
            title='Total Success vs Failure for All Sites',
            color='class',  # Color the pie chart based on the class (success vs failure)
            labels={'class': 'Mission Outcome (Success=1, Failure=0)'}
        )
        return fig
    else:
        # Filter data by selected site
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        
        # Create the pie chart for the selected site
        fig = px.pie(
            filtered_df, 
            names='class', 
            title=f'Success vs. Failure for {entered_site} Launch Site',
            color='class',
            labels={'class': 'Mission Outcome (Success=1, Failure=0)'}
        )
        return fig

# TASK 4: Callback for rendering the scatter plot
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id='payload-slider', component_property='value')]
)
def update_scatter_chart(selected_site, selected_payload_range):
    # Filter data based on payload range
    filtered_df = spacex_df[
        (spacex_df['Payload Mass (kg)'] >= selected_payload_range[0]) &
        (spacex_df['Payload Mass (kg)'] <= selected_payload_range[1])
    ]
    
    # If a specific launch site is selected
    if selected_site != 'ALL':
        filtered_df = filtered_df[filtered_df['Launch Site'] == selected_site]
    
    # Create the scatter plot
    fig = px.scatter(
        filtered_df,
        x='Payload Mass (kg)',
        y='class',
        color='Booster Version Category',  # Color points by Booster Version
        title=f'Payload vs. Mission Outcome for {selected_site} Launch Site' if selected_site != 'ALL' else 'Payload vs. Mission Outcome for All Sites',
        labels={'class': 'Mission Outcome (Success=1, Failure=0)', 'Payload Mass (kg)': 'Payload Mass (kg)'}
    )
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server()
