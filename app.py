from flask import Flask, redirect, url_for, render_template, request
import sheets

app = Flask(__name__)

amount = 0
description = ""
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/infiniaPoints/add", methods=["POST", "GET"])
def login():
    global description
    global amount
    if request.method == "POST":
        user = request.form["nm"].lower()
        description = request.form["desc"]
        amount = request.form["amount"]
        points = request.form["points"]
        action = request.form["action"]
        calculate = request.form["calculate"]
        if points and amount:
            return redirect(url_for("wrong_input"))
        elif points and action == "add":
            return redirect(url_for("wrong_input"))
        elif amount and action == "sub":
            return redirect(url_for("wrong_input"))
        if user in ["ram", "nikhil"]:
            sheets.call_sheets(user=user, description=description, amount=amount, action=action, points=points, calculate=calculate)
            return redirect(url_for("user", usr=user))
        else:
            return redirect(url_for("unauth_user"))
    else:
        return render_template("details.html")


@app.route("/<usr>")
def user(usr):
    plain_str =  f"<h1>Submitted</h1><p>Thanks {usr}, The Amount: {amount} has been added with description: {description}</p>" \
                 f"""<br><a href="https://docs.google.com/spreadsheets/d/1nB1f7ukYTxhDDyFF01IxV_WAUaIG4YBNplNSK0erBz0/edit#gid=0">Click here to view your entry</a>"""
    return plain_str

@app.route("/unauth_user")
def unauth_user():
    return f"<h1>unauthorise user</h1>"

@app.route("/wrong_input")
def wrong_input():
    return f"<p>wrong_input given, At a point only amount can be added or point can be subtracted from the list. Please give one.</p>"


if __name__ == "__main__":
    app.run(debug=True)
