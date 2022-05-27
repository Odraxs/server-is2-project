from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return {'user': 'David'}


# We only need this for local development.
if __name__ == '__main__':
    app.run()