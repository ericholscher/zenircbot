from flask import Flask
from flask import request

from lib import api

app = Flask(__name__)

#curl -i -X POST  -H "Content-Type: application/json" -d '{"chan": "deploys", "msg": "what up son"}' http://localhost:5000/deploys/
@app.route('/', methods=['GET', 'POST'])
def send_json():
    msg = request.json['chan']
    msg = request.json['msg']
    ret = 'Sending %s to #%s' % (msg, chan)
    api.send_privmsg('#%s' % chan, msg)
    return ret

#curl -i -X POST  -H "Content-Type: application/json" -d '{"msg": "what up son"}' http://localhost:5000/deploys/
@app.route('/<chan>/', methods=['GET', 'POST'])
def send_json(chan):
    msg = request.json['msg']
    ret = 'Sending %s to #%s' % (msg, chan)
    api.send_privmsg('#%s' % chan, msg)
    return ret

#curl http://localhost:5000/deploys/what%20up%20son/
@app.route('/<chan>/<msg>/')
def send_url(chan, msg):
    ret = 'Sending %s to #%s' % (msg, chan)
    api.send_privmsg('#%s' % chan, msg)
    return ret

if __name__ == '__main__':
    app.run()
    #app.run(debug=True)
