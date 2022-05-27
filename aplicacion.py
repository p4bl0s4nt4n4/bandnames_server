from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on("mensaje")
def mensaje(mensaje):
    emit('mensa', mensaje)

if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0',debug=True)