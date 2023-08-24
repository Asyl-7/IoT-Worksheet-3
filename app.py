import serial
from flask import Flask, render_template
from flask_socketio import SocketIO
from threading import Lock

# use python thread to get real time updates
thread = None
thread_lock = Lock()

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')

# serial connection to the microbit usb please change accordingly
ser = serial.Serial('COM3', 115200)


# generate background task
def background_task():
    try:
        while True:
            sensor_data = ser.readline().decode('utf-8').strip()  # Read serial data from Micro:bit
            # socketio.emit('data_update', sensor_data, broadcast=True)
            socketio.emit('data_update', {'data': sensor_data})

    except Exception as e:
        return f'Error: {e}'

#flask app route basically homepage renders html file
@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

#flask socketio connection on connect get data
@socketio.on('connect')
def connect():
    global thread
    print('Client connected')

    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_task)


if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=5000)
