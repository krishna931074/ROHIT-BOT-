from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Tech VJ'


if __name__ == "__Rohit__":
    app.run()
