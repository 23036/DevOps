from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"
@app.route('/about')
def about():
    return "This is the page profile"
if __name__ == '__main__':
    app.run(debug=True, port=5000)
