var assert = require('assert')
var botname = 'ZenBot';
var pattern_str = '/^:(.*?)!.*?PRIVMSG (#?\w+) :(?:(' + botname + '):)?(?:!(\w*) )?(.*)$/';
// var pattern      = /^:(.*?)!.*?PRIVMSG (#?\w+) :(?:!(\w*) )?(.*)$/;
var pattern = new RegExp(pattern_str);
var tests = {};

tests.normal_chat = function(pattern) {
    sender = 'Wraithan';
    channel = '#pdxbots';
    message = 'This is an average line of text';
    chatter = ':' + sender + '!~wraithan@206.125.170.2 PRIVMSG ' + channel + ' :' + message;

    console.log(chatter);
    assert.ok(pattern.test(chatter));
    privmsg = pattern.exec(chatter);
    assert.equal(privmsg[1], sender);
    assert.equal(privmsg[2], channel);
    assert.equal(privmsg[3]);
    assert.equal(privmsg[4]);
    assert.equal(privmsg[5], message);
    return true;
};

tests.direct_msg = function(pattern) {
    sender = 'Wraithan';
    message = 'This is an average line of text';
    chatter = ':' + sender + '!~wraithan@206.125.170.2 PRIVMSG ' + sender + ' :' + message;

    assert.ok(pattern.test(chatter));
    privmsg = pattern.exec(chatter);
    assert.equal(privmsg[1], sender);
    assert.equal(privmsg[2], sender);
    assert.equal(privmsg[3]);
    assert.equal(privmsg[4]);
    assert.equal(privmsg[5], message);
    return true;
};

tests.command_msg = function(pattern) {
    sender = 'Wraithan';
    channel = '#pdxbots';
    message = 'This is an average line of text';
    command = 'calc';
    chatter = ':' + sender + '!~wraithan@206.125.170.2 PRIVMSG ' + channel + ' :!' + command + ' ' + message;

    assert.ok(pattern.test(chatter));
    privmsg = pattern.exec(chatter);
    assert.equal(privmsg[1], sender);
    assert.equal(privmsg[2], channel);
    assert.equal(privmsg[3]);
    assert.equal(privmsg[4], command, privmsg);
    assert.equal(privmsg[5], message);
    return true;
};

tests.hightlight_msg = function(pattern) {
    sender = 'Wraithan';
    channel = '#pdxbots';
    message = 'This is an average line of text';
    chatter = ':' + sender + '!~wraithan@206.125.170.2 PRIVMSG ' + channel + ' :' + message;

    assert.ok(pattern.test(chatter));
    privmsg = pattern.exec(chatter);
    assert.equal(privmsg[1], sender);
    assert.equal(privmsg[2], channel);
    assert.equal(privmsg[3], botname);
    assert.equal(privmsg[4]);
    assert.equal(privmsg[5], message);
    return true;
};

for (var i in tests) {
    if (tests[i](pattern)) {
	console.log(i + '... passed');
    }
}
