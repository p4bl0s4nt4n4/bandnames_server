from flask import Flask
from flask_socketio import SocketIO, emit

from modelos.banda import Banda
from modelos.bandas import Bandas

banda1 = Banda("AC/SC")
banda2 = Banda("Iron Maiden")
banda3 = Banda("Metallica")
banda4 = Banda("Queen")

grupo = Bandas()
grupo.agregarBanda(banda1)
grupo.agregarBanda(banda2)
grupo.agregarBanda(banda3)
grupo.agregarBanda(banda4)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on("connect")
def conexion():
    print("cliente conectado")
    print(grupo.obtenerBandas())
    emit("bandas-activas", grupo.obtenerBandas())

@socketio.on("disconnect")
def desconexion():
    print("cliente desconectado")

@socketio.on("crear-banda")
def crear(obj):
    nuevaBanda = Banda(obj["nombre"])
    grupo.agregarBanda(nuevaBanda)
    emit("bandas-activas", grupo.obtenerBandas())

@socketio.on("eliminar-banda")
def eliminar(obj):
    print(obj)
    grupo.eliminarBanda(obj["id"])
    emit("bandas-activas", grupo.obtenerBandas())

@socketio.on("votar-banda")
def votar(obj):
    grupo.votarPorBanda(obj["id"])
    emit("bandas-activas", grupo.obtenerBandas())


if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0',debug=True)