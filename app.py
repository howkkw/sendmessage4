from flask import Flask,request
import requests
import socket


app = Flask(__name__)

@app.route('/')
def hello_world():
    phone = request.args.get('phone')
    content = request.args.get('content')
    requests.post('https://apis.aligo.in/send/', data={'key': 'jzxjtxg01idsymsflwl9rl4n6x7t2ig8',
            'userid': 'howkk',
            'sender': '010-3025-4032',
            'receiver': phone,
            'msg': content,
            'msg_type' : 'SMS',
            'title' : 'title',
            'destination' : '01000000000|홍길동',
    })


    return "sent"
