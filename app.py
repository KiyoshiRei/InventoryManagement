from flask import Flask , render_template, url_for, request, redirect,session

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])

def login():
    return render_template("login.html")

@app.route('/dashboard',methods=['POST','GET'])

def dash():
    return render_template("dashboard.html")


@app.route('/dashboard')

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
def logout():  
    return redirect(url_for('login'))



if __name__=="__main__":
    app.run(debug=True,port=5000)

@app.route('/dashboard')

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
def logout():  
    return redirect(url_for('login'))



if __name__=="__main__":
    app.run(debug=True,port=5000)
