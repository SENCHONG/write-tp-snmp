# # -*- coding: utf-8 -*-

# from flask import Flask
# from flask_restful import reqparse, abort, Api, Resource
# import write_tp_snmp

# app = Flask(__name__)
# api = Api(app)

# TODOS = {
#     'todo1': {'task': 'build an API'},
#     'todo2': {'task': '哈哈哈'},
#     'todo3': {'task': 'profit!'},
#     'nodes': [
#         {"abc": 1},
#         {"abc":2}
#     ]
# }


# class getGraph(Resource):
#     def get(self):
#         return write_tp_snmp.snmpData()


# # 设置路由
# api.add_resource(getGraph, '/get_graph')

# if __name__ == '__main__':
#     app.run(debug=True)
