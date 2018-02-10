from threading import Thread
from aiohttp import web
import socketio
from queue import  Queue
from twitter.twitterStreaming import TwiteerStreaming
from analysis.services.vaderServiceEn import VaderServiceEn
from mongo.tweetService import TweetService

import json

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)
tweetStream = TwiteerStreaming()
vaderService = VaderServiceEn()
tweetService = TweetService()

async def index(request):
    """Serve the client-side application."""
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

@sio.on('connect')
def connect(sid, environ):
    print("connect ", sid)

@sio.on('get_tweets')
async def message(sid, data):
    q = Queue()

    print(data["location"])

    thread = Thread(target=tweetStream.filter, args=(q, data["location"],))
    thread.start()

    while True:
        item = q.get()
        itm = json.loads(item)
        vadeScore = vaderService.getScore(itm["text"])
        itm["vader"] = vadeScore
        tweetService.add(itm)
        await sio.emit("tweet", {"text":itm["text"],"vader":vadeScore})
        q.task_done()


@sio.on('disconnect', namespace='/chat')
def disconnect(sid):
    print('disconnect ', sid)

app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app)