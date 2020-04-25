from flask import Flask, jsonify, request, render_template
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host="3.84.44.187", port=8000)