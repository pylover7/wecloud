from zgrobot import ZgRoBot

myrobot = ZgRoBot(token='token')


@myrobot.handler
def hello(message):
    return 'Hello World!'
