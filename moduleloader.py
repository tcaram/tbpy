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

from .module import Module

import os


class ModuleLoader:
    def __init__(self, path):
        self.__path = path
        self.__loaded = []

        self.__load()

    def get_loaded_modules(self):
        return self.__loaded

    def __load(self):
<<<<<<< HEAD
        dir_path = os.path.join(self.__path, "modules")
=======
        dir_path = os.path.join(self.__path, "functions")
>>>>>>> e4b4729534963bf9d9ba2cd5a992562184b8d20d
        for file in os.listdir(dir_path):
            if self.__is_module_file(file):
                module = Module(self.__construct_name(file))
                self.__loaded.append(module)

    def __construct_name(self, file):
<<<<<<< HEAD
        return "plugins.taonline.modules." + self.__sanitize_name(file)
=======
        return "plugins.taonline.functions." + self.__sanitize_name(file)
>>>>>>> e4b4729534963bf9d9ba2cd5a992562184b8d20d

    def __sanitize_name(self, file):
        return file.replace(".py", "")

    def __is_module_file(self, file):
        return not file.startswith("_") and file.endswith(".py")
