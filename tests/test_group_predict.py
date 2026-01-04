"""
Test group_predict.py
Author: Cod3W1ld01@proton.me
"""
from src.build_data.predict_data import get_group_predict


def test_group_predict():
    """
    Tests group_predict function
    :return:
    """
    ob = get_group_predict()
    assert isinstance(ob, dict)
    assert isinstance(ob['groups'], list)
    assert ob['status'] is True
    assert len(ob['groups']) == 3
    assert len(ob['image']) == 3
