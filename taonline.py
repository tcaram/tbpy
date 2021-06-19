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

# Python 3 compatibility
from __future__ import print_function

from TurtleArt.tapalette import make_palette
from TurtleArt.taprimitive import Primitive, ArgSlot
from TurtleArt.tatype import TYPE_CHAR, TYPE_STRING, TYPE_INT, TYPE_FLOAT, TYPE_BOOL

from gettext import gettext as _

from plugins.plugin import Plugin

import re
import os
import inspect
import importlib


class Taonline(Plugin):
    def __init__(self, parent):
        Plugin.__init__(self)
        self.tw = parent
        self.modules = []

    def log(self, text):
        print("taonline: %s" % text)

    def load_modules(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        for file in os.listdir(os.path.join(dir_path, "blocks")):
            if not file.startswith("_") and file.endswith(".py"):
                module_name = "plugins.taonline.blocks." + file.replace(".py", "")
                self.modules.append(importlib.import_module(module_name))
                self.log("Succesfuly imported %s" % (module_name))
        # print(self.modules)

    def parse_docstring(self, func):
        req_metadata = ["Label", "Description", "Params", "Example", "Colors"]
        doc = func.__doc__

        metadata = {}
        for met in req_metadata:
            reg = r"(?<=" + met + r"\()(.*)(?=\))"
            res = re.findall(reg, doc)
            if len(res) != 0:
                metadata[met] = res[0]
        return metadata

    def parse_params(self, params):
        _params = []
        params_list = params.split(", ")
        params_tuple = [tuple(p.split(" ")) for p in params_list]
        for ptype, pname in params_tuple:
            _params.append((pname, self.builtin_to_tatype(ptype)))
            # print(ptype, self.builtin_to_tatype(ptype), pname)
        return _params

    def builtin_to_tatype(self, x):
        """Return the tatype.Type representation of a given built-in type."""

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
        }

        return d[x]

    def parse_example(self, x):
        args = x.split(",")
        if len(args) > 1:  # return params as a list
            return args
        else:  # one or zero params
            return x

    def params_to_labels(self, params):
        return [label for label, _ in params]

    def params_to_argslot(self, params):
        return [ArgSlot(tatype) for _, tatype in params]

    def parse_color(self, x):
        return x.split(",")

    def setup(self):
        self.load_modules()
        self.palette = make_palette(
            "taonline",
            ["#00FF00", "#008000"],
            _("TurtleBots Online"),
            translation=_("taonline"),
        )
        for module in self.modules:
            # fetch module metadata
            # mod_name = module.MODULE_NAME
            funcs = inspect.getmembers(module, inspect.isfunction)
            for name, func in funcs:
                if not name.startswith("_"):
                    metadata = self.parse_docstring(func)
                    print(metadata)

                    if "Label" not in metadata:
                        raise Exception("Label configuration is required.")

                    if "Params" not in metadata:
                        raise Exception("Params configuration is required.")

                    # required config
                    mod_label = metadata["Label"]
                    mod_params = self.parse_params(metadata["Params"])

                    # optional config
                    mod_descr = None
                    if "Description" in metadata:
                        mod_descr = metadata["Description"]

                    mod_example = None
                    if "Example" in metadata:
                        mod_example = self.parse_example(metadata["Example"])

                    mod_color = None
                    if "Colors" in metadata:
                        mod_color = self.parse_color(metadata["Colors"])
                        if len(mod_color) != 2:
                            raise Exception(
                                "Colors config syntax is #background,#border, i.e: #ff0000, #bb0000"
                            )

                    if not (len(mod_params) in [1, 2, 3, 7]):
                        raise Exception(
                            "Currently only one, two, three or seven parameters parameters are supported."
                        )

                    self.palette.add_block(
                        mod_label,
                        style="basic-style-" + str(len(mod_params)) + "arg",
                        label=[mod_label] + self.params_to_labels(mod_params),
                        prim_name=mod_label,
                        default=mod_example,
                        help_string=mod_descr,
                        colors=mod_color,
                    )

                    self.tw.lc.def_prim(
                        mod_label,
                        len(mod_params),
                        Primitive(func, arg_descs=self.params_to_argslot(mod_params)),
                    )
