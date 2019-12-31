# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import write_tp_snmp

app = Flask(__name__)
api = Api(app)

class getGraph(Resource):
    def get(self):
        return write_tp_snmp.getData()


# 设置路由
api.add_resource(getGraph, '/graph')

if __name__ == '__main__':
    app.run(debug=True)
