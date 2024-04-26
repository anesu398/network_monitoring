from flask import Flask, render_template
from flask_socketio import SocketIO
import os
app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app)

class Config:
    # Set the secret key to protect against CSRF attacks
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'

    # Database configuration for SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Debugging option
    DEBUG = True