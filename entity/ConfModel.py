class ConfModel:

    def __init__(self, file_info: str):
        tmp_dict = eval(file_info)
        self.host = tmp_dict['server']
        self.port = int(tmp_dict['port'])
        self.user = tmp_dict['email']
        self.password = tmp_dict['pass']
