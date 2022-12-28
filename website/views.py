from flask import Blueprint, render_template

views = Blueprint("views", __name__)


@views.route("/")
def home():
    # return "<h1>Test</h1>"
    text_to_show = "Test bla"

    return render_template("index.html", text=text_to_show)