"""
Main file for Autoria learn
Author: Cod3W1ld01@proton.me
"""
# pylint: disable=too-few-public-methods
import pandas as pd
from src.helps.help import (get_year, get_switch_resource, clear_city,
                            get_type_fuel, get_accident, get_distance)


class AutoriaMain:
    """
    Main class for Autoria learn
    """
    def __init__(self):
        """
        Main class for Autoria learn
        """
        try:
            self.data = pd.read_json("data/in/results.json")
            self.data['year'] = self.data['title'].apply(get_year).copy()
            self.data['title'] = (self.data['title']
                                  .apply(lambda x: x[:len(x) - 4]))
            self.data['name'] = (self.data['title']
                                 .apply(lambda x: x.split()[0]))
            self.data['model'] = (self.data['title']
                                  .apply(lambda x: x.split()[1:]))
            self.data['city'] = (self.data['city']
                                 .apply(clear_city))
            self.data['switch_resource'] = (self.data['switch_resource']
                                            .apply(get_switch_resource))
            self.data['switch'] = (self.data['switch_resource']
                                   .apply(lambda x: x[0]))
            self.data['resource'] = (self.data['switch_resource']
                                     .apply(lambda x: x[1]))
            self.data['type_fuel'] = (self.data['type_fuel']
                                      .apply(get_type_fuel))
            self.data['type'] = self.data['type_fuel'].apply(lambda x: x[0])
            self.data['volume'] = (self.data['type_fuel']
                                   .apply(lambda x: x[1]))
            self.data['capacity'] = (self.data['type_fuel']
                                     .apply(lambda x: x[2]))
            self.data['accident'] = self.data['context'].apply(get_accident)
            self.data['distance'] = self.data['distance'].apply(get_distance)
        except FileNotFoundError:
            self.data = pd.DataFrame()
