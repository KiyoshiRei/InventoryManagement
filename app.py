from flask import Flask , render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])

def login():
    return render_template("login.html")

@app.route('/dashboard',methods=['POST','GET'])

def dash():
    return render_template("dashboard.html")

if __name__=="__main__":
    app.run(debug=True,port=5000)