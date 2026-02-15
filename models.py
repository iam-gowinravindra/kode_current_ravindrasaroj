from flask import Flask, render_template, request

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
