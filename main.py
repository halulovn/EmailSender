from Mailer import Mailer


def main():
    mailer = Mailer()
    mailer.connect()
    mailer.send_mail()
    mailer.close()


if __name__ == '__main__':
    main()
