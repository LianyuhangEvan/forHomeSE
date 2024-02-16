from flask import Flask
app = Flask(__name__)

@app.route('/Hello', methods=['GET', 'POST']) #change the routing: http://127.0.0.1:5000/Hello
def hello():
    return "Hello"
@app.route('/hi', methods=['POST'])  # Method Not AllowedThe method is not allowed for the requested URL.
def hi():
    return "Baga"
if __name__ == '__main__':
    app.run()