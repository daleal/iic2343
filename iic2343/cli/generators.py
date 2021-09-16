"""
A module to hold the CLI parser generators.
"""

from argparse import ArgumentParser, _SubParsersAction

import iic2343
from iic2343.cli.utils import setup_serial_ports_arguments


def generate_main_parser() -> ArgumentParser:
    """Generates the main parser."""
    # Create parser
    parser = ArgumentParser(
        description="Command line interface tool for iic2343.",
    )

    # Add version flag
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"iic2343 version {iic2343.__version__}",
    )

    # Create subparsers
    subparsers = parser.add_subparsers(help="Action to be executed.")

    # Serial ports subparser
    generate_serial_ports_subparser(subparsers)

    return parser


def generate_serial_ports_subparser(subparsers: _SubParsersAction) -> ArgumentParser:
    """Generates the serial ports action for the parser."""
    serial_ports_subparser = subparsers.add_parser("ports")
    serial_ports_subparser.set_defaults(action="ports")
    return setup_serial_ports_arguments(serial_ports_subparser)
