from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "logout"


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        email = request.form.get('email')
        password = request.form.get('password')
        password1 = request.form.get('password1')

        if len(email) < 5:
            flash('Please enter a valid email address.')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 characters')
        elif len(lastName):
            flash('Last name must be greater than 1 characters')
        elif password != password1:
            flash('Passwords must match')
        elif len(password) < 7:
            flash('Password must be at least 7 characters')
        else:
            flash('Success')

    return render_template("register.html")

