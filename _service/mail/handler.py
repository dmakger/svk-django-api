import re

from _service.mail.mail import Mail
from api import settings
from bugs.models import MailBody
from client.models import Client


class MailType:
    AUTO_WRITE_TO_APPLICATION = 1
    NEW_APPLICATION = 2


class MailHandler(Mail):
    types = MailType

    # Уведломление о новой заявке
    def send_new_application(self, recipients: list = None, subject: str = None, content: dict = None,
                             new_subject: str = ''):
        new_content = ''
        if content is not None:
            person: Client = Client.objects.get(id=content['client'])
            social = [x.link for x in person.communication.all()]
            link_django = f"{settings.CURRENT_HOST}/admin/client/businessrequest/{content['id']}/change/"
            new_content = f"Email: {person.email}<br>" \
                          f"Имя: {person.username}<br>" \
                          f"Номер телефона: {person.number_phone}<br>" \
                          f"Соц. сети: {' | '.join(social)}<br>" \
                          f"Ссылка на django: {link_django}<br>" \
                          f"Название бизнес-проекта: {content['title']}<br>" \
                          f"Комментарий: {content['description']}<br>" \


        self.send_html(
            type_mail=self.types.NEW_APPLICATION,
            recipients=recipients, subject=subject,
            new_content=new_content,
            new_subject=new_subject,
        )

    # Авто письмо для пользователя
    def send_auto_write_to_application(self, recipients: list = None, subject: str = None, new_content: str = '',
                                       new_subject: str = ''):
        self.send_html(
            type_mail=self.types.AUTO_WRITE_TO_APPLICATION,
            recipients=recipients, subject=subject,
            new_content=new_content,
            new_subject=new_subject,
        )

    def send_html(self, type_mail: int, recipients: list = None, subject: str = None, new_content: str = '',
                  new_subject: str = ''):
        body: MailBody = self.get_body(id_mail=type_mail)
        if body is None:
            return None

        if subject is None:
            subject = body.title + new_subject
        content = self.format_html_message(body.content + new_content + body.footer.content)
        self.send(
            recipients=recipients,
            html_message=content,
            subject=subject,
        )

    @staticmethod
    def format_html_message(content):
        pattern = r'<img[^>]+src="(/media/uploads/[^">]+)"'
        return re.sub(pattern, fr'<img src="{settings.CURRENT_HOST}\1"', content)

    @staticmethod
    def get_body(id_mail: int):
        bodies = MailBody.objects.filter(id=id_mail)
        if len(bodies) == 0:
            return False
        return bodies[0]
