from contextlib import AbstractContextManager
import _csv


class CSVReader(AbstractContextManager):
    def __init__(self, file_path: str, file_encoding: str = "utf-8") -> None:
        self.__file_path = file_path
        self.__file_encoding = file_encoding
        self.__fp = None

    def __enter__(self) -> _csv._reader:
        return self.open()

    def __exit__(self, *e) -> None:
        return self.close()

    def open(self) -> _csv._reader:
        self.__fp = open(self.__file_path, "r",
                         encoding=self.__file_encoding, newline='')
        return _csv.reader(self.__fp)

    def close(self) -> None:
        return self.__fp.close()
