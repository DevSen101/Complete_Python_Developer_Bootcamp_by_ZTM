from flask import Flask, render_template

app = Flask(__name__)


# @app.route("/")
# def hello_world():
#     return render_template('./index.html')


@app.route("/<username>")
def hello_world2(username=None):
    return render_template("./index.html", name = username)


@app.route("/home")
def home_route():
    return render_template("./index.html")


if __name__ == "__main__":
    app.run(debug=True)
