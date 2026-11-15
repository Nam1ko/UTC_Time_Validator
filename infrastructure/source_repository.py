from urllib.request import urlopen
from urllib.error import URLError, HTTPError

class SourceRepository:

    def get_from_input(self):
        return input("Введите текст: ")

    def get_from_file(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()
        except (FileNotFoundError, PermissionError, OSError):
            return None

    def get_from_url(self, url):
        try:
            with urlopen(url, timeout=10) as response:
                return response.read().decode("utf-8")
        except (URLError, HTTPError, TimeoutError, UnicodeDecodeError, ValueError):
            return None