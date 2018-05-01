from flask import Flask, render_template
from flask.json import jsonify
from flask_cors import CORS
from web.reviewApi import reviews
from web.gamesApi import games
from web.yelpAPI import yelp
from web.twitterAPI import tweets
from web.hashtagsAPI import hashtags
from flask_socketio import SocketIO,emit

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

app.register_blueprint(reviews, url_prefix='/review')
app.register_blueprint(games, url_prefix='/game')
app.register_blueprint(yelp, url_prefix='/yelp')
app.register_blueprint(tweets, url_prefix='/twitter')
app.register_blueprint(hashtags, url_prefix='/hashtag')



