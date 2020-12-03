from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine
from flask_testing import TestCase
from flask import url_for, jsonify
import requests
import json

from dossierchargen import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestCharGeneration(TestBase):
    def testCharGeneration(self):
        char_list_responce = self.client.get(url_for('get_letters'))
        responce_data = json.loads(char_list_responce.data)

        if str(responce_data["data"][0]).isnumeric():
            assert False
        else:
            assert True