from unittest.mock import patch
from flask import url_for, jsonify
from flask_testing import TestCase
from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine

from app import app, db

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

class TestTask(TestBase):
    def testURITask(self):
        with patch("requests.get") as g:
            with patch("requests.post") as h:
                g.return_value.json.return_value = ({'data':['19','1','1','1','1','1']})
                h.return_value.json.return_value = ({'data':'Steal the DB_URI from'})

                responce = self.client.get(url_for('index'))
                self.assertIn(b'19 1 1 1 1 1', responce.data)
                self.assertIn(b'Steal the DB_URI from', responce.data)

    def testFolowTask(self):
        with patch("requests.get") as g:
            with patch("requests.post") as h:
                g.return_value.json.return_value = ({'data':['6','1','1','1','1','1']})
                h.return_value.json.return_value = ({'data':'Follow'})

                responce = self.client.get(url_for('index'))
                self.assertIn(b'6 1 1 1 1 1', responce.data)
                self.assertIn(b'Follow', responce.data)
