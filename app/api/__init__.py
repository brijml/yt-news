#import all the controllers to work
from app import app
from flask_restful import Api
from .controllers.base import AppInitResource

api = Api(app)
api.add_resource(AppInitResource, '/')