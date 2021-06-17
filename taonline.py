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
from TurtleArt.tatype import TYPE_FLOAT

from gettext import gettext as _

from plugins.plugin import Plugin

from pydoc import locate

import re
import os
import sys
import glob
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
            if not file.startswith('_') and file.endswith(".py"):
                module_name = "plugins.taonline.blocks." + file.replace('.py', '')
                self.modules.append(importlib.import_module(module_name))
                self.log("Succesfuly imported %s" % (module_name))
        # print(self.modules)

    def parse_docstring(self, func):
        req_metadata = ["Label", "Description", "Params", "Example"]
        doc = func.__doc__

        metadata = {}
        for met in req_metadata:
            reg = r"(?<=" + met + r"\()(.*)(?=\))"
            res = re.findall(reg, doc)
            if (len(res) != 0):
                metadata[met] = res[0]
        return metadata

    def parse_param(self, params):
        params_list = params.split(", ")
        params_tuple = [tuple(p.split(" ")) for p in params_list]
        for ptype, pname in params_tuple:
            t = locate(ptype)

    def setup(self):
        self.load_modules()
        self.palette = make_palette('taonline', ["#00FF00","#008000"], _('TurtleBots Online'), translation=_('taonline'))
        for module in self.modules:
            # fetch module metadata
            mod_name = module.MODULE_NAME
            funcs = inspect.getmembers(module, inspect.isfunction)
            for name, func in funcs:
                if (not name.startswith("_")):
                    metadata = self.parse_docstring(func)
                    # print(metadata)
                    mod_label = metadata['Label']
                    mod_descr = metadata['Description']
                    mod_params = metadata['Params']
                    mod_example = metadata['Example']
                    # self.parse_param(mod_params)

                    param_count = len(mod_params.split(","))

                    if not (param_count in [1, 2, 3, 7]):
                        raise Exception("Currently only one, two, three or seven parameters parameters are supported.")

                    style = 'basic-style-' + str(param_count) + 'arg'

                    self.palette.add_block(mod_label, 
                        style=style,
                        label=[mod_label, 'lat', 'long'],
                        prim_name=mod_label,
                        default=[-34.921, -56.159],
                        help_string=mod_descr)

                    self.tw.lc.def_prim(mod_label, param_count, Primitive(func, arg_descs=[ArgSlot(TYPE_FLOAT), ArgSlot(TYPE_FLOAT)]))