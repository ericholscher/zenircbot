import redis
import json

def load_config(name):
    with open(name) as f:
        return json.loads(f.read())

config = load_config('bot.json')
redis_config = config['redis']
r = redis.StrictRedis(host=redis_config['host'], port=redis_config['port'], db=redis_config['db'])

def send_privmsg(to, message):
    r.publish('out',
                json.dumps({
                'version': 1,
                'type': 'privmsg',
                'data': {
                    'to': to,
                    'message': message,
                    }
                }))

