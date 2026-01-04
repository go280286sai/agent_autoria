"""
Start service bentoml
Author: Cod3W1ld01@proton.me
"""
import os
import threading
from typing import Dict, Any
import bentoml
from scrapy.crawler import CrawlerProcess
from dotenv import load_dotenv
from fastapi.responses import FileResponse
from src.agent_orchestrator import AgentOrchestrator
from src.agent_scrapy.autoria_scrapy import AppAutoriaSpider
from src.logging_config import setup_logging

setup_logging()
load_dotenv()


@bentoml.service
class ScrapingAgentService:
    """BentoML service for deployment"""

    def __init__(self):
        self.orchestrator = AgentOrchestrator()

    @bentoml.api
    def create_scrapy(self) -> dict:
        """
        Scrapy API
        :return:
        """
        process = CrawlerProcess(settings={
            "FEEDS": {
                "data/in/results.json": {"format": "json"},
            },
        })
        process.crawl(AppAutoriaSpider)
        process.start()
        return {"status": True}

    @bentoml.api
    def generate_report_group_models_city(self,
                                          name: str,
                                          city: str
                                          ) -> Dict[str, Any]:
        """
        Generate report groups models for city
        :param name:
        :param city:
        :return:
        """
        thread = threading.Thread(
            target=self.orchestrator.agent_get_group_models_city,
            args=(name, city)
        )
        thread.start()
        return {"report": "processing"}

    @bentoml.api
    def generate_report_group_models_name(self, name: str) -> Dict[str, Any]:
        """
        Generate report groups models for name
        :param name:
        :return:
        """
        thread = threading.Thread(
            target=self.orchestrator.agent_get_group_models_name,
            args=(name,)
        )
        thread.start()
        return {"report": "processing"}

    @bentoml.api
    def generate_report_group_year(self, year: int) -> Dict[str, Any]:
        """
        Generate report groups models for year
        :param year:
        :return:
        """
        thread = threading.Thread(
            target=self.orchestrator.agent_get_group_year,
            args=(year,)
        )
        thread.start()
        return {"report": "processing"}

    @bentoml.api
    def generate_report_group_names(self) -> Dict[str, Any]:
        """
        Generate report groups models for name
        :return:
        """
        thread = threading.Thread(
            target=self.orchestrator.agent_get_group_names,
            args=()
        )
        thread.start()
        return {"report": "processing"}

    @bentoml.api
    def generate_report_group_years(self) -> Dict[str, Any]:
        """
        Generate report groups models for name
        :return:
        """
        thread = threading.Thread(
            target=self.orchestrator.agent_get_group_years,
            args=()
        )
        thread.start()
        return {"report": "processing"}

    @bentoml.api
    def generate_report_group_types(self) -> Dict[str, Any]:
        """
        Generate report groups models for type
        :return:
        """
        thread = threading.Thread(
            target=self.orchestrator.agent_get_group_types,
            args=()
        )
        thread.start()
        return {"report": "processing"}

    @bentoml.api
    def generate_report_predict(self) -> Dict[str, Any]:
        """
        Generate report predict
        :return:
        """
        thread = threading.Thread(
            target=self.orchestrator.agent_get_group_predict,
            args=()
        )
        thread.start()
        return {"report": "processing"}

    @bentoml.api
    def generate_report_group_switch(self) -> Dict[str, Any]:
        """
        Generate report groups models for switch
        :return:
        """
        thread = threading.Thread(
            target=self.orchestrator.agent_get_group_switch
        )
        thread.start()
        return {"report": "processing"}

    @bentoml.api
    def list_reports(self) -> Dict[str, Any]:
        """
        List reports
        :return:
        """
        arr = os.listdir("data/out")
        # формируем ссылки на PDF
        links = [f"/files/{fname}" for fname in arr if fname.endswith(".pdf")]
        return {"reports": links}

    # 🔥 Добавляем API для отдачи PDF по ссылке
    @bentoml.api(route="/files/{filename}")
    def get_report_file(self, filename: str):
        """
        Get report file
        :param filename:
        :return:
        """
        file_path = os.path.join("data/out", filename)
        if os.path.exists(file_path):
            return FileResponse(file_path, media_type="application/pdf")
        return {"error": "File not found"}
