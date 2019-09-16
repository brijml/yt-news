from flask import Response, jsonify


class ResponseUtil:

	def __init__(self, code, status):
		self.code = code
		self.status = status

	def json_message_response(self, message):
		return jsonify({"code":self.code, "status":self.status, "message":message})

	def json_data_response(self, data):
		return jsonify({"code":self.code, "status":self.status, "data":data})