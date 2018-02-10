from flask import Flask, render_template
from flask.json import jsonify
from flask_cors import CORS
from web.reviewApi import reviews
from web.gamesApi import games
from flask_socketio import SocketIO,emit

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/test')
def index():
    return render_template('index.html')

@socketio.on('my event')
def test_message(message):
    print(message)
    emit('response', {'data': 'got it!'})


@app.route("/categories")
def getCategories():
    return  jsonify([{"text":"asdas"}, {"text":"asdasdas"}])

app.register_blueprint(reviews, url_prefix='/review')
app.register_blueprint(games, url_prefix='/game')

