"""
Author: Cod3W1ld01
Date: 2025-12-18
Title: Autoria operations
"""
from typing import Dict
import matplotlib.pyplot as plt
import matplotlib
from src.helps.autoria_exceptions import (AutoriaDataZeroException,
                                          AutoriaDataColumnException)
from src.autoria_learn.autoria_main import AutoriaMain
from src.helps.help import get_sort_count, get_percent
matplotlib.use("Agg")


class AutoriaOperations(AutoriaMain):
    """
    Autoria operations
    """

    def get_group_names(self) -> Dict:
        """
        Get group names
        :return:
        """
        try:
            if 'name' not in self.data.columns:
                raise AutoriaDataColumnException('Name cannot be empty')

            names = self.data.groupby('name').agg({
                'price_usd': ['mean', 'max', 'min', 'count']
            })
            names.columns = names.columns.droplevel(0)
            names_sorted = get_sort_count(names)
            names_sorted['percent'] = get_percent(names_sorted)
            names_sorted.reset_index(inplace=True)
            plt.figure(figsize=(15, 15))
            plt.pie(
                names_sorted['percent'],
                labels=names_sorted['name'],
                autopct='%1.1f%%'
            )
            plt.title(
                label="Percentage of popular cars, %",
                fontweight='bold', fontsize='24'
            )
            plt.legend(names_sorted.index)
            plt.savefig('data/img/get_group_names.png')
            return {
                "status": True,
                "data": {
                    "groups": names_sorted,
                    "image": "get_group_names.png"
                },
                "error": False
            }
        except AutoriaDataColumnException as e:
            return {
                "status": False,
                "data": None,
                "error": str(e)
            }

    def get_group_models(self, name: str) -> Dict:
        """
        Get groups models
        :param name:
        :return:
        """
        try:
            if 'name' not in self.data.columns:
                raise AutoriaDataColumnException('Name cannot be empty')
            if not self.data['name'].str.contains(name).any():
                raise AutoriaDataZeroException("Name not found")
            models = (self.data[self.data['name'] == name]
                      .groupby(['title'])
                      .agg({
                           'price_usd': ['mean', 'max', 'min', 'count']
                           }))
            models.columns = models.columns.droplevel(0)
            models_sort = get_sort_count(models)
            models_sort['percent'] = get_percent(models_sort)
            models_sort.reset_index(inplace=True)
            cars = self.data[self.data['name'] == name]
            plt.figure(figsize=(15, 15))
            plt.pie(
                models_sort['percent'],
                labels=models_sort['title'],
                autopct='%1.1f%%',
                textprops={'fontsize': 16}
            )
            plt.title(
                label=f"Percentage of popular cars {name}, %",
                fontweight='bold', fontsize=24
            )
            plt.legend(models_sort.index)
            plt.savefig('data/img/get_group_models.png')

            return {
                "status": True,
                "data": {
                    "groups": models_sort,
                    "selected": cars,
                    "image": "get_group_models.png"
                },
                "error": False
            }
        except (AutoriaDataColumnException, AutoriaDataZeroException) as e:
            return {
                "status": False,
                "data": None,
                "error": str(e)
            }

    def get_group_model_city(self, name: str, city: str) -> Dict:
        """
        Get groups models for city
        :param name:
        :param city:
        :return:
        """
        try:
            if 'name' not in self.data.columns:
                raise AutoriaDataColumnException('Name cannot be empty')
            if 'city' not in self.data.columns:
                raise AutoriaDataColumnException('City cannot be empty')
            if not self.data['name'].str.contains(name).any():
                raise AutoriaDataZeroException("Name not found")
            if not self.data['city'].str.contains(city).any():
                raise AutoriaDataZeroException("City not found")
            models = (
                self.data[(self.data['name'] == name)
                          & (self.data['city'] == city)]
                .groupby(['title'])
                .agg({
                    'price_usd': ['mean', 'max', 'min', 'count']
                })
            ).round(2)
            models.columns = models.columns.droplevel(0)
            models_sort = get_sort_count(models)
            models_sort['percent'] = get_percent(models_sort)
            models_sort.reset_index(inplace=True)
            cars = self.data[(self.data['name'] == name)
                             & (self.data['city'] == city)].copy()

            cars.drop(columns=[
                'context',
                'switch_resource',
                'type_fuel', 'price_hrn'
            ], inplace=True)
            plt.figure(figsize=(15, 15))
            plt.pie(
                models_sort['percent'],
                autopct='%1.1f%%',
                labels=models_sort['title'],
                textprops={'fontsize': 16}
            )
            plt.title(
                label=f"Percentage of popular cars {name} in the city {city}",
                fontweight='bold',
                fontsize=24
            )
            plt.savefig('data/img/get_group_model_city.png')

            return {
                "status": True,
                "data": {
                    "groups": models_sort,
                    "selected": cars,
                    "image": "get_group_model_city.png"
                },
                "error": False
            }
        except (AutoriaDataColumnException, AutoriaDataZeroException) as e:
            return {
                "status": False,
                "data": None,
                "error": str(e)
            }

    def get_group_years(self) -> Dict:
        """
        Get groups years
        :return:
        """
        try:
            if 'name' not in self.data.columns:
                raise AutoriaDataColumnException('Name cannot be empty')
            if 'year' not in self.data.columns:
                raise AutoriaDataColumnException('Year cannot be empty')
            models = (
                self.data
                .groupby(['year', 'name'])
                .agg({
                    'price_usd': ['mean', 'max', 'min', 'count']
                })
            )
            models.columns = models.columns.droplevel(0)
            # сортируем по количеству
            models_sort = models.sort_values('year', ascending=False)

            models_sort.reset_index(inplace=True)
            return {
                "status": True,
                "data": {
                    "groups": models_sort
                },
                "error": False
            }
        except AutoriaDataColumnException as e:
            return {
                "status": False,
                "data": None,
                "error": str(e)
            }

    def get_group_year(self, year: int) -> Dict:
        """
        Get groups year
        :param year:
        :return:
        """
        try:
            if 'year' not in self.data.columns:
                raise AutoriaDataColumnException('Year cannot be empty')
            if year not in self.data['year'].tolist():
                raise AutoriaDataZeroException("Year not found")
            # фильтруем по году
            models = (
                self.data[self.data['year'] == year]
                .groupby(['name'])
                .agg({
                    'price_usd': ['mean', 'max', 'min', 'count']
                })
            )
            models.columns = models.columns.droplevel(0)
            cars = self.data[self.data['year'] == year]
            # сортируем по количеству
            models_sort = get_sort_count(models)

            # добавляем процентное содержание
            models_sort['percent'] = get_percent(models_sort)
            models_sort.reset_index(inplace=True)

            # строим круговую диаграмму
            plt.figure(figsize=(15, 15))
            plt.pie(
                models_sort['percent'],
                autopct='%1.1f%%',
                labels=models_sort['name']
            )
            plt.title(
                label=f"Percentage of popular cars {year} year, %",
                fontweight='bold',
                fontsize=24
            )
            plt.savefig('data/img/get_group_year.png')

            return {
                "status": True,
                "data": {
                    "groups": models_sort,
                    "selected": cars,
                    "image": "get_group_year.png"
                }
            }
        except (AutoriaDataColumnException, AutoriaDataZeroException) as e:
            return {
                "status": False,
                "data": None,
                "error": str(e)
            }

    def get_group_types(self) -> Dict:
        """
        Get groups types
        :return:
        """
        try:
            if 'type' not in self.data.columns:
                raise AutoriaDataColumnException('Type cannot be empty')
            # фильтруем по году
            models = (
                self.data
                .groupby(['type'])
                .agg({
                    'price_usd': ['count']
                })
            )
            models.columns = models.columns.droplevel(0)

            # сортируем по количеству
            models_sort = get_sort_count(models)

            # добавляем процентное содержание
            models_sort['percent'] = get_percent(models_sort)
            models_sort.reset_index(inplace=True)

            # строим круговую диаграмму
            plt.figure(figsize=(15, 15))
            plt.pie(
                models_sort['percent'],
                autopct='%1.1f%%',
                labels=models_sort['type'],
                textprops={'fontsize': 16}
            )
            plt.title(
                label="Percentage of popular cars, %",
                fontweight='bold',
                fontsize=24
            )
            plt.savefig('data/img/get_group_types.png')

            return {
                "status": True,
                "data": {
                    "groups": models_sort,
                    "image": "get_group_types.png"
                },
                "error": False
            }
        except AutoriaDataColumnException as e:
            return {
                "status": False,
                "data": None,
                "error": str(e)
            }

    def get_group_switch(self) -> Dict:
        """
        Get groups switch
        :return:
        """
        try:
            if 'switch' not in self.data.columns:
                raise AutoriaDataColumnException('Switch cannot be empty')
            models = (
                self.data
                .groupby(['switch'])
                .agg({
                    'price_usd': ['count']
                })
            )
            models.columns = models.columns.droplevel(0)
            # сортируем по количеству
            models_sort = get_sort_count(models)

            # добавляем процентное содержание
            models_sort['percent'] = get_percent(models_sort)
            models_sort.reset_index(inplace=True)

            # строим круговую диаграмму
            plt.figure(figsize=(10, 10))
            plt.pie(
                models_sort['percent'],
                autopct='%1.1f%%',
                labels=models_sort['switch'],
                textprops={'fontsize': 16}
            )
            plt.title(
                label="Percentage of popular cars, %",
                fontweight='bold',
                fontsize=24
            )
            plt.savefig("data/img/get_group_switch.png")

            return {
                "status": True,
                "data": {
                    "groups": models_sort,
                    "image": "get_group_switch.png"
                },
                "error": False
            }
        except AutoriaDataColumnException as e:
            return {
                "status": False,
                "data": None,
                "error": str(e)
            }
