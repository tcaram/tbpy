#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

from .function import Function

import inspect
import importlib


class Group:
    def __init__(self, name):
        self.__group = importlib.import_module(name)

    def get_functions(self):
        return [
            Function(name, func)
            for name, func in inspect.getmembers(self.__group, inspect.isfunction)
            if not name.startswith("_")
        ]

    def get_name(self):
        return self.__group["GROUP_NAME"]

    def get_author(self):
        return self.__group["GROUP_AUTHOR"]

    def get_version(self):
        return self.__group["GROUP_VERSION"]

    def get_primitive(self):
        return self.__group
