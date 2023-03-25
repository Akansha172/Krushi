from flask import Flask,render_template,url_for,redirect,request
app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/answer/<string:ans>')
def func(ans):
    print(ans)
    return render_template('index2.html',answ=ans)

@app.route('/submit',methods=['POST','GET'])
def submit():
  if request.method=='POST':
    question='======================'
    question=request.form['textbox']
    print(question)
    questionvoice=request.form['speechtotext']
    print(questionvoice)
    ansr="this will be answer"
  return redirect(url_for('func',ans=ansr))


if __name__=='__main__':
    app.run(debug=True)