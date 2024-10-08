from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, IntegerField, FloatField, SubmitField, URLField, BooleanField, EmailField, TelField
from wtforms.widgets import CheckboxInput, ListWidget
from wtforms.validators import DataRequired
from locale import LC_ALL, setlocale

setlocale(LC_ALL, 'it_IT.UTF-8')


class AddLapForm(FlaskForm):
    date = StringField("Data della tappa", validators=[DataRequired()])
    start = StringField("Partenza", validators=[DataRequired()])
    destination = StringField("Arrivo", validators=[DataRequired()])
    distance = FloatField("Distanza")
    ascent = IntegerField("Dislivello salita")
    descent = IntegerField("Dislivello discesa")
    duration = StringField("Tempo previsto")
    gpx = FileField("Track file (.gpx)", validators=[FileAllowed(['gpx'])])
    submit = SubmitField('OK')


class UpdLapForm(FlaskForm):
    date = StringField("Data della tappa", validators=[DataRequired()])
    distance = FloatField("Distanza")
    ascent = IntegerField("Dislivello salita")
    descent = IntegerField("Dislivello discesa")
    duration = StringField("Tempo previsto")
    gpx = FileField("Track file (.gpx)", validators=[FileAllowed(['gpx'])])
    done = BooleanField('OK è fatta!')
    submit = SubmitField('OK')


class AddHotelForm(FlaskForm):
    name = StringField("Albergo", validators=[DataRequired()])
    address = StringField("Indirizzo", validators=[DataRequired()])
    town = StringField("Città", validators=[DataRequired()])
    geo_lat = FloatField("Lat. & Long.")
    geo_long = FloatField()
    email = EmailField("E-mail")
    phone = TelField("Telefono")
    check_in = StringField("Data check-in")
    check_out = StringField("Data check-out")
    price = FloatField("Costo")
    photo = FileField("Foto dell'albergo", validators=[FileAllowed(['webp', 'jpg', 'jpeg'])])
    website = URLField("Web site")
    reserved = BooleanField('È prenotato')
    submit = SubmitField('OK')


class UpdHotelForm(FlaskForm):
    email = EmailField("E-mail")
    phone = TelField("Telefono")
    geo_lat = FloatField("Lat. & Long.")
    geo_long = FloatField()
    check_in = StringField("Data check-in")
    check_out = StringField("Data check-out")
    price = FloatField("Costo")
    photo = FileField("Foto dell'albergo", validators=[FileAllowed(['webp', 'jpg', 'jpeg'])])
    website = URLField("Web site")
    reserved = BooleanField('È prenotato')
    submit = SubmitField('OK')
