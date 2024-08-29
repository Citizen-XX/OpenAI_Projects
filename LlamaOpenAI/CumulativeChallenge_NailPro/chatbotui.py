from dash import dcc, html, Input, Output, State, Dash
import dash_bootstrap_components as dbc
import requests

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout of the app
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("API Chat Interface"), className="text-center")
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Textarea(
                id='input-text',
                placeholder='Type your message here...',
                style={'width': '100%', 'height': 100},
            ),
            dbc.Button('Send', id='send-button', color='primary', className="mt-2"),
            html.Hr(),
            html.Div(id='chat-history', style={'whiteSpace': 'pre-wrap'}),
        ])
    ])
])

# Callback to handle the chat interaction
@app.callback(
    Output('chat-history', 'children'),
    Output('input-text', 'value'),  # Clear input after sending
    Input('send-button', 'n_clicks'),
    State('input-text', 'value'),
    State('chat-history', 'children')
)
def update_chat(n_clicks, input_text, chat_history):
    if n_clicks is None or input_text is None:
        return chat_history or "", ""  # Return empty string for input value to clear it

    # Example of sending the user's message to the API
    api_url = "http://localhost:8000/ask"
    data = {"question": input_text}

    # Send the request to the API
    response = requests.post(api_url, json=data)
    
    if response.status_code == 200:
        api_response = response.json().get("response", "")
        # Update the chat history
        new_chat_history = f"{chat_history}\nYou: {input_text}\nNailAssistant: {api_response}"
        return new_chat_history, ""  # Clear the input text
    else:
        return f"Error: {response.status_code} - {response.text}", ""  # Clear the input text even on error

# Run the app
if __name__ == '__main__':
    app.run_server(port=5000, debug=True)
