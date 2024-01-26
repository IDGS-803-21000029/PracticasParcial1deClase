from flask import Flask, render_template, request

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

if __name__ == "__main__":
    app.run(debug=True)