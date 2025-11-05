from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/red")
def red():
    return render_template("red.html")


@app.route("/green")
def green():
    return render_template("green.html")


@app.route("/blue")
def blue():
    return render_template("blue.html")


if __name__ == "__main__":
    app.run(debug=True)
