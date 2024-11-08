#!/usr/bin/env python3
"""
Basic Flask app with Babel setup for internationalization and language support.
"""

from flask import Flask, render_template
from flask_babel import Babel

class Config:
    """
    Configuration class for setting up supported languages and default localization settings.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__)
app.config.from_object(Config)

# Initialize Babel after setting up the configuration
babel = Babel(app)

@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """
    Render the index page with a welcome message.
    """
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run(debug=True)
