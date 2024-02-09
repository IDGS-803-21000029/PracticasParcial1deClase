from flask import Flask, render_template, request
import forms
import math
import coloresResistencia

app = Flask(__name__)

# Raiz
@app.route("/")
def index():
    escuela = "UTL"
    alumnos = ["Mario", "Pedro", "Luis", "Dario"]

    return render_template("index.html", escuela=escuela, alumnos=alumnos)

# Practica de Operaciones
@app.route("/formulario")
def form():
    return render_template("formOperaciones.html")

@app.route("/operacion", methods=["POST"])
def operaciones():
    ope = request.form.get("ope")
    num1 = request.form.get("n1")
    num2 = request.form.get("n2")
    
    if ope == "1":
        return "<h1>La suma es: {}</h1>".format(str(int(num1) + int(num2)))
    elif ope == "2":
        return "<h1>La resta es: {}</h1>".format(str(int(num1) - int(num2)))
    elif ope == "3":
        return "<h1>La multiplicacion es: {}</h1>".format(str(int(num1) * int(num2)))
    elif ope == "4":
        return "<h1>La division es: {}</h1>".format(str(int(num1) / int(num2)))
    else:
        return "<h1>No se ha podido identificar la operacion</h1>"
    
# BOLETOS CINEPOLIS
@app.route("/cinepolis", methods=["POST", "GET"])
def cine():
    if request.method == "GET":
        return render_template("cinepolis.html", total=0, nombre="")
    else:
        nombre = request.form.get("txtNombre")
        cantidadCompradores = request.form.get("txtCantCompradores")
        tarjeta = request.form.get("card")
        cantidadBoletos = request.form.get("txtCantBoletos")

        if int(cantidadBoletos) > int(cantidadCompradores) * 7:
            return render_template("cinepolis.html", mensaje="No se pueden vender mas de 7 boletos por persona, vuelva a intentarlo", total=0)
        else:
            valorSubtotal = float(cantidadBoletos) * 12.000
        
        if int(cantidadBoletos) > 5:
            valorTotal = valorSubtotal - (valorSubtotal * 0.15)
        elif int(cantidadBoletos) > 2:
            valorTotal = valorSubtotal - (valorSubtotal * 0.10)
        else:
            valorTotal = valorSubtotal

        if tarjeta == "1":
            valorTotal = valorTotal - (valorTotal * 0.10)

        return render_template("cinepolis.html", total=float(valorTotal), nombre=str(nombre))
    
# FORMULA DISTANCIA
@app.route("/distancia", methods=("GET", "POST"))
def distancia():
    dis_form = forms.distanceForm(request.form)
    if request.method == "GET":
        return render_template("distanciaEntrePuntos.html", form=dis_form, total=0)
    else:
        x1 = float(dis_form.x1.data)
        y1 = float(dis_form.y1.data)
        x2 = float(dis_form.x2.data)
        y2 = float(dis_form.y2.data)
        total:float = 0

        sum = (math.pow((x2 - x1), 2)) + (math.pow((y2 - y1), 2))
        total = math.sqrt(sum)

        return render_template("distanciaEntrePuntos.html", form=dis_form, total=float(total))
    
# CALCULADORA DE RESISTENCIAS
@app.route("/resistencia", methods=["GET", "POST"])
def calculoResistencias():
    res_form = forms.resistenciaForm(request.form)

    if request.method == "GET":
        return render_template("calculoResistencias.html", form=res_form, valor=0, valorMax=0, valorMin=0, colb1="", colb2="", colb3="", coltol="")
    else:
        banda1 = str(res_form.banda1.data)
        banda2 = str(res_form.banda2.data)
        banda3 = str(res_form.banda3.data)
        tolerancia = str(res_form.tolerancia.data)

        resultado = coloresResistencia.calcularResistencia(banda1, banda2, banda3, tolerancia)
        colb1 = coloresResistencia.obtenerColores(banda1)
        colb2 = coloresResistencia.obtenerColores(banda2)
        colb3 = coloresResistencia.obtenerColores(banda3)
        coltol = coloresResistencia.obtenerColores(tolerancia)
        
        return render_template("calculoResistencias.html", form=res_form, valor=resultado[0], valorMax=resultado[1], valorMin=resultado[2], colb1=colb1, colb2=colb2, colb3=colb3, coltol=coltol)



if __name__ == "__main__":
    app.run(debug=True)