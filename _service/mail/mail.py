from django.core.mail import send_mail

from api import settings


class Mail:
    SUBJECT = 'Письмо от «СДЕЛАНО В КОРОЛËВЕ»'
    SENDER = settings.EMAIL_HOST_USER
    RECIPIENTS = ['made_in_korolev@vk.com']
    # RECIPIENTS = ['dmakger@yandex.ru']

    def send(self, message=None, html_message=None, subject=SUBJECT, sender=SENDER, recipients=None):
        if recipients is None:
            recipients = self.RECIPIENTS
        send_mail(subject, message, sender, recipients, html_message=html_message)
