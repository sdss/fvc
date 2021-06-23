#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2021-06-23
# @Filename: commands.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

from __future__ import annotations

from typing import TYPE_CHECKING

from clu.parsers.click import command_parser as fvc_parser


if TYPE_CHECKING:
    from clu.command import Command

    from .actor import FVCActor

    CommandType = Command[FVCActor]


@fvc_parser.command()
async def ieb(command: CommandType):
    """Reports status of the IEB."""

    ieb = command.actor.ieb

    print(await ieb.read_device("rtd1"))
