from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    # logic to login
    flash('You were successfully logged in')
    return redirect(url_for('home'))

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    # logic to register
    flash('You were successfully registered and can log in now')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
