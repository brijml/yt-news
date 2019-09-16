from flask import Flask
import os
from lib.youtube_api import YouTube
from conf import constants as C

import atexit
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

environment = os.environ.get('prod_env','development')

""" Setting up the environment from the mainconf """

if environment == 'production':
	app.config.from_object('conf.mainconf.ProductionConfig') 
else:
	app.config.from_object('conf.mainconf.DevelopmentConfig')


""" Initiating the logger"""
logger = app.logger 
logger.setLevel('DEBUG')


""" Initiating mongodb db object """

#uncomment to connect to db
#db = MongoKit(app)


"""Set the app secret to use sessions """
app.secret_key = 'A0Zr98j/3yX R~XHH!jmladjfKsj$kjd'


def print_yt_data():
	for channel in C.CHANNELS:
		stats = YouTube().get_stats(channel)
		print(stats)
	return


scheduler = BackgroundScheduler()
scheduler.add_job(func=print_yt_data, trigger="interval", days=1)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())

#import the dependencies
from . import api