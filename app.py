from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/problems")
def problems():
    return render_template("problems.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        team_name = request.form["team_name"]
        email = request.form["email"]

        print("New Registration:")
        print("Team:", team_name)
        print("Email:", email)

        return "Registration Successful!"

    return render_template("register.html")


@app.route("/submit")
def submit():
    return render_template("submit.html")

@app.route("/track")
def track():
    return render_template("track.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        role = request.form.get("role")  # Captures 'student' or 'admin'

        print(f"Login Attempt - Role: {role}, Email: {email}")

        if role == "admin":
            # In the future, verify admin credentials here
            return render_template("admin.html")
        else:
            # In the future, verify student credentials here
            return render_template("track.html")

    return render_template("login.html")



app = app


