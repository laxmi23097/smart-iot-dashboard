from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/on')
def on():
    print("ON clicked")
    return "ON"

@app.route('/off')
def off():
    print("OFF clicked")
    return "OFF"

@app.route('/toggle')
def toggle():
    print("MODE changed")
    return "TOGGLED"

import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
