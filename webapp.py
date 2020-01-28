import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear()
    
    return redirect('/')

@app.route('/page1')
def renderPage1():
    return render_template('page1.html', methods=['GET', 'POST'])
    
@app.route('/page2')
def renderPage2():
    return render_template('page2.html', methods=['GET', 'POST'])

if __name__=="__main__":
    app.run(debug=True)
