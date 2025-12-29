"""
Module predict model, feature importance, correlations
"""
# pylint: disable=ungrouped-imports, duplicate-code
import pandas as pd
import seaborn as sns
from xgboost import XGBRegressor
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import matplotlib
from src.autoria_learn.autoria_main import AutoriaMain
from src.helps.autoria_exceptions import AutoriaDataZeroException
matplotlib.use('Agg')


class AutoriaPredict(AutoriaMain):
    """
    Autoria predict model, feature importance, correlations
    """

    def __init__(self):
        super().__init__()
        self.x = pd.DataFrame()

    def get_importance(self):
        """
        Autoria predict model, feature importance, correlations
        :return:
        """
        try:
            if self.data.empty:
                raise AutoriaDataZeroException("Data is null")
            self.x = self.data.drop(columns=[
                'title', 'short_description',
                'price_usd', 'price_hrn',
                'switch_resource', 'type_fuel',
                'context', 'description',
                'model', 'name'
            ])
            y = self.data['price_usd']
            self.x['accident'] = (LabelEncoder()
                                  .fit_transform(self.x['accident']))
            self.x['city'] = LabelEncoder().fit_transform(self.x['city'])
            self.x['switch'] = LabelEncoder().fit_transform(self.x['switch'])
            self.x['type'] = LabelEncoder().fit_transform(self.x['type'])
            model = XGBRegressor(
                max_depth=9, n_estimators=100,
                learning_rate=0.1, random_state=0,
                n_jobs=-1
            )
            model.fit(self.x, y)
            importance = model.feature_importances_
            feature_names = self.x.columns
            impotent = (pd.DataFrame({
                'feature': feature_names,
                'importance': importance
            }).sort_values(by='importance', ascending=False)
                        .reset_index(drop=True))
            plt.figure(figsize=(8, 6))
            plt.barh(
                impotent['feature'],
                impotent['importance'],
                color='skyblue'
            )
            plt.xlabel("Importance")
            plt.ylabel("Feature")
            plt.title("XGBoost Feature Importance's")
            plt.tight_layout()
            plt.savefig('data/img/get_importance.png')
            return {
                "status": True,
                "data": {
                    "groups": impotent,
                    "image": "get_importance.png"
                },
                "error": False
            }
        except AutoriaDataZeroException as e:
            return {
                "status": False,
                "data": None,
                "error": str(e)
            }

    def get_corr(self):
        """
        Get correlations
        :return:
        """
        try:
            if self.x.empty:
                raise AutoriaDataZeroException("No data")
            plt.figure(figsize=(10, 6))
            corr_matrix = self.x.corr().round(2)  # округляем до сотых
            sns.heatmap(corr_matrix, cmap='viridis', annot=True)
            plt.title("Correlation Heatmap")
            plt.savefig('data/img/get_corr.png')
            return {
                "status": True,
                "data": {
                    "groups": corr_matrix,
                    "image": "get_corr.png",
                },
                "error": False
            }
        except AutoriaDataZeroException as e:
            return {
                "status": False,
                "data": None,
                "error": str(e)
            }
