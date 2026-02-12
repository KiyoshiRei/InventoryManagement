from flask import Flask , render_template, url_for, request, redirect,session
from flask_login import LoginManager , login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
load_dotenv()
from db import get_connection
from models.usermodel import User


app = Flask(__name__)
app.secret_key="idkwhyiamputtingthisintheopenhereiwillchangeitlateron"

login_manager= LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(uid):
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute(
        "select uid,username,role from users where uid = %s",(uid,) 
    )
    
    row = cur.fetchone()

    cur.close()
    conn.close()

    if row:
        return User(*row)
    return None


@app.route('/',methods=['POST','GET'])

def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "select uid,username,passwd_hash,role from users where username = %s",(username,)
        )
    
        row = cur.fetchone()

        cur.close()
        conn.close()

        if row and check_password_hash(row[2],password):
            user = User(row[0],row[1],row[3])
            login_user(user)
            return redirect(url_for("dashboard"))

        return "Invalid Credentials"

    return render_template("login.html")



@app.route('/dashboard')

@login_required
def dashboard():
    '''if 'user' not in session:
        return redirect(url_for('login'))'''
    return render_template('dashboard.html')


@app.route('/add_item', methods=['GET', 'POST'])

def add_item():
    return render_template('add_item.html')


@app.route('/items')

def list_items():
    return render_template('list_items.html')


@app.route('/warehouses')

def list_warehouses():
    return render_template('list_warehouses.html')


@app.route('/logout')
@login_required
def logout():  
    logout_user()
    return redirect(url_for('login'))



if __name__=="__main__":
    app.run(debug=True,port=5000)
