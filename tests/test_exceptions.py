"""
Testing exceptions
author: Cod3W1ld01@proton.me
"""
# pylint: disable=too-few-public-methods, import-error
import pytest

from src.helps.autoria_exceptions import (AutoriaDataZeroException,
                                          AutoriaDataColumnException)


class AutoriaDataZeroExceptionFake:
    """
    Testing exceptions
    """

    def __init__(self, n):
        """
        :param n: number of exceptions
        :param n:
        """
        if n == 0:
            raise AutoriaDataZeroException(message="n is 0")


class AutoriaDataColumnExceptionFake:
    """
    Testing exceptions
    """

    def __init__(self, n):
        """
        Testing exceptions
        :param n:
        """
        if n == 0:
            raise AutoriaDataColumnException(message="n is 0")


def test_autoria_data_zero_exception():
    """
    Testing exceptions
    :return:
    """
    with pytest.raises(AutoriaDataZeroException):
        AutoriaDataZeroExceptionFake(n=0)


def test_autoria_data_column_exception():
    """
    Testing exceptions
    :return:
    """
    with pytest.raises(AutoriaDataColumnException):
        AutoriaDataColumnExceptionFake(n=0)
