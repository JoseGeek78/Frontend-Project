from flask import Flask, render_template

app = Flask(__name__)

# Datos de ejemplo, reemplaza estos con tus datos reales
recetas = [...]
descripciones = [...]
ingredientes = [...]
instrucciones = [...]

@app.route('/')
def index():
    # Devuelve un archivo index.html renderizado con algunos datos
    return render_template('index.html', recetas=recetas)

@app.route("/receta/<int:id>")
def receta(id):
    # Devuelve un archivo receta.html renderizado con datos para una receta específica
    return render_template('receta.html', id=id, receta=recetas[id], descripcion=descripciones[id], ingredientes=ingredientes[id], instrucciones=instrucciones[id])

@app.route('/login')
def login():
    # Devuelve un archivo login.html renderizado para la página de inicio de sesión
    return render_template('login.html')
