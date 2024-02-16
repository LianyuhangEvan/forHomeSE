from flask import Flask
app = Flask(__name__)
@app.route('/user/<username>')
def index(username):
    if username == "1":
        return "Hello"
    if username == "2":
        return "follow"
    if username == "3":
        return "unfollow"
    return "fuck"

if __name__ == '__main__':
    app.run()