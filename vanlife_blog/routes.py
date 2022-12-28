from flask import Blueprint, render_template, request, flash, url_for, redirect, jsonify
from flask_login import login_user, logout_user, login_required, current_user, login_manager
from vanlife_blog import app, db
from vanlife_blog.models import User, Post, Comment, Like

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
    else:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted.', 'success')
    
    return redirect(url_for('blog'))


@app.route('/edit_post/<post_id>', methods=('GET', 'POST'))
@login_required
def edit_post(post_id):
    text = request.form.get('text')

    if request.method == 'POST':
        text = request.form.get('text')
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('blog'))

    return render_template('edit_post.html')


@app.route("/posts/<username>")
@login_required
def posts(username):
    user = User.query.filter_by(username=username).first()

    if not user:
        flash('User does not exist', 'error')
        return redirect(url_for('home'))

    posts = user.posts
    return render_template('posts.html', user=current_user, posts=posts, username=username)


@app.route("/create-comment/<post_id>", methods=["POST"])
@login_required
def create_comment(post_id):
    text = request.form.get('text')

    if not text:
        flash('Comment cannot be empty', 'error')
    else:
        post = Post.query.filter_by(id=post_id)
        if post:
            comment = Comment(text=text, author=current_user.id, post_id=post_id)
            db.session.add(comment)
            db.session.commit()
        else:
            flash('Post does not exist', 'error')

    return redirect(url_for('blog'))


@app.route("/delete-comment/<comment_id>")
@login_required
def delete_comment(comment_id):
    comment = Comment.query.filter_by(id=comment_id).first()

    if not comment:
        flash('Comment does not exist', 'error')
    else:
        db.session.delete(comment)
        db.session.commit()
    
    return redirect(url_for('blog'))


@app.route("/like-post/<post_id>", methods=["POST"])
@login_required
def like(post_id):
    post = Post.query.filter_by(id=post_id).first()
    like = Like.query.filter_by(author=current_user.id, post_id=post_id).first()

    if not post:
        return jsonify({'error': 'Post does not exist.'}, 400)
    elif like:
        db.session.delete(like)
        db.session.commit()
    else:
        like = Like(author=current_user.id, post_id=post_id)
        db.session.add(like)
        db.session.commit()
    
    return jsonify({"likes": len(post.likes), "liked": current_user.id in map(lambda x: x.author, post.likes)})
        
