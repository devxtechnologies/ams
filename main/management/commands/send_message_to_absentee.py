from django.core.management.base import BaseCommand, CommandError
from main.models import *
from main.mixins import SendSMSMixin

import datetime
from django.utils import timezone


class Command(SendSMSMixin, BaseCommand):
    help = 'Runs through absentees and sends message.'
    url = 'https://www.smsgatewayhub.com/api/mt/SendSMS?APIKey=62sxGWT6MkCjDul6eNKejw&senderid=BMSITM&channel=2&DCS=0&flashsms=0&'
    
    def handle(self, *args, **options):
        self.find_absentee_and_send_sms()
    
    def get_msg(self, name, klass):
        today = datetime.datetime.now().date()
        msg = f"Your ward {name} was absent for the class {klass} on {today}."
        return msg

    def find_absentee_and_send_sms(self):
        today = timezone.now()
        absentees = Absentees.objects.filter(attendance__date_time=today)
        for student in absentees:
            msg = self.get_msg(student.user.first_name, student.attendance.teaches.subject)
            self.send_msg(student.user.phone_parent, msg)