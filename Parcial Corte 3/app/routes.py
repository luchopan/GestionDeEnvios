from init import app
from config import cursor, connection
from flask import render_template, request, redirect, url_for

# Ruta principal para mostrar envíos
@app.route('/')
def index():
    cursor.execute('SELECT * FROM Envios')
    envios = cursor.fetchall()
    return render_template('index.html', envios=envios)

# Ruta para agregar un nuevo envío
@app.route('/add', methods=['POST'])
def add_envio():
    nombre = request.form['nombre']
    apellidos = request.form['apellido']
    identificacion = request.form['identificacion']
    direccion = request.form['direccion']
    codigo_postal = request.form['codigo_postal']
    productos = request.form['productos']

    cursor.execute('INSERT INTO Envios (Nombre, Apellido, Identificacion, [Direccion De Envio], [Codigo Postal], Productos) VALUES (?, ?, ?, ?, ?, ?)',
                   (nombre, apellidos, identificacion, direccion, codigo_postal, productos))
    connection.commit()
    return redirect(url_for('index'))

# Ruta para eliminar un envío
@app.route('/delete/<int:envio_id>')
def delete_envio(envio_id):
    cursor.execute('DELETE FROM Envios WHERE IdEnvio = ?', (envio_id,))
    connection.commit()
    return redirect(url_for('index'))