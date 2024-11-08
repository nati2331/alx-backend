#!/usr/bin/env python3
"""A Basic Flask app demonstrating Babel localization with language selection.
"""

from flask import Flask, render_template, request
from flask_babel import Babel

class Config:
    """Configuration for supported languages and localization settings.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False  # Handle URLs with and without trailing slashes
babel = Babel(app)

@babel.localeselector
def get_locale() -> str:
    """Retrieve the best-matching language for the request.
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])

@app.route('/')
def index() -> str:
    """Render the homepage template with localized content.
    """
    return render_template('2-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
