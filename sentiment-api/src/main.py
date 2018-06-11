from app import app, socketio
from web.twitterAPI import *

if __name__ == "__main__":
    print ("started")
    socketio.run(app, port=5000)