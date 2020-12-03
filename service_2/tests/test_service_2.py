from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine
from flask_testing import TestCase
from flask import url_for, jsonify
import requests
import json

from dossiernumgen import app

class TestBase(TestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
        
        #Creates the tables for data to be input
        engine = create_engine('sqlite:///data.db')
        meta = MetaData()
        missions = Table(
            'missions', meta,
            Column('mission_id', Integer, primary_key = True),
            Column('dossier_num', String),
            Column('mission_obj', String),
            Column('mission_trgt', String)
        )
        meta.create_all(engine)

        return app

class TestNumGeneration(TestBase):
    def testnumberGeneration(self):
        num_list_responce = self.client.get(url_for('get_numbers'))
        responce_data = json.loads(num_list_responce.data)

        if int(responce_data["data"][0]) < 20 and int(responce_data["data"][0]) >= 0:
            assert True
        else:
            assert False