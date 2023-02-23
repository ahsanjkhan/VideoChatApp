import flask
from flask import request
import sys
app = flask.Flask(__name__)
users = []

@app.route('/', methods=['GET'])
def registerGET():
    return flask.render_template('register.html')

@app.route('/register', methods=['POST'])
def registerPOST():
    username = request.form["name"]
    print(username)
    return flask.render_template('register.html')

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    #testing branches
    #testing branches #2
    #testing branches #3
    #testing branches #4
    #testing branches #5
    app.run(host='0.0.0.0', port=port, debug=True)
