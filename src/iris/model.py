from sklearn.datasets import load_iris
from .parses import features_parser
from flask_restful import Resource
from flask import jsonify

import xgboost as xgb
import numpy as np
import pickle
import os


class Model(Resource):
    FEATURES = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

    LABELS = {
        0: 'Iris setosa',
        1: 'Iris versicolor',
        2: 'Iris virginica',
    }

    def __init__(self):
        self.params = {
            'max_depth': 5,
            'eta': 0.01,
            'silent': 0,
            'gamma': 1,
            'objective': 'multi:softprob',
            'num_class': 3,
            'min_child_weight': 1,
            'subsample': 0.7,
            'colsample_bytree': 0.7,
            'n_estimators': 500
        }

        self.model_name = '/app/iris-model'

    def train(self):
        print("Training XGBoost iris classification...")
        # get training set
        x, y = self._get_data()

        # train xgboost
        d_train = xgb.DMatrix(x, label=y)
        model = xgb.train(self.params, d_train, num_boost_round=500)

        self.save_model(model)

        return model

    def save_model(self, model):
        pickle.dump(model, open(self.model_name, "wb"))

    def _get_data(self):
        data = load_iris()
        return data.data, data.target

    def predict(self, x: list):
        # get model
        print(os.getcwd())
        model = pickle.load(open(self.model_name, "rb"))
        # predict
        d_test = xgb.DMatrix(x)
        y_rat = model.predict(d_test)[0]
        # set return
        label_index = np.argmax(y_rat)
        p = y_rat[label_index]
        name = self.LABELS[label_index]

        return p, name

    def post(self):
        args = features_parser.parse_args()
        x = [args.sepal_length, args.sepal_width, args.petal_length, args.petal_width]
        p, name = self.predict(x)

        response = {
            'classification': name,
            'probability': float(p)
        }

        return jsonify(response)



