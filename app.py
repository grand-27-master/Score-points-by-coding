from flask import Flask,request,render_template
import joblib

app=Flask(__name__)

model=joblib.load('model.pkl')

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def marks():
    if request.method=='POST':
        hours=int(request.form['hours'])
        marks=str(model.predict([[hours]]))

    return render_template('index.html',your_marks=marks)

if __name__=='__main__':
    app.run(debug=True)
