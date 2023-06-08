from flask import Blueprint, render_template

views = Blueprint("views", __name__)


@views.route("/")
def home():
    # return "<h1>Test</h1>"
    # with open('andelsbiodling.txt','r') as file:
    #     text_to_show = file.read()
    text_to_show = "bla bla"
    # return render_template("base.html", text=text_to_show)
    # return render_template("andelsbiodling.html", text=text_to_show)
    return render_template("home.html")