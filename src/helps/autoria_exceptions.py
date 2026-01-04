"""
Autoria exceptions
Author: Cod3W1ld01@proton.me
"""


class AutoriaDataZeroException(Exception):
    """
    Autoria exceptions
    """

    def __init__(self, message="Data is empty"):
        """
        Author: Cod3W1ld01@proton.me
        :param message:
        """
        super().__init__(message)


class AutoriaDataColumnException(Exception):
    """
    Autoria exceptions
    """

    def __init__(self, message="Column not found"):
        """
        Author: Cod3W1ld01@proton.me
        :param message:
        """
        super().__init__(message)
