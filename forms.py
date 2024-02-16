from wtforms import Form
from wtforms import IntegerField, SelectField, RadioField, StringField
from wtforms import validators

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

class insertarPalabraFrom(Form):
    palabraIngles = StringField('Ingles', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=2, max=20, message='Ingresa una palabra valida')
    ])
    palabraEspanol = StringField('Español', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=2, max=20, message='Ingresa una palabra valida')
    ])

class buscarPalabraForm(Form):
    lenguaje = RadioField('Idioma', [
        validators.DataRequired(message='Selecciona un idioma')
    ], choices=[('Español'), ('Ingles')])
    palabra = StringField('Palabra', [
        validators.DataRequired(message='Ingresa la palabra que deseas buscar'),
        validators.length(min=2, max=20, message='Ingresa una palabra valida')
    ])
    