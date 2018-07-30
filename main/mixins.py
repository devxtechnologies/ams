from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class SendSMSMixin(object):
	message = str()
	to_number = str()
	url = str()

    def get_msg(self):
    	message = self.message
    	return message

    def send_msg(self):
    	pass





