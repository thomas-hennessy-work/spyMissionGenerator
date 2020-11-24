from flask import Flask, render_template
import requests

app = Flask(__name__)

service_2_api = 'http://localhost:5001'
service_3_api = 'http://localhost:5002'

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

    task = ""
    target = ""

    if (first_num == "19"):
        task="Steal the DB_URI from"
    elif (int(first_num) % 3) == 0:
        task="Follow"
    elif (int(first_num) >= 10):
        task="Collect information about"
    else:
        task="Meet with"

    vowles = "aeiou"
    chars1 = "bcdfghj"
    chars2 = "klmnpqr"

    if first_letter == "z":
        target=" the flask developer"
    elif first_letter in vowles:
        target=" the double agent"
    elif first_letter in chars1:
        target=" the dictator"
    elif first_letter in chars2:
        target=" the head of Odin"
    else:
        target=" Duchess"

    while count < 6:
        finalDossier += str(num_list[count]) + " "
        finalDossier += str(char_list[count]) + " "
        count += 1

    #return(finalDossier)
    return render_template('index.html', finalDossier=finalDossier, task=task, target=target)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')