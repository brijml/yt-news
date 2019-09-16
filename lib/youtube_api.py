import os
import googleapiclient.discovery
from conf import constants as C

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

#set this enironment variable 
developer_key = C.DEVELOPER_KEY
if not developer_key:
	raise Exception('Developer Key not found. Please set this environment variable to your api Key')

api_service_name = "youtube"
api_version = "v3"
part = ",".join(["snippet","contentDetails","statistics"])


class YouTube(object):

	def __init__(self):
		super(YouTube, self).__init__()
		
	def get_youtube_content(self, channel_id):
		youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=developer_key)

		request = youtube.channels().list(
			part=part,
			id=channel_id
		)
		response = request.execute()
		return response

	def get_stats(self, channel_id):
		response = self.get_youtube_content(channel_id)
		return response['items'][0]['statistics']


if __name__ == "__main__":
	channel_id = 'UC-CSyyi47VX1lD9zyeABW3w'
	yt_stats = YouTube().get_stats(channel_id)
	print(yt_stats)