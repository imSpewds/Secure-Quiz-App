import os
from flask import Flask, url_for, render_template, request, Markup
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

@app.route('/page1', methods=['GET', 'POST'])
def renderPage1():
    return render_template('page1.html')
    
@app.route('/page2', methods=['GET', 'POST'])
def renderPage2():
    if 'firstQ' not in session:
        session['firstQ'] = request.form['firstQ']
    return render_template('page2.html')
    
@app.route('/page3', methods=['GET', 'POST'])
def renderPage3():
    if 'secondQ' not in session:
        session['secondQ'] = request.form['secondQ']
    return render_template('page3.html')

@app.route('/page4', methods=['GET', 'POST'])
def renderpage4():
    if 'thirdQ' not in session:
        session['thirdQ'] = request.form['thirdQ']
    return render_template('page4.html', isRight1 = isRight1(), isRight2 = isRight2(), isRight3 = isRight3())
    
def isRight1():
    response = session['firstQ']
    first = response.lower()
    answer = ""
    if first == "asia":
        answer = answer + Markup("Correct")
    else:
        answer = answer + Markup("Wrong")
    return answer
    
def isRight2():
    response = session['secondQ']
    second = response.lower()
    answer = ""
    if second == "mount everest":
        answer = answer + Markup("Correct")
    else:
        answer = answer + Markup("Wrong")
    return answer
    
def isRight3():
    response = session['thirdQ']
    third = response.lower()
    answer = ""
    if third == "florida":
        answer = answer + Markup("Correct")
    else:
        answer = answer + Markup("Wrong")
    return answer
    
if __name__=="__main__":
    app.run(debug=True)
