"""Models for the headers of the various regions"""
#  Copyright 2020 Parakoopa
#
#  This file is part of SkyTemple.
#
#  SkyTemple is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  SkyTemple is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with SkyTemple.  If not, see <https://www.gnu.org/licenses/>.
from abc import ABC, abstractmethod
from collections import OrderedDict
from typing import OrderedDict as OrderedDictType

from skytemple_files.common.ppmdu_config.data import LANG_EN, LANG_FR, LANG_IT, LANG_SP, LANG_DE, LANG_JP
from skytemple_files.common.util import *


class AbstractSsbHeader(ABC):
    @property
    @abstractmethod
    def data_offset(self) -> int:
        pass

    @property
    @abstractmethod
    def number_of_constants(self) -> int:
        pass

    @property
    @abstractmethod
    def number_of_strings(self) -> int:
        pass

    @property
    @abstractmethod
    def constant_strings_start(self) -> int:
        """(in bytes)"""
        pass

    @property
    @abstractmethod
    def const_table_length(self) -> int:
        """(in bytes)"""
        pass

    @property
    @abstractmethod
    def string_table_lengths(self) -> OrderedDictType[str, int]:
        """Returns an OrderedDict where keys are languages and values are the number of bytes in that table"""
        pass

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.__class__.__name__}<{str({k:v for k,v in self.__dict__.items() if v  is not None})}>"


class SsbHeaderUs(AbstractSsbHeader):
    def __init__(self, data: bytes):
        if not isinstance(data, memoryview):
            data = memoryview(data)
        self._number_of_constants = read_uintle(data, 0x0, 2)
        self._number_of_strings = read_uintle(data, 0x2, 2)
        self._constant_strings_start = read_uintle(data, 0x4, 2) * 2
        self._const_table_length = read_uintle(data, 0x6, 2) * 2
        self._string_table_lengths = OrderedDict({
            LANG_EN: read_uintle(data, 0x8, 2) * 2
        })
        self._unknown = read_uintle(data, 0xA, 2)

    @property
    def data_offset(self) -> int:
        return 0x0C

    @property
    def number_of_constants(self) -> int:
        return self._number_of_constants

    @property
    def number_of_strings(self) -> int:
        return self._number_of_strings

    @property
    def constant_strings_start(self) -> int:
        return self._constant_strings_start

    @property
    def const_table_length(self) -> int:
        return self._const_table_length

    @property
    def string_table_lengths(self) -> OrderedDictType[str, int]:
        return self._string_table_lengths

    @property
    def unknown(self) -> int:
        return self._unknown


class SsbHeaderEu(AbstractSsbHeader):
    def __init__(self, data: bytes):
        if not isinstance(data, memoryview):
            data = memoryview(data)
        self._number_of_constants = read_uintle(data, 0x0, 2)
        self._number_of_strings = read_uintle(data, 0x2, 2)
        self._constant_strings_start = read_uintle(data, 0x4, 2) * 2
        self._const_table_length = read_uintle(data, 0x6, 2) * 2
        self._string_table_lengths = OrderedDict({
            LANG_EN: read_uintle(data, 0x8, 2) * 2,
            LANG_FR: read_uintle(data, 0xA, 2) * 2,
            LANG_DE: read_uintle(data, 0xC, 2) * 2,
            LANG_IT: read_uintle(data, 0xE, 2) * 2,
            LANG_SP: read_uintle(data, 0x10, 2) * 2
        })

    @property
    def data_offset(self) -> int:
        return 0x12

    @property
    def number_of_constants(self) -> int:
        return self._number_of_constants

    @property
    def number_of_strings(self) -> int:
        return self._number_of_strings

    @property
    def constant_strings_start(self) -> int:
        return self._constant_strings_start

    @property
    def const_table_length(self) -> int:
        return self._const_table_length

    @property
    def string_table_lengths(self) -> OrderedDictType[str, int]:
        return self._string_table_lengths