"""
A module to route the CLI traffic.
"""

from typing import Any

from iic2343.cli.generators import generate_main_parser
from iic2343.cli.utils import display_ports
from iic2343.core import Basys3


def dispatcher(*args: Any, **kwargs: Any) -> None:
    """
    Main CLI method, recieves the command line action and dispatches it to
    the corresponding method.
    """
    parser = generate_main_parser()
    parsed_args = parser.parse_args(*args, **kwargs)

    basys3 = Basys3()

    display_ports(basys3.available_ports, parsed_args.verbose)
