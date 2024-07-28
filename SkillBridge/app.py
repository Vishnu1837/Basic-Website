from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

def validate_login(email, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
    user = c.fetchone()
    conn.close()
    return user

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = validate_login(email, password)
        if user:
            flash('Login successful!', 'success')
            return render_template('home.html')
        else:
            flash('Invalid email or password', 'danger')
    return render_template('loginpage.html')
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conf_password = request.form['confirm_password']
        if password != conf_password:
            flash('Passwords do not match', 'danger')
            return redirect(url_for('signup'))
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
        conn.commit()
        conn.close()
        
        flash('Signup successful! Please login.', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html')
@app.route('/AboutUs')
def AboutUs():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
