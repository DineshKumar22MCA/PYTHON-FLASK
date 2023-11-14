from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return "<h2> vd computer education chennai</h2>"

@app.route("/user/<name>")
def user(name):
    return "<h3>welcom {}</h3>".format(name)

if __name__=="__main__":
    app.run(debug=True)



