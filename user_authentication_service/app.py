#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, jsonify, request, redirect, abort
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"])
def welcome():
    """Return a welcome message"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users():
    """Return a list of users"""
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already registered"})


@app.route("/sessions", methods=["POST"])
def login():
    """login"""
    email = request.form.get("email")
    password = request.form.get("password")

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response
    else:
        abort(401)


@app.route("/sessions", methods=["DELETE"])
def logout():
    """logout"""
    session_cookie = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_cookie)
    if user:
        AUTH.destroy_session(user.id)
        return redirect("/")
    else:
        abort(403)


@app.route("/profile", methods=["GET"])
def profile():
    """Return user profile"""
    session_cookie = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_cookie)
    if user:
        return jsonify({"email": user.email})
    else:
        abort(403)


@app.route("/reset_password", methods=["POST"])
def get_reset_password_token():
    """get reset password token"""
    email = request.form.get("email")
    try:
        token = AUTH.get_reset_password_token(email)
        if token:
            return jsonify({"email": email, "reset_token": token})
        else:
            abort(403)
    except ValueError:
        abort(403)


@app.route("/reset_password", methods=["PUT"])
def update_password():
    """update password"""
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    password = request.form.get("password")
    try:
        AUTH.update_password(reset_token, password)
        return jsonify({"email": email, "message": "Password updated"})
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
