from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests
from os import getenv

app = Flask(__name__)
db = SQLAlchemy(app)
db_password = getenv('MYSQL_ROOT_PASSWORD')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:' + db_password + '@database:3306/database'

service_2_api = 'http://spy-app_service_2:5001'
service_3_api = 'http://spy-app_service_3:5002'
service_4_api = 'http://spy-app_service_4:5003'

class Missions(db.Model):
    mission_id = db.Column(db.Integer, primary_key=True)
    dossier_num = db.Column(db.String(63), nullable=False)
    mission_obj = db.Column(db.String(63), nullable=False)
    mission_trgt = db.Column(db.String(63), nullable=False)

@app.route('/')
def index():
    num_list_responce = requests.get(service_2_api + '/dossiernum')
    char_list_responce = requests.get(service_3_api + '/dossierletter')

    num_list = list(num_list_responce.json()["data"])
    char_list = list(char_list_responce.json()["data"])

    count = 0
    finalDossier = ""

    first_num = str(num_list[0])
    first_letter = str(char_list[0])

    while count < 6:
        finalDossier += str(num_list[count]) + " "
        finalDossier += str(char_list[count]) + " "
        count += 1

    print(service_4_api + '/dossierchar/' + first_letter)
    print(service_4_api + '/dossiernum/' + first_num)

    targetResponce = requests.post(service_4_api + '/dossierchar/' + first_letter)
    taskResponce = requests.post(service_4_api + '/dossiernum/' + first_num)

    task = str(taskResponce.json()["data"])
    target = str(targetResponce.json()["data"])

    mission_to_add = Missions(dossier_num=finalDossier,
                mission_obj=task,
                mission_trgt=target)
    db.session.add(mission_to_add)
    db.session.commit()

    return render_template('index.html', finalDossier=finalDossier, task=task, target=target)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')