"""
Helps functions
Author: Cod3W1ld01@proton.me
"""
from typing import Union
import pandas as pd

from src.build_report.create_report import Report


def clear_city(txt: str) -> str:
    """
    Clear city info
    :param txt:
    :return:
    """
    if "(" in txt:
        n = txt.index("(")
        return txt[:n].strip()
    return txt


def get_year(txt: str) -> int:
    """
    Get year
    :param txt:
    :return:
    """
    n = txt[-4:]
    if n.isdigit():
        return int(n)
    return 0


def get_switch_resource(txt: str) -> tuple[str, float]:
    """
    Get switch resource
    :param txt:
    :return:
    """
    if txt[0].isdigit():
        return "Электро", float(txt.split()[0])
    return txt, 0.0


def get_type_fuel(txt: str) -> tuple[str, float, float]:
    """
    Get fuel type
    :param txt:
    :return:
    """
    text = txt.split(",")
    if len(text) == 1:
        if " л" in text[0]:
            a = float(text[0].split()[0])
            b = 0.0
            c = "Not specified"
        else:
            a = 0.0
            b = 0.0
            c = text[0]
    elif " л" in text[1]:
        a = float(text[1].split()[0])
        b = 0.0
        c = text[0]
    else:
        a = 0.0
        b = float(text[1].split()[0])
        c = text[0]
    return c, a, b


def get_accident(arr: list[str]) -> str:
    """
    Get accident
    :param arr:
    :return:
    """
    acc = arr.copy()
    for el in acc:
        if "Був в ДТП" in el:
            return "Was in a traffic accident"
    return "Was not in an accident"


def get_distance(txt: str) -> float:
    """
    Get distance
    :param txt:
    :return:
    """
    if "Без пробігу" in txt:
        return 0.0
    return float("".join([i for i in txt if i.isdigit()]))


def get_sort_count(arr: pd.DataFrame) -> pd.DataFrame:
    """
    Get sort count
    :param arr:
    :return:
    """
    return arr.sort_values('count', ascending=False)


def get_percent(arr: pd.DataFrame) -> pd.DataFrame:
    """
    Get percentage
    :param arr:
    :return:
    """
    return round(arr['count'] / arr['count'].sum() * 100, 2)


def report(
        name: str,
        title: Union[str, list],
        data: Union[list, dict]
) -> str | None:
    """
    Report the data
    :param name:
    :param title:
    :param data:
    :return:
    """
    try:
        report_ = Report(name=name)
        if isinstance(data, dict):
            report_.create_pages(
                title=title,
                image=data.get("image"),
                groups=data["groups"],
                message=data["message"]
            )

        else:
            raise TypeError("data must be list or dict")

        report_.build_report()
        return f"data/out/{name}.pdf"

    except (ValueError, TypeError) as e:
        print(f"[REPORT ERROR] {e}")
        return None
