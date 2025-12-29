"""
Test autoria operations
author: Cod3W1ld01@proton.me
"""
# pylint: disable=unused-argument, import-error
import pytest
import pandas as pd
import matplotlib
from src.autoria_learn.autoria_operations import AutoriaOperations


@pytest.fixture(autouse=True)
def matplotlib_no_gui(monkeypatch):
    """
    Fixture fixture to disable matplotlib
    :param monkeypatch:
    :return:
    """
    matplotlib.use("Agg")


class TestClass:
    """
    Test autoria operations
    """
    autoria = AutoriaOperations()

    def test_get_group_names(self, monkeypatch):
        """
        Test autoria operations
        :param monkeypatch:
        :return:
        """
        ob = self.autoria.get_group_names()
        assert isinstance(ob, dict)
        assert ob['status'] is True
        monkeypatch.setattr(self.autoria, "data", pd.DataFrame())
        ob = self.autoria.get_group_names()
        assert ob['status'] is False
        assert ob['error'] == "Name cannot be empty"

    @pytest.mark.parametrize('name', ['BMW', 'Opel', 'Some model'])
    def test_get_group_models(self, name, monkeypatch):
        """
        Test autoria operations
        :param name:
        :param monkeypatch:
        :return:
        """
        ob = self.autoria.get_group_models(name=name)
        if name != 'Some model':
            assert isinstance(ob, dict)
            assert ob['status'] is True
            monkeypatch.setattr(self.autoria, "data", pd.DataFrame())
            ob = self.autoria.get_group_models(name=name)
            assert ob['status'] is False
            assert ob['error'] == "Name cannot be empty"
        else:
            assert ob['status'] is False
            assert ob['error'] == "Name not found"

    @pytest.mark.parametrize('name, city', [
        ('BMW', 'Херсон'),
        ('Opel', 'Варшава'),
        ('Some model', 'Херсон')
    ])
    def test_get_group_model_city(self, name, city, monkeypatch):
        """
        Test autoria operations
        :param name:
        :param city:
        :param monkeypatch:
        :return:
        """
        ob = self.autoria.get_group_model_city(name=name, city=city)
        if name == 'Some model':
            assert ob['status'] is False
            assert ob['error'] == "Name not found"
        elif city == 'Варшава':
            assert ob['status'] is False
            assert ob['error'] == "City not found"
        else:
            assert ob['status'] is True
            monkeypatch.setattr(self.autoria, "data", pd.DataFrame())
            ob = self.autoria.get_group_model_city(name=name, city=city)
            assert ob['status'] is False
            assert ob['error'] == "Name cannot be empty"

    def test_get_group_years(self, monkeypatch):
        """
        Test autoria operations
        :param monkeypatch:
        :return:
        """
        ob = self.autoria.get_group_years()
        assert ob['status'] is True
        monkeypatch.setattr(self.autoria, "data", pd.DataFrame())
        ob = self.autoria.get_group_years()
        assert ob['status'] is False
        assert ob['error'] == "Name cannot be empty"

    @pytest.mark.parametrize('year', [2018, 2019, 2029])
    def test_get_group_model_year(self, year, monkeypatch):
        """
        Test autoria operations
        :param year:
        :param monkeypatch:
        :return:
        """
        ob = self.autoria.get_group_year(year=year)
        if year == 2029:
            assert ob['status'] is False
            assert ob['error'] == "Year not found"
        else:
            assert ob['status'] is True
            monkeypatch.setattr(self.autoria, "data", pd.DataFrame())
            ob = self.autoria.get_group_year(year=year)
            assert ob['status'] is False
            assert ob['error'] == "Year cannot be empty"

    def test_get_types(self, monkeypatch):
        """
        Test autoria operations
        :param monkeypatch:
        :return:
        """
        ob = self.autoria.get_group_types()
        assert ob['status'] is True
        monkeypatch.setattr(self.autoria, "data", pd.DataFrame())
        ob = self.autoria.get_group_types()
        assert ob['status'] is False
        assert ob['error'] == "Type cannot be empty"

    def test_get_switch(self, monkeypatch):
        """
        Test autoria operations
        :param monkeypatch:
        :return:
        """
        ob = self.autoria.get_group_switch()
        assert ob['status'] is True
        monkeypatch.setattr(self.autoria, "data", pd.DataFrame())
        ob = self.autoria.get_group_switch()
        assert ob['status'] is False
        assert ob['error'] == "Switch cannot be empty"
