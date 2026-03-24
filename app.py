from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Dummy sensor data
data = {
    "pir": 0,
    "ldr": 43290,
    "led1": "ON",
    "led2": "ON",
    "mode": "MANUAL"
}

@app.route('/')
def home():
    return render_template("index.html", data=data)

@app.route('/on')
def on():
    data["led1"] = "ON"
    data["led2"] = "ON"
    return jsonify(data)

@app.route('/off')
def off():
    data["led1"] = "OFF"
    data["led2"] = "OFF"
    return jsonify(data)

@app.route('/mode')
def mode():
    data["mode"] = "AUTO" if data["mode"] == "MANUAL" else "MANUAL"
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
