"""
Group year data.
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

SYSTEM_MESSAGE = ("Please provide the most complete, "
                  "structured and analytical answer possible.")

TEMPLATE = """
*name* - Car brand
*year* - Year of vehicle manufacture
*model* - Vehicle model
*city* - City where the vehicle is sold
*switch_resource* - Gearbox or battery life for an electric vehicle
*switch* - Gearbox type (manual, automatic, robotic, electric)
*resource* - Battery life
*type_fuel* - Fuel type (diesel, gasoline, electric)
*volume* - Engine displacement (liters)
*capacity* - Battery capacity
*accident* - Whether the vehicle has been in an accident
*distance* - Mileage (in thousands of kilometers)
*short_description* - Short description
*price_usd* - Price in USD
*price_hrn* - Price in UAH
*context* - Additional parameters
*description* - Seller's description

Ad details:
{groups}

Analyze cars sold in a single country, Ukraine, for a specified year. Provide a detailed analytical review:

1. General characteristics of the models
2. Typical features of the trim levels
3. What is most often mentioned in *context* and *description*
4. Which parameters most influence the price (*price_usd*)
5. What should a buyer pay attention to?

Format your answer as a coherent analytical text with logical paragraphs.
"""


def get_group_year(model: ChatOllama, year: int):
    """
    Method to get group year data.
    :param model:
    :param year:
    :return:
    """
    try:
        ob = AutoriaOperations()
        body = ob.get_group_year(year=year)

        if body["status"] is False:
            raise AutoriaDataZeroException("No data")

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
