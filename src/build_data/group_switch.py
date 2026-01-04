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

SYSTEM_MESSAGE = ("Please provide the most complete, "
                  "structured and analytical answer possible.")

TEMPLATE = """
*switch* – passenger car transmission type (manual, automatic, robotic, hybrid, etc.)
*count* – number of cars for the specified year of manufacture
*percent* – percentage of transmission types

Ad details:
{groups}

Analyze the consumption of different types of fuel for automobiles sold in Ukraine.
Provide a detailed analytical overview:

1. Highlight the most popular
2. Highlight the least used
3. Which types of transmissions are cheaper to maintain
4. Which types of transmissions require less frequent repairs

Format your answer as a coherent analytical text with logical paragraphs.
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
