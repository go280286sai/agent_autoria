"""
Create a group_switch
Author Cod3W1ld01@proton.me
"""
# pylint: disable=duplicate-code
import json
import logging
from langchain_ollama.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import SystemMessage
from src.autoria_learn.autoria_operations import AutoriaOperations
from src.helps.autoria_exceptions import AutoriaDataZeroException
logger = logging.getLogger(__name__)

SYSTEM_MESSAGE = ("Дай максимально полный, структурированный "
                  "и аналитический ответ на русском языке")

TEMPLATE = """
*switch* – тип коробки передач легкового автомобиля(
механика, автомат, робот, гибрид и т.д.)
*count* – количество автомобилей за указанный год выпуска
*percent* - процентное содержание типов коробок передач

Данные объявлений:
{groups}

Проанализируй потребление разных вид топлив для автомобиля,
продаваемые в одной стране Украина.
Сделай детальный аналитический обзор:

1. Выдели самые популярные
2. Выдели редко используемые
3. Какие виды коробок передач дешевле в обслуживании
4. Какие виды коробок передач реже ремонтируют

Ответ оформи в виде связного аналитического текста с логическими абзацами.
"""


def get_group_switch(model: ChatOllama):
    """
    Create a group_switch
    :param model:
    :return:
    """
    try:
        ob = AutoriaOperations()
        body = ob.get_group_switch()

        if body["status"] is False:
            raise AutoriaDataZeroException("Данные отсутствуют")

        groups_df = body["data"]["groups"]
        image = body["data"]["image"]

        groups_text = json.dumps(
            groups_df.to_dict(orient="records"),
            ensure_ascii=False,
            indent=2
        )

        prompt = PromptTemplate(
            input_variables=["groups"],
            template=TEMPLATE
        )

        parser = StrOutputParser()

        chain = (
            prompt
            | model
            | parser
        )

        response_text = chain.invoke(
            {
                "groups": groups_text
            },
            config={
                "messages": [
                    SystemMessage(content=SYSTEM_MESSAGE)
                ]
            }
        )
        return {
            "status": True,
            "groups": groups_df,
            "image": image,
            "message": response_text
        }

    except AutoriaDataZeroException as e:
        logger.info(str(e))
        return {
            "status": False,
            "data": None,
            "error": str(e)
        }
