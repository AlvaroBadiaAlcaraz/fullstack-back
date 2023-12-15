""" Api flask """
from flask import Flask, request, redirect, Response

app = Flask(__name__)
@app.route("/pizza", methods = ['POST'])

def get_data():
    """Obtener datos """
    nombre = request.form.get("p1")
    apellido = request.form.get("p2")

    print(nombre)
    print(apellido)

    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write(nombre + " " + apellido + "\n")
        file.close()

    return redirect("http://localhost/PIZZA FULL STACK RELEASE/solicita_pedido.html", code=302)

@app.route("/checksize", methods = ['POST'])
def checksize():
    """ Comprueba disponibilidad de un tamaño de pizza"""
    opcion = request.form.get("size")
    if opcion == "S":
        mensaje = "No disponible"
    elif opcion in ["M", "L", "XXL"]:
        mensaje = "Disponible"
    return Response(mensaje, 200, {'Access-Control-Allow-Origin':'*'})
