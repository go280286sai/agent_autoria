"""
Test build functions
author: Cod3W1ld01@proton.me
"""
# pylint: disable=unused-argument, import-error, too-few-public-methods
import pandas as pd
from src.build_data.group_models_city import get_group_models_city
from src.build_data.group_models_name import get_group_models_name
from src.build_data.group_names import get_group_names
from src.build_data.group_switch import get_group_switch
from src.build_data.group_types import get_group_types
from src.build_data.group_year import get_group_year
from src.build_data.group_years import get_group_years


class ChatOllamaFake:
    """
    Test build functions
    """

    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, inputs, config=None):
        # inputs будет словарь {"groups": "..."}
        return f"fake response for {inputs}"


def test_group_models_city(monkeypatch):
    """
    Test build functions
    :param monkeypatch:
    :return:
    """

    def mock_get_group_models_city(*args, **kwargs):
        """
        Test build functions
        :param args:
        :param kwargs:
        :return:
        """
        return {
            "status": True,
            "data": {
                "groups": pd.DataFrame(),
                "selected": pd.DataFrame(),
                "image": "get_group_model_city.png"
            },
            "error": False
        }

    # Подменяем оригинальный ChatOllama на фейковый
    monkeypatch.setattr(
        "langchain_ollama.chat_models.ChatOllama",
        ChatOllamaFake
    )

    # Подменяем метод AutoriaOperations.get_group_model_city
    monkeypatch.setattr(
        "src.autoria_learn.autoria_operations.AutoriaOperations"
        ".get_group_model_city",
        mock_get_group_models_city
    )

    response = get_group_models_city(
        model=ChatOllamaFake(),
        city="test city",
        name="test name"
    )

    assert response["status"] is True
    assert response["image"] == "get_group_model_city.png"
    assert "fake response" in response["message"]


def test_group_models_name(monkeypatch):
    """
    Test build functions
    :param monkeypatch:
    :return:
    """

    def mock_get_group_models_name(*args, **kwargs):
        return {
            "status": True,
            "data": {
                "groups": pd.DataFrame(),
                "selected": pd.DataFrame(),
                "image": "get_group_model_city.png"
            },
            "error": False
        }

    # Подменяем оригинальный ChatOllama на фейковый
    monkeypatch.setattr(
        "langchain_ollama.chat_models.ChatOllama",
        ChatOllamaFake
    )

    monkeypatch.setattr(

        "src.autoria_learn.autoria_operations.AutoriaOperations"
        ".get_group_models",
        mock_get_group_models_name
    )

    response = get_group_models_name(
        model=ChatOllamaFake(),
        name="test name"
    )

    assert response["status"] is True
    assert response["image"] == "get_group_model_city.png"
    assert "fake response" in response["message"]


def test_group_name(monkeypatch):
    """
    Test build functions
    :param monkeypatch:
    :return:
    """

    def mock_get_group_names(*args, **kwargs):
        """
        Test build functions
        :param args:
        :param kwargs:
        :return:
        """
        return {
            "status": True,
            "data": {
                "groups": pd.DataFrame(),
                "selected": pd.DataFrame(),
                "image": "get_group_names.png"
            },
            "error": False
        }

    # Подменяем оригинальный ChatOllama на фейковый
    monkeypatch.setattr(
        "langchain_ollama.chat_models.ChatOllama",
        ChatOllamaFake
    )

    monkeypatch.setattr(
        "src.autoria_learn.autoria_operations.AutoriaOperations"
        ".get_group_names",
        mock_get_group_names
    )

    response = get_group_names(model=ChatOllamaFake())

    assert response["status"] is True
    assert response["image"] == "get_group_names.png"
    assert "fake response" in response["message"]


def test_group_switch(monkeypatch):
    """
    Test build functions
    :param monkeypatch:
    :return:
    """

    def mock_get_group_switch(*args, **kwargs):
        """
        Test build functions
        :param args:
        :param kwargs:
        :return:
        """
        return {
            "status": True,
            "data": {
                "groups": pd.DataFrame(),
                "selected": pd.DataFrame(),
                "image": "get_group_switch.png"
            },
            "error": False
        }

    # Подменяем оригинальный ChatOllama на фейковый
    monkeypatch.setattr(
        "langchain_ollama.chat_models.ChatOllama",
        ChatOllamaFake
    )

    monkeypatch.setattr(
        "src.autoria_learn.autoria_operations.AutoriaOperations"
        ".get_group_switch",
        mock_get_group_switch
    )

    response = get_group_switch(model=ChatOllamaFake())

    assert response["status"] is True
    assert response["image"] == "get_group_switch.png"
    assert "fake response" in response["message"]


def test_group_types(monkeypatch):
    """
    Test build functions
    :param monkeypatch:
    :return:
    """

    def mock_get_group_types(*args, **kwargs):
        """
        Test build functions
        :param args:
        :param kwargs:
        :return:
        """
        return {
            "status": True,
            "data": {
                "groups": pd.DataFrame(),
                "selected": pd.DataFrame(),
                "image": "get_group_types.png"
            },
            "error": False
        }

    # Подменяем оригинальный ChatOllama на фейковый
    monkeypatch.setattr(
        "langchain_ollama.chat_models.ChatOllama",
        ChatOllamaFake
    )

    monkeypatch.setattr(
        "src.autoria_learn.autoria_operations.AutoriaOperations"
        ".get_group_types",
        mock_get_group_types
    )

    response = get_group_types(model=ChatOllamaFake())

    assert response["status"] is True
    assert response["image"] == "get_group_types.png"
    assert "fake response" in response["message"]


def test_group_year(monkeypatch):
    """
    Test build functions
    :param monkeypatch:
    :return:
    """

    def mock_get_group_year(*args, **kwargs):
        """
        Test build functions
        :param args:
        :param kwargs:
        :return:
        """
        return {
            "status": True,
            "data": {
                "groups": pd.DataFrame(),
                "selected": pd.DataFrame(),
                "image": "get_group_year.png"
            },
            "error": False
        }

    # Подменяем оригинальный ChatOllama на фейковый
    monkeypatch.setattr(
        "langchain_ollama.chat_models.ChatOllama",
        ChatOllamaFake
    )

    monkeypatch.setattr(
        "src.autoria_learn.autoria_operations.AutoriaOperations"
        ".get_group_year",
        mock_get_group_year
    )

    response = get_group_year(model=ChatOllamaFake(), year=2000)

    assert response["status"] is True
    assert response["image"] == "get_group_year.png"
    assert "fake response" in response["message"]


def test_group_years(monkeypatch):
    """
    Test build functions
    :param monkeypatch:
    :return:
    """

    def mock_get_group_years(*args, **kwargs):
        """
        Test build functions
        :param args:
        :param kwargs:
        :return:
        """
        return {
            "status": True,
            "data": {
                "groups": pd.DataFrame(),
                "selected": pd.DataFrame()
            },
            "error": False
        }

    # Подменяем оригинальный ChatOllama на фейковый
    monkeypatch.setattr(
        "langchain_ollama.chat_models.ChatOllama",
        ChatOllamaFake
    )

    monkeypatch.setattr(
        "src.autoria_learn.autoria_operations.AutoriaOperations"
        ".get_group_years",
        mock_get_group_years
    )

    response = get_group_years(model=ChatOllamaFake())

    assert response["status"] is True
    assert "fake response" in response["message"]
