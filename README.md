Flask-Sockets Demo
==================

This is a small [Flask](http://flask.pocoo.org/docs/) application
that uses [Flask Sockets](https://github.com/kennethreitz/flask-sockets)
to constantly push the current time to a web browser over a 
[WebSocket](http://en.wikipedia.org/wiki/WebSocket) connection.

## Installation

Download the code

	git clone git@github.com:kljensen/flask-sockets-demo.git
	cd flask-sockets-demo

Create a [virtualenv](http://www.virtualenv.org/en/latest/).

	virtualenv venv
	. ./venv/bin/activate

Install the dependenties

	pip install requirements.txt

Run the code

	honcho start

or, if you don't want to use [Honcho](https://github.com/nickstenning/honcho)
(which is a [Foreman](https://github.com/ddollar/foreman) clone), just
run [gunicorn](http://gunicorn.org/) directly.

	gunicorn -k flask_sockets.worker hello:app

## Authors

* [Kyle Jensen](https://github.com/kljensen)

## License (MIT)

Copyright (c) 2014 the Authors

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.