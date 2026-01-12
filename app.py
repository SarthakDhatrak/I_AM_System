from flask import Flask, render_template, request, redirect, session
from auth import authenticate, get_permissions

app = Flask(__name__)
app.secret_key = "iam_secret_key"

@app.route("/", methods=["GET", "POST"])
def login():
    error = ""
    if request.method == "POST":
        user = authenticate(
            request.form["username"],
            request.form["password"]
        )

        if user:
            session["user"] = user["username"]
            session["role"] = user["role"]
            session["permissions"] = get_permissions(user["role"])
            return redirect("/dashboard")
        else:
            error = "Invalid credentials"

    return render_template("login.html", error=error)

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")

    return render_template(
        "dashboard.html",
        role=session["role"],
        permissions=session["permissions"]
    )

@app.route("/admin")
def admin():
    if "MANAGE_USERS" not in session.get("permissions", []):
        return "Access Denied", 403

    return render_template("admin.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
