from wtforms import Form
from wtforms import IntegerField, SelectField, RadioField

class distanceForm(Form):
    x1 = IntegerField("Punto X1")
    y1 = IntegerField("Punto Y1")
    x2 = IntegerField("Punto X2")
    y2 = IntegerField("Punto Y2")


class resistenciaForm(Form):
    banda1 = SelectField("Banda 1", coerce=str, choices=[('Negro'), ('Cafe'), ('Rojo'), ('Naranja'), ('Amarillo'), ('Verde'), ('Azul'), ('Violeta'), ('Gris'), ('Blanco')])
    banda2 = SelectField("Banda 2", coerce=str, choices=[('Negro'), ('Cafe'), ('Rojo'), ('Naranja'), ('Amarillo'), ('Verde'), ('Azul'), ('Violeta'), ('Gris'), ('Blanco')])
    banda3 = SelectField("Banda 3", coerce=str, choices=[('Negro'), ('Cafe'), ('Rojo'), ('Naranja'), ('Amarillo'), ('Verde'), ('Azul'), ('Violeta'), ('Gris'), ('Blanco')])
    tolerancia = RadioField("Tolerancia", choices = [('Dorado'), ('Plata'), ('Rojo')])
    