"""
Test autoria predict
author: Cod3W1ld01@proton.me
"""
import pandas as pd
# pylint: disable=unused-argument, import-error
from src.autoria_learn.autoria_predict import AutoriaPredict


class TestAutoriaPredict:
    """
    Test autoria predict
    """
    predict = AutoriaPredict()

    def test_autoria_predict(self, monkeypatch):
        """
        Test autoria predict
        :param monkeypatch:
        :return:
        """
        response = self.predict.get_importance()
        assert response['status'] is True
        monkeypatch.setattr(self.predict, "data", pd.DataFrame())
        response = self.predict.get_importance()
        assert response['status'] is False

    def test_autoria_corr(self, monkeypatch):
        """
        Test autoria predict
        :param monkeypatch:
        :return:
        """
        self.predict.get_importance()
        response = self.predict.get_corr()
        assert response['status'] is True
        monkeypatch.setattr(self.predict, "x", pd.DataFrame())
        response = self.predict.get_corr()
        assert response['status'] is False
