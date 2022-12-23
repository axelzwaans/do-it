from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask_login import UserMixin, login_required, LoginManager, current_user, logout_user, login_user
from vanlife_blog import app, db
from vanlife_blog.models import User, Post


@app.route('/')
# @login_required
def home():
    return render_template("home.html")


@app.route('/blog', methods=['GET', 'POST'])
@login_required
def blog():
    if request.method == 'POST':
        text = request.form.get('text')

        if not text:
            flash('Post cannot be empty', 'error')
        else:
            post = Post(text=text, author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash('Post created!', category='success')

    posts = Post.query.all()        
    return render_template("blog.html", user=current_user, posts=posts)