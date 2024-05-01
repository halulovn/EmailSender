class ConfModel:

    def __init__(self, file_info: str):
        tmp_dict = eval(file_info)
        self.host, self.port = tmp_dict['server'], int(tmp_dict['port'])
        self.user, self.password = tmp_dict['email'], tmp_dict['pass']
