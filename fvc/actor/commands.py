#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2021-06-23
# @Filename: commands.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

from __future__ import annotations

from typing import TYPE_CHECKING
import click

from clu.parsers.click import command_parser as fvc_parser
from clu.command import Command


if TYPE_CHECKING:

    from .actor import FVCActor

    CommandType = Command[FVCActor]


@fvc_parser.group()
def ieb():
    """Reports the status of the IEB and sets values."""

    pass


@ieb.command()
async def status(command: CommandType):
    """Reports status of the IEB."""

    ieb = command.actor.ieb

    values = []
    for module in ieb.modules.values():
        for device in module.devices.values():
            value = (await device.read())[0]
            if device.__type__ == "relay":
                if value == "closed":
                    values.append(True)
                else:
                    values.append(False)
            else:
                values.append(round(value, 2))

    return command.finish(ieb=values)


@ieb.command()
@click.argument("device_name", metavar="DEVICE", type=str)
@click.argument("VALUE", type=str)
async def set(command: CommandType, device_name: str, value: str):
    """Sets the value of a device."""

    try:
        device = command.actor.ieb.get_device(device_name)
    except ValueError:
        return command.fail(error=f"Device {device_name!r} is not connected.")

    if device.__type__ == "relay":
        if value.lower() not in ["on", "off"]:
            return command.fail(error="Value for relays must be 'on' or 'off'.")
        if value.lower() == 'on':
            await device.close()
        else:
            await device.open()
    elif device.category == 'led':
        raw_value = 32 * int(1023 * (float(value) / 100))
        await device.write(raw_value)
    else:
        return command.fail(error=f"The value of device {device_name!r} cannot be set.")

    await Command('ieb status', parent=command).parse()

    return command.finish()
