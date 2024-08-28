import dash
from dash import html

students = [
    {"name": "Alice", "surname": "Smith", "age": 14, "grade": "A"},
    {"name": "Bob", "surname": "Johnson", "age": 15, "grade": "B"},
    {"name": "Charlie", "surname": "Williams", "age": 14, "grade": "C"},
    {"name": "Diana", "surname": "Brown", "age": 16, "grade": "A"},
    {"name": "Ethan", "surname": "Jones", "age": 15, "grade": "B"},
    {"name": "Fiona", "surname": "Garcia", "age": 14, "grade": "A"},
    {"name": "George", "surname": "Miller", "age": 16, "grade": "C"},
    {"name": "Hannah", "surname": "Davis", "age": 15, "grade": "B"},
    {"name": "Ian", "surname": "Martinez", "age": 14, "grade": "A"},
    {"name": "Julia", "surname": "Rodriguez", "age": 16, "grade": "A"},
    {"name": "Kevin", "surname": "Martinez", "age": 15, "grade": "B"},
    {"name": "Lena", "surname": "Taylor", "age": 14, "grade": "C"},
    {"name": "Mike", "surname": "Anderson", "age": 16, "grade": "B"},
    {"name": "Nina", "surname": "Thomas", "age": 14, "grade": "A"},
    {"name": "Oscar", "surname": "Hernandez", "age": 15, "grade": "C"},
    {"name": "Paula", "surname": "Moore", "age": 16, "grade": "A"},
    {"name": "Quincy", "surname": "Martin", "age": 14, "grade": "B"},
    {"name": "Rachel", "surname": "Jackson", "age": 15, "grade": "A"},
    {"name": "Sam", "surname": "Thompson", "age": 16, "grade": "B"},
    {"name": "Tina", "surname": "White", "age": 14, "grade": "A"},
]

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Student Data", style={"color":"#2222ff"}),
    dash.dash_table.DataTable(students, page_size=5)
])

if __name__ == "__main__":
    app.run(debug=True)