from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    courses = ["C", "C++", "Java", "Python", "HTML", "CSS"]
    id = False
    return render_template("index.html", courses=courses,id=id)


@app.route('/about')
def about():
    return '<h3>Tutor Joes Computer Education Salem</h3>'


@app.route('/contact')
def contact():
    return '<h3>Contact Us</h3>'


@app.route('/users/<name>')
def users(name):
    # return  "<h3>Welcome {}</h3>".format(name.upper())
    fruits = ["Apple", "Orange", "Pineapple"]
    profile = {"father": "Joes", "age": 25, "City": "Salem"}
    return render_template("users.html", user_name=name, fruits=fruits, profile=profile)


if __name__ == '__main__':
    app.run(debug=True)
