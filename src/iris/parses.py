from flask_restful import reqparse

features_parser = reqparse.RequestParser()
features_parser.add_argument('sepal_length', type=float)
features_parser.add_argument('sepal_width', type=float)
features_parser.add_argument('petal_length', type=float)
features_parser.add_argument('petal_width', type=float)
