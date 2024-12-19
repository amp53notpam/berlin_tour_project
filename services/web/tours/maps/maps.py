from datetime import date, timedelta
from os.path import join
from flask import (
    Blueprint, flash, render_template, current_app, url_for, jsonify, session, typing as ft
)
from flask.views import View
from sqlalchemy.exc import OperationalError, ProgrammingError
from .. import db
from ..models import Lap, Hotel, Tour, Media
from ..utils import make_header, make_short_template

map_bp = Blueprint('map_bp', __name__,
                   url_prefix="/maps",
                   static_folder='static',
                   template_folder='templates'
                   )

@map_bp.context_processor
def add_upload_path():
    return dict(upload_path=current_app.config['UPLOAD_FOLDER'])

def get_trip():
    active_trip = db.session.execute(db.select(Tour).where(Tour.is_active == True)).fetchone()
    return active_trip.Tour.id


class HotelMap(View):
    def dispatch_request(self, lat, long):
        hotel = db.session.execute(db.select(Hotel).where(Hotel.lat == lat and Hotel.long == long)).scalar()
        gpx = db.session.get(Lap, hotel.lap_id).gpx

        return render_template("map_hotel.jinja2", lat=lat, long=long, popup=hotel.name, media=None, track=gpx)


class PhotoMap(View):
    def dispatch_request(self, lat, long):
        media = db.session.execute(db.select(Media).where(Media.lat == lat and Media.long == long)).scalar()
        gpx = db.session.get(Lap, media.lap_id).gpx
        foto_on_track = db.session.execute(db.select(Media).where(Media.lap_id == media.lap_id, Media.lat != None)).fetchall()

        #gpx = join(current_app.config['UPLOAD_FOLDER'], 'tracks', gpx)

        return render_template("map_photo.jinja2", lat=lat, long=long, media=foto_on_track, track=gpx)


map_bp.add_url_rule('/albergi/<float:lat>/<float:long>', view_func=HotelMap.as_view('hotel_map'))
map_bp.add_url_rule('/foto/<float:lat>/<float:long>', view_func=PhotoMap.as_view('photo_map'))
