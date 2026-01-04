"""
Group Types
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
*type* – fuel/energy consumption type (
gasoline, diesel, gas/petrol, electric, etc.)
*max* – maximum vehicle price for the specified year of manufacture
*min* – minimum vehicle price for the specified year of manufacture
*mean* – average vehicle price for the specified year of manufacture
*count* – number of vehicles for the specified year of manufacture

Ad data:
{groups}

Analyze the consumption of different types of fuel for vehicles
sold in one country, Ukraine.
Provide a detailed analytical review:

1. Highlight the most popular
2. Highlight the rarely used
3. Which types of fuel are cheaper
4. Which types of fuel increase engine life

Format your answer as a coherent analytical text with logical paragraphs.
"""


def get_group_types(model: ChatOllama) -> dict:
    """
    Method to get group types from chat.
    :param model:
    :return:
    """
    try:
        ob = AutoriaOperations()
        body = ob.get_group_types()

        if body["status"] is False:
            raise AutoriaDataZeroException("No data")

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
