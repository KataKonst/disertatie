from flask_socketio import send, emit
from app import socketio
from kafka import KafkaConsumer
from flask import Blueprint, request
import time
from app import app

from aiokafka import AIOKafkaConsumer
import asyncio

loop = asyncio.get_event_loop()

async def consume():
 with app.test_request_context():
    consumer = AIOKafkaConsumer(
        'hdfs_log_test', 'my_other_topic',
        loop=loop, bootstrap_servers='localhost:9092',
        group_id="my-group")
    # Get cluster layout and join group `my-group`
    await consumer.start()
    try:
        # Consume messages
        async for msg in consumer:
           emit("tweet","aaa")
    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()

loop.run_until_complete(consume())



twitter = Blueprint('tweeter', __name__, template_folder='web')

@socketio.on('message')
def handle_message(message):
    send(message)

@socketio.on('json')
def handle_json(json):
    send(json, json=True)

@socketio.on('get_tweets')
def handle_my_custom_event(json):
   consume()