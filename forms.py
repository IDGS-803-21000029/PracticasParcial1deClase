from wtforms import Form
from wtforms import IntegerField

class distanceForm(Form):
    x1 = IntegerField("Punto X1")
    y1 = IntegerField("Punto Y1")
    x2 = IntegerField("Punto X2")
    y2 = IntegerField("Punto Y2")


