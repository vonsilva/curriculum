from flask import Flask, jsonify, request, render_template, redirect, url_for, send_file
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/files')
def file():
    return redirect(url_for('static', filename='files/curriculojoao.pdf'))


if __name__ == '__main__':
    app.run()