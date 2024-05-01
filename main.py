from Mailer import Mailer
from core.services.FileService import FileService


def main():
    mailer = Mailer(FileService())
    mailer.connect()
    mailer.send_mail()
    mailer.close()


if __name__ == '__main__':
    main()
