from flask import Flask
import requests

app = Flask(__name__)

service_2_api = 'http://localhost:5001'
service_3_api = 'http://localhost:5002'

@app.route('/')
def index():
    num_list_responce = requests.get(service_2_api + '/dossiernum')
    char_list_responce = requests.get(service_3_api + '/dossierletter')

    num_list = str(num_list_responce.json()["data"])
    char_list = str(char_list_responce.json()["data"])

    count = 0
    finalDossier = ""

    while count < 6:
        finalDossier = finalDossier + num_list[count]
        finalDossier = finalDossier + char_list[count]
        count += 1

    #return(finalDossier)
    return(finalDossier + " numlist: " + num_list + " charlist: " + char_list)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')