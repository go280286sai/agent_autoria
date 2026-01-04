"""
Create group models auto from city
Author: Cod3W1ld01@proton.me
"""
# pylint: disable=duplicate-code
import logging
from src.autoria_learn.autoria_predict import AutoriaPredict
from src.helps.autoria_exceptions import AutoriaDataZeroException

logger = logging.getLogger(__name__)


def get_group_predict():
    """
    Method to create group important and corr
    :return:
    """
    try:
        ob = AutoriaPredict()
        # Get important
        body = ob.get_importance()
        if body["status"] is False:
            raise AutoriaDataZeroException("No data")
        groups_df = [body["data"]["groups"]]
        images = [body["data"]["image"]]
        # Get corr
        corr = ob.get_corr()
        if corr["status"] is False:
            raise AutoriaDataZeroException("No data")
        groups_df.append(corr["data"]["groups"])
        images.append(corr["data"]["image"])
        # Get catalogs
        data = ob.data[['title', 'switch', 'city', 'price_usd']]
        data = data.sort_values(by=['title'], ascending=False)
        groups_df.append(data)
        images.append(None)
        return {
            "status": True,
            "groups": groups_df,
            "image": images,
            "message": ""
        }

    except AutoriaDataZeroException as e:
        logger.info(str(e))
        return {
            "status": False,
            "data": None,
            "error": str(e)
        }
