#===========================================================
# PROJECT NAME HERE
# By YOUR NAME HERE
#===========================================================

from flask import Flask, request, session, render_template, flash, redirect, send_file, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from os import getenv
from io import BytesIO
import html
from app.helpers import *


# Create the app
app = Flask(__name__)


#===========================================================
# App Routes Handlers
#===========================================================

# #-----------------------------------------------------------
# # Home page - Show all notes
# #-----------------------------------------------------------
# @app.get("/")
# def show_home_page():
#     with connect_db() as db:
#         sql = """
#             SELECT id, title, body, pinned, created
#             FROM note
#             ORDER BY pinned DESC, created DESC
#         """
#         params = ()
#         notes = db.execute(sql, params).fetchall()

#         flash("Test message")
#         flash("Test SUCCESS message", "success")
#         flash("Test INFO message", "info")
#         flash("Test WARNING message", "warning")
#         flash("Test ERROR message", "error")

#         return render_template("pages/note_list.jinja", notes=notes)


#===========================================================
# Home Page
#===========================================================
@app.get("/")
def show_home_page():
    return render_template("pages/home.jinja")

#===========================================================
# Sign Up Page
#===========================================================
@app.get("/signup/form")
def show_sign_up_page():
    return render_template("pages/sign_up.jinja")

#===========================================================
# Create New Account
#===========================================================
@app.post("/signup")
def create_account():
    username = request.form.get('username', '').strip().lower()
    password = request.form.get('password', '').strip()

    with connect_db() as db:
        sql = "SELECT id FROM users WHERE username=?"
        params = (username,)
        user = db.execute(sql, params).fetchone()

        if user:
            flash(f"That username is already taken.", "error")
            return redirect("/signup/form")

        pass_hash = generate_password_hash(password)

        sql = """
            INSERT INTO users (username, pass_hash)
            VALUES (?, ?)
        """
        params = (username, pass_hash)
        db.execute(sql, params)

        flash("Account created, please login", "success")
        return redirect("/login/form")

#===========================================================
# Log In Page
#===========================================================
@app.get("/login/form")
def show_log_in_page():
    return render_template("pages/log_in.jinja")

#===========================================================
# LogIn User
#===========================================================
@app.post("/login")
def log_in():
    username = request.form.get('username', '').strip().lower()
    password = request.form.get('password', '').strip()

    with connect_db() as db:
        sql = """
            SELECT id, username, pass_hash
            FROM users
            WHERE username=?
        """
        params = (username,)
        user = db.execute(sql, params).fetchone()

        if not user:
            flash(f"This account does not exist.", "error")
            return redirect("/login/form")

        if not check_password_hash(user["pass_hash"], password):
            flash(f"That password does not match ", "error")
            return redirect("/login/form")

        session["logged_in"] = True
        session["user"] = {
            "id":       user["id"],
            "username": user["username"],
        }

        flash("Login successful", "success")
        return redirect("/")

#===========================================================
# LogOut User
#===========================================================
@app.get("/logout")
def log_out():
    session.clear()
    flash(f"Logged out successfuly", "success")
    return redirect("/")

#===========================================================
# Search Tracker ID
#===========================================================
@app.post("/search")
def search():
    target_id = request.form.get('id', '').strip()

    with connect_db() as db:
        sql = """
            SELECT id, name
            FROM trackers
            where id = ?
        """
        params = (target_id,)
        tracker = db.execute(sql, params).fetchone()

        if not tracker:
            flash(f"No results found matching that ID", "error")
            return redirect("/")

        return render_template("pages/view_page.jinja", info = tracker)



#===========================================================
# Configure the app
#===========================================================
load_dotenv()
app.config.from_prefixed_env()
init_logging(app)
init_text_filters(app)
init_date_filters(app)
init_error_handlers(app)
init_database()
register_commands(app)

