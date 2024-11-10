from datetime import datetime, date
from os import walk
from re import search
from . import db
from sqlalchemy import func
from flask import session, current_app
from .models import Tour, Lap

def make_header(lang):
    if 'trip' in session:
        trip = db.session.execute(db.select(Tour.id).where(Tour.name==session['trip'])).scalar()
        start = db.session.execute(db.select(Lap.start, Lap.date).where(
            Lap.date == db.session.execute(db.select(func.min(Lap.date)).where(Lap.tour_id == trip)).scalar())).fetchone()
        end = db.session.execute(db.select(Lap.destination, Lap.date).where(
            Lap.date == db.session.execute(db.select(func.max(Lap.date)).where(Lap.tour_id == trip)).scalar())).fetchone()
        header = f"""
            <h2>{start.start } - {end.destination }</h2>
            <h4>{start.date.strftime("%d %b %Y")} - {end.date.strftime("%d %b %Y")}</h4>
        """
    else:
        if lang == 'it':
            header = " <h2>I miei viaggi</h2>"
        elif lang == 'en':
            header = "<h2>My trips</h2>"
    return header

def make_dd_lang(lang):
    dd_lang = """
	    <div class='w3-dropdown-click w3-right'>
	    """
    if lang == 'it':
        dd_lang += '<button  id="dd_btn" class="w3-button w3-theme w3-hover-theme w3-ripple" data-cur-lang="it">ITA <i id="dd_caret" class="fa-solid fa-caret-down"></i></button>'
    elif lang == 'en':
        dd_lang += '<button  id="dd_btn" class="w3-button w3-theme w3-hover-theme w3-ripple" data-cur-lang="en">ENG <i id="dd_caret" class="fa-solid fa-caret-down"></i></button>'
    dd_lang += """
	    <div id="dd_menu" class="w3-dropdown-content w3-bar-block w3-border w3-card-4 w3-border-theme">
		    <button class="w3-bar-item w3-button w3-theme-l2 w3-hover-theme" data-lang="it">ITA</button>
		    <button class="w3-bar-item w3-button w3-theme-l2 w3-hover-theme" data-lang="en">ENG</button>
		</div>
	</div>
    """
    return dd_lang

def make_short_template(full_template):
    for root, dirs, files in walk(current_app.root_path):
        if full_template in files:
            templates_dir = root
            break

    with open(f"{templates_dir}/{full_template}") as IN, open(f"{templates_dir}/s_{full_template}", 'w') as OUT:
        copy = False
        for line in IN:
            if not copy:
                if search("\$Begin", line):
                    copy = True
            else:
                if search("\$End", line):
                    copy = False
                else:
                    OUT.write(line)

        return f"s_{full_template}"