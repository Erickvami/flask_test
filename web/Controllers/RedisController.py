from flask import jsonify,request
from flask_restful import Resource
from flask_expects_json import expects_json
from redis import Redis
from rq import Queue

r= Redis(host='redis',port=6379,db=0)
q= Queue(connection= r)

def addToQueue(message):
    r.sadd('messages',message)
    return True

class RedisController():
    class RedisDefault(Resource):
        def get(self):
            x= str(type(list(r.smembers('messages').iterable)))
            return jsonify({"messages":x})
        def post(self):
            result = addToQueue(request.json["message"])#q.enqueue(addToQueue,request.json["message"])
            return jsonify({"message":result})
