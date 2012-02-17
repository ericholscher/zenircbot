import gevent
import redis
import json

from irc import IRCBot, run_bot
from gevent import monkey
from services.lib.api import load_config
monkey.patch_all()

config = load_config('bot.json')
redis_config = config['redis']

r = redis.StrictRedis(host=redis_config['host'], port=redis_config['port'], db=redis_config['db'])

class RelayBot(IRCBot):

    def __init__(self, *args, **kwargs):
        super(RelayBot, self).__init__(*args, **kwargs)
        gevent.spawn(self.do_sub)

    def do_sub(self):
        self.pubsub = r.pubsub()
        self.pubsub.subscribe('out')
        for msg in self.pubsub.listen():
            message = json.loads(msg['data'])
            print "Got %s" % message
            if message['version'] == 1:
                if message['type'] == 'privmsg':
                    self.respond(message['data']['message'], channel=message['data']['to'])

    def do_pub(self, nick, message, channel):
        to_publish = json.dumps({
            'version': 1,
            'type': 'privmsg',
            'data': {
                'sender': nick,
                'channel': channel,
                'message': message,
                },
            })

        r.publish('in', to_publish)
        print "Sending to in %s" % to_publish

    def command_patterns(self):
        return (
            ('.*', self.do_pub),
        )


run_bot(RelayBot, config['servers'][0]['hostname'], config['servers'][0]['port'],
        config['servers'][0]['nick'], config['servers'][0]['channels'])
