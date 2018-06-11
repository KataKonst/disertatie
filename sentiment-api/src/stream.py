from threading import Thread
import time
import socketio
from queue import  Queue
from twitter.twitterStreaming import TwiteerStreaming
from analysis.services.vaderServiceEn import VaderServiceEn
from analysis.services.stanfordService import StanfordService
from analysis.services.naiveBayesService import NaiveBayesService
from analysis.services.svmService import SVMService
from analysis.services.meService import MaximumEntropyService
from analysis.services.tfService import TFService
from mongo.tweetService import TweetService
import json
from sanic import Sanic
from sanic.response import html

sio = socketio.AsyncServer(async_mode="sanic")
app = Sanic()
app.config.KEEP_ALIVE =10000
app.config.REQUEST_TIMEOUT= 10000
app.config.RESPONSE_TIMEOUT= 10000
app.config.DB_NAME = 'appdb'
app.config.DB_NAME = 'appdb'

sio.attach(app)
tweetStream = TwiteerStreaming()
vaderService = VaderServiceEn()
tweetService = TweetService()
stanfordService = StanfordService()
bayesService = NaiveBayesService("en")
svmService = SVMService("en")
meService = MaximumEntropyService("en")
tfService = TFService()

@app.route('/')
async def index(request):
    with open('index.html') as f:
        return html(f.read())


@sio.on('connect')
def connect(sid, environ):
    print("connect ", sid)

@sio.on('get_tweets')
async def message(sid, data):
    q = Queue()
    thread = Thread(target=tweetStream.filter, args=(q, data["location"],))
    thread.start()
    import sys

    try:
       while True:
        time.sleep(1)
        item = q.get()
        itm = json.loads(item)
        text = itm.get("text", "empty")
        if "extended_tweet" in itm:
            text = itm["extended_tweet"]["full_text"]

        vadeScore = vaderService.getScore(text)
        itm["vader"] = vadeScore
        itm["svm"] = 1 if svmService.getScore(text) == "positive" else 0
        itm["bayes"] = 1 if bayesService.getScore(text) == "positive" else 0
        #itm["stanford"] = {"result": stanfordService.getScore(text)}
        itm["me"]=1 if meService.getScore(text) == "positive" else 0
        itm["tf"]= {"result": tfService.getScore(text)}

        tweetService.add(itm)
        location =itm.get("place")
        location_name = location.get("full_name")
        await sio.emit("tweet", { "text":text,
                                  "vader":vadeScore,
                                  "location":location_name})
        q.task_done()

    except Exception as e:
        print(e)
        sys.exit(1)

@sio.on('disconnect', namespace='/chat')
def disconnect(sid):
    print('disconnect ', sid)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
