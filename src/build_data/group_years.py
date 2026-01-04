"""
Group Years
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
*name* - car brand
*max* - maximum price of a car for the specified year of manufacture
*min* - minimum price of a car for the specified year of manufacture
*mean* - average price of a car for the specified year of manufacture
*count* - number of cars for the specified year of manufacture

Ad data:
{groups}

Analyze cars for this year, of different years of manufacture,
sold in one country, Ukraine.
Create a detailed analytical review:

1. Identify the top 10 best-selling (liquid) models
2. Identify the top 10 slowest-selling cars
3. Which parameters most influence price (*price_usd*)
4. What should a buyer pay attention to?

Format your answer as a coherent analytical text with logical paragraphs.
"""


def get_group_years(model: ChatOllama):
    """
    Method to get group years
    :param model:
    :return:
    """
    try:
        ob = AutoriaOperations()
        body = ob.get_group_years()

        if body["status"] is False:
            raise AutoriaDataZeroException("No data")

        groups_df = body["data"]["groups"]

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
            "message": response_text
        }

    except AutoriaDataZeroException as e:
        logger.info(str(e))
        return {
            "status": False,
            "data": None,
            "error": str(e)
        }
