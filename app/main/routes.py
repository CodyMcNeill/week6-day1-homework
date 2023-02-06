from app import app
from flask import render_template, request, redirect, url_for, Blueprint

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def homePage():
    # indexCopy1 = 'This is all placeholder text! Currently learning to pass python data through html via flask + jinja. This will all be beautified later down the road, I promise!'
    return render_template('index.html')