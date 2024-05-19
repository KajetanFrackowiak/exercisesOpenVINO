from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
Socketio = SocketIO(app)

from app import routes