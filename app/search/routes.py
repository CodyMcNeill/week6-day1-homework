from flask import render_template, request, redirect, url_for, Blueprint
from .forms import searchPoke
from ..models import Pokemon, db, Team
from .services import get_poke_info
from flask_login import login_user, logout_user, current_user, login_required

search = Blueprint('search', __name__)

@search.route('/pokedex', methods=['GET', 'POST'])
def pokedexPage():
    form = searchPoke()
    if request.method == 'POST':
        if form.validate_on_submit():
            search = form.searchBody.data.lower()
            data = get_poke_info(search)
            name = data['name']
            ability = data['ability']
            base_xp = data['base_xp']
            front_shiny = data['front_shiny']
            base_atk = data['base_atk']
            base_hp = data['base_hp']
            base_def = data['base_def']
            pokemon = Pokemon(name, ability, base_xp, front_shiny, base_atk, base_hp, base_def)
            test = Pokemon.query.filter_by(name=name).first()
            if test:
                pass
            else:
                pokemon.saveToDB()
            
            if current_user.is_authenticated:
                team = db.session.query(Pokemon).join(Team, Team.poke_name == Pokemon.name).filter(Team.user_id == current_user.id).all()
            return render_template('search.html', name=name, ability=ability, base_xp=base_xp, front_shiny=front_shiny, base_atk=base_atk, base_hp=base_hp, base_def=base_def)
    return render_template('pokedex.html', form = form)


@search.route('/pokedex/capture/<poke_name>', methods= ['GET', 'POST'])
@login_required
def capturePage(poke_name):
    team = Team(current_user.id, poke_name)
    team_count = Team.query.filter_by(user_id=current_user.id).count()
    existing_poke = Team.query.filter_by(user_id=current_user.id, poke_name=poke_name).all()
    print(existing_poke)
    if team_count > 5:
        pass
    else:
        team.saveToDB()
    return redirect(url_for('battle.battlePage'))

@search.route('/pokedex/release/<poke_name>', methods= ['GET', 'POST'])
@login_required
def releasePage(poke_name):
    team = Team.query.filter_by(user_id=current_user.id, poke_name=poke_name).first()
    team.deleteFromDB()
    return redirect(url_for('battle.battlePage'))

