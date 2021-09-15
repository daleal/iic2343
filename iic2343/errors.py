"""Module used to hold potential errors present on the client code."""


class BaseIIC2343Error(Exception):
    """
    A base error class to be able to handle every error thrown by the
    library at the same time.
    """


class CannotOpenPortError(BaseIIC2343Error):
    """Error for when a port cannot be opened."""


class InvalidPortError(BaseIIC2343Error):
    """Error for when no ports are selected or an invalid port is selected."""


class NoPortsPresentError(BaseIIC2343Error):
    """Error for when no ports can be found on the machine."""
