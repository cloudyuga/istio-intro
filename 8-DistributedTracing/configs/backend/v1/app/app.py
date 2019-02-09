import os
import sys

from flask import Flask, abort, request
import requests

app = Flask(__name__)

def getForwardHeaders(request):
    headers = {}

    incoming_headers = [ 'x-request-id',
                         'x-b3-traceid',
                         'x-b3-spanid',
                         'x-b3-parentspanid',
                         'x-b3-sampled',
                         'x-b3-flags',
                         'x-ot-span-context'
    ]

    for ihdr in incoming_headers:
        val = request.headers.get(ihdr)
        if val is not None:
            headers[ihdr] = val
            print("incoming: "+ihdr+":"+val, file=sys.stderr)
    return headers


@app.route("/")
@app.route("/index")
def hello():
   return "We are on backend v1"


@app.route("/e1")
def f1():
    tracking_headers = getForwardHeaders(request)
    return requests.get('http://paytm-svc', headers=tracking_headers).content


@app.route("/e2")
def f2():
    tracking_headers = getForwardHeaders(request)
    return requests.get('http://paytm-svc/v1', headers=tracking_headers).content

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=9090)
