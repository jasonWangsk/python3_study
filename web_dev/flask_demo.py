from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<a href="/home">Hello World!</a>'


@app.route("/home")
def home():
    return "这个是主页"


@app.route("/login")
def login():
    return "这个是登录"


if __name__ == '__main__':
    app.run(debug=True)
