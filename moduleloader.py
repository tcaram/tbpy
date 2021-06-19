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

from taonline.module import Module


class ModuleLoader:
	def __init__(self, path):
		self.__path = path
		self.__loaded = []

		self.__load()

    def get_loaded_modules(self)
    	return self.__loaded

    def __load(self):
        dir_path = os.path.dirname(self.__path)
        for file in os.listdir(os.path.join(dir_path, "blocks")):
            if self.__is_module_file(self, file):
                module = Module(self.__construct_name())
                self.__loaded.append(module)

    def __construct_name(self):
    	return 'plugins.taonline.blocks.' + self.__sanitize_name()

    def __sanitize_name(self):
    	return self.path.replace('.py', '')

    def __is_module_file(self, file):
    	return not file.startswith("_") and file.endswith(".py")

class Module:
	def __init__(self, name):
		self.__module = importlib.import_module(name)

	@property
	def name(self):
		return self.module['MODULE_NAME']

	@property
	def author(self):
		return self.module['MODULE_AUTHOR']

	@property
	def version(self)
		return self.module['MODULE_VERSION']

	def get_primitive(self):
		return self.__module

class Function:
	def __init__(self):
		self.name = name
		self.params = None
		self.ret_type = None
		self.docs = None # .__docs__
		self.metadata = {}
		# self.

		self.__parse_docstring()
		self.__parse_parameters()
		self.__parse_ret_type()
		self.__parse_example()
		self.__

	def __parse_docstring(self):
		pattern = r"@(\w.+)\((?<=\()(.*)(?=\))"
        for (key, val) in re.findall(pattern, self.docs):
        	self.metadata[key] = val

    def get_doc(self, key):
    	return self.docs[key]
