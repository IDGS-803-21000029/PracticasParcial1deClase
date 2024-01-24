from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    escuela = "UTL"
    alumnos = ["Mario", "Pedro", "Luis", "Dario"]

    return render_template("index.html", escuela=escuela, alumnos=alumnos)

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


if __name__ == "__main__":
    app.run(debug=True)