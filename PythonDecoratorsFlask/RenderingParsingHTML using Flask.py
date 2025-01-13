from flask import Flask
"""
        Rendering HTML is referred to generating and returning an HTML page to the client (browser)
    when a user requests a specific route in your Flask application.
    
        However, parsing means analyzing and extracting information from HTML elements, often done on the
    server side or client side.
"""
app = Flask(__name__)
@app.route("/")
def hello_world():
    return '<h1 style = "text-align: center"><b>Hello, World!</b></h1>' \
    '<p>This is a paragraph.</p>' \
    '<img src = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGg2ZnJwNzhuZ2gxN3V2dHRnYnhnbnM5aDBtNnlyMnJnemUzb3Q4MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/CkMnLcOgKOxfa/giphy.gif" width = 800>'
@app.route("/bye")
def bye():
    return "Bye"
@app.route("/<name>/<int:number>")
def greet(name, number):
    title_cased  = (f"hello, {name}! You have {number} days to finish the project!")
    return title_cased
if __name__ == "__main__":
    app.run(debug = True)






