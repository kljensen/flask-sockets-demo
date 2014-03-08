# -*- coding: utf-8 -*-
"""
    Small Flask application that shows how to push data
    in real time to a browser using Flask-Sockets.
"""
from flask import Flask
from flask_sockets import Sockets
from flask import render_template
import gevent
import datetime

app = Flask(__name__)
sockets = Sockets(app)


@sockets.route('/time')
def time_socket(ws):
    """ Handler for websocket connections that constantly pushes
        the current time.
    """
    while True:
        gevent.sleep(3)
        ws.send(datetime.datetime.now().isoformat())


@app.route('/')
def hello():
    """ Render our default template
    """
    return render_template('index.html')
