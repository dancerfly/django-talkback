from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from talkback.settings import CONFIG

def send_notification_email(feedback_item, site):
	if (not CONFIG['FEEDBACK_RECIPIENTS']):
		return
	recipients = CONFIG['FEEDBACK_RECIPIENTS']
	ctx = {
		'feedback_item': feedback_item,
		'site': site
	}
	email_content = render_to_string("talkback/email_notification.txt", ctx)
	send_mail("[{0}] New Feedback".format(site.name), email_content,
			  settings.DEFAULT_FROM_EMAIL, [x[1] for x in recipients])
