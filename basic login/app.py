from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary in-memory user storage
users = {}


@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            return f"<h2>Welcome, {username}!</h2>"
        else:
            return "<h3>Invalid credentials! Try again.</h3>"

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            return "<h3>User already exists!</h3>"
        else:
            users[username] = password
            return redirect(url_for('login'))

    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
