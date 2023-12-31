from __future__ import annotations
from contextlib import AbstractContextManager
from typing import Self
from iostuff.common.binary import BinaryEndian
from struct import pack as pk
from io import BytesIO


class MemoryWriter(BytesIO):
    def __init__(self, endian: BinaryEndian = BinaryEndian.Little) -> None:
        self.__endian = "<" if endian == BinaryEndian.Little else ">"

    def __write_num(self, type: str, number: int) -> int:
        return self.write(pk(f"{self.__endian}{type}", number))

    def write_ubyte(self, number: int) -> int:
        return self.__write_num("B", number)

    def write_byte(self, number: int) -> int:
        return self.__write_num("b", number)

    def write_ushort(self, number: int) -> int:
        return self.__write_num("H", number)

    def write_short(self, number: int) -> int:
        return self.__write_num("h", number)

    def write_uint(self, number: int) -> int:
        return self.__write_num("I", number)

    def write_int(self, number: int) -> int:
        return self.__write_num("i", number)

    def write_ulong(self, number: int) -> int:
        return self.__write_num("Q", number)

    def write_long(self, number: int) -> int:
        return self.__write_num("q", number)

    def write_utf8_string(self, string: str) -> int:
        return self.write(string.encode('utf-8'))

    def write_utf8_nt_string(self, string: str, nt: int = 0) -> int:
        return self.write_utf8_string(string) + self.write_ubyte(nt)

    def align(self, number: int) -> int:
        offset = self.tell()
        align = (number - (offset % number)) % number
        return self.seek(offset + align)

    def skip(self, number: int) -> int:
        return self.seek(self.tell() + number)


class BinaryWriter(AbstractContextManager, MemoryWriter):
    def __init__(self, file_path: str, endian: BinaryEndian = BinaryEndian.Little) -> None:
        super().__init__(endian)
        self.__file_path = file_path
        self.__fp = None

    def __enter__(self) -> Self:
        return self.open()

    def __exit__(self, *e) -> None:
        return self.close()

    def open(self) -> Self:
        self.__fp = open(self.__file_path, "wb")
        return self

    def close(self) -> None:
        self.__fp.write(self.getbuffer())
        return self.__fp.close()
