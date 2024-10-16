from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quienes")
def quienes():
    return render_template("quienes.html")

@app.route("/servicios")
def servicios():
    return render_template("servicios.html")

@app.route("/noticias")
def noticias():
    return render_template("noticias.html")

@app.route("/contacto", methods=["GET", "POST"])  # Acepta métodos GET y POST
def contacto():
    if request.method == "POST":
        # Aquí puedes manejar el envío del formulario
        nombre = request.form["nombre"]
        email = request.form["email"]
        mensaje = request.form["mensaje"]
        # Maneja el envío, por ejemplo, guardando la información o enviando un correo
        return redirect(url_for('index'))  # Redirige a la página de inicio
    return render_template("contacto.html")

if __name__ == "__main__":
    app.run(port=5001)