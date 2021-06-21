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
from TurtleArt.taprimitive import Primitive

from plugins.plugin import Plugin

from .moduleloader import ModuleLoader

from TurtleArt.tatype import TYPE_CHAR, TYPE_STRING, TYPE_INT, TYPE_FLOAT, TYPE_BOOL

import os

class Taonline(Plugin):
    def __init__(self, parent):
        Plugin.__init__(self)
        self.tw = parent
        self.loader = None

    def setup(self):
        self.loader = ModuleLoader(os.path.dirname(os.path.realpath(__file__)))
        self.palette = make_palette(
            "taonline",
            ["#00FF00", "#008000"],
            "TurtleBots Online",
            translation="taonline",
        )

        for module in self.loader.get_loaded_modules():
            for func in module.get_functions():
                self.palette.add_block(
                    func.get_label(),
                    style=func.get_style(),
                    label=[func.get_label()] + func.get_parameters_labels(),
                    prim_name=func.get_label(),
                    default=func.get_example(),
                    help_string=func.get_description(),
                    colors=func.get_color(),
                )

                self.tw.lc.def_prim(
                    func.get_label(),
                    len(func.get_parameters()),
                    Primitive(
                        func.get_function(),
                        return_type=TYPE_INT,
                        arg_descs=func.get_parameters_as_argslot(),
                    ),
                )

            #     if not (len(mod_params) in [1, 2, 3, 7]):
            #         raise Exception(
            #             "Currently only one, two, three or seven parameters parameters are supported."
            #         )
