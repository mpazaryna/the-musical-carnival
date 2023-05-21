"""
This module provides functionalities for XYZ.

Author: Your Name
"""
import os
from dotenv import load_dotenv
from flask import Flask, render_template

# Load environment variables from the .env file
load_dotenv()

# Read the API key from the environment variable
api_key = os.getenv("API_KEY")

app = Flask(__name__)

@app.route('/')
def hello():
    """
    Render the home page template.

    Returns:
        A rendered HTML template.
    """
    return render_template('home.html')

@app.route('/about')
def about():
    """
    Render the about page template.

    Returns:
        A rendered HTML template.
    """
    return render_template('about.html')

if __name__ == '__main__':
    app.run()
