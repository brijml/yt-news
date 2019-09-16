from flask_restful import Resource
from .custom_utils import ResponseUtil


class AppInitResource(Resource):
		
	def get(self):
		return ResponseUtil(200, True).json_data_response({"vesion":'1.0.0', "app_name":"yt-news"})
