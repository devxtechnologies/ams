from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

import urllib.parse as ap
import requests

class SendSMSMixin(object):
	message = str()
	to_number = str()
	url = str()

	def get_msg(self, *args, **kwargs):
		message = self.message
		return message

	def get_number(self, *args, **kwargs):
		number = self.to_number
		return number

	def send_msg(self, number=None, msg=None):
		if msg is None:
			msg = self.get_msg()
		if number is None:
			number = self.get_number()
		params = { 'numbers' : number, 'message' : msg }
		r = requests.get(self.url + ap.urlencode(params))





