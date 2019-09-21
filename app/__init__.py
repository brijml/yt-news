import os
from mongoengine import *
from flask import Flask
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
connect(app.config.get('MONGODB_DATABASE'))

"""Set the app secret to use sessions """
app.secret_key = 'A0Zr98j/3yX R~XHH!jmladjfKsj$kjd'

#import the dependencies
from . import api
from .api.models.youtube_entities_models import * 

def print_yt_data():
	for obj in Channels.objects:
		stats = YouTube().get_stats(obj.channel_id)
		print(stats)
	return

scheduler = BackgroundScheduler()
scheduler.add_job(func=print_yt_data, trigger="interval", days=1)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())