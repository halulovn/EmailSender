import os


class FileService:

    def __init__(self):
        self._current_directory = os.path.abspath(os.curdir) + '/'

    def read_img(self, file_name: str):
        with open(self._current_directory + file_name, 'rb') as file:
            file_content = file.read()
            file.close()

        return file_content

    def read_from(self, file_name: str):
        with open(self._current_directory + file_name) as file:
            file_content = file.read()
            file.close()

        return file_content

    def read_list_from(self, file_name: str):
        result_list = []
        with open(self._current_directory + file_name, 'r') as file:
            for line in file:
                tmp = (line, line[:-1])["\n" in line].lower()
                result_list.append(tmp)
            file.close()

        return result_list

    def write_list_to(self, file_name: str, information: list[str]):
        with open(self._current_directory + file_name, 'w') as file:
            information.sort()
            for item in information:
                file.write("%s\n" % item)
            file.close()
