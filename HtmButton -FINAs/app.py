from flask import Flask, request, render_template, jsonify
from waitress import serve
app = Flask(__name__)
state = "off"

@app.route("/")
def index():
    return render_template("index.html", state=state)

@app.route("/state")
def get_state():
    return jsonify(switch=state)

@app.route("/", methods=["POST"])
def toggle_switch():
    global state
    state = "on" if state == "off" else "off"
    return jsonify(switch=state)

if __name__ == '__main__':
    serve(app, host='0.0.0.0',port=80,threads=2)