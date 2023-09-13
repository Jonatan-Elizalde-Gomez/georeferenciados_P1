from flask import Flask, render_template, url_for

#Render: para renderizar, url: para navegar

app=Flask(__name__) 

@app.route('/')
def index():
    edad = 18
    return render_template('index.html', edad = edad)

@app.route('/proyectos/<string:nombre>/<int:edad>')
def proyectos(nombre=None, edad = None):
    if nombre is None:
        return render_template('proyectos.html')
    else:
        return render_template('proyectos.html', nombre = nombre, edad = edad)

@app.route('/loops')
def loops():
    lista=["Frutas", "Verduras", "Limpieza", "Abarrotes"]
    return render_template('loops.html', lista=lista)

@app.route('/mapa/<string:lat>/<string:long>/<string:cadena>/<string:zoom>/<string:altura>/<string:ancho>')
def mapa(lat, long, cadena, zoom, altura, ancho):
    return render_template('mapa.html', lat=lat, long=long, cadena=cadena, zoom=zoom, altura=altura, ancho=ancho)