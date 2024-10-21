from flask import Flask
import json

# create the app
app = Flask(__name__)

#this is our first endpoint
@app.get ("/")
def home()
    # return the component
    return "hello from flask"
@app.get("/about")
def about()
    #return your name on a json format
    name2 = {"name":"Denielle Black"}
    return json.dumps(name2)
# when you were using JS, the "`" helps you to cocatenate,
# here in python we use f"""<h1></h1>"""

# minichallange
# Create 3 new routes:
1#/greet/{name}: This route should accept a name as part of the URL and return an HTML
# message saying "Hello, {name}!" styled with css

@app.get("/greet/<name>")
def greet(name)
return f"""
<h1 style= 'color:orange;text-align;:center;'>
Hello, {name}
</h1>
"""

2#/square/ {number}: This route should take a number as part of the Url and return
# the sqare root of that number in a styled <p> tag.
@app.get("/square/<int:number>")
def square(number);
    return f"""
    <p style= 'font-size:18px;color:blue;>
    the square of {number} is (number*number)
    </p>
    """
3#Add a /farewell/{name} route thsts says goodbye to a person in a <h2> tag with
# some CSS styling (e.g., font color, size, etc.).
@app.get("/farewell/<name>")
def farewell(name):
    return f"""
    <h1 style='color:brown;text-align: center;'>
    Goodbye, {name}
    </h1>
    """

# when i save my code, the changes will be applied
app.run(debug=True)