import socketio

sio = socketio.Client()
sio.connect('http://localhost:4001')


@sio.on('event')
def my_event_handler(data):
    print("data received is ", data)


sio.emit("chat message", {"message": "message"})

# https://python-socketio.readthedocs.io/en/latest/client.html#emitting-events
# https://socket.io/get-started/chat/
