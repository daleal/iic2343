"""
A module to hold some CLI utilities.
"""

from argparse import ArgumentParser
from typing import List

from serial.tools.list_ports_common import ListPortInfo


def setup_serial_ports_arguments(parser: ArgumentParser) -> ArgumentParser:
    """Sets up the serial ports action for the parser."""
    # Verbose
    parser.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        action="store_true",
        help="Show verbose output.",
    )

    return parser


def display_ports(ports: List[ListPortInfo], verbose: bool) -> None:
    """Prints the ports to the console."""
    processed = [format_port(index, port, verbose) for index, port in enumerate(ports)]
    for port in processed:
        print(port)
    print(f"{len(processed)} {'ports' if len(processed) != 1 else 'port'} found")


def format_port(index: int, port: ListPortInfo, verbose: bool) -> str:
    """
    Given an index, a port and a verbose flag, returns a formatted
    string that gives the relevant information of said port.
    """
    name = port.device if verbose else port.name
    description = (
        (f"      desc: {port.description}\n" f"      hwid: {port.hwid}")
        if verbose
        else (f"      desc: {port.description}")
    )
    return f"({index}) {name}\n{description}"
