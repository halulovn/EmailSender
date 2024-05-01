from email.message import EmailMessage


class MsgContent:

    def __init__(self, text, attachments):
        self.text, self.attachments = text, attachments

    def make_msg(self, receiver: str):
        msg = EmailMessage()
        msg['From'] = 'Maksym Sytyi'
        msg['Subject'] = 'Family from Ukraine'
        msg['To'] = receiver
        msg.set_content(self.text)

        for item in self.attachments:
            msg.add_attachment(item.data, maintype=item.type, subtype=item.subtype, filename=item.name)

        return msg
