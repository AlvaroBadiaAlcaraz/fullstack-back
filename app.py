""" Api flask """
from flask import Flask, request, redirect

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
