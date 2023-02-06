from flask import Blueprint
from flask_login import login_user, logout_user, current_user, login_required
from ..models import Pokemon, db, Team

battle = Blueprint('battle', __name__)

