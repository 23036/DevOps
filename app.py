from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"
@app.route('/main')
def object():
    return "Notre objectif est de collaborer"
if __name__ == '__main__':
    app.run(debug=True, port=5000)
