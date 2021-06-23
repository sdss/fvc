#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2019-11-12
# @Filename: cli.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

import logging
import os
import pathlib

import click
from click_default_group import DefaultGroup

from sdsstools.daemonizer import DaemonGroup, cli_coro

from fvc import config, log
from fvc.actor import FVCActor


@click.group(cls=DefaultGroup, default="actor", default_if_no_args=True)
@click.option(
    "-c",
    "--config",
    "config_file",
    type=click.Path(exists=True, dir_okay=False),
    help="Path to the user configuration file.",
)
@click.option(
    "-v",
    "--verbose",
    count=True,
    help="Debug mode. Use additional v for more details.",
)
def fvc(config_file, verbose):
    """CLI for the SDSS-V FVC.

    If called without subcommand starts the actor.

    """

    if verbose == 1:
        log.sh.setLevel(logging.INFO)
    elif verbose == 2:
        log.sh.setLevel(logging.DEBUG)
    elif verbose >= 3:
        log.sh.setLevel(logging.DEBUG)

    if config_file:
        config.load(config_file)


@fvc.group(cls=DaemonGroup, prog="fvc_actor", workdir=os.getcwd())
@cli_coro()
async def actor():
    """Runs the actor."""

    config = pathlib.Path(__file__).parent / "etc/fvc.yml"

    fvc_actor = await FVCActor.from_config(str(config)).start()
    await fvc_actor.run_forever()
