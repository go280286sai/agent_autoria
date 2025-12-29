"""
Tests agent orchestrator
author: Cod3W1ld01@proton.me
"""
# pylint: disable=unused-argument, import-error
import pandas as pd
from src.agent_orchestrator import AgentOrchestrator


def fake_agent_orchestrator(*args, **kwargs):
    """
    A fake agent orchestrator
    :param args:
    :param kwargs:
    :return:
    """
    return {
        "groups": pd.DataFrame({"name": [0, 1, 2]}),
        "image": None,
        "message": "return some text"
    }


def fake_report(*args, **kwargs):
    """
    A fake report
    :param args:
    :param kwargs:
    :return:
    """
    return "fake_report"


class TestAgentOrchestrator:
    """
    Tests agent orchestrator
    """

    def test_get_group_models_city(self, monkeypatch):
        """
        Tests get_group_models_city
        :param monkeypatch:
        :return:
        """
        monkeypatch.setattr(
            "src.build_data.group_models_city.get_group_models_city",
            fake_agent_orchestrator
        )
        monkeypatch.setattr("src.agent_orchestrator.report", fake_report)
        ob = AgentOrchestrator()
        result = ob.agent_get_group_models_city(
            name="BMW",
            city="San Francisco"
        )
        assert isinstance(result, str)
        assert result == "fake_report"

    def test_get_group_models_name(self, monkeypatch):
        """
        Tests get_group_models_name
        :param monkeypatch:
        :return:
        """
        monkeypatch.setattr(
            "src.agent_orchestrator.get_group_models_name",
            fake_agent_orchestrator
        )
        monkeypatch.setattr(
            "src.agent_orchestrator.report",
            fake_report
        )
        ob = AgentOrchestrator()
        result = ob.agent_get_group_models_name(name="BMW")
        assert isinstance(result, str)
        assert result == "fake_report"

    def test_get_group_year(self, monkeypatch):
        """
        Tests get_group_year
        :param monkeypatch:
        :return:
        """
        monkeypatch.setattr(
            "src.agent_orchestrator.get_group_year",
            fake_agent_orchestrator
        )
        monkeypatch.setattr(
            "src.agent_orchestrator.report",
            fake_report
        )
        ob = AgentOrchestrator()
        result = ob.agent_get_group_year(year=2022)
        assert isinstance(result, str)
        assert result == "fake_report"

    def test_get_group_names(self, monkeypatch):
        """
        Tests get_group_names
        :param monkeypatch:
        :return:
        """
        monkeypatch.setattr(
            "src.agent_orchestrator.get_group_names",
            fake_agent_orchestrator
        )
        monkeypatch.setattr(
            "src.agent_orchestrator.report",
            fake_report
        )
        ob = AgentOrchestrator()
        result = ob.agent_get_group_names()
        assert isinstance(result, str)
        assert result == "fake_report"

    def test_get_group_years(self, monkeypatch):
        """
        Tests get_group_years
        :param monkeypatch:
        :return:
        """
        monkeypatch.setattr(
            "src.agent_orchestrator.get_group_years",
            fake_agent_orchestrator
        )
        monkeypatch.setattr(
            "src.agent_orchestrator.report",
            fake_report
        )
        ob = AgentOrchestrator()
        result = ob.agent_get_group_years()
        assert isinstance(result, str)
        assert result == "fake_report"

    def test_get_group_types(self, monkeypatch):
        """
        Tests get_group_types
        :param monkeypatch:
        :return:
        """
        monkeypatch.setattr(
            "src.agent_orchestrator.get_group_types",
            fake_agent_orchestrator
        )
        monkeypatch.setattr(
            "src.agent_orchestrator.report",
            fake_report
        )
        ob = AgentOrchestrator()
        result = ob.agent_get_group_types()
        assert isinstance(result, str)
        assert result == "fake_report"

    def test_get_group_switch(self, monkeypatch):
        """
        Tests get_group_switch
        :param monkeypatch:
        :return:
        """
        monkeypatch.setattr(
            "src.agent_orchestrator.get_group_switch",
            fake_agent_orchestrator
        )
        monkeypatch.setattr(
            "src.agent_orchestrator.report",
            fake_report
        )
        ob = AgentOrchestrator()
        result = ob.agent_get_group_switch()
        assert isinstance(result, str)
        assert result == "fake_report"
