import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/response')
def renderPage1():
    return render_template('page1.html')

if __name__=="__main__":
    app.run(debug=True)
