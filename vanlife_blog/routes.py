from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask_login import login_user, logout_user, login_required, current_user, login_manager
from vanlife_blog import app, db
from vanlife_blog.models import User, Post

# views = Blueprint('routes', __name__)


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
            flash('Post created!', 'success')

    posts = Post.query.all()
    return render_template("blog.html", user=current_user, posts=posts)


@app.route("/delete-post/<id>")
@login_required
def delete_post(id):
    post = Post.query.filter_by(id=id).first()

    if not post:
        flash("Post does not exist.", 'error')
    elif current_user.id != post.id:
        flash('You do not have permission to delete this post.', 'error')
    else:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted.', 'success')
    
    return redirect(url_for('blog'))


@app.route("/posts/<username>")
@login_required
def posts(username):
    user = User.query.filter_by(username=username).first()

    if not user:
        flash('User does not exist', 'error')
        return redirect(url_for('home'))

    posts = Post.query.filter_by(author=user.id).all()
    return render_template('posts.html', user=current_user, posts=posts, username=username)