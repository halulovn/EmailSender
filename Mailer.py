from core.services.FileService import FileService
from core.services.PColors import PColors
import smtplib

from entity.ConfModel import ConfModel
from entity.ImageModel import ImageModel
from entity.MsgContent import MsgContent


class Mailer:

    def __init__(self, file_service: FileService):
        config = ConfModel(file_service.read_from("mail.cfg"))
        self._smtpObj = smtplib.SMTP(host=config.host, port=config.port)
        self._user = config.user
        self._password = config.password
        self._service = file_service

    def _make_msg_content(self):
        msg_txt = self._service.read_from("msg.txt")
        files = ["IMG_5023.jpeg", "IMG_8456.jpg", "IMG_9624.jpg"]
        attachments = []

        for filename in files:
            img_data = self._service.read_img(filename)
            attachments.append(ImageModel(filename, img_data))

        print('MSG > Content')
        return MsgContent(msg_txt, attachments)

    def connect(self):
        self._smtpObj.starttls()

        try:
            self._smtpObj.login(user=self._user, password=self._password)
            print("Logged")
        except smtplib.SMTPException as e:
            print(e)

    def send_mail(self):
        sent_mail_list = self._service.read_list_from("sent_mail_list.cfg")
        mail_list = self._service.read_list_from("mail_list.cfg")
        already_sent_list = []
        msg = self._make_msg_content()

        for receiver in mail_list:
            if receiver in sent_mail_list:
                print(f"MSG > {PColors.FAIL}Already sent{PColors.ENDC} {receiver}")
            else:
                print('MSG > {}'.format(receiver))
                self._smtpObj.send_message(msg.make_msg(receiver))
                already_sent_list.append(receiver)

        sent_mail_list += already_sent_list
        self._service.write_list_to("sent_mail_list.cfg", sent_mail_list)
        self._service.write_list_to("mail_list.cfg", [])
        print('FILE > Write completed')

    def close(self):
        self._smtpObj.quit()
        self._smtpObj.close()
        print('Close')
