"""Core module for the package. It holds the main object to be used."""

from typing import List, Optional

import serial
from serial.tools import list_ports
from serial.tools.list_ports_common import ListPortInfo

from iic2343.utils import (
    can_be_written,
    close_port,
    configure_port,
    open_port,
    validate_port_selection,
    write_to_port,
)


class Basys3:

    """
    Encapsulates the behaviour required for the data to be written to
    the Basys3 board.
    """

    def __init__(self) -> None:
        self.__port = serial.Serial()

    @property
    def available_ports(self) -> List[ListPortInfo]:
        """Get available ports."""
        return sorted(list_ports.comports())

    def begin(self, port_number: Optional[int] = None) -> None:
        """Configure and initialize the port to be used."""
        validate_port_selection(port_number, self.available_ports)
        self.__port = configure_port(self.__port)
        self.__port.port = self.available_ports[port_number or 0].device
        open_port(self.__port)

    def end(self) -> None:
        """Close the port."""
        close_port(self.__port)

    def write(self, address: int, word: bytearray) -> int:
        """Write to the initialized port."""
        if not can_be_written(self.__port, address, word):
            return 0
        return write_to_port(self.__port, address, word)
