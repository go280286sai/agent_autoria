"""
Test suite for help module
author: Cod3W1ld01@proton.me
"""
# pylint: disable=import-error, import-outside-toplevel
import pandas as pd
import pytest
from src.helps.help import (get_year, get_switch_resource,
                            clear_city, get_type_fuel,
                            get_accident, get_distance,
                            get_sort_count, get_percent)


@pytest.mark.parametrize("txt", [
    "Рівне (Рівненська)",
    "Дніпро (Дніпропетровськ)",
    "Львів (Львівська)",
    "Київ"
])
def test_clear_city(txt: str):
    """
    Test clear city function
    :param txt:
    :return:
    """
    city = clear_city(txt)
    assert "(" not in city


@pytest.mark.parametrize("txt", [
    "qwerty 2009",
    "qwerty 2020",
    "qwerty 2018",
    "qwerty ert"
])
def test_get_year(txt: str):
    """
    Test get_year function
    :param txt:
    :return:
    """
    year = get_year(txt)
    assert isinstance(year, int)


@pytest.mark.parametrize("txt", ["Автомат", "Варіатор", "621 км", "705 км"])
def test_get_switch_resource(txt: str):
    """
    Test get_switch_resource function
    :param txt:
    :return:
    """
    switch, resource = get_switch_resource(txt)
    assert isinstance(switch, str)
    assert isinstance(resource, float)


@pytest.mark.parametrize("txt", [
    "Електро, 24 кВт-год",
    "Бензин, 3.5 л",
    "Бензин", "3.5 л"
])
def test_get_type_fuel(txt: str):
    """
    Test get_type_fuel function
    :param txt:
    :return:
    """
    a, b, c = get_type_fuel(txt)
    assert isinstance(a, str)
    assert isinstance(b, float)
    assert isinstance(c, float)


@pytest.mark.parametrize("arr", [
    [
        "Автомат",
        "Дизель, 3 л",
        "Торг",
        "4 дні тому"
    ],
    [
        "ТОП 38",
        "Автомат",
        "Бензин, 1.98 л",
        "Був в ДТП",
        "6 днів тому"
    ]
])
def test_get_accident(arr: list[str]):
    """
    Test get_accident function
    :param arr:
    :return:
    """
    n = get_accident(arr)
    assert isinstance(n, str)


@pytest.mark.parametrize("txt", [
    "Без пробігу",
    "100 km",
    "200 km",
    "300 km",
    "400 km",
    "500 km"
])
def test_get_distance(txt: str):
    """
    Test get_distance function
    :param txt:
    :return:
    """
    n = get_distance(txt)
    if txt == "Без пробігу":
        assert n == 0.0
    assert isinstance(n, float)


data = pd.DataFrame([8, 6, 4, 7, 2, 3, 1, 5], columns=['count'])
data2 = pd.DataFrame([8, 7, 6, 5, 4, 3, 2, 1], columns=['count'])


@pytest.mark.parametrize("arr", [data])
def test_get_sort(arr: pd.DataFrame):
    """
    Test get_distance function
    :param arr:
    :return:
    """
    n = get_sort_count(arr).reset_index(drop=True)
    for i in range(0, n.shape[0]):
        assert n.loc[i, 'count'] == data2.loc[i, 'count']


@pytest.mark.parametrize("arr", [data])
def test_get_percent(arr: pd.DataFrame):
    """
    Test get_percent function
    :param arr:
    :return:
    """
    arr['percent'] = get_percent(arr)
    for i in range(0, arr.shape[0]):
        assert isinstance(arr.loc[i, 'percent'], float)
        assert arr.loc[i, 'percent'] == round(arr.loc[i, 'percent'], 2)


def test_report():
    """
    Test report function
    :return:
    """
    from src.helps.help import report
    import os
    t = "Test"
    arr = os.listdir("data/out")
    for el in arr:
        assert el != t
    report(
        name=t,
        title="Test Report",
        data={"groups": data, "message": "Test Report"}
    )
    arr = os.listdir("data/out")
    assert t + ".pdf" in arr
    if t + ".pdf" in arr:
        os.remove("data/out/" + t + ".pdf")
