#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2021-06-23
# @Filename: actor.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

import os

from clu.legacy import LegacyActor

from fvc import __version__
from fvc.ieb import IEB


class FVCActor(LegacyActor):
    """The FVC SDSS-style actor."""

    def __init__(self, *args, **kwargs):

        jaeger_base = os.path.join(os.path.dirname(__file__), "..")
        if "schema" in kwargs:
            if not os.path.isabs(kwargs["schema"]):
                kwargs["schema"] = os.path.join(jaeger_base, kwargs["schema"])

        super().__init__(*args, **kwargs)

        self.version = __version__

        self.ieb = IEB.from_config(self.config["ieb"])
