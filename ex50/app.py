from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def index():
    # http://127.0.0.1:5000/?name=lol
    greeting = "Hello world"

    if request.method == 'POST':
        name = request.form['name']
        greet = request.form['greet']
        greeting = f"{greet}, {name}"
        return render_template("index.html", greeting=greeting)
    return render_template("hello_form.html")


@app.route('/form')
def form():
    return render_template("hello_form.html")


if __name__ == "__main__":
    app.run()

# @app.route('/', methods=["POST", "GET"])
# def index():
#     # http://127.0.0.1:5000/?name=lol
#     name = request.args.get('name', 'Nobody')
#     greet = request.args.get('greet', 'yo-ho-ho')

#     if name or greet:
#         greeting = f"{greet}, {name}"
#     else:
#         greeting = "Hello world"
#     return render_template("index.html", greeting=greeting)
