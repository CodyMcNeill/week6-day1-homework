from flask import render_template, request, redirect, url_for, Blueprint
from flask_login import login_user, logout_user, current_user, login_required
from ..models import Pokemon, db, Team, User

battle = Blueprint('battle', __name__)

@battle.route('/battle', methods=['GET', 'POST'])
@login_required
def battlePage():
    team = db.session.query(Pokemon).join(Team, Team.poke_name == Pokemon.name).filter(Team.user_id == current_user.id).all()
    # test = 'charmander'
    # for poke in team:
    #     if poke.name == test:
    #         print(True)
    # print(team)
    # print(team[0].name)
    enemies = db.session.query(User).filter(User.id != current_user.id).all()
    return render_template('battle.html', team=team, enemies=enemies)

@battle.route('/battle/<username>', methods=['GET', 'POST'])
@login_required
def fightPage(username, **do_battle):
    username = db.session.query(User).filter(User.username == username).first()
    my_team = db.session.query(Pokemon).join(Team, Team.poke_name == Pokemon.name).filter(Team.user_id == current_user.id).all()
    enemy_team = db.session.query(Pokemon).join(Team, Team.poke_name == Pokemon.name).filter(Team.user_id == username.id).all()
    do_battle = False
    if do_battle == True:
        for my_poke in my_team:
            print(sum(my_poke.base_hp))
        do_battle = False
        return redirect('battle.fightPage')
    return render_template('fight.html', my_team=my_team, enemy_team=enemy_team, username=username, do_battle=do_battle)
