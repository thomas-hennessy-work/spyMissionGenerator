from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine
from flask_testing import TestCase
from flask import url_for, jsonify
import requests
import json

from missiongen import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestTargets(TestBase):
    def testZ(self):
        mission_responce = self.client.post(url_for('get_dossier_target', firstchar='z'))
        responce_data = json.loads(mission_responce.data)

        if str(responce_data["data"]) == " the flask developer":
            assert True
        else:
            assert False

    def testVowles(self):
        mission_responce = self.client.post(url_for('get_dossier_target', firstchar='a'))
        responce_data = json.loads(mission_responce.data)

        if str(responce_data["data"]) == " the double agent":
            assert True
        else:
            assert False

    def testChars1(self):
        mission_responce = self.client.post(url_for('get_dossier_target', firstchar='b'))
        responce_data = json.loads(mission_responce.data)

        if str(responce_data["data"]) == " the dictator":
            assert True
        else:
            assert False

    def testChars2(self):
        mission_responce = self.client.post(url_for('get_dossier_target', firstchar='k'))
        responce_data = json.loads(mission_responce.data)

        if str(responce_data["data"]) == " the head of Odin":
            assert True
        else:
            assert False

    def testRest(self):
        mission_responce = self.client.post(url_for('get_dossier_target', firstchar='x'))
        responce_data = json.loads(mission_responce.data)

        if str(responce_data["data"]) == " Duchess":
            assert True
        else:
            assert False

class TestTasks(TestBase):
    def test19(self):
        mission_responce = self.client.post(url_for('get_dossier_task', firstnum='19'))
        responce_data = json.loads(mission_responce.data)

        if str(responce_data["data"]) == "Steal the DB_URI from":
            assert True
        else:
            assert False

    def test3s(self):
        mission_responce = self.client.post(url_for('get_dossier_task', firstnum='3'))
        responce_data = json.loads(mission_responce.data)

        if str(responce_data["data"]) == "Follow":
            assert True
        else:
            assert False

    def testAbove10(self):
        mission_responce = self.client.post(url_for('get_dossier_task', firstnum='17'))
        responce_data = json.loads(mission_responce.data)

        if str(responce_data["data"]) == "Collect information about":
            assert True
        else:
            assert False

    def testRest(self):
        mission_responce = self.client.post(url_for('get_dossier_task', firstnum='2'))
        responce_data = json.loads(mission_responce.data)

        if str(responce_data["data"]) == "Meet with":
            assert True
        else:
            assert False