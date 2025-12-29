from src.build_data.predict_data import get_group_predict


def test_group_predict():
    ob = get_group_predict()
    assert isinstance(ob, dict)
    assert isinstance(ob['groups'], list)
    assert ob['status'] is True
    assert len(ob['groups']) == 3
    assert len(ob['image']) == 3

test_group_predict()