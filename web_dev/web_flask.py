from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello_world'


@app.route('/user/<user>')
def hello_x(user):
    return 'Hello %s' % user


if __name__ == '__main__':
    app.run()
