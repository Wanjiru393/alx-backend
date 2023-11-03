#!/usr/bin/env python3
"""Basic flask application"""


from flask import Flask, render_template, request
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


@babel.localeselector
def get_locale():
    """using request.accept_languages to determine the best
    match with supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """ serves 2-index.html file for route /"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(debug=True)
