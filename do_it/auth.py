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
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')
        password1 = request.form.get('password1')

        if len(email) < 5:
            flash('Please enter a valid email address.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 characters', category='error')
        elif password != password1:
            flash('Passwords must match', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            flash('Success', category='success')

    return render_template("register.html")

