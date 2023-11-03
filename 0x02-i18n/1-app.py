#!/usr/bin/env python3
"""Basic flask application"""


from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """A config class with default
    local and timezone
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/")
def index():
    """ serves 0-index.html file for route /"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
