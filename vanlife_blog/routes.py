from flask import render_template, request, flash, url_for, redirect, jsonify
from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user,
    login_manager,
)
from vanlife_blog import app, db
from vanlife_blog.models import User, Post, Comment, Like


@app.route("/")
def home():
    """
    Create home page route
    """
    return render_template("home.html")


@app.route("/blog", methods=["GET", "POST"])
@login_required
def blog():
    """
    Create blog post route & and handle blog post form
    """
    if request.method == "POST":
        text = request.form.get("text")

        if not text:
            flash("Post cannot be empty", "error")
        else:
            post = Post(text=text, author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash("Post created", "success")

    posts = Post.query.all()
    return render_template("blog.html", user=current_user, posts=posts)


@app.route("/delete-post/<id>")
@login_required
def delete_post(id):
    """
    Create route to delete posts
    """
    post = Post.query.filter_by(id=id).first()

    if not post:
        flash("Post does not exist", "error")
    else:
        db.session.delete(post)
        db.session.commit()
        flash("Post deleted", "success")

    return redirect(url_for("blog"))


@app.route("/edit_post/<id>", methods=("GET", "POST"))
@login_required
def edit_post(id):
    """
    Create route to edit posts
    """
    post = Post.query.filter_by(id=id).first()

    if request.method == "POST":
        text = request.form.get("text")

        if not text:
            flash("Post cannot be empty", "error")
        else:
            post.text = request.form.get("text")
            db.session.commit()
            flash("Post updated!", "success")
            return redirect(url_for("blog"))

    return render_template("edit_post.html", post=post)


@app.route("/posts/<username>")
@login_required
def posts(username):
    """
    Create posts route to view user posts
    """
    user = User.query.filter_by(username=username).first()

    if not user:
        flash("User does not exist", "error")
        return redirect(url_for("home"))

    posts = user.posts
    return render_template(
        "posts.html", user=current_user, posts=posts, username=username
    )


@app.route("/create-comment/<post_id>", methods=["POST"])
@login_required
def create_comment(post_id):
    """
    Create route that handles comments
    """
    text = request.form.get("text")

    if not text:
        flash("Comment cannot be empty", "error")
    else:
        post = Post.query.filter_by(id=post_id)
        if post:
            comment = Comment(
                text=text,
                author=current_user.id,
                post_id=post_id
            )
            db.session.add(comment)
            db.session.commit()
        else:
            flash("Post does not exist", "error")

    return redirect(url_for("blog"))


@app.route("/delete-comment/<comment_id>")
@login_required
def delete_comment(comment_id):
    """
    Create route to delete comments
    """
    comment = Comment.query.filter_by(id=comment_id).first()

    if not comment:
        flash("Comment does not exist", "error")
    else:
        flash("Comment deleted", "success")
        db.session.delete(comment)
        db.session.commit()

    return redirect(url_for("blog"))


@app.route("/like-post/<post_id>", methods=["POST"])
@login_required
def like(post_id):
    """
    Create route that handles like function
    """
    post = Post.query.filter_by(id=post_id).first()
    like = Like.query.filter_by(
        author=current_user.id,
        post_id=post_id
    ).first()

    if not post:
        return jsonify({"error": "Post does not exist."}, 400)
    elif like:
        db.session.delete(like)
        db.session.commit()
    else:
        like = Like(author=current_user.id, post_id=post_id)
        db.session.add(like)
        db.session.commit()

    return jsonify(
        {
            "likes": len(post.likes),
            "liked": current_user.id in map(lambda x: x.author, post.likes),
        }
    )


@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    """
    Create route for dashboard page
    """
    app_users = User.query.order_by(User.date_created)
    admin = current_user.id

    return render_template("dashboard.html", app_users=app_users, admin=admin)


@app.route("/edit_user/<id>", methods=["GET", "POST"])
@login_required
def edit_user(id):
    """
    Create route that handles form to edit user
    """
    username_to_update = User.query.filter_by(id=id).first()

    if request.method == "POST":
        text = request.form.get("username")
        username = request.form.get("username")
        username_exists = User.query.filter_by(username=username).first()

        if not text:
            flash("Username cannot be empty", "error")
        elif username_exists:
            flash("Username is already in use", "error")
        else:
            username_to_update.username = request.form["username"]
            db.session.commit()
            flash("Username updated", "success")
            return redirect(url_for("dashboard"))

    return render_template(
        "edit_user.html",
        username_to_update=username_to_update
    )


@app.route("/delete_user/<id>", methods=["GET", "POST"])
@login_required
def delete_user(id):
    """
    Create route to delete users
    """
    user_to_delete = User.query.filter_by(id=id).first()

    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        flash("User deleted", "success")
        return render_template("dashboard.html", user_to_delete=user_to_delete)

    except Exception():
        flash("User does not exist", "error")
