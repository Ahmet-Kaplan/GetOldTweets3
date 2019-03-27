
from urllib.parse import urlparse
import json

class Tweet:

	def __str__(self):
		dict = {}
		url_comp = urlparse(self.permalink)

		self.username = url_comp.path.split('/')[1]

        dict['username'] = str(self.username)
        for key in ['id', 'permalink', 'original_text','text', 'type','replies', 'retweets', 'favorites', 'mentions', 'hashtags', 'geo','urls','language','original_text_and_emojis','emojis','full_html']:
       		dict[key] =  str(self.__dict__[key])
        dict['date'] = self.date.strftime('%d/%m/%Y %H:%M:%S')

		return json.dumps(dict)

	def __init__(self):
		pass

	def __repr__(self):
		return self.__str__()

