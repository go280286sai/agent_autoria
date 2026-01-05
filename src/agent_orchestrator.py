"""
Agent Orchestrator
author: Cod3W1ld01@proton.me
"""
from langchain_ollama.chat_models import ChatOllama
from src.build_data.group_models_city import get_group_models_city
from src.build_data.group_models_name import get_group_models_name
from src.build_data.group_names import get_group_names
from src.build_data.group_switch import get_group_switch
from src.build_data.group_year import get_group_year
from src.build_data.group_years import get_group_years
from src.build_data.group_types import get_group_types
from src.build_data.predict_data import get_group_predict
from src.build_report.create_report import Report
from src.helps.help import report
from src.logging_config import setup_logging

setup_logging()


class AgentOrchestrator:
    """Main orchestrator using LangGraph"""

    def __init__(self):
        self.llm = ChatOllama(
            model="gemma3:1b",
            base_url="http://192.168.50.218:11434",
            temperature=0.4,
            validate_model_on_init=True)

    def agent_get_group_predict(self) -> str | None:
        """
        Method  get group predict
        :return:
        """
        response = get_group_predict()
        title = [
            'Feature Importance Assessment',
            'Correlation Assessment',
            'Car Catalog'
        ]
        report_ = Report("report_predict")
        for i in range(0, len(response['groups'])):
            report_.create_pages(
                title=title[i],
                groups=response['groups'][i],
                image=response['image'][i],
                message=None
            )
        report_.build_report()
        return ""

    def agent_get_group_models_city(self, name: str, city: str) -> str | None:
        """
        Method  get group models in the city
        :param name:
        :param city:
        :return:
        """
        response = get_group_models_city(model=self.llm, name=name, city=city)
        title = f"Car analysis {name} in the {city}"
        return report(
            name="report_group_models_city",
            title=title,
            data=response
        )

    def agent_get_group_models_name(self, name: str) -> str | None:
        """
        Method  get group_models name
        :param name:
        :return:
        """
        response = get_group_models_name(model=self.llm, name=name)
        title = f"Car analysis {name} in the country"
        return report(
            name="report_group_models_name",
            title=title,
            data=response
        )

    def agent_get_group_year(self, year: int) -> str | None:
        """
        Method  get group year
        :param year:
        :return:
        """
        response = get_group_year(model=self.llm, year=year)
        title = f"Car analysis in the country {year} year"
        return report(
            name="report_group_year",
            title=title,
            data=response
        )

    def agent_get_group_names(self) -> str | None:
        """
        Method  get group names
        :return:
        """
        response = get_group_names(model=self.llm)
        title = "Car analysis in Ukraine"
        return report(
            name="report_group_names",
            title=title,
            data=response
        )

    def agent_get_group_years(self) -> str | None:
        """
        Method  get group years
        :return:
        """
        response = get_group_years(model=self.llm)
        title = "Car analysis in Ukraine today"
        return report(
            name="report_group_years",
            title=title,
            data=response
        )

    def agent_get_group_types(self) -> str | None:
        """
        Method  get group types
        :return:
        """
        response = get_group_types(model=self.llm)
        title = "Analysis of different types of fuel for cars in Ukraine"
        return report(
            name="report_group_types",
            title=title,
            data=response
        )

    def agent_get_group_switch(self) -> str | None:
        """
        Method  get group switch
        :return:
        """
        response = get_group_switch(model=self.llm)
        title = "Analysis of different types of gearboxes for cars in Ukraine"
        return report(
            name="report_group_switch",
            title=title,
            data=response
        )
