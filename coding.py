from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import logging

mydb = mysql.connector.connect(user="root", password="Rocket246!", database="login")
logging.basicConfig(filename='flask_errors.log', level=logging.ERROR)

template = "./template"
appointments_csv = "./appointments.csv"
app = Flask(__name__, template_folder=template)
cur = mydb.cursor()
cur.execute("select * from userinfo")
a = cur.fetchall()
for i in a:
    print(i)


@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('landing.html')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cur = mydb.cursor()
        cur.execute("SELECT * FROM userinfo WHERE mailid = %s AND password = %s", (username, password))
        user = cur.fetchone()

        if user is not None:
            # Redirect to the signup page
            return redirect(url_for('maps'))
        else:
            # If user doesn't exist or credentials are incorrect, display error message
            error = "Invalid username or password. Please try again."
            return render_template('login.html', error=error)
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirmPassword']

        # Basic password validation
        if password != confirm_password:
            error = "Passwords do not match."
            return render_template('signup.html', error=error)

        # Save user data to database
        try:
            cur.execute("INSERT INTO userinfo (mailid, password) VALUES (%s, %s)", (username, password))
            mydb.commit()
            return redirect(url_for('login_page'))
        except mysql.connector.Error as err:
            error = f"Error: {err}"
            return render_template('signup.html', error=error)

    return render_template('signup.html')
@app.route('/maps', methods=['GET', 'POST'])
def maps():
    return render_template('map.html')
if __name__ == '__main__':
    app.run(debug=True, port=8001)
