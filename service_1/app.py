from flask import Flask, render_template
import requests

app = Flask(__name__)

service_2_api = 'http://localhost:5001'
service_3_api = 'http://localhost:5002'
service_4_api = 'http://localhost:5003'

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

    return render_template('index.html', finalDossier=finalDossier, task=task, target=target)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')