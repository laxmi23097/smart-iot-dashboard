from flask import Flask, render_template, request
import requests

app = Flask(__name__)

ESP_IP = "http://YOUR_ESP_IP"   # replace with your ESP IP

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/on')
def on():
    requests.get(ESP_IP + "/on")
    return "ON"

@app.route('/off')
def off():
    requests.get(ESP_IP + "/off")
    return "OFF"

@app.route('/toggle')
def toggle():
    requests.get(ESP_IP + "/toggle_mode")
    return "TOGGLED"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)