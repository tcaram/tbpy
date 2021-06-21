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

from TurtleArt.tatype import TYPE_CHAR, TYPE_STRING, TYPE_INT, TYPE_FLOAT, TYPE_BOOL
from TurtleArt.taprimitive import ArgSlot

import re

class Function:
    REQUIRED_CONFIG = ("Label", "Parameters", "Return")

    def __init__(self, name, function):
        self.name = name
        self.function = function
        self.docs = function.__doc__

        self.metadata = {}

        self.params = []
        self.ret_type = None
        self.example = None
        self.color = None

        self.__parse_docstring()
        if not self.__check_required_config():
            raise Exception(
                "Failed to load %s function. Make sure the docstring contains values for all of the required configuration values: %s"
                % (self.name, ", ".join(self.REQUIRED_CONFIG))
            )

        self.__parse_parameters()
        self.__parse_ret_type()
        self.__parse_example()
        self.__parse_color()

    def __check_required_config(self):
        """Return true iff all of the required config (self.REQUIRED_CONFIG) is already
        loaded into self.metadata"""
        return all(conf in self.metadata for conf in self.REQUIRED_CONFIG)

    # Parsers
    def __parse_docstring(self):
        pattern = r"@(\w.+)\((?<=\()(.*)(?=\))"
        for (key, val) in re.findall(pattern, self.docs):
            self.metadata[key] = val

    def __parse_parameters(self):
        if self.metadata["Parameters"] is not "":
            params_list = self.metadata["Parameters"].split(", ")
            params_tuple = [tuple(p.split(" ")) for p in params_list]
            for ptype, pname in params_tuple:
                self.params.append((pname, self.__builtin_to_tatype(ptype)))

    def __parse_ret_type(self):
        self.ret_type = self.__builtin_to_tatype(self.metadata["Return"])

    def __parse_example(self):
        if "Example" in self.metadata:
            args = self.metadata["Example"].split(",")
            if len(args) > 1:  # if multiple params, unpack into a list
                self.example = args
            else:  # one or zero params, return as it is
                self.example = self.metadata["Example"]

    def __parse_color(self):
        if self.__is_valid_hexadecimal_color(self.metadata["Color"]):
            self.color = [
                self.metadata["Color"],
                self.__color_variant(self.metadata["Color"], 1.5),
            ]
        else:
            self.color = ["#bb0000", "#ff0000"]

    # Utils 
    def __builtin_to_tatype(self, x):
        d = {
            "chr": TYPE_CHAR,
            "char": TYPE_CHAR,
            "string": TYPE_STRING,
            "str": TYPE_STRING,
            "integer": TYPE_INT,
            "int": TYPE_INT,
            "bool": TYPE_BOOL,
            "boolean": TYPE_BOOL,
            "long": TYPE_INT,
            "float": TYPE_FLOAT,
            "complex": False,
            "none": None
        }

        return d[x]

    def __is_valid_hexadecimal_color(self, hex_color):
        return re.search(r"^#(?:[0-9a-fA-F]{3}){1,2}$", hex_color)

    def __color_variant(self, hex_color, brightness_offset=1):
        """Takes a color like #87c95f and produces a lighter or darker variant.
        Source: https://chase-seibert.github.io/blog/2011/07/29/python-calculate-lighterdarker-rgb-colors.html"""

        if len(hex_color) != 7:
            raise Exception(
                "Passed %s into color_variant(), needs to be in #87c95f format."
                % hex_color
            )
        rgb_hex = [hex_color[x: x + 2] for x in [1, 3, 5]]
        new_rgb_int = [int(hex_value, 16) + brightness_offset for hex_value in rgb_hex]
        new_rgb_int = [
            min([255, max([0, i])]) for i in new_rgb_int
        ]  # make sure new values are between 0 and 255

        return "#%02x%02x%02x" % (
            new_rgb_int[0],
            new_rgb_int[1],
            new_rgb_int[2],
        )  # convert back to hexadecimal

    # Getters 
    def get_function(self):
        return self.function

    def get_label(self):
        return self.metadata["Label"]

    def get_description(self):
        return self.metadata["Description"]

    def get_parameters(self):
        return self.params

    def get_parameters_as_argslot(self):
        return [ArgSlot(tatype) for _, tatype in self.params]

    def get_parameters_labels(self):
        return [name for name, _ in self.params]

    def get_ret_type(self):
        return self.ret_type

    def get_example(self):
        return self.example

    def get_color(self):
        return self.color

    def get_style(self):
        if len(self.params) == 0:
            return 'box-style'

        if self.ret_type == TYPE_BOOL:
            return "boolean-block-style"
        elif self.ret_type in [TYPE_INT, TYPE_FLOAT]:
            return "number-style"
        elif self.ret_type in [TYPE_CHAR, TYPE_STRING]:
            return "number-style"

        return "basic-style-" + str(len(self.params)) + "arg"

    def get_doc(self, key):
        return self.metadata[key]
