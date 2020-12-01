from flask import Flask, jsonify
import requests
app = Flask(__name__)

@app.route('/dossierchar/<string:firstchar>', methods=['POST'])
def get_dossier_target(firstchar):
    target = ""

    vowles = "aeiou"
    chars1 = "bcdfghj"
    chars2 = "klmnpqr"

    if firstchar == "z":
        target=" the flask developer"
    elif firstchar in vowles:
        target=" the double agent"
    elif firstchar in chars1:
        target=" the dictator"
    elif firstchar in chars2:
        target=" the head of Odin"
    else:
        target=" Duchess"
    
    return jsonify({'data':target})

@app.route('/dossiernum/<string:firstnum>', methods=['POST'])
def get_dossier_task(firstnum):
    task = ""

    if (firstnum == "19"):
        task="Steal the DB_URI from"
    elif (int(firstnum) % 3) == 0:
        task="Follow"
    elif (int(firstnum) >= 10):
        task="Collect information about"
    else:
        task="Meet with"

    return jsonify({'data':task})

if __name__ == '__main__':
    app.run(port=5003, host='0.0.0.0')
