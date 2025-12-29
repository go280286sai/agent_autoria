"""
Create group models auto from city
Author: Cod3W1ld01@proton.me
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
*name* - марка легкового автомобиля
*year* - год выпуска автомобиля
*model* - модель автомобиля
*city* - город, в котором продается автомобиль
*switch_resource* - коробка передач или ресурс аккумулятора для электромобиля
*switch* - тип коробки передач (механика, автомат, робот, электро)
*resource* - ресурс аккумулятора
*type_fuel* - тип топлива (дизель, бензин, электро)
*volume* - объем двигателя (л)
*capacity* - емкость аккумулятора
*accident* - был ли автомобиль в ДТП
*distance* - пробег, тыс. км
*short_description* - краткое описание
*price_usd* - цена в USD
*price_hrn* - цена в гривнах
*context* - дополнительные параметры
*description* - описание от продавца

Данные объявлений:
{groups}

Проанализируй автомобили одной марки, продаваемые в одном городе.
Сделай детальный аналитический обзор:

1. Общие характеристики моделей
2. Типичные особенности комплектаций
3. Что чаще всего упоминается в *context* и *description*
4. Какие параметры сильнее всего влияют на цену (*price_usd*)
5. На что стоит обращать внимание покупателю

Ответ оформи в виде связного аналитического текста с логическими абзацами.
"""


def get_group_models_city(model: ChatOllama, name: str, city: str):
    """
    Method to create group models auto from city
    :param model:
    :param name:
    :param city:
    :return:
    """
    try:
        ob = AutoriaOperations()
        body = ob.get_group_model_city(name=name, city=city)

        if body["status"] is False:
            raise AutoriaDataZeroException("Данные отсутствуют")

        groups_df = body["data"]["groups"]
        image = body["data"]["image"]
        selected = body["data"]["selected"]

        groups_text = json.dumps(
            selected.to_dict(orient="records"),
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
